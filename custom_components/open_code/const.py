"""Constants for the OpenCode integration."""

import logging

from homeassistant.const import CONF_LLM_HASS_API, CONF_PROMPT
from homeassistant.helpers import llm

DOMAIN = "open_code"
LOGGER = logging.getLogger(__package__)

OPENCODE_BASE_URL = "https://opencode.ai/zen/go/v1"

CONF_RECOMMENDED = "recommended"

RECOMMENDED_CONVERSATION_OPTIONS = {
    CONF_RECOMMENDED: True,
    CONF_LLM_HASS_API: [llm.LLM_API_ASSIST],
    CONF_PROMPT: llm.DEFAULT_INSTRUCTIONS_PROMPT,
}
