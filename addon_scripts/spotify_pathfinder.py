"""Search Spotify audiobooks through the web player's internal "pathfinder" API.

Spotify's public Web API returns no audiobooks when searching from markets such
as the Netherlands, while the Spotify app and website do find them. This module
asks the same internal search the website uses (operation ``searchDesktop``)
with an anonymous web-player token, and returns the audiobook ids it finds. The
caller loads those ids through the official Web API, which works for them.

This is unofficial and can break whenever Spotify changes its web player:
- the token request needs a TOTP made from a secret embedded in the web player
  (TOTP_SECRETS below; Spotify rotates it now and then);
- the search is a persisted GraphQL query identified by a hash that changes on
  web player releases (rediscovered from the web player's JavaScript when the
  known hash is rejected).
Every failure raises PathfinderError so the caller can fall back quietly.

Installed next to Music Assistant's Spotify provider at image build time by
addon_scripts/patch_spotify_audiobook_search.py.
"""

from __future__ import annotations

import asyncio
import base64
import hashlib
import hmac
import json
import re
import time
from typing import Any

import aiohttp

WEB_PLAYER = "https://open.spotify.com"
TOKEN_URL = "https://open.spotify.com/api/token"
CLIENT_TOKEN_URL = "https://clienttoken.spotify.com/v1/clienttoken"
PATHFINDER_URL = "https://api-partner.spotify.com/pathfinder/v2/query"
CDN_BUILD = "https://open.spotifycdn.com/cdn/build/web-player/"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
)

# TOTP secrets by version, newest first. Taken from the web player.
TOTP_SECRETS: dict[int, list[int]] = {
    61: [44, 55, 47, 42, 70, 40, 34, 114, 76, 74, 50, 111, 120, 97, 75, 76, 94, 102, 43,
         69, 49, 120, 118, 80, 64, 78],
    60: [79, 109, 69, 123, 90, 65, 46, 74, 94, 34, 58, 48, 70, 71, 92, 85, 122, 63, 91, 64,
         87, 87],
    59: [123, 105, 79, 70, 110, 59, 52, 125, 60, 49, 80, 70, 89, 75, 80, 86, 63, 53, 123, 37,
         117, 49, 52, 93, 77, 62, 47, 86, 48, 104, 68, 72],
}
SEARCH_DESKTOP_HASH = "eef7cc54888d91bdd6802623477873caa3948ae173a0c34fd86827b267e94c03"
REQUEST_TIMEOUT = aiohttp.ClientTimeout(total=10)


class PathfinderError(Exception):
    """Pathfinder search could not be completed."""


def _totp(secret: list[int], now: float | None = None) -> str:
    transformed = [value ^ ((index % 33) + 9) for index, value in enumerate(secret)]
    key = "".join(str(value) for value in transformed).encode("ascii")
    counter = int((now if now is not None else time.time()) / 30).to_bytes(8, "big")
    digest = hmac.new(key, counter, hashlib.sha1).digest()
    offset = digest[19] & 0x0F
    code = int.from_bytes(digest[offset : offset + 4], "big") & 0x7FFFFFFF
    return str(code % 1_000_000).zfill(6)


