"""Build-time patch: find Spotify audiobooks in Music Assistant search.

When the Spotify provider runs on a developer session (own client ID), Spotify's
search API returns no audiobooks: neither for type=audiobook nor as shows. The
same books do appear for Spotify's own client, and MA can load them by id
(library sync and audiobook details work). MA already searches playlists on the
"global" session for this reason.

This appends a wrapper to MA's Spotify provider: when audiobooks are searched,
it also searches them on the global session and, failing that, looks for
audiobook-shaped shows ("Author(s): ... Narrator(s): ...") and loads those
through the audiobooks endpoint. It logs what it found at debug level.

Run once while building the image. If MA's Spotify provider changed so the
patch no longer fits, the original file is kept and the build continues.
"""

from __future__ import annotations

import pathlib
import py_compile
import sys

MARKER = "# --- firstchair: audiobook search via shows ---"

PATCH = '''

# --- firstchair: audiobook search via shows ---
# Appended at image build time by addon_scripts/patch_spotify_audiobook_search.py


def _fc_is_audiobook_show(item: dict[str, Any] | None) -> bool:
    if not item or not item.get("id"):
        return False
    description = item.get("description") or ""
    return description.startswith("Author(s):") and "Narrator(s):" in description


async def _fc_search(
    provider: SpotifyProvider, search_query: str, search_type: str, limit: int, use_global: bool
) -> list[dict[str, Any]]:
    api_result = await provider._get_data(
        "search",
        q=search_query.replace("'", ""),
        type=search_type,
        limit=limit,
        offset=0,
        use_global_session=use_global,
    )
    section = (api_result or {}).get(f"{search_type}s") or {}
    return [item for item in section.get("items") or [] if item and item.get("id")]


async def _fc_find_audiobooks(
    provider: SpotifyProvider, search_query: str, limit: int
) -> list[Audiobook]:
    use_global = bool(getattr(provider, "dev_session_active", False))
    items = await _fc_search(provider, search_query, "audiobook", limit, use_global)
    books = [parse_audiobook(item, provider) for item in items]
    shows = await _fc_search(provider, search_query, "show", limit, use_global)
    show_ids = [item["id"] for item in shows if _fc_is_audiobook_show(item)]
    known = {book.item_id for book in books}
    show_ids = [show_id for show_id in show_ids if show_id not in known]
    if show_ids:
        data = await provider._get_data("audiobooks", ids=",".join(show_ids[:50]))
        books += [
            parse_audiobook(item, provider)
            for item in (data or {}).get("audiobooks") or []
            if item and item.get("id")
        ]
    provider.logger.debug(
        "Audiobook search %r (global session: %s): %s audiobook result(s), "
        "%s show result(s) of which %s audiobook-shaped",
        search_query,
        use_global,
        len(items),
        len(shows),
        len(show_ids),
    )
    return books


def _fc_patch_audiobook_search() -> None:
    original_search = SpotifyProvider.search

    async def search(
        self: SpotifyProvider,
        search_query: str,
        media_types: list[MediaType] | None = None,
        limit: int = 5,
        **kwargs: Any,
    ) -> SearchResults:
        result = await original_search(self, search_query, media_types, limit, **kwargs)
        if not media_types or MediaType.AUDIOBOOK not in media_types:
            return result
        if not self.audiobooks_supported:
            return result
        try:
            books = await _fc_find_audiobooks(self, search_query, limit)
        except Exception as err:  # noqa: BLE001 - never break search over this
            self.logger.debug("Extra audiobook search failed: %s", err)
            return result
        known = {book.item_id for book in result.audiobooks}
        extra = [book for book in books if book.item_id not in known]
        if extra:
            result.audiobooks = [*result.audiobooks, *extra]
        return result

    search.__doc__ = original_search.__doc__
    SpotifyProvider.search = search  # type: ignore[method-assign]


_fc_patch_audiobook_search()
'''

REQUIRED_NAMES = (
    "class SpotifyProvider(",
    "async def search(",
    "async def _get_data(",
    "use_global_session",
    "parse_audiobook",
    "def audiobooks_supported",
    "MediaType",
    "SearchResults",
    "Audiobook",
    "Any",
)


def main() -> int:
    import music_assistant

    path = (
        pathlib.Path(music_assistant.__file__).parent / "providers" / "spotify" / "provider.py"
    )
    if not path.is_file():
        print(f"spotify audiobook patch: {path} not found, skipped")
        return 0
    source = path.read_text()
    if MARKER in source:
        print("spotify audiobook patch: already applied")
        return 0
    missing = [name for name in REQUIRED_NAMES if name not in source]
    if missing:
        print(f"spotify audiobook patch: provider changed ({', '.join(missing)}), skipped")
        return 0
    path.write_text(source + PATCH)
    try:
        py_compile.compile(str(path), doraise=True)
    except py_compile.PyCompileError as err:
        path.write_text(source)
        print(f"spotify audiobook patch: compile failed, reverted: {err}")
        return 0
    print("spotify audiobook patch: applied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
