from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from simulation.run_simulation import summarize
from src.weather_analysis import dry_spell_before, estimate_training_hazards


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"
RESULTS = ROOT / "results"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compare_frames(left: pd.DataFrame, right: pd.DataFrame, keys: list[str]) -> None:
    left = left.sort_values(keys).reset_index(drop=True)
    right = right.sort_values(keys).reset_index(drop=True)
    check(left.columns.tolist() == right.columns.tolist(), "Column mismatch")
    check(len(left) == len(right), "Row-count mismatch")
    for column in left:
        if pd.api.types.is_numeric_dtype(left[column]):
            check(
                np.allclose(
                    left[column].to_numpy(dtype=float),
                    right[column].to_numpy(dtype=float),
                    equal_nan=True,
                ),
                f"Numeric mismatch in {column}",
            )
        else:
            check(left[column].equals(right[column]), f"Text mismatch in {column}")


def audit_weather(config: dict) -> dict[str, object]:
    weather = pd.read_csv(
        ROOT / "data" / "processed" / "daily_weather_features.csv.gz",
        parse_dates=["date"],
    )
    expected_days = len(
        pd.date_range(
            config["study_period"]["start"],
            config["study_period"]["end"],
            freq="D",
        )
    ) * len(config["regions"])
    check(len(weather) == expected_days, "Unexpected region-day count")
    check(
        not weather.duplicated(["region", "date"]).any(),
        "Duplicate region-date weather records",
    )
    check(weather["precip_mm"].notna().all(), "Missing precipitation observations")

    threshold = float(config["primary_rain_threshold_mm"])
    for _, group in weather.groupby("region", sort=False):
        group = group.sort_values("date")
        precipitation = group["precip_mm"].to_numpy(dtype=float)
        expected_dry_spell = dry_spell_before(precipitation, threshold)
        check(
            np.array_equal(
                group["dry_spell"].to_numpy(dtype=int), expected_dry_spell
            ),
            "Dry-spell values use information beyond the prior day",
        )
        expected_roll = (
            pd.Series(precipitation).shift(1).rolling(30, min_periods=25).sum()
        )
        check(
            np.allclose(
                group["roll30_mm"].to_numpy(dtype=float),
                expected_roll.to_numpy(dtype=float),
                equal_nan=True,
            ),
            "Rolling deficits are not prior-data-only",
        )
        for rain_threshold in (0.1, 1.0, 5.0):
            rain = precipitation >= rain_threshold
            for window in config["success_windows_days"]:
                expected = np.zeros(len(group), dtype=int)
                for lag in range(1, int(window) + 1):
                    expected[:-lag] |= rain[lag:]
                column = f"success_{rain_threshold:g}mm_{window}d"
                check(
                    np.array_equal(group[column].to_numpy(dtype=int), expected),
                    f"Outcome mismatch or event-day leakage in {column}",
                )

    hazards = pd.read_csv(ANALYSIS / "training_hazards.csv")
    recomputed = estimate_training_hazards(weather.copy(), config)
    compare_frames(
        hazards,
        recomputed,
        ["region", "month", "dry_bin"],
    )
    return {
        "region_days": len(weather),
        "locations": weather["region"].nunique(),
        "missing_precipitation": int(weather["precip_mm"].isna().sum()),
        "training_hazard_rows": len(hazards),
    }


def audit_events(config: dict) -> dict[str, object]:
    events = pd.read_csv(ANALYSIS / "pseudo_events.csv", parse_dates=["date"])
    cutoff = pd.Timestamp(config["study_period"]["end"]) - pd.Timedelta(
        days=max(config["success_windows_days"])
    )
    check(
        events["date"].gt(pd.Timestamp(config["training_end"])).all(),
        "Training-period event found",
    )
    check(events["date"].le(cutoff).all(), "Incomplete follow-up event found")
    hazard_columns = [
        column
        for column in events
        if column.startswith("success_1mm_") and column.endswith("_mean")
    ]
    check(hazard_columns and events[hazard_columns].notna().all().all(), "Missing hazard")

    hazards = pd.read_csv(ANALYSIS / "training_hazards.csv")
    threshold_by_region = (
        hazards.groupby("region", observed=True)["success_1mm_7d_mean"]
        .quantile(0.75)
        .to_dict()
    )
    high = events[events["rule"] == "high prospective hazard"]
    check(
        (
            high["success_1mm_7d_mean"]
            >= high["region"].map(threshold_by_region)
        ).all(),
        "High-hazard event below a training-derived threshold",
    )

    model_data = events.dropna(
        subset=[
            "success_1mm_7d",
            "scenario_wtp",
            "success_1mm_7d_mean",
            "drought_severity",
        ]
    )
    cluster = pd.read_csv(ANALYSIS / "cluster_robust_price_success.csv")
    check(cluster["n"].eq(len(model_data)).all(), "Regression sample mismatch")
    check(
        cluster["clusters"].eq(
            (model_data["region"] + "_" + model_data["year"].astype(str)).nunique()
        ).all(),
        "Region-year cluster-count mismatch",
    )
    check(
        cluster["region_rule_clusters"].eq(
            (model_data["region"] + "_" + model_data["rule"]).nunique()
        ).all(),
        "Region-rule cluster-count mismatch",
    )
    permutation = pd.read_csv(
        ANALYSIS / "price_permutation_falsification.csv"
    ).iloc[0]
    check(permutation["permutations"] == 1000, "Permutation-count mismatch")
    check(
        0 <= permutation["permutation_p_two_sided"] <= 1,
        "Invalid permutation p-value",
    )
    return {
        "pseudo_events": len(events),
        "regression_n": len(model_data),
        "region_year_clusters": int(cluster["clusters"].iloc[0]),
        "region_rule_clusters": int(cluster["region_rule_clusters"].iloc[0]),
        "permutation_strata": int(
            model_data.groupby(["region", "month", "rule"]).ngroups
        ),
        "permutations": int(permutation["permutations"]),
    }


