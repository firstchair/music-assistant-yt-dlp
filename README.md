# Music Assistant Server with YouTube Provider — Stable + Beta

> **Fork of [giantorth/music-assistant-yt-dlp](https://github.com/giantorth/music-assistant-yt-dlp)** that ships **two add-on variants** — one tracking the Music Assistant stable channel, one tracking the beta channel — plus custom feature additions (daily playlist, etc.).

A Home Assistant add-on repository that packages the [Music Assistant](https://music-assistant.io/) server with a YouTube provider powered by yt-dlp. Both variants share the same YouTube provider code (`youtube_provider/` at repo root); only the underlying MA base image differs.

## Add-ons in this repository

| Add-on | Tracks | MA channel | Image |
|---|---|---|---|
| **Music Assistant Server (Firstchair)** | latest stable MA release | `releases/latest` (e.g. `2.8.6`) | `ghcr.io/firstchair/music-assistant-yt-dlp/<arch>` |
| **Music Assistant Server (Firstchair) BETA** | latest non-draft, non-`.dev` MA release | beta or stable, whichever is newer (e.g. `2.9.0b9`) | `ghcr.io/firstchair/music-assistant-yt-dlp-beta/<arch>` |

> Only **one** of the two can run at a time — they both bind to port 8094. Pick a channel, install that one, and uninstall the other if you switch.

## Installation

[![Add to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ffirstchair%2Fmusic-assistant-yt-dlp)

Or manually:

1. In Home Assistant, go to **Settings > Add-ons > Add-on Store**
2. Click the three-dot menu (top right) and select **Repositories**
3. Add: `https://github.com/firstchair/music-assistant-yt-dlp`
4. Pick either **Music Assistant Server (Firstchair)** (stable) or **Music Assistant Server (Firstchair) BETA** and install

> **Note:** Either variant replaces the official Music Assistant add-on. Do not run both simultaneously — they all use port 8094.

## How It Works

- The official `ghcr.io/music-assistant/server` image is used as a base
- `youtube_provider/` (at repo root) is copied into the container's providers directory at build time
- Two GitHub Actions workflows watch upstream MA releases every 6 hours:
  - `sync-upstream.yaml` → tracks **stable** (`releases/latest`), bumps `music_assistant_youtube/`
  - `sync-upstream-beta.yaml` → tracks **beta** (latest non-`.dev`), bumps `music_assistant_youtube_beta/`
- The `build.yaml` workflow uses a matrix to build both add-ons in parallel (4 jobs: 2 addons × 2 architectures)

## Configuration

Once installed, add the YouTube provider in Music Assistant under **Settings > Providers**. All configuration options are optional — the provider works out of the box with yt-dlp alone.

### YouTube Data API Key

Providing a [YouTube Data API v3](https://console.cloud.google.com/apis/credentials) key improves search reliability and metadata quality by using the official API instead of scraping.

### Artist Playlist Limit

Controls the maximum number of channel playlists returned as albums per artist. Defaults to 25.

### YouTube Cookies

Paste your YouTube cookies to enable playback of age-restricted or member-only content. Netscape/`cookies.txt` format or raw cookie header — both accepted. Leave empty for public content only.

## Repo Layout

```
firstchair/music-assistant-yt-dlp/
├── youtube_provider/                   # SOURCE OF TRUTH (committed)
├── music_assistant_youtube/            # STABLE add-on (config + Dockerfile)
│   ├── .upstream-version               # current stable MA version
│   ├── config.yaml
│   ├── build.yaml
│   ├── Dockerfile
│   ├── icon.png
│   └── logo.png
├── music_assistant_youtube_beta/       # BETA add-on
│   └── (same structure, different versions)
├── repository.yaml                     # HA add-on store metadata
└── .github/workflows/
    ├── sync-upstream.yaml              # stable channel
    ├── sync-upstream-beta.yaml         # beta channel
    └── build.yaml                      # builds both via matrix
```

The build workflow copies `youtube_provider/` into each addon dir before docker build (the in-addon copies are gitignored).

## Updating the YouTube Provider

Edit `youtube_provider/` (at repo root) and push to `main`. The build workflow rebuilds **both** addons.

## Syncing With Upstream giantorth

```bash
git fetch upstream
git merge upstream/main
# resolve conflicts (likely in youtube_provider/), then:
git push
```

## Data Export / Import (sync between stable and beta)

Both addon images ship two CLI tools — `firstchair-export` and
`firstchair-import` — that snapshot/restore the addon's `/data`
directory to/from `/share/firstchair/exports/`. Since `/share/` is a
host-shared volume, an export from one variant is visible in the other.

```bash
# In the BETA container — snapshot current state:
docker exec addon_5894c5a0_music_assistant_youtube_beta firstchair-export my-test

# In the STABLE container — restore from latest export:
ha apps stop  5894c5a0_music_assistant_youtube
docker exec addon_5894c5a0_music_assistant_youtube firstchair-import --latest
ha apps start 5894c5a0_music_assistant_youtube
```

`firstchair-import` always backs up the current `/data` to a
timestamped tarball before overwriting, so you can roll back.
List available exports:

```bash
docker exec addon_5894c5a0_music_assistant_youtube firstchair-import --list
```

For one-click access, expose them via HA `shell_command` + a Lovelace
button — see [docs/ui-buttons.md](#one-click-buttons-in-ha) (TODO).

## Architecture Support

- `amd64`
- `aarch64`
