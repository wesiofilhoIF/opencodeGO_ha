"""The OpenCode integration."""

from __future__ import annotations

from openai import AsyncOpenAI, AuthenticationError, OpenAIError

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_API_KEY, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryError, ConfigEntryNotReady

from .const import LOGGER, OPENCODE_BASE_URL

PLATFORMS = [Platform.AI_TASK, Platform.CONVERSATION]

type OpenCodeConfigEntry = ConfigEntry[AsyncOpenAI]


def _create_client(api_key: str) -> AsyncOpenAI:
    """Create OpenAI client outside the event loop."""
    return AsyncOpenAI(
        base_url=OPENCODE_BASE_URL,
        api_key=api_key,
    )


async def async_setup_entry(hass: HomeAssistant, entry: OpenCodeConfigEntry) -> bool:
    """Set up OpenCode from a config entry."""
    client = await hass.async_add_executor_job(
        _create_client,
        entry.data[CONF_API_KEY],
    )

    try:
        async for _ in client.with_options(timeout=10.0).models.list():
            break
    except AuthenticationError as err:
        LOGGER.error("Invalid API key: %s", err)
        raise ConfigEntryError("Invalid API key") from err
    except OpenAIError as err:
        raise ConfigEntryNotReady(err) from err

    entry.runtime_data = client
    entry.async_on_unload(client.close)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(_async_update_listener))

    return True


async def _async_update_listener(
    hass: HomeAssistant, entry: OpenCodeConfigEntry
) -> None:
    """Handle update."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: OpenCodeConfigEntry) -> bool:
    """Unload OpenCode."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
