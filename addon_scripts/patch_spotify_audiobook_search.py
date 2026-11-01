"""Build-time patch: find Spotify audiobooks in Music Assistant search.

Spotify's public Web API returns no audiobooks when searching from markets such
as the Netherlands: not for type=audiobook, not as shows, and not on the global
session either. The Spotify app and website do find them, through the web
player's internal "pathfinder" search. The audiobooks themselves load fine
through the Web API by id (library sync and audiobook details use that).

This installs spotify_pathfinder.py next to MA's Spotify provider and appends a
wrapper to the provider: when audiobooks are searched, it also asks pathfinder
for audiobook ids and loads them through the Web API. Failures are logged at
debug level and the normal search results are returned unchanged.

Run once while building the image. If MA's Spotify provider changed so the
patch no longer fits, the original file is kept and the build continues.
"""

from __future__ import annotations

import pathlib
import py_compile
import shutil
import sys

MARKER = "# --- firstchair: audiobook search via pathfinder ---"
MODULE_NAME = "_fc_pathfinder.py"

PATCH = '''

# --- firstchair: audiobook search via pathfinder ---
# Appended at image build time by addon_scripts/patch_spotify_audiobook_search.py

from ._fc_pathfinder import PathfinderClient as _FcPathfinderClient  # noqa: E402

_fc_pathfinder = _FcPathfinderClient()


async def _fc_load_audiobooks(provider: SpotifyProvider, ids: list[str]) -> list[Audiobook]:
    # Not every Spotify account may load every audiobook (the Web API answers
    # null/404 for some accounts). MA searches through one Spotify instance, so
    # load what it cannot through the other Spotify instances.
    candidates = [provider] + [
        other
        for other in provider.mass.get_providers()
        if isinstance(other, SpotifyProvider)
        and other is not provider
        and other.audiobooks_supported
    ]
    loaded: dict[str, Audiobook] = {}
    for candidate in candidates:
        missing = [audiobook_id for audiobook_id in ids if audiobook_id not in loaded]
        if not missing:
            break
        try:
            data = await candidate._get_data("audiobooks", ids=",".join(missing[:50]))
        except Exception as err:  # noqa: BLE001 - try the next instance
            candidate.logger.debug("Pathfinder audiobook load failed: %s", err)
            continue
        for item in (data or {}).get("audiobooks") or []:
            if item and item.get("id") in missing:
                loaded[item["id"]] = parse_audiobook(item, candidate)
    return [loaded[audiobook_id] for audiobook_id in ids if audiobook_id in loaded]


async def _fc_find_audiobooks(
    provider: SpotifyProvider, search_query: str, limit: int
) -> list[Audiobook]:
    ids = await _fc_pathfinder.search_audiobook_ids(search_query, min(limit, 50))
    books = await _fc_load_audiobooks(provider, ids) if ids else []
    provider.logger.debug(
        "Pathfinder audiobook search %r: %s id(s), %s loaded", search_query, len(ids), len(books)
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
            self.logger.debug("Pathfinder audiobook search failed: %s", err)
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
    "parse_audiobook",
    "def audiobooks_supported",
    "MediaType",
    "SearchResults",
    "Audiobook",
    "Any",
)


def main() -> int:
    import music_assistant

    spotify_dir = pathlib.Path(music_assistant.__file__).parent / "providers" / "spotify"
    path = spotify_dir / "provider.py"
    module_source = pathlib.Path(__file__).with_name("spotify_pathfinder.py")
    if not path.is_file():
        print(f"spotify audiobook patch: {path} not found, skipped")
        return 0
    if not module_source.is_file():
        print(f"spotify audiobook patch: {module_source} not found, skipped")
        return 0
    source = path.read_text()
    if MARKER in source:
        print("spotify audiobook patch: already applied")
        return 0
    missing = [name for name in REQUIRED_NAMES if name not in source]
    if missing:
        print(f"spotify audiobook patch: provider changed ({', '.join(missing)}), skipped")
        return 0
    module_path = spotify_dir / MODULE_NAME
    shutil.copyfile(module_source, module_path)
    path.write_text(source + PATCH)
    try:
        py_compile.compile(str(module_path), doraise=True)
        py_compile.compile(str(path), doraise=True)
    except py_compile.PyCompileError as err:
        path.write_text(source)
        module_path.unlink(missing_ok=True)
        print(f"spotify audiobook patch: compile failed, reverted: {err}")
        return 0
    print("spotify audiobook patch: applied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
