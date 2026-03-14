# Music Assistant Server with YouTube Provider

A Home Assistant add-on that packages the [Music Assistant](https://music-assistant.io/) server with a YouTube provider powered by yt-dlp.

## Installation

1. In Home Assistant, go to **Settings > Add-ons > Add-on Store**
2. Click the three-dot menu (top right) and select **Repositories**
3. Add this repository URL:
   ```
   https://github.com/giantorth/music-assistant-yt-dlp
   ```
4. Find **Music Assistant Server (YouTube)** in the add-on store and install it

> **Note:** This add-on replaces the official Music Assistant add-on. Do not run both simultaneously — they use the same port (8095).

## How It Works

- The official `ghcr.io/music-assistant/server` image is used as a base
- The YouTube provider is copied into the container's providers directory at build time
- A GitHub Actions workflow checks for new upstream MA releases every 6 hours and rebuilds automatically

## Updating the YouTube Provider

Edit the files in `youtube_provider/` and push to `main`. The build workflow will automatically rebuild and publish new container images.

## Architecture Support

- `amd64`
- `aarch64`
