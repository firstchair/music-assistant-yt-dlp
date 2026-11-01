"""Build-time patch: find Spotify audiobooks in Music Assistant search.

In markets such as the Netherlands, Spotify's search API returns nothing for
type=audiobook. The books come back as "shows" whose description starts with
"Author(s): ... Narrator(s): ...", and Music Assistant drops those from the
podcast results because they are audiobooks. So they appear nowhere.

This appends a wrapper to MA's Spotify provider: when audiobooks are searched,
it also searches shows, keeps the audiobook-shaped ones and loads them through
the audiobooks endpoint (which does work there; library sync uses it).

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


async def _fc_audiobooks_from_shows(
    provider: SpotifyProvider, search_query: str, limit: int
) -> list[Audiobook]:
    api_result = await provider._get_data(
        "search", q=search_query.replace("'", ""), type="show", limit=limit, offset=0
    )
    shows = (api_result or {}).get("shows") or {}
    ids = [item["id"] for item in shows.get("items") or [] if _fc_is_audiobook_show(item)]
    if not ids:
        return []
    data = await provider._get_data("audiobooks", ids=",".join(ids[:50]))
    return [
        parse_audiobook(item, provider)
        for item in (data or {}).get("audiobooks") or []
        if item and item.get("id")
    ]


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
            books = await _fc_audiobooks_from_shows(self, search_query, limit)
        except Exception as err:  # noqa: BLE001 - never break search over this
            self.logger.debug("Audiobook search via shows failed: %s", err)
            return result
        known = {book.item_id for book in result.audiobooks}
        extra = [book for book in books if book.item_id not in known]
        if extra:
            self.logger.debug("Found %s audiobook(s) via show search", len(extra))
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
