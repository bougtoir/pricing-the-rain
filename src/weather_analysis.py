from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "regions.yml"
PROCESSED = ROOT / "data" / "processed"
ANALYSIS = ROOT / "analysis"
FIGURES = ROOT / "figures"
TABLES = ROOT / "tables"


def dry_spell_before(values: np.ndarray, threshold: float) -> np.ndarray:
    counts = np.zeros(len(values), dtype=int)
    running = 0
    for index, value in enumerate(values):
        counts[index] = running
        running = running + 1 if value < threshold else 0
    return counts


def load_weather() -> tuple[pd.DataFrame, dict]:
    config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    threshold = float(config["primary_rain_threshold_mm"])
    rows = []
    for region in config["regions"]:
        path = ROOT / "data" / "raw" / "weather" / (
            f"{region['id']}_era5_1991_2020.json"
        )
        payload = json.loads(path.read_text(encoding="utf-8"))
        frame = pd.DataFrame(
            {
                "date": pd.to_datetime(payload["daily"]["time"]),
                "precip_mm": pd.to_numeric(
                    payload["daily"]["precipitation_sum"], errors="coerce"
                ),
            }
        )
        frame["region"] = region["id"]
        frame["region_name"] = region["name"]
        frame["regime"] = region["regime"]
        frame["dry_spell"] = dry_spell_before(
            frame["precip_mm"].fillna(0).to_numpy(), threshold
        )
        frame["roll30_mm"] = (
            frame["precip_mm"]
            .shift(1)
            .rolling(30, min_periods=25)
            .sum()
            .to_numpy()
        )
        rows.append(frame)
    weather = pd.concat(rows, ignore_index=True)
    weather["month"] = weather["date"].dt.month
    weather["year"] = weather["date"].dt.year
    weather["dry_bin"] = pd.cut(
        weather["dry_spell"],
        bins=[-1, 2, 5, 9, 19, np.inf],
        labels=["0–2", "3–5", "6–9", "10–19", "20+"],
    ).astype(str)
    return weather, config


def add_drought_and_outcomes(weather: pd.DataFrame, config: dict) -> pd.DataFrame:
    training_end = pd.Timestamp(config["training_end"])
    train = weather["date"] <= training_end
    climatology = (
        weather.loc[train]
        .groupby(["region", "month"], observed=True)["roll30_mm"]
        .agg(["mean", "std"])
        .reset_index()
        .rename(columns={"mean": "roll30_mean", "std": "roll30_sd"})
    )
    weather = weather.merge(climatology, on=["region", "month"], how="left")
    weather["drought_z"] = (
        (weather["roll30_mm"] - weather["roll30_mean"])
        / weather["roll30_sd"].replace(0, np.nan)
    )
    weather["drought_severity"] = (-weather["drought_z"]).clip(lower=0, upper=4)
    for threshold in (0.1, 1.0, 5.0):
        rain = weather["precip_mm"] >= threshold
        for window in config["success_windows_days"]:
            future = pd.Series(False, index=weather.index)
            for lag in range(1, window + 1):
                future |= (
                    rain.groupby(weather["region"], observed=True)
                    .shift(-lag)
                    .astype("boolean")
                    .fillna(False)
                    .astype(bool)
                )
            weather[f"success_{threshold:g}mm_{window}d"] = future.astype(int)
    return weather


def estimate_training_hazards(weather: pd.DataFrame, config: dict) -> pd.DataFrame:
    training_cutoff = pd.Timestamp(config["training_end"]) - pd.Timedelta(
        days=max(config["success_windows_days"])
    )
    training = weather[weather["date"] <= training_cutoff]
    outcomes = [
        f"success_1mm_{window}d" for window in config["success_windows_days"]
    ]
    hazards = (
        training.groupby(["region", "month", "dry_bin"], observed=True)[outcomes]
        .agg(["mean", "count"])
        .reset_index()
    )
    hazards.columns = [
        "_".join(str(value) for value in column if value)
        if isinstance(column, tuple)
        else column
        for column in hazards.columns
    ]
    region_month = (
        training.groupby(["region", "month"], observed=True)[outcomes]
        .mean()
        .reset_index()
    )
    for outcome in outcomes:
        hazard_col = f"{outcome}_mean"
        count_col = f"{outcome}_count"
        hazards[hazard_col] = hazards[hazard_col].where(
            hazards[count_col] >= 20
        )
        fallback = region_month.rename(columns={outcome: f"{outcome}_fallback"})
        hazards = hazards.merge(fallback, on=["region", "month"], how="left")
        hazards[hazard_col] = hazards[hazard_col].fillna(
            hazards[f"{outcome}_fallback"]
        )
        hazards = hazards.drop(columns=[f"{outcome}_fallback"])
    return hazards


