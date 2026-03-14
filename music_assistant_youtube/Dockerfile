ARG BUILD_FROM=ghcr.io/music-assistant/server:latest
FROM ${BUILD_FROM}

# Find the site-packages path dynamically and inject the YouTube provider
COPY youtube_provider/ /tmp/youtube_provider/
RUN SITE_PKGS=$(python3 -c "import music_assistant, pathlib; print(pathlib.Path(music_assistant.__file__).parent)") && \
    cp -r /tmp/youtube_provider "$SITE_PKGS/providers/youtube" && \
    python3 -m compileall -q "$SITE_PKGS/providers/youtube" && \
    rm -rf /tmp/youtube_provider
