"""Constants for the YouTube provider."""

from music_assistant_models.enums import ProviderFeature

CONF_API_KEY = "api_key"
CONF_COOKIES = "cookies"
CONF_PLAYLIST_LIMIT = "playlist_limit"
CONF_CACHE_ENABLED = "cache_enabled"
CONF_CACHE_DIR = "cache_dir"
CONF_CACHE_MAX_SIZE_MB = "cache_max_size_mb"
CONF_ACTION_CLEAR_CACHE = "clear_cache"
CONF_POT_SERVER_URL = "pot_server_url"

DEFAULT_PLAYLIST_LIMIT = 25
DEFAULT_CACHE_ENABLED = True
DEFAULT_CACHE_DIR = "/media/music-assistant-youtube-cache"
DEFAULT_CACHE_MAX_SIZE_MB = 2048  # 0 = unlimited
PREFETCH_AHEAD = 3

# bgutil PO token provider: yt-dlp plugin + the HTTP server it talks to (e.g. the
# "YT Music PO Token Generator" add-on, which publishes port 4416 on the host).
# The plugin's major version must match the server's.
POT_PLUGIN_REQUIREMENT = "bgutil-ytdlp-pot-provider>=2,<3"
DEFAULT_POT_SERVER_URL = "http://127.0.0.1:4416"

YT_DATA_API_BASE = "https://www.googleapis.com/youtube/v3"

YT_DOMAIN = "https://www.youtube.com"

# How long before a signed stream URL expires (in seconds). YouTube stream URLs
# carry an `expire` query parameter; we fall back to this default when it cannot
# be parsed from the URL.
DEFAULT_STREAM_URL_EXPIRATION = 3600

# How long before a live stream URL expires (shorter since HLS manifests refresh).
DEFAULT_LIVE_STREAM_URL_EXPIRATION = 300

# yt-dlp live_status values that indicate an active live stream.
LIVE_STATUSES = {"is_live", "is_upcoming"}

SUPPORTED_FEATURES = {
    ProviderFeature.SEARCH,
    ProviderFeature.ARTIST_ALBUMS,
    ProviderFeature.ARTIST_TOPTRACKS,
}
