"""API client for the EHEIM Professional 5e filter."""

from __future__ import annotations

from dataclasses import dataclass

import aiohttp


@dataclass
class EheimApiClient:
    """Simple API client for the filter."""

    ip_address: str
    session: aiohttp.ClientSession

    async def async_get_status(self) -> dict[str, int | str | float]:
        """Fetch status data from the filter."""
        url = f"http://{self.ip_address}/api"
        async with self.session.get(url, params={"to": ""}, timeout=10) as response:
            response.raise_for_status()
            data = await response.json()

        if not isinstance(data, dict):
            raise ValueError("Unexpected API response")

        return data
