"""EHEIM Professional 5e integration."""

from .const import DOMAIN


async def async_setup(hass, config):
    """Set up the EHEIM Professional 5e integration."""
    hass.data.setdefault(DOMAIN, {})
    return True