def choose_events(weather: pd.DataFrame, hazards: pd.DataFrame, config: dict) -> pd.DataFrame:
    evaluation_cutoff = pd.Timestamp(config["study_period"]["end"]) - pd.Timedelta(
        days=max(config["success_windows_days"])
    )
    evaluation = weather[
        (weather["date"] > pd.Timestamp(config["training_end"]))
        & (weather["date"] <= evaluation_cutoff)
    ].copy()
    hazard_columns = [
        f"success_1mm_{window}d_mean" for window in config["success_windows_days"]
    ]
    evaluation = evaluation.merge(
        hazards[["region", "month", "dry_bin", *hazard_columns]],
        on=["region", "month", "dry_bin"],
        how="left",
    )
    training_cutoff = pd.Timestamp(config["training_end"]) - pd.Timedelta(
        days=max(config["success_windows_days"])
    )
    training = weather[weather["date"] <= training_cutoff]
    fallback_columns = {
        f"success_1mm_{window}d": f"success_1mm_{window}d_fallback"
        for window in config["success_windows_days"]
    }
    region_month_fallback = (
        training.groupby(["region", "month"], observed=True)[
            list(fallback_columns)
        ]
        .mean()
        .rename(columns=fallback_columns)
        .reset_index()
    )
    evaluation = evaluation.merge(
        region_month_fallback,
        on=["region", "month"],
        how="left",
    )
    for window in config["success_windows_days"]:
        hazard = f"success_1mm_{window}d_mean"
        fallback = f"success_1mm_{window}d_fallback"
        evaluation[hazard] = evaluation[hazard].fillna(evaluation[fallback])
    evaluation = evaluation.drop(columns=list(fallback_columns.values()))
    evaluation = evaluation.sort_values(["region", "date"]).reset_index(drop=True)
    evaluation["previous_dry_spell"] = evaluation.groupby("region")[
        "dry_spell"
    ].shift(1)
    evaluation["previous_drought"] = evaluation.groupby("region")[
        "drought_severity"
    ].shift(1)
    rng = np.random.default_rng(20260924)
    event_frames = []

    dry = evaluation[
        (evaluation["dry_spell"] >= 7) & (evaluation["previous_dry_spell"] < 7)
    ].copy()
    dry["rule"] = "dry-spell threshold"
    event_frames.append(dry)

    deficit = evaluation[
        (evaluation["drought_severity"] >= 1)
        & (evaluation["previous_drought"] < 1)
    ].copy()
    deficit["rule"] = "30-day deficit threshold"
    event_frames.append(deficit)

    drought_pool = evaluation[
        (evaluation["dry_spell"] >= 4) | (evaluation["drought_severity"] >= 0.5)
    ]
    random_parts = []
    for region, group in drought_pool.groupby("region"):
        target = max(
            1,
            int(
                (
                    dry["region"].eq(region).sum()
                    + deficit["region"].eq(region).sum()
                )
                / 2
            ),
        )
        sample = group.sample(
            n=min(target, len(group)), random_state=int(rng.integers(1, 2**31 - 1))
        )
        random_parts.append(sample)
    random_drought = pd.concat(random_parts)
    random_drought["rule"] = "random drought day"
    event_frames.append(random_drought)

    training_thresholds = (
        hazards.groupby("region", observed=True)["success_1mm_7d_mean"]
        .quantile(0.75)
        .to_dict()
    )
    threshold_by_region = evaluation["region"].map(training_thresholds)
    high_hazard = (
        (evaluation["success_1mm_7d_mean"] >= threshold_by_region)
        & (evaluation["drought_severity"] >= 0.5)
    )
    previous_high = (
        high_hazard.groupby(evaluation["region"])
        .shift(1)
        .astype("boolean")
        .fillna(False)
        .astype(bool)
    )
    strategic = evaluation[high_hazard & ~previous_high].copy()
    strategic["rule"] = "high prospective hazard"
    event_frames.append(strategic)

    placebo_parts = []
    candidate = evaluation[
        (evaluation["drought_severity"] < 0.25) & (evaluation["dry_spell"] < 3)
    ]
    for _, event in dry.iterrows():
        pool = candidate[
            (candidate["region"] == event["region"])
            & (candidate["month"] == event["month"])
            & (candidate["year"] == event["year"])
        ]
        if pool.empty:
            pool = candidate[
                (candidate["region"] == event["region"])
                & (candidate["month"] == event["month"])
            ]
        if not pool.empty:
            placebo_parts.append(
                pool.sample(
                    n=1, random_state=int(rng.integers(1, 2**31 - 1))
                )
            )
    if placebo_parts:
        placebo = pd.concat(placebo_parts).drop_duplicates(["region", "date"])
        placebo["rule"] = "season-matched placebo"
        event_frames.append(placebo)

    events = pd.concat(event_frames, ignore_index=True)
    events = events.drop_duplicates(["region", "date", "rule"]).sort_values(
        ["date", "region", "rule"]
    )
    return add_observer_prices(events, hazards)


