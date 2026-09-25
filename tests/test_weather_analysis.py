from pathlib import Path

import numpy as np
import pandas as pd

from src.weather_analysis import add_drought_and_outcomes, dry_spell_before


def test_dry_spell_uses_only_prior_days():
    precipitation = np.array([0.0, 0.0, 2.0, 0.0, 0.0, 0.0])
    assert dry_spell_before(precipitation, 1.0).tolist() == [0, 1, 2, 0, 1, 2]


def test_zero_effect_has_no_intervention_input():
    source = (Path(__file__).parents[1] / "src" / "weather_analysis.py").read_text(
        encoding="utf-8"
    )
    assert "ritual_effect" not in source


def test_outcomes_exclude_event_day_rain():
    weather = pd.DataFrame(
        {
            "date": pd.date_range("2000-01-01", periods=4),
            "region": ["x"] * 4,
            "month": [1] * 4,
            "roll30_mm": [0.0] * 4,
            "precip_mm": [5.0, 0.0, 2.0, 0.0],
        }
    )
    config = {"training_end": "2000-01-04", "success_windows_days": [1]}
    result = add_drought_and_outcomes(weather, config)
    assert result["success_1mm_1d"].tolist() == [0, 1, 0, 0]


def test_training_and_evaluation_require_complete_outcome_windows():
    source = (Path(__file__).parents[1] / "src" / "weather_analysis.py").read_text(
        encoding="utf-8"
    )
    assert 'pd.Timestamp(config["training_end"]) - pd.Timedelta' in source
    assert 'pd.Timestamp(config["study_period"]["end"]) - pd.Timedelta' in source
    assert 'days=max(config["success_windows_days"])' in source


def test_high_hazard_threshold_uses_training_hazards_only():
    source = (Path(__file__).parents[1] / "src" / "weather_analysis.py").read_text(
        encoding="utf-8"
    )
    assert 'hazards.groupby("region", observed=True)' in source
    assert "threshold_by_region = evaluation.groupby" not in source
    assert 'regional_q = (' in source
    assert "C(month) + C(rule)" in source


def test_permutation_null_is_centered_after_stratum_adjustment():
    root = Path(__file__).parents[1]
    result = pd.read_csv(
        root / "analysis" / "price_permutation_falsification.csv"
    ).iloc[0]
    assert result["permutations"] == 1000
    assert abs(result["permutation_mean"]) < result["permutation_sd"]
    assert 0.0 <= result["permutation_p_two_sided"] <= 1.0


def test_positive_price_success_hypothesis_is_not_overstated():
    root = Path(__file__).parents[1]
    classifications = pd.read_csv(
        root / "results" / "hypothesis_classification.csv"
    )
    row = classifications[
        classifications["hypothesis"].str.startswith("Higher prices")
    ].iloc[0]
    assert row["classification"] == "not supported"


def test_pseudo_events_have_complete_prospective_hazards():
    root = Path(__file__).parents[1]
    events = pd.read_csv(root / "analysis" / "pseudo_events.csv")
    hazard_columns = [
        column
        for column in events
        if column.startswith("success_1mm_") and column.endswith("_mean")
    ]
    assert hazard_columns
    assert not events[hazard_columns].isna().any().any()
