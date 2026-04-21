import numpy as np
import os
import json
from tqdm import tqdm
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator
from scipy.interpolate import interp1d


basis_er = np.array(
    [
        0.04,
        0.05,
        0.07,
        0.08,
        0.09,
        0.1,
        0.125,
        0.15,
        0.175,
        0.2,
        0.225,
        0.25,
        0.275,
        0.3,
        0.325,
        0.35,
        0.375,
        0.4,
        0.425,
        0.45,
        0.475,
        0.5,
        0.525,
        0.55,
        0.575,
        0.60,
        0.625,
        0.65,
        0.675,
        0.70,
        0.75,
        0.80,
        0.85,
        0.90,
        0.95,
        1.0,
    ]
)

basis_nr = np.array(
    [
        0.5,
        0.51,
        0.55,
        0.6,
        0.65,
        0.7,
        0.75,
        0.8,
        0.9,
        1.0,
        1.1,
        1.2,
        1.3,
        1.4,
        1.5,
        1.6,
        1.7,
        1.8,
        1.9,
        2.0,
        2.1,
        2.2,
        2.3,
        2.4,
        2.5,
        2.6,
        2.7,
        2.8,
        2.9,
        3.0,
        3.1,
        3.2,
        3.3,
        3.4,
        3.5,
        3.6,
        3.7,
        3.8,
        3.9,
        4.0,
        4.1,
        4.2,
        4.3,
        4.4,
        4.5,
        4.6,
        4.7,
        4.8,
        4.9,
        5.0,
    ]
)


def centers_to_edges(centers):
    centers = np.asarray(centers, dtype=float).ravel()
    mids = 0.5 * (centers[1:] + centers[:-1])

    edges = np.empty(len(centers) + 1, dtype=float)
    edges[1:-1] = mids
    edges[0] = centers[0] - 0.5 * (centers[1] - centers[0])
    edges[-1] = centers[-1] + 0.5 * (centers[-1] - centers[-2])
    return edges


cs2_edges = np.linspace(80, 500, 8)
cs2_centers = 0.5 * (cs2_edges[1:] + cs2_edges[:-1])
exposure_sr = dict(sr0=1.50, sr1=2.44, sr2=3.89)


def patch_s2_only_model(data, dtype="wimp"):
    """
    Patch real data to fead to alea
    """
    if dtype == "cevns":
        # No cevns_rate_multiplier is given
        dtype = [
            ("ae_sr0_rate_multiplier", "<f8"),
            ("ae_sr1_rate_multiplier", "<f8"),
            ("cathode_sr0_rate_multiplier", "<f8"),
            ("cathode_sr1_rate_multiplier", "<f8"),
            ("cathode_sr2_rate_multiplier", "<f8"),
            ("de_sr0_rate_multiplier", "<f8"),
            ("de_sr1_rate_multiplier", "<f8"),
            ("de_sr2_rate_multiplier", "<f8"),
            ("signal_efficiency_sr0", "<f8"),
            ("signal_efficiency_sr1", "<f8"),
            ("signal_efficiency_sr2", "<f8"),
            ("t_qy", "<f8"),
            ("t_qy_er", "<f8"),
            ("t_sys_sr0", "<f8"),
            ("t_sys_sr1", "<f8"),
            ("t_sys_sr2", "<f8"),
        ]
    elif dtype == "wimp":
        dtype = [
            ("ae_sr0_rate_multiplier", "<f8"),
            ("ae_sr1_rate_multiplier", "<f8"),
            ("cathode_sr0_rate_multiplier", "<f8"),
            ("cathode_sr1_rate_multiplier", "<f8"),
            ("cathode_sr2_rate_multiplier", "<f8"),
            ("cevns_rate_multiplier", "<f8"),
            ("de_sr0_rate_multiplier", "<f8"),
            ("de_sr1_rate_multiplier", "<f8"),
            ("de_sr2_rate_multiplier", "<f8"),
            ("signal_efficiency_sr0", "<f8"),
            ("signal_efficiency_sr1", "<f8"),
            ("signal_efficiency_sr2", "<f8"),
            ("t_qy", "<f8"),
            ("t_sys_sr0", "<f8"),
            ("t_sys_sr1", "<f8"),
            ("t_sys_sr2", "<f8"),
        ]
    elif dtype == "er":
        dtype = [
            ("ae_sr0_rate_multiplier", "<f8"),
            ("ae_sr1_rate_multiplier", "<f8"),
            ("cathode_sr0_rate_multiplier", "<f8"),
            ("cathode_sr1_rate_multiplier", "<f8"),
            ("cathode_sr2_rate_multiplier", "<f8"),
            ("cevns_rate_multiplier", "<f8"),
            ("de_sr0_rate_multiplier", "<f8"),
            ("de_sr1_rate_multiplier", "<f8"),
            ("de_sr2_rate_multiplier", "<f8"),
            ("signal_efficiency_sr0", "<f8"),
            ("signal_efficiency_sr1", "<f8"),
            ("signal_efficiency_sr2", "<f8"),
            ("t_qy", "<f8"),
            ("t_qy_er", "<f8"),
            ("t_sys_sr0", "<f8"),
            ("t_sys_sr1", "<f8"),
            ("t_sys_sr2", "<f8"),
        ]
    _data = np.zeros(
        1,
        dtype=dtype,
    )
    for field in _data.dtype.names:
        if "multiplier" in field or "signal_efficiency" in field:
            _data[field] = 1.0
    data["ancillary"] = _data
    return data