def add_observer_prices(
    events: pd.DataFrame, hazards: pd.DataFrame
) -> pd.DataFrame:
    events = events.copy()
    events["observer_mean_before"] = np.nan
    events["perceived_delta_before"] = np.nan
    events["scenario_wtp"] = np.nan
    states: dict[tuple[str, str], list[float]] = {}
    regional_q = (
        hazards.groupby("region", observed=True)["success_1mm_7d_mean"]
        .mean()
        .to_dict()
    )
    for index, row in events.iterrows():
        key = (row["region"], row["rule"])
        alpha, beta = states.get(key, [1.0, 1.0])
        belief = alpha / (alpha + beta)
        delta = max(0.0, belief - regional_q[row["region"]])
        social_utility = 3.0
        rainfall_value = 20.0 * (1.0 + 0.5 * row["drought_severity"])
        ability_to_pay = 1.0 / (1.0 + 0.12 * row["drought_severity"] ** 2)
        wtp = ability_to_pay * (rainfall_value * delta + social_utility)
        events.at[index, "observer_mean_before"] = belief
        events.at[index, "perceived_delta_before"] = delta
        events.at[index, "scenario_wtp"] = wtp
        outcome = float(row["success_1mm_7d"])
        states[key] = [alpha + outcome, beta + 1.0 - outcome]
    return events


def summarize(
    events: pd.DataFrame, weather: pd.DataFrame, config: dict
) -> None:
    ANALYSIS.mkdir(parents=True, exist_ok=True)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    weather.to_csv(
        PROCESSED / "daily_weather_features.csv.gz",
        index=False,
        compression={"method": "gzip", "compresslevel": 6, "mtime": 0},
    )
    events.to_csv(ANALYSIS / "pseudo_events.csv", index=False)

    success_columns = [
        column
        for column in events.columns
        if column.startswith("success_") and not column.endswith("_mean")
    ]
    summary = (
        events.groupby(["rule", "region"], observed=True)[success_columns]
        .agg(["mean", "count"])
        .reset_index()
    )
    summary.columns = [
        "_".join(str(value) for value in column if value)
        if isinstance(column, tuple)
        else column
        for column in summary.columns
    ]
    summary.to_csv(ANALYSIS / "pseudo_event_success.csv", index=False)

    model_data = events.dropna(
        subset=[
            "success_1mm_7d",
            "scenario_wtp",
            "success_1mm_7d_mean",
            "drought_severity",
        ]
    ).copy()
    naive = smf.logit("success_1mm_7d ~ scenario_wtp", data=model_data).fit(
        disp=False
    )
    adjusted = smf.logit(
        "success_1mm_7d ~ scenario_wtp + success_1mm_7d_mean + "
        "drought_severity + C(region) + C(month) + C(rule)",
        data=model_data,
    ).fit(disp=False, maxiter=200)
    rows = []
    for name, model in [("naive", naive), ("hazard-adjusted", adjusted)]:
        for term in ["scenario_wtp", "success_1mm_7d_mean", "drought_severity"]:
            if term in model.params:
                rows.append(
                    {
                        "model": name,
                        "term": term,
                        "coefficient": model.params[term],
                        "standard_error": model.bse[term],
                        "ci_low": model.conf_int().loc[term, 0],
                        "ci_high": model.conf_int().loc[term, 1],
                        "p_value": model.pvalues[term],
                        "n": int(model.nobs),
                    }
                )
    pd.DataFrame(rows).to_csv(ANALYSIS / "price_success_models.csv", index=False)
    make_figures(weather, events, config)


