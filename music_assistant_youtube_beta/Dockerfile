ARG BUILD_FROM=ghcr.io/music-assistant/server:latest
FROM ${BUILD_FROM}

# Inject the YouTube music provider AND the Firstchair Tools plugin
# into MA's installed package directory.
COPY youtube_provider/   /tmp/youtube_provider/
COPY firstchair_tools/   /tmp/firstchair_tools/
RUN SITE_PKGS=$(python3 -c "import music_assistant, pathlib; print(pathlib.Path(music_assistant.__file__).parent)") && \
    cp -r /tmp/youtube_provider   "$SITE_PKGS/providers/youtube" && \
    cp -r /tmp/firstchair_tools   "$SITE_PKGS/providers/firstchair_tools" && \
    python3 -m compileall -q "$SITE_PKGS/providers/youtube" && \
    python3 -m compileall -q "$SITE_PKGS/providers/firstchair_tools" && \
    rm -rf /tmp/youtube_provider /tmp/firstchair_tools

# Install firstchair export/import CLI tools
COPY addon_scripts/firstchair-export addon_scripts/firstchair-import /usr/local/bin/
RUN chmod +x /usr/local/bin/firstchair-export /usr/local/bin/firstchair-import

# Make Spotify audiobooks findable in search (the Web API search misses them in NL).
# Skips itself if MA's Spotify provider changed; never fails the build.
COPY addon_scripts/patch_spotify_audiobook_search.py addon_scripts/spotify_pathfinder.py /tmp/fc_spotify/
RUN python3 /tmp/fc_spotify/patch_spotify_audiobook_search.py && rm -rf /tmp/fc_spotify
