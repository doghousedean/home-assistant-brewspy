from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN

class BrewSpyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for BrewSpy."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="BrewSpy", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("device_id"): str
            }),
            description_placeholders={"url": "https://brewspy.app"}
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Return the options flow handler."""
        return BrewSpyOptionsFlowHandler(config_entry)


class BrewSpyOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle BrewSpy options flow."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the BrewSpy options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required("device_id", default=self.config_entry.data.get("device_id")): str
            })
        )