def make_figures(
    weather: pd.DataFrame, events: pd.DataFrame, config: dict
) -> None:
    training_cutoff = pd.Timestamp(config["training_end"]) - pd.Timedelta(
        days=max(config["success_windows_days"])
    )
    train = weather[weather["date"] <= training_cutoff]
    hazard = (
        train.groupby(["region", "dry_bin"], observed=True)["success_1mm_7d"]
        .agg(["mean", "count"])
        .reset_index()
    )
    order = ["0–2", "3–5", "6–9", "10–19", "20+"]
    figure, axis = plt.subplots(figsize=(9.0, 5.8))
    for region, group in hazard.groupby("region"):
        group = group.set_index("dry_bin").reindex(order)
        axis.plot(order, group["mean"], marker="o", label=region.replace("_", " ").title())
    axis.set(
        xlabel="Preceding dry-spell duration (days, binned)",
        ylabel="Probability of ≥1 mm rain within 7 days",
        title="Empirical rainfall hazard is region-specific and not uniformly increasing",
    )
    axis.legend(ncol=2, fontsize=8, frameon=False)
    axis.grid(axis="y", alpha=0.25)
    figure.tight_layout()
    figure.savefig(FIGURES / "figure2_empirical_hazard.pdf")
    figure.savefig(FIGURES / "figure2_empirical_hazard.png", dpi=500)
    plt.close(figure)

    plot = (
        events.groupby("rule", observed=True)[
            ["success_1mm_1d", "success_1mm_3d", "success_1mm_7d", "success_1mm_14d"]
        ]
        .mean()
        .rename(
            columns={
                "success_1mm_1d": "1 day",
                "success_1mm_3d": "3 days",
                "success_1mm_7d": "7 days",
                "success_1mm_14d": "14 days",
            }
        )
    )
    figure, axis = plt.subplots(figsize=(9.0, 5.8))
    plot.plot(kind="bar", ax=axis)
    axis.set(
        xlabel="Fictional pseudo-intervention timing rule",
        ylabel="Apparent success proportion",
        title="Natural rainfall produces substantial apparent success under zero efficacy",
    )
    axis.legend(title="Attribution window", frameon=False)
    axis.tick_params(axis="x", rotation=20)
    axis.grid(axis="y", alpha=0.25)
    figure.tight_layout()
    figure.savefig(FIGURES / "figure3_pseudo_event_success.pdf")
    figure.savefig(FIGURES / "figure3_pseudo_event_success.png", dpi=500)
    plt.close(figure)


def run() -> None:
    weather, config = load_weather()
    weather = add_drought_and_outcomes(weather, config)
    hazards = estimate_training_hazards(weather, config)
    ANALYSIS.mkdir(parents=True, exist_ok=True)
    hazards.to_csv(ANALYSIS / "training_hazards.csv", index=False)
    events = choose_events(weather, hazards, config)
    summarize(events, weather, config)
    print(f"Analyzed {len(weather):,} region-days and {len(events):,} pseudo-events")


if __name__ == "__main__":
    run()
