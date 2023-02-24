# python libraries
import dataclasses
from dataclasses import dataclass

# femmt libraries
import femmt.functions as ff

# 3rd party libraries
import numpy as np


@dataclass
class InputConfig:
    l_s_target: float
    l_h_target: float
    n_target: float
    time_current_1_vec: np.ndarray
    time_current_2_vec: np.ndarray
    material_list: list
    core_inner_diameter_min_max_count_list: list
    window_w_min_max_count_list: list
    window_h_top_min_max_count_list: list
    window_h_bot_min_max_count_list: list
    factor_max_flux_density: float
    n_p_top_min_max_list: list
    n_p_bot_min_max_list: list
    n_s_top_min_max_list: list
    n_s_bot_min_max_list: list
    primary_litz_wire_list: list
    secondary_litz_wire_list: list

@dataclass
class SweepTensor:
    t1_n_p_top: np.ndarray
    t1_n_p_bot: np.ndarray
    t1_n_s_top: np.ndarray
    t1_n_s_bot: np.ndarray
    t1_window_h_top: np.ndarray
    t1_window_h_bot: np.ndarray
    t1_window_w: np.ndarray
    t1_core_material: list
    t1_core_inner_diameter: np.ndarray
    t1_primary_litz_wire_list: list
    t1_secondary_litz_wire_list: list
    time_current_1_vec: np.ndarray
    time_current_2_vec: np.ndarray
    l_s_target_value: float
    l_h_target_value: float
    n_target_value: float
    factor_max_flux_density: float
@dataclass

class ResultFile:
    case: int
    # geometry parameters
    air_gap_top: float
    air_gap_bot: float
    air_gap_middle: float
    n_p_top: int
    n_p_bot: int
    n_s_top: int
    n_s_bot: int
    window_h_top: float
    window_h_bot: float
    window_w: float
    core_material: str
    core_inner_diameter: float
    primary_litz_wire: str
    secondary_litz_wire: str

    # reluctance model results
    flux_top_max: float
    flux_bot_max: float
    flux_stray_max: float
    p_hyst: float
    primary_litz_wire_loss: float
    secondary_litz_wire_loss: float
    core_2daxi_total_volume: float
    total_loss: float

    # fem simulation results




def print_result_file(result_file: ResultFile):
    for field in dataclasses.fields(result_file):
        ff.femmt_print(f"{field = }")