def audit_simulation(config: dict) -> dict[str, object]:
    simulations = pd.read_csv(RESULTS / "simulation_replications.csv.gz")
    expected_rows = int(config["replications_per_model"]) * len(config["models"])
    check(len(simulations) == expected_rows, "Principal simulation row-count mismatch")
    check(
        simulations.groupby("model").size().eq(config["replications_per_model"]).all(),
        "Unequal model replication counts",
    )
    check(
        simulations.groupby("replication")["weather_draw"].nunique().eq(1).all(),
        "Models do not share the same sampled weather-year draw within replication",
    )
    fixed = simulations[simulations["model"].isin(config["models"][:4])]
    check(
        np.allclose(
            fixed["mean_price"].dropna(),
            float(config["parameters"]["fixed_price"]),
        ),
        "Fixed-price models contain varying prices",
    )
    check(
        fixed["price_success_difference"].dropna().eq(0).all(),
        "Fixed-price models have nonzero price-success differences",
    )
    check(
        fixed["provider_price_dispersion"].dropna().eq(0).all(),
        "Fixed-price models have provider price dispersion",
    )
    check(
        np.allclose(
            simulations["provider_resource_cost"],
            float(config["parameters"]["provider_cost"]) * simulations["events"],
        ),
        "Provider resource-cost identity failed",
    )
    check(
        np.allclose(
            simulations["provider_revenue"],
            simulations["community_expenditure"],
        ),
        "Transfer identity failed",
    )
    check(
        np.allclose(
            simulations["provider_profit"],
            simulations["provider_revenue"]
            - simulations["provider_resource_cost"],
        ),
        "Provider-profit identity failed",
    )
    check(
        np.allclose(
            simulations["total_social_surplus"],
            simulations["provider_profit"]
            + simulations["community_material_social_utility"],
        ),
        "Social-surplus identity failed",
    )

    generated_summary = pd.read_csv(RESULTS / "simulation_summary.csv")
    recomputed_summary = summarize(simulations)
    compare_frames(generated_summary, recomputed_summary, ["model", "outcome"])
    convergence = pd.read_csv(RESULTS / "simulation_convergence.csv")
    max_mcse = convergence[
        (convergence["sample_size"] == config["replications_per_model"])
        & (convergence["outcome"] == "apparent_success")
    ]["monte_carlo_se"].max()
    check(max_mcse < 0.003, "Principal apparent-success MCSE exceeds 0.003")
    return {
        "seed": int(config["seed"]),
        "replications": len(simulations),
        "replications_per_model": int(config["replications_per_model"]),
        "models": len(config["models"]),
        "providers": int(config["providers"]),
        "max_apparent_success_mcse": float(max_mcse),
    }


def audit_manuscript() -> dict[str, object]:
    manuscript = (ROOT / "manuscript" / "manuscript.md").read_text()
    metrics = json.loads(
        (ROOT / "manuscript" / "manuscript_metrics.json").read_text()
    )
    check(metrics["main_text_words_excluding_references"] <= 8000, "Word limit")
    check(metrics["abstract_words"] <= 250, "Abstract limit")
    check(metrics["max_highlight_characters"] <= 85, "Highlight limit")
    check(
        not re.search(r"\{\{(?!FIGURE_|TABLE_)[A-Z0-9_]+\}\}", manuscript),
        "Unresolved manuscript value token",
    )
    sections = {
        "abstract": manuscript.split("## Abstract", 1)[1].split("## 1.", 1)[0],
        "introduction": manuscript.split("## 1. Introduction", 1)[1].split(
            "## 2.", 1
        )[0],
        "results": manuscript.split("## 4. Results", 1)[1].split("## 5.", 1)[0],
        "discussion": manuscript.split("## 5. Discussion", 1)[1].split(
            "## 6.", 1
        )[0],
        "conclusion": manuscript.split("## 6. Conclusion", 1)[1].split(
            "## References", 1
        )[0],
    }
    for name, text in sections.items():
        normalized = text.lower().replace("–", "-")
        check("price-success" in normalized, f"Price-success result absent from {name}")
        check(
            "negative" in normalized
            or "not supported" in normalized
            or re.search(r"-[0-9]", normalized),
            f"Unfavorable price-success result unclear in {name}",
        )
    cover = (ROOT / "manuscript" / "cover_letter.md").read_text().lower()
    check(
        "negative mean contemporaneous price–success differences" in cover,
        "Unfavorable result absent from cover letter",
    )
    archive_path = (
        ROOT
        / "manuscript"
        / "pricing_apparent_environmental_performance_submission.zip"
    )
    with zipfile.ZipFile(archive_path) as archive:
        archive_names = archive.namelist()
    check(
        not any(name.startswith("data/raw/") for name in archive_names),
        "Raw or restricted source included in submission archive",
    )
    return {
        **metrics,
        "submission_archive_files": len(archive_names),
        "author_actions_required": True,
    }


def main() -> None:
    region_config = yaml.safe_load(
        (ROOT / "config" / "regions.yml").read_text(encoding="utf-8")
    )
    simulation_config = yaml.safe_load(
        (ROOT / "config" / "simulation.yml").read_text(encoding="utf-8")
    )
    payload = {
        "status": "passed",
        "weather": audit_weather(region_config),
        "events_and_inference": audit_events(region_config),
        "simulation": audit_simulation(simulation_config),
        "manuscript_and_package": audit_manuscript(),
    }
    destination = RESULTS / "final_audit.json"
    destination.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"Final statistical, numerical, and package audit passed: {destination}")


if __name__ == "__main__":
    main()
