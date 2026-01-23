"""Data update coordinator for the EHEIM Professional 5e integration."""

from __future__ import annotations

from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

import aiohttp

from .api import EheimApiClient
from .const import DEFAULT_SCAN_INTERVAL, DOMAIN


class EheimDataUpdateCoordinator(DataUpdateCoordinator[dict]):
    """Coordinator for fetching filter data."""

    def __init__(self, hass: HomeAssistant, client: EheimApiClient) -> None:
        super().__init__(
            hass,
            logger=logging.getLogger(__name__),
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.client = client

    async def _async_update_data(self) -> dict:
        try:
            return await self.client.async_get_status()
        except (aiohttp.ClientError, ValueError) as err:
            raise UpdateFailed(f"API error: {err}") from err
