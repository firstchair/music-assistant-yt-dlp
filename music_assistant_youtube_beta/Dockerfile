ARG BUILD_FROM=ghcr.io/music-assistant/server:latest
FROM ${BUILD_FROM}

# Inject the YouTube provider into MA's installed package directory
COPY youtube_provider/ /tmp/youtube_provider/
RUN SITE_PKGS=$(python3 -c "import music_assistant, pathlib; print(pathlib.Path(music_assistant.__file__).parent)") && \
    cp -r /tmp/youtube_provider "$SITE_PKGS/providers/youtube" && \
    python3 -m compileall -q "$SITE_PKGS/providers/youtube" && \
    rm -rf /tmp/youtube_provider

# Install firstchair export/import CLI tools
COPY addon_scripts/firstchair-export addon_scripts/firstchair-import /usr/local/bin/
RUN chmod +x /usr/local/bin/firstchair-export /usr/local/bin/firstchair-import