class PathfinderClient:
    """Anonymous web-player session that can run searchDesktop."""

    def __init__(self) -> None:
        self._lock = asyncio.Lock()
        self._access_token = ""
        self._client_token = ""
        self._client_version = ""
        self._web_player_js = ""
        self._expires_at = 0.0
        self._search_hash = SEARCH_DESKTOP_HASH

    async def search_audiobook_ids(self, query: str, limit: int) -> list[str]:
        """Return Spotify ids of audiobooks matching ``query``, best match first."""
        await self._ensure_tokens()
        data = await self._search(query, limit)
        if _persisted_query_missing(data):
            self._search_hash = await self._discover_search_hash()
            data = await self._search(query, limit)
        if data.get("errors") and not data.get("data"):
            raise PathfinderError(f"search failed: {json.dumps(data['errors'])[:300]}")
        search = (data.get("data") or {}).get("searchV2") or {}
        ids: list[str] = []
        for wrapper in (search.get("audiobooks") or {}).get("items") or []:
            item = (wrapper or {}).get("data") or {}
            if item.get("__typename") != "Audiobook":
                continue
            uri = item.get("uri") or ""
            if uri.count(":") == 2 and uri.rsplit(":", 1)[1] not in ids:
                ids.append(uri.rsplit(":", 1)[1])
        return ids[:limit]

    async def _ensure_tokens(self) -> None:
        async with self._lock:
            if self._access_token and time.time() < self._expires_at - 60:
                return
            async with aiohttp.ClientSession(
                timeout=REQUEST_TIMEOUT, headers={"User-Agent": USER_AGENT}
            ) as session:
                async with session.get(WEB_PLAYER) as resp:
                    if resp.status != 200:
                        raise PathfinderError(f"web player returned {resp.status}")
                    html = await resp.text()
                device_id = ""
                for cookie in session.cookie_jar:
                    if cookie.key == "sp_t":
                        device_id = cookie.value
                self._client_version = _client_version(html)
                self._web_player_js = _web_player_js(html)
                token = await self._fetch_access_token(session)
                payload = {
                    "client_data": {
                        "client_version": self._client_version,
                        "client_id": token.get("clientId", ""),
                        "js_sdk_data": {
                            "device_brand": "unknown",
                            "device_model": "unknown",
                            "os": "windows",
                            "os_version": "NT 10.0",
                            "device_id": device_id,
                            "device_type": "computer",
                        },
                    }
                }
                async with session.post(
                    CLIENT_TOKEN_URL, json=payload, headers={"Accept": "application/json"}
                ) as resp:
                    if resp.status != 200:
                        raise PathfinderError(f"client token returned {resp.status}")
                    client_token = ((await resp.json()).get("granted_token") or {}).get("token")
            if not client_token:
                raise PathfinderError("no client token granted")
            self._access_token = token["accessToken"]
            self._client_token = client_token
            expires_ms = token.get("accessTokenExpirationTimestampMs")
            self._expires_at = expires_ms / 1000 if expires_ms else time.time() + 1800

    async def _fetch_access_token(self, session: aiohttp.ClientSession) -> dict[str, Any]:
        last_status = 0
        for version, secret in TOTP_SECRETS.items():
            code = _totp(secret)
            params = {
                "reason": "init",
                "productType": "web-player",
                "totp": code,
                "totpVer": str(version),
                "totpServer": code,
            }
            async with session.get(TOKEN_URL, params=params) as resp:
                last_status = resp.status
                if resp.status == 200:
                    token = await resp.json(content_type=None)
                    if token.get("accessToken"):
                        return token
        raise PathfinderError(
            f"web player token refused (HTTP {last_status}); the TOTP secret probably rotated"
        )

    async def _search(self, query: str, limit: int) -> dict[str, Any]:
        payload = {
            "variables": {
                "searchTerm": query,
                "offset": 0,
                "limit": limit,
                "numberOfTopResults": 5,
                "includeAudiobooks": True,
                "includeArtistHasConcertsField": False,
                "includePreReleases": False,
                "includeAuthors": False,
            },
            "operationName": "searchDesktop",
            "extensions": {"persistedQuery": {"version": 1, "sha256Hash": self._search_hash}},
        }
        headers = {
            "User-Agent": USER_AGENT,
            "Authorization": f"Bearer {self._access_token}",
            "Client-Token": self._client_token,
            "Spotify-App-Version": self._client_version,
            "Content-Type": "application/json;charset=UTF-8",
        }
        async with aiohttp.ClientSession(timeout=REQUEST_TIMEOUT) as session:
            async with session.post(PATHFINDER_URL, json=payload, headers=headers) as resp:
                if resp.status == 401:
                    self._expires_at = 0
                    raise PathfinderError("pathfinder rejected the token (401)")
                if resp.status == 412:
                    # Stale persisted query hash ("Invalid query hash").
                    return {"errors": [{"message": "PersistedQueryNotFound"}]}
                if resp.status not in (200, 400):
                    raise PathfinderError(f"pathfinder returned {resp.status}")
                return await resp.json(content_type=None)

    async def _discover_search_hash(self) -> str:
        """Find the current searchDesktop hash in the web player's JavaScript."""
        if not self._web_player_js:
            raise PathfinderError("search hash expired and web player script unknown")
        pattern = re.compile(r'"searchDesktop","query","([0-9a-f]{64})"')
        async with aiohttp.ClientSession(
            timeout=REQUEST_TIMEOUT, headers={"User-Agent": USER_AGENT}
        ) as session:
            async with session.get(self._web_player_js) as resp:
                bundle = await resp.text()
            if match := pattern.search(bundle):
                return match.group(1)
            for chunk in _chunk_names(bundle):
                async with session.get(CDN_BUILD + chunk) as resp:
                    if resp.status != 200:
                        continue
                    if match := pattern.search(await resp.text()):
                        return match.group(1)
        raise PathfinderError("current searchDesktop hash not found in web player")


def _persisted_query_missing(data: dict[str, Any]) -> bool:
    return any(
        "PersistedQueryNotFound" in json.dumps(error) for error in data.get("errors") or []
    )


def _client_version(html: str) -> str:
    if match := re.search(r'<script id="appServerConfig" type="text/plain">([^<]+)</script>', html):
        try:
            config = json.loads(base64.b64decode(match.group(1)))
            if version := config.get("clientVersion"):
                return str(version)
        except (ValueError, TypeError):
            pass
    if match := re.search(r'"clientVersion":"([^"]+)"', html):
        return match.group(1)
    return ""


def _web_player_js(html: str) -> str:
    for src in re.findall(r'<script[^>]+src="([^"]+\.js)"', html):
        if "web-player/web-player" in src:
            return src if src.startswith("http") else WEB_PLAYER + src
    return ""


def _chunk_names(bundle: str) -> list[str]:
    """Return lazily loaded chunk file names referenced by the web player bundle.

    The bundle holds an id->name map ("xpui-routes-search") directly followed by
    an id->hash map ("2aa27db9"); the file is "<name>.<hash>.js". Search chunks
    come first since that is where searchDesktop lives.
    """

    def parse(text: str) -> dict[str, str]:
        result = {}
        for entry in re.split(r",(?=\d+:)", text[1:-1]):
            key, _, value = entry.partition(":")
            result[key.strip()] = value.strip().strip('"')
        return result

    maps = [parse(text) for text in re.findall(r'\{\d+:"[^"]+"(?:,\d+:"[^"]+")*\}', bundle)]
    for names, hashes in zip(maps, maps[1:]):
        if any(value.startswith("xpui") for value in names.values()) and all(
            re.fullmatch(r"[0-9a-f]{8}", value) for value in hashes.values()
        ):
            chunks = [f"{name}.{hashes[key]}.js" for key, name in names.items() if key in hashes]
            return sorted(chunks, key=lambda chunk: "search" not in chunk)
    return []
