from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN

class BrewSpyOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle BrewSpy options."""

    def __init__(self, config_entry: config_entries.ConfigEntry):
        """Initialize BrewSpy options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the BrewSpy options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(
                    "device_id",
                    default=self.config_entry.options.get(
                        "device_id", self.config_entry.data.get("device_id")
                    ),
                ): str
            })
        )
