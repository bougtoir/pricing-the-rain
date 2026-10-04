from pathlib import Path

import numpy as np

from simulation.run_simulation import WeatherYear, simulate_one


def test_simulation_does_not_change_weather_outcomes():
    weather = WeatherYear(
        region="test",
        rain=np.array([0, 1] * 20),
        dry_spell=np.arange(40, dtype=float),
        drought=np.ones(40),
        hazard=np.repeat(0.5, 40),
    )
    original = weather.rain.copy()
    parameters = {
        "random_request_probability": 1.0,
        "provider_cost": 0.5,
        "fixed_price": 3.0,
        "social_utility": 3.0,
        "rainfall_value": 20.0,
        "selective_success_weight": 1.5,
        "selective_failure_weight": 0.6,
        "recency": 0.85,
        "selection_intercept": -1.2,
        "selection_slope": 5.0,
        "prior_mean": 0.5,
        "prior_strength": 2.0,
    }
    simulate_one(5, weather, np.random.default_rng(1), parameters, 4)
    assert np.array_equal(weather.rain, original)


def test_fixed_price_models_have_no_price_success_difference():
    weather = WeatherYear(
        region="test",
        rain=np.array([0, 1] * 20),
        dry_spell=np.arange(40, dtype=float),
        drought=np.ones(40),
        hazard=np.repeat(0.5, 40),
    )
    parameters = {
        "random_request_probability": 1.0,
        "provider_cost": 0.5,
        "fixed_price": 3.0,
        "social_utility": 3.0,
        "rainfall_value": 20.0,
        "selective_success_weight": 1.5,
        "selective_failure_weight": 0.6,
        "recency": 0.85,
        "selection_intercept": -1.2,
        "selection_slope": 5.0,
        "prior_mean": 0.5,
        "prior_strength": 2.0,
    }
    result = simulate_one(0, weather, np.random.default_rng(2), parameters, 4)
    assert result["price_success_difference"] == 0.0
    assert result["provider_price_dispersion"] == 0.0
    assert result["provider_resource_cost"] == (
        parameters["provider_cost"] * result["events"]
    )


def test_main_models_share_sampled_weather_years_by_replication():
    source = (
        Path(__file__).parents[1] / "simulation" / "run_simulation.py"
    ).read_text(encoding="utf-8")
    assert "for replication, weather_index in enumerate(weather_indices):" in source
    assert 'for model_index, model in enumerate(config["models"]):' in source
