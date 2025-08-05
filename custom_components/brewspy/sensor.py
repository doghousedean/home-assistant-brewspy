import logging
import aiohttp
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

SENSOR_TYPES = {
    "ts": {"name": "Timestamp"},
    "gravity": {"name": "Gravity"},
    "temperature": {"name": "Temperature", "native_unit_of_measurement": "°C", "device_class": "temperature"},
    "angle": {"name": "Tilt"},
    "battery_voltage": {"name": "Battery Voltage", "native_unit_of_measurement": "V"},
    "battery": {"name": "Battery Percentage", "native_unit_of_measurement": "%", "device_class": "battery"},
    "wifi": {"name": "RSSI"}
}

EXPORT_URL = "https://brewspy.app/api/export?token={}&limit=1&sort=desc&format=json"


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    device_id = entry.options.get("device_id") or entry.data["device_id"]

    # Fetch initial data asynchronously
    try:
        data = await fetch_brewspy_data(hass, device_id)
    except Exception as e:
        _LOGGER.error("Failed to fetch BrewSpy data: %s", e)
        return

    sensors = []
    for key, desc in SENSOR_TYPES.items():
        if key == "battery_voltage" and "battery" in data:
            sensors.append(BrewSpySensor(device_id, "battery_voltage", desc, data))
        elif key == "battery" and "battery" in data:
            sensors.append(BrewSpySensor(device_id, "battery", desc, data))
        elif key in data:
            sensors.append(BrewSpySensor(device_id, key, desc, data))

    async_add_entities(sensors, True)


async def fetch_brewspy_data(hass: HomeAssistant, device_id: str):
    url = EXPORT_URL.format(device_id)
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url) as response:
            response.raise_for_status()
            json_data = await response.json()
            if isinstance(json_data, list) and len(json_data) > 0:
                return json_data[0]
            return {}


def voltage_to_percentage(voltage):
    curve = [
        (4.20, 100),
        (4.00, 85),
        (3.85, 60),
        (3.70, 40),
        (3.50, 20),
        (3.30, 5),
        (3.00, 0)
    ]

    for i in range(len(curve) - 1):
        v1, p1 = curve[i]
        v2, p2 = curve[i + 1]
        if v2 <= voltage <= v1:
            return int(p1 + (p2 - p1) * (voltage - v1) / (v2 - v1))
    return 0


class BrewSpySensor(SensorEntity):
    def __init__(self, device_id, key, desc, data):
        self._device_id = device_id
        self._key = key
        self._name = f"BrewSpy {desc['name']}"
        self._unit = desc.get("native_unit_of_measurement")
        self._device_class = desc.get("device_class")
        self._state = data.get(key)

    async def async_update(self):
        try:
            data = await fetch_brewspy_data(self.hass, self._device_id)
            raw_value = data.get(self._key)

            if self._key == "battery" and raw_value is not None:
                try:
                    voltage = float(raw_value)
                    percent = voltage_to_percentage(voltage)
                    self._state = percent
                except Exception as e:
                    _LOGGER.warning("Battery voltage conversion failed: %s", e)
                    self._state = None
            else:
                self._state = raw_value
        except Exception as e:
            _LOGGER.warning("Could not update BrewSpy data: %s", e)

    @property
    def name(self):
        return self._name

    @property
    def native_value(self):
        return self._state

    @property
    def native_unit_of_measurement(self):
        return self._unit

    @property
    def device_class(self):
        return self._device_class

    @property
    def unique_id(self):
        return f"{self._device_id}_{self._key}"
