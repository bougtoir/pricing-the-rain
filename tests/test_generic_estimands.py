"""Controlled-estimand tests for the generic rare-event simulation.

Verifies the sign and magnitude structure documented in
docs/EXOGENOUS_BENCHMARK_AUDIT.md: under truly exogenous observation the
observed support is representative (selection gap ~ 0), while endogenous
observation shifts the observed support toward high-hazard periods.
"""

from __future__ import annotations

import numpy as np
import yaml
from pathlib import Path

from simulation.general_rare_event import simulate_cell

ROOT = Path(__file__).resolve().parents[1]


def _cfg(**overrides) -> dict:
    cfg = yaml.safe_load(
        (ROOT / "config" / "general_simulation.yml").read_text()
    )
    cfg["_replications"] = 200
    cfg["horizon"] = 1500
    cfg["burn_in"] = 100
    for key, value in overrides.items():
        section, _, field = key.partition("__")
        if field:
            cfg[section][field] = value
        else:
            cfg[key] = value
    return cfg


def _run(regime_p: float, rule: str, cfg: dict, **cell_kwargs) -> dict:
    regime = {"name": "test", "base_prob": regime_p}
    rng = np.random.default_rng(12345)
    return simulate_cell(regime, rule, cfg, rng, **cell_kwargs)


def _gap(cell: dict) -> tuple[float, float]:
    """(p_ref_observed - p_bar, p_exp - p_ref)."""
    p = cell["p"].mean()
    O = cell["O"]
    p_ref = cell["p"][O].mean()
    p_exp = (cell["Y"] & O).sum() / O.sum()
    return p_ref - p, p_exp - p_ref


def test_homogeneous_p_exogenous_is_unbiased() -> None:
    cfg = _cfg(hazard_state__high_share=0.0)
    cell = _run(0.10, "exogenous", cfg)
    gap, record = _gap(cell)
    assert abs(gap) < 0.01
    assert abs(record) < 0.01


def test_heterogeneous_p_exogenous_is_unbiased() -> None:
    cfg = _cfg()
    cell = _run(0.10, "exogenous", cfg)
    gap, record = _gap(cell)
    assert abs(gap) < 0.01
    assert abs(record) < 0.01


def test_endogenous_observation_gap_is_positive() -> None:
    cfg = _cfg()
    cell = _run(0.10, "endogenous", cfg)
    gap, record = _gap(cell)
    assert gap > 0.0
    assert abs(record) < 0.02


def test_decreasing_observation_gap_is_negative() -> None:
    cfg = _cfg(acceptance__slope=-4.0, demand__slope=-2.4)
    cell = _run(0.10, "endogenous", cfg)
    gap, _ = _gap(cell)
    assert gap < 0.0
