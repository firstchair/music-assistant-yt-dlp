"""Firstchair Tools — export & import MA /data via Settings → Plugins.

Import safety strategy: run the import synchronously, then immediately
ask Supervisor to restart this addon. The container exits, /data is
already swapped out, the new MA process boots from the imported state.
A small race exists where MA might write to library.db in the
millisecond between import-finished and restart — acceptable in
practice (idle MA writes are infrequent and SQLite recovers from
partial writes).
"""

from __future__ import annotations

import asyncio
import os
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

import aiohttp
from music_assistant_models.config_entries import (
    ConfigEntry,
    ConfigValueOption,
    ConfigValueType,
)
from music_assistant_models.enums import ConfigEntryType

from .provider import FirstchairToolsProvider

if TYPE_CHECKING:
    from music_assistant_models.config_entries import ProviderConfig
    from music_assistant_models.provider import ProviderManifest

    from music_assistant import MusicAssistant
    from music_assistant.models import ProviderInstanceType


EXPORT_DIR = Path("/share/firstchair/exports")
EXPORT_BIN = "/usr/local/bin/firstchair-export"
IMPORT_BIN = "/usr/local/bin/firstchair-import"
SUPERVISOR_API = "http://supervisor"

CONF_EXPORT_NAME = "export_name"
CONF_EXPORT_NOW = "export_now"
CONF_IMPORT_TARGET = "import_target"
CONF_IMPORT_RESTART = "import_restart"


async def setup(
    mass: MusicAssistant, manifest: ProviderManifest, config: ProviderConfig
) -> ProviderInstanceType:
    """Initialize provider(instance) with given configuration."""
    return FirstchairToolsProvider(mass, manifest, config)


