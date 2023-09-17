"""OreSat0.5 object dictionary and beacon globals."""

import json
import os

from .. import NodeId, OreSatId
from .._json_to_od import gen_od_db, read_json_od_config
from ..base import (
    BAT_CONFIG,
    C3_CONFIG,
    CFC_CONFIG,
    DXWIFI_CONFIG,
    FW_COMMON_CONFIG,
    GPS_CONFIG,
    IMU_CONFIG,
    RW_CONFIG,
    SOLAR_CONFIG,
    ST_CONFIG,
    SW_COMMON_CONFIG,
)

ORESAT_ID = OreSatId.ORESAT0_5

_JSON_DIR = f"{os.path.dirname(os.path.abspath(__file__))}/jsons"
with open(f"{_JSON_DIR}/beacon.json", "r") as f:
    BEACON_DEF = json.load(f)


OD_DB = gen_od_db(
    ORESAT_ID,
    BEACON_DEF,
    {
        NodeId.C3: (C3_CONFIG, SW_COMMON_CONFIG),
        NodeId.BATTERY_1: (BAT_CONFIG, FW_COMMON_CONFIG),
        NodeId.SOLAR_MODULE_1: (SOLAR_CONFIG, FW_COMMON_CONFIG),
        NodeId.SOLAR_MODULE_2: (SOLAR_CONFIG, FW_COMMON_CONFIG),
        NodeId.SOLAR_MODULE_3: (SOLAR_CONFIG, FW_COMMON_CONFIG),
        NodeId.SOLAR_MODULE_4: (SOLAR_CONFIG, FW_COMMON_CONFIG),
        NodeId.SOLAR_MODULE_5: (SOLAR_CONFIG, FW_COMMON_CONFIG),
        NodeId.SOLAR_MODULE_6: (SOLAR_CONFIG, FW_COMMON_CONFIG),
        NodeId.IMU: (IMU_CONFIG, FW_COMMON_CONFIG),
        NodeId.REACTION_WHEEL_1: (RW_CONFIG, FW_COMMON_CONFIG),
        NodeId.REACTION_WHEEL_2: (RW_CONFIG, FW_COMMON_CONFIG),
        NodeId.REACTION_WHEEL_3: (RW_CONFIG, FW_COMMON_CONFIG),
        NodeId.REACTION_WHEEL_4: (RW_CONFIG, FW_COMMON_CONFIG),
        NodeId.GPS: (GPS_CONFIG, SW_COMMON_CONFIG),
        NodeId.STAR_TRACKER_1: (ST_CONFIG, SW_COMMON_CONFIG),
        NodeId.DXWIFI: (DXWIFI_CONFIG, SW_COMMON_CONFIG),
        NodeId.CFC: (CFC_CONFIG, SW_COMMON_CONFIG),
    },
)

# direct access to ODs
C3_OD = OD_DB[NodeId.C3]
BATTERY_1_OD = OD_DB[NodeId.BATTERY_1]
SOLAR_MODULE_1_OD = OD_DB[NodeId.SOLAR_MODULE_1]
SOLAR_MODULE_2_OD = OD_DB[NodeId.SOLAR_MODULE_2]
SOLAR_MODULE_3_OD = OD_DB[NodeId.SOLAR_MODULE_3]
SOLAR_MODULE_4_OD = OD_DB[NodeId.SOLAR_MODULE_4]
SOLAR_MODULE_5_OD = OD_DB[NodeId.SOLAR_MODULE_5]
SOLAR_MODULE_6_OD = OD_DB[NodeId.SOLAR_MODULE_6]
IMU_OD = OD_DB[NodeId.IMU]
REACTION_WHEEL_1_OD = OD_DB[NodeId.REACTION_WHEEL_1]
REACTION_WHEEL_2_OD = OD_DB[NodeId.REACTION_WHEEL_2]
REACTION_WHEEL_3_OD = OD_DB[NodeId.REACTION_WHEEL_3]
REACTION_WHEEL_4_OD = OD_DB[NodeId.REACTION_WHEEL_4]
GPS_OD = OD_DB[NodeId.GPS]
STAR_TRACKER_1_OD = OD_DB[NodeId.STAR_TRACKER_1]
DXWIFI_OD = OD_DB[NodeId.DXWIFI]
CFC_OD = OD_DB[NodeId.CFC]
