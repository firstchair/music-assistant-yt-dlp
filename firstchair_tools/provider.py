"""Minimal PluginProvider implementation for Firstchair Tools.

This plugin does not provide an audio source, TTS, or AI query — its
functionality lives entirely in `get_config_entries()` (action buttons
that call the firstchair-export / firstchair-import shell tools).
"""

from __future__ import annotations

from music_assistant.models.plugin import PluginProvider


class FirstchairToolsProvider(PluginProvider):
    """A no-op PluginProvider whose UI is just action buttons."""

    @property
    def supported_features(self) -> set:
        """No ProviderFeatures declared — UI-only plugin."""
        return set()

    async def loaded_in_mass(self) -> None:
        """Called after plugin is loaded — nothing to do."""
        self.logger.info("Firstchair Tools loaded.")

    async def unload(self, is_removed: bool = False) -> None:  # noqa: ARG002
        """Called on unload — nothing to clean up."""