def _list_exports() -> list[str]:
    """Return available export tarballs sorted newest-first."""
    if not EXPORT_DIR.exists():
        return []
    files = sorted(
        EXPORT_DIR.glob("*.tar.gz"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return [f.name for f in files]


async def _run_export(name: str) -> str:
    """Run firstchair-export and return its stdout (or error)."""
    proc = await asyncio.create_subprocess_exec(
        EXPORT_BIN,
        name,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )
    stdout, _ = await proc.communicate()
    output = stdout.decode("utf-8", errors="replace") if stdout else ""
    if proc.returncode != 0:
        return f"❌ Export failed (exit {proc.returncode}):\n{output[-500:]}"
    return f"✅ {output[-300:].strip()}"


async def _run_import(target: str) -> tuple[bool, str]:
    """Run firstchair-import. Returns (ok, message)."""
    proc = await asyncio.create_subprocess_exec(
        IMPORT_BIN,
        target,
        "--force",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )
    stdout, _ = await proc.communicate()
    output = stdout.decode("utf-8", errors="replace") if stdout else ""
    if proc.returncode != 0:
        return False, f"Import failed (exit {proc.returncode}):\n{output[-600:]}"
    return True, output[-400:].strip()


async def _restart_self() -> tuple[bool, str]:
    """Ask Supervisor to restart this addon. Returns (ok, message)."""
    token = os.environ.get("SUPERVISOR_TOKEN")
    if not token:
        return False, "SUPERVISOR_TOKEN not set — restart manually via HA UI."

    url = f"{SUPERVISOR_API}/addons/self/restart"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, timeout=10) as resp:
                if resp.status in (200, 202):
                    return True, "Restart triggered."
                body = await resp.text()
                return False, f"Supervisor returned HTTP {resp.status}: {body[:200]}"
    except Exception as e:  # noqa: BLE001
        return False, f"Could not reach Supervisor: {e}"


async def get_config_entries(
    mass: MusicAssistant,  # noqa: ARG001
    instance_id: str | None = None,  # noqa: ARG001
    action: str | None = None,
    values: dict[str, ConfigValueType] | None = None,
) -> tuple[ConfigEntry, ...]:
    """Render plugin config UI; handle Export and Import actions."""
    values = values or {}
    status: str | None = None

    # ── Action handlers ────────────────────────────────────────────
    if action == CONF_EXPORT_NOW:
        raw_name = str(values.get(CONF_EXPORT_NAME) or "").strip()
        name = raw_name or f"snapshot-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        status = await _run_export(name)

    elif action == CONF_IMPORT_RESTART:
        target = str(values.get(CONF_IMPORT_TARGET) or "").strip()
        if not target:
            status = "⚠️ No snapshot selected — pick one from the dropdown above."
        else:
            ok, import_msg = await _run_import(target)
            if not ok:
                status = f"❌ {import_msg}"
            else:
                # Import succeeded — trigger restart immediately
                restart_ok, restart_msg = await _restart_self()
                if restart_ok:
                    status = (
                        f"✅ Imported `{target}`. Restart triggered — "
                        "MA will be back in ~10 seconds with the new data."
                    )
                else:
                    status = (
                        f"✅ Imported `{target}`, but auto-restart failed: "
                        f"{restart_msg}\n\n"
                        f"Restart this addon manually via HA UI to apply."
                    )

    exports = _list_exports()

    entries: list[ConfigEntry] = []

    if status:
        entries.append(
            ConfigEntry(
                key="action_status",
                type=ConfigEntryType.ALERT,
                label=status,
                required=False,
            )
        )

    # ── Export ─────────────────────────────────────────────────────
    entries.append(
        ConfigEntry(
            key="export_divider",
            type=ConfigEntryType.DIVIDER,
            label="Export",
        )
    )
    entries.append(
        ConfigEntry(
            key="export_help",
            type=ConfigEntryType.LABEL,
            label=(
                "Snapshot `/data` to `/share/firstchair/exports/<name>.tar.gz`. "
                "The other Firstchair variant (stable ↔ beta) sees the same "
                "share, so the snapshot can be imported there afterwards."
            ),
        )
    )
    entries.append(
        ConfigEntry(
            key=CONF_EXPORT_NAME,
            type=ConfigEntryType.STRING,
            label="Snapshot name",
            description="Optional. Leave blank to use a timestamp.",
            required=False,
            default_value="",
        )
    )
    entries.append(
        ConfigEntry(
            key=CONF_EXPORT_NOW,
            type=ConfigEntryType.ACTION,
            label="Export now",
            description="Hot snapshot — works while MA runs. Excludes cache files.",
            action=CONF_EXPORT_NOW,
            action_label="Export current state",
            required=False,
        )
    )

    # ── Import ─────────────────────────────────────────────────────
    entries.append(
        ConfigEntry(
            key="import_divider",
            type=ConfigEntryType.DIVIDER,
            label="Import",
        )
    )
    if not exports:
        entries.append(
            ConfigEntry(
                key="no_exports",
                type=ConfigEntryType.LABEL,
                label="_(No exports yet — make one first via Export above.)_",
            )
        )
    else:
        entries.append(
            ConfigEntry(
                key="import_help",
                type=ConfigEntryType.LABEL,
                label=(
                    "Pick a snapshot to import. The current `/data` is "
                    "automatically backed up before being overwritten, then "
                    "the addon restarts automatically so MA boots with the "
                    "imported data."
                ),
            )
        )
        entries.append(
            ConfigEntry(
                key=CONF_IMPORT_TARGET,
                type=ConfigEntryType.STRING,
                label="Snapshot to import",
                description="Pick from available exports",
                options=[ConfigValueOption(title=e, value=e) for e in exports],
                required=False,
            )
        )
        entries.append(
            ConfigEntry(
                key=CONF_IMPORT_RESTART,
                type=ConfigEntryType.ACTION,
                label="Import + restart addon",
                description=(
                    "Replaces /data with the selected snapshot, then asks "
                    "Supervisor to restart this addon. The page will go "
                    "blank for ~10 seconds while MA reboots."
                ),
                action=CONF_IMPORT_RESTART,
                action_label="Import + restart",
                required=False,
            )
        )

    # ── Snapshots list ─────────────────────────────────────────────
    entries.append(
        ConfigEntry(
            key="snapshots_divider",
            type=ConfigEntryType.DIVIDER,
            label="Available snapshots",
        )
    )
    if exports:
        entries.append(
            ConfigEntry(
                key="exports_list",
                type=ConfigEntryType.LABEL,
                label="\n".join(f"- `{e}`" for e in exports[:15]),
            )
        )
    else:
        entries.append(
            ConfigEntry(
                key="exports_empty",
                type=ConfigEntryType.LABEL,
                label="_(none yet)_",
            )
        )

    return tuple(entries)
