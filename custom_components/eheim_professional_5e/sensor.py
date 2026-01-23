"""Sensor platform for the EHEIM Professional 5e integration."""

from __future__ import annotations

from collections.abc import Callable

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.const import UnitOfTime
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import EheimDataUpdateCoordinator


class EheimSensorEntityDescription(SensorEntityDescription):
    """Describe an EHEIM sensor entity."""

    value_fn: Callable[[dict], float | int | str | None] | None = None


SENSOR_DESCRIPTIONS: tuple[EheimSensorEntityDescription, ...] = (
    EheimSensorEntityDescription(
        key="filterActive",
        name="Filter Active",
        value_fn=lambda data: data.get("filterActive"),
    ),
    EheimSensorEntityDescription(
        key="freq",
        name="Rotor Frequency",
        value_fn=lambda data: data.get("freq"),
    ),
    EheimSensorEntityDescription(
        key="freqSoll",
        name="Target Rotor Frequency",
        value_fn=lambda data: data.get("freqSoll"),
    ),
    EheimSensorEntityDescription(
        key="dfs",
        name="Dynamic Frequency Scaling",
        value_fn=lambda data: data.get("dfs"),
    ),
    EheimSensorEntityDescription(
        key="dfsFaktor",
        name="Dynamic Scaling Factor",
        value_fn=lambda data: data.get("dfsFaktor"),
    ),
    EheimSensorEntityDescription(
        key="rotSpeed",
        name="Rotor Speed",
        native_unit_of_measurement="Hz",
        value_fn=lambda data: (data.get("rotSpeed") or 0) / 100,
    ),
    EheimSensorEntityDescription(
        key="pumpMode",
        name="Pump Mode",
        value_fn=lambda data: data.get("pumpMode"),
    ),
    EheimSensorEntityDescription(
        key="runTime",
        name="Run Time",
        native_unit_of_measurement=UnitOfTime.MINUTES,
        value_fn=lambda data: data.get("runTime"),
    ),
    EheimSensorEntityDescription(
        key="serviceHour",
        name="Service Hours Remaining",
        native_unit_of_measurement=UnitOfTime.HOURS,
        value_fn=lambda data: data.get("serviceHour"),
    ),
    EheimSensorEntityDescription(
        key="version",
        name="Hardware Version",
        value_fn=lambda data: data.get("version"),
    ),
    EheimSensorEntityDescription(
        key="turnOffTime",
        name="Turn Off Time",
        native_unit_of_measurement=UnitOfTime.MINUTES,
        value_fn=lambda data: data.get("turnOffTime"),
    ),
    EheimSensorEntityDescription(
        key="turnTimeFeeding",
        name="Feeding Mode Time",
        native_unit_of_measurement=UnitOfTime.MINUTES,
        value_fn=lambda data: data.get("turnTimeFeeding"),
    ),
    EheimSensorEntityDescription(
        key="pm_dfs_soll_high",
        name="Pump Mode DFS High",
        value_fn=lambda data: data.get("pm_dfs_soll_high"),
    ),
    EheimSensorEntityDescription(
        key="pm_dfs_soll_low",
        name="Pump Mode DFS Low",
        value_fn=lambda data: data.get("pm_dfs_soll_low"),
    ),
    EheimSensorEntityDescription(
        key="pm_time_high",
        name="Pump Mode Time High",
        native_unit_of_measurement=UnitOfTime.SECONDS,
        value_fn=lambda data: data.get("pm_time_high"),
    ),
    EheimSensorEntityDescription(
        key="pm_time_low",
        name="Pump Mode Time Low",
        native_unit_of_measurement=UnitOfTime.SECONDS,
        value_fn=lambda data: data.get("pm_time_low"),
    ),
    EheimSensorEntityDescription(
        key="nm_dfs_soll_day",
        name="Night Mode DFS Day",
        value_fn=lambda data: data.get("nm_dfs_soll_day"),
    ),
    EheimSensorEntityDescription(
        key="nm_dfs_soll_night",
        name="Night Mode DFS Night",
        value_fn=lambda data: data.get("nm_dfs_soll_night"),
    ),
    EheimSensorEntityDescription(
        key="start_time_night_mode",
        name="Night Mode Start",
        native_unit_of_measurement=UnitOfTime.MINUTES,
        value_fn=lambda data: data.get("start_time_night_mode"),
    ),
    EheimSensorEntityDescription(
        key="end_time_night_mode",
        name="Night Mode End",
        native_unit_of_measurement=UnitOfTime.MINUTES,
        value_fn=lambda data: data.get("end_time_night_mode"),
    ),
    EheimSensorEntityDescription(
        key="isEheim",
        name="Is EHEIM",
        value_fn=lambda data: data.get("isEheim"),
    ),
)


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up sensors from a config entry."""
    coordinator: EheimDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        EheimSensor(coordinator, description, entry.entry_id)
        for description in SENSOR_DESCRIPTIONS
    )


class EheimSensor(CoordinatorEntity[EheimDataUpdateCoordinator], SensorEntity):
    """Representation of a sensor for the filter."""

    def __init__(
        self,
        coordinator: EheimDataUpdateCoordinator,
        description: EheimSensorEntityDescription,
        entry_id: str,
    ) -> None:
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{entry_id}_{description.key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry_id)},
            name="EHEIM Professional 5e",
            manufacturer="EHEIM",
            model="Professional 5e",
        )

    @property
    def native_value(self):
        """Return the value reported by the device."""
        data = self.coordinator.data or {}
        if self.entity_description.value_fn is not None:
            return self.entity_description.value_fn(data)
        return data.get(self.entity_description.key)
