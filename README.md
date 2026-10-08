# OpenCode Home Assistant Integration

This integration allows you to use the **OpenCode Go** API as a conversation agent in Home Assistant.
The code is based on the official Open Router component.

## Installation

Place the `custom_components` folder in your configuration directory (or add its contents to an existing `custom_components` folder). Alternatively install via [HACS](https://hacs.xyz/).

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=wesiofilhoIF&repository=opencodeGO_ha&category=integration)

## Configuration

To add the **OpenCode** service to your Home Assistant instance, use this My button:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start?domain=open_code)

Manual configuration steps:

1. Browse to your Home Assistant instance.
2. Go to **Settings > Devices & services**.
3. In the bottom right corner, select the **Add Integration** button.
4. From the list, select **OpenCode**.
5. Follow the instructions on screen to complete the setup.

## Generate an API Key

The API key is used to authenticate requests to OpenCode Go. To generate an API key:

1. Sign in to the [OpenCode Console](https://opencode.ai/console) or create an account.
2. Subscribe to **OpenCode Go** or **Go Plus**.
3. Go to the **API Keys** section in your workspace settings.
4. Select **Create API Key**.
5. Give the key a name and configure any necessary limits.

## Supported functionality

The OpenCode integration allows you to generate data using AI models available on OpenCode Go. You can use this functionality in automations, scripts, or directly in the Home Assistant UI.

## Removing the integration

1. Go to **Settings > Devices & services** and select the integration card.
2. From the list of devices, select the integration instance you want to remove.
3. Next to the entry, select the three dots menu. Then, select **Delete**.
