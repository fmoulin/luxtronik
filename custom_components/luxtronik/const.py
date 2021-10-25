"""Constants for the Paul Novus 300 Bus integration."""
import logging
from typing import Final

DOMAIN: Final = "luxtronik2"

DEFAULT_PORT: Final = 8888

ATTR_PARAMETER: Final = "parameter"
ATTR_VALUE: Final = "value"

CONF_SAFE: Final = "safe"
CONF_LOCK_TIMEOUT: Final = "lock_timeout"
CONF_UPDATE_IMMEDIATELY_AFTER_WRITE: Final = "update_immediately_after_write"

CONF_PARAMETERS: Final = "parameters"
CONF_CALCULATIONS: Final = "calculations"
CONF_VISIBILITIES: Final = "visibilities"

CONF_COORDINATOR: Final = "coordinator"

LOGGER: Final[logging.Logger] = logging.getLogger(__package__)

# "binary_sensor", "sensor"
PLATFORMS: Final[list[str]] = ["climate"]

PRESET_SECOND_HEATSOURCE: Final = 'second_heatsource'

LUX_MODE_OFF: Final = 'Off'
LUX_MODE_AUTOMATIC: Final = 'Automatic'
LUX_MODE_SECOND_HEATSOURCE: Final = 'Second heatsource'
LUX_MODE_PARTY: Final = 'Party'
LUX_MODE_HOLIDAYS: Final = 'Holidays'

LUX_STATUS_NO_REQUEST: Final = 'no request'
LUX_STATUS_HEATING: Final = 'heating'
LUX_STATUS_DOMESTIC_WATER: Final = 'hot water'
LUX_STATUS_DEFROST: Final = 'defrost'
LUX_STATUS_EVU: Final = 'evu'

# region Luxtronik Sensor ids
LUX_SENSOR_DETECT_COOLING: Final = 'calculations.ID_WEB_FreigabKuehl'
LUX_SENSOR_STATUS: Final = 'calculations.ID_WEB_WP_BZ_akt'

LUX_SENSOR_DOMESTIC_WATER_CURRENT_TEMPERATURE: Final = 'calculations.ID_WEB_Temperatur_TBW'
LUX_SENSOR_DOMESTIC_WATER_TARGET_TEMPERATURE: Final = 'calculations.ID_WEB_Einst_BWS_akt'
LUX_SENSOR_DOMESTIC_WATER_TARGET_TEMPERATURE_WRITE: Final = 'ID_Einst_BWS_akt'
LUX_SENSOR_DOMESTIC_WATER_HEATER: Final = 'parameters.ID_Ba_Bw_akt'
# endregion Luxtronik Sensor ids
