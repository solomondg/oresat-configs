import os
import json

from . import NodeId
from ._json_to_od import read_json_od_config, make_od, add_all_subscribe_data

_file_path = os.path.dirname(os.path.abspath(__file__))
_oresat0_5_json_dir = f'{_file_path}/jsons/oresat0.5'

_sw_core_config = read_json_od_config(f'{_oresat0_5_json_dir}/sw_core.json')
_solar_config = read_json_od_config(f'{_oresat0_5_json_dir}/solar.json')
_battery_config = read_json_od_config(f'{_oresat0_5_json_dir}/battery.json')
_imu_config = read_json_od_config(f'{_oresat0_5_json_dir}/imu.json')
_rw_config = read_json_od_config(f'{_oresat0_5_json_dir}/reaction_wheel.json')
_c3_config = read_json_od_config(f'{_oresat0_5_json_dir}/c3.json')
_gps_config = read_json_od_config(f'{_oresat0_5_json_dir}/gps.json')
_st_config = read_json_od_config(f'{_oresat0_5_json_dir}/star_tracker.json')
_cfc_config = read_json_od_config(f'{_oresat0_5_json_dir}/cfc.json')
_dxwifi_config = read_json_od_config(f'{_oresat0_5_json_dir}/dxwifi.json')

# make ODs for all nodes
C3_OD = make_od(_c3_config, NodeId.C3)
BATTERY_1_OD = make_od(_battery_config, NodeId.BATTERY_1)
SOLAR_MODULE_1_OD = make_od(_solar_config, NodeId.SOLAR_MODULE_1)
SOLAR_MODULE_2_OD = make_od(_solar_config, NodeId.SOLAR_MODULE_2)
SOLAR_MODULE_3_OD = make_od(_solar_config, NodeId.SOLAR_MODULE_3)
SOLAR_MODULE_4_OD = make_od(_solar_config, NodeId.SOLAR_MODULE_4)
SOLAR_MODULE_5_OD = make_od(_solar_config, NodeId.SOLAR_MODULE_5)
SOLAR_MODULE_6_OD = make_od(_solar_config, NodeId.SOLAR_MODULE_6)
GPS_OD = make_od(_gps_config, NodeId.GPS, _sw_core_config)
STAR_TRACKER_1_OD = make_od(_st_config, NodeId.STAR_TRACKER_1, _sw_core_config)
CFC_OD = make_od(_cfc_config, NodeId.CFC_PROCESSOR, _sw_core_config)
DXWIFI_OD = make_od(_dxwifi_config, NodeId.DXWIFI, _sw_core_config)
REACTION_WHEEL_1_OD = make_od(_rw_config, NodeId.REACTION_WHEEL_1)
REACTION_WHEEL_2_OD = make_od(_rw_config, NodeId.REACTION_WHEEL_2)
REACTION_WHEEL_3_OD = make_od(_rw_config, NodeId.REACTION_WHEEL_3)
REACTION_WHEEL_4_OD = make_od(_rw_config, NodeId.REACTION_WHEEL_4)
IMU_OD = make_od(_imu_config, NodeId.IMU)

# subscribe the c3 to all publish data
add_all_subscribe_data(C3_OD, BATTERY_1_OD)
add_all_subscribe_data(C3_OD, SOLAR_MODULE_1_OD)
add_all_subscribe_data(C3_OD, SOLAR_MODULE_2_OD)
add_all_subscribe_data(C3_OD, SOLAR_MODULE_3_OD)
add_all_subscribe_data(C3_OD, SOLAR_MODULE_4_OD)
add_all_subscribe_data(C3_OD, SOLAR_MODULE_5_OD)
add_all_subscribe_data(C3_OD, SOLAR_MODULE_6_OD)
add_all_subscribe_data(C3_OD, GPS_OD)
add_all_subscribe_data(C3_OD, STAR_TRACKER_1_OD)
add_all_subscribe_data(C3_OD, IMU_OD)
add_all_subscribe_data(C3_OD, REACTION_WHEEL_1_OD)
add_all_subscribe_data(C3_OD, REACTION_WHEEL_2_OD)
add_all_subscribe_data(C3_OD, REACTION_WHEEL_3_OD)
add_all_subscribe_data(C3_OD, REACTION_WHEEL_4_OD)
add_all_subscribe_data(C3_OD, CFC_OD)
add_all_subscribe_data(C3_OD, DXWIFI_OD)

with open(f'{_oresat0_5_json_dir}/beacon.json', 'r') as f:
    BEACON_DEF = json.load(f)