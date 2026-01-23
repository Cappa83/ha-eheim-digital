"""Config flow for EHEIM Professional 5e."""

from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS

from .const import DOMAIN


class EheimProfessional5eConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for EHEIM Professional 5e."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_IP_ADDRESS],
                data={CONF_IP_ADDRESS: user_input[CONF_IP_ADDRESS]},
            )

        schema = vol.Schema({vol.Required(CONF_IP_ADDRESS): str})
        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
