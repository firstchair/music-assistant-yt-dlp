"""YouTube URL parsing helpers."""

from __future__ import annotations

import re
from urllib.parse import parse_qs, urlparse

YOUTUBE_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com"}
VIDEO_ID_RE = re.compile(r"[A-Za-z0-9_-]{11}")
PLAYLIST_ID_RE = re.compile(r"(?:PL|OLAK5uy_|UU|FL|RD)[A-Za-z0-9_-]{10,}")
# path prefixes followed by a video id, e.g. /shorts/<id>
VIDEO_PATH_PREFIXES = ("shorts", "live", "embed", "v")


def resolve_youtube_search_target(search_query: str) -> tuple[str, str] | None:
    """Return the direct YouTube media target for a URL-like search query.

    Returns a tuple of ``(target_type, target_id)`` where ``target_type`` is
    ``"track"`` for videos and ``"playlist"`` for playlists.

    Music Assistant replaces every "/" in a search query with a space before it
    reaches the provider, so "https://youtu.be/<id>" arrives as
    "https:  youtu.be <id>"; such queries are restored before parsing. A bare
    video or playlist id is accepted as well.
    """
    raw_query = search_query.strip()
    if not raw_query:
        return None
    candidates = [raw_query]
    if " " in raw_query and re.search(r"youtube\.com|youtu\.be", raw_query, re.IGNORECASE):
        candidates.append(raw_query.replace(" ", "/"))
    for candidate in candidates:
        if target := _parse_url(candidate):
            return target
    return _parse_bare_id(raw_query)


def _parse_url(query: str) -> tuple[str, str] | None:
    normalized = query
    if not urlparse(query).scheme and query.lower().startswith(
        tuple(f"{host}/" for host in YOUTUBE_HOSTS) + ("youtu.be/",)
    ):
        normalized = f"https://{query}"
    parsed = urlparse(normalized)
    host = parsed.netloc.lower().split(":", 1)[0]
    query_params = parse_qs(parsed.query)
    if host in YOUTUBE_HOSTS:
        path = parsed.path.rstrip("/")
        if path == "/watch":
            video_id = query_params.get("v", [""])[0]
            if VIDEO_ID_RE.fullmatch(video_id):
                return "track", video_id
        if path == "/playlist":
            playlist_id = query_params.get("list", [""])[0]
            if playlist_id:
                return "playlist", playlist_id
        parts = path.strip("/").split("/")
        if len(parts) >= 2 and parts[0] in VIDEO_PATH_PREFIXES and VIDEO_ID_RE.fullmatch(parts[1]):
            return "track", parts[1]
    if host == "youtu.be":
        video_id = parsed.path.strip("/").split("/", 1)[0]
        if VIDEO_ID_RE.fullmatch(video_id):
            return "track", video_id
    return None


def _parse_bare_id(query: str) -> tuple[str, str] | None:
    if PLAYLIST_ID_RE.fullmatch(query):
        return "playlist", query
    # an 11 character word could also be a normal search ("Voorleesboe");
    # only take it as a video id when it does not look like a plain word
    if VIDEO_ID_RE.fullmatch(query) and (
        any(char.isdigit() or char in "-_" for char in query)
        or any(char.isupper() for char in query[1:])
    ):
        return "track", query
    return None
