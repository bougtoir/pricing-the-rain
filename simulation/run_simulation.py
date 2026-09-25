from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "simulation.yml"
WEATHER = ROOT / "data" / "processed" / "daily_weather_features.csv.gz"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"


@dataclass(frozen=True)
class WeatherYear:
    region: str
    rain: np.ndarray
    dry_spell: np.ndarray
    drought: np.ndarray
    hazard: np.ndarray


def expit(value: float) -> float:
    return 1.0 / (1.0 + np.exp(-value))


def load_weather_years() -> list[WeatherYear]:
    weather = pd.read_csv(WEATHER, parse_dates=["date"])
    weather = weather[weather["year"].between(2011, 2020)].copy()
    hazard = pd.read_csv(ROOT / "analysis" / "training_hazards.csv")
    weather = weather.merge(
        hazard[["region", "month", "dry_bin", "success_1mm_7d_mean"]],
        on=["region", "month", "dry_bin"],
        how="left",
    )
    years = []
    for (region, _), group in weather.groupby(["region", "year"], sort=True):
        group = group.sort_values("date")
        rain = (group["precip_mm"].to_numpy(dtype=float) >= 1.0).astype(int)
        future = np.zeros(len(group), dtype=int)
        for lag in range(1, 8):
            future[:-lag] |= rain[lag:]
        years.append(
            WeatherYear(
                region=region,
                rain=future,
                dry_spell=group["dry_spell"].to_numpy(dtype=float),
                drought=group["drought_severity"].fillna(0).to_numpy(dtype=float),
                hazard=group["success_1mm_7d_mean"]
                .fillna(group["success_1mm_7d_mean"].mean())
                .to_numpy(dtype=float),
            )
        )
    return years


def simulate_one(
    model_index: int,
    weather_year: WeatherYear,
    rng: np.random.Generator,
    parameters: dict[str, float],
    providers: int,
) -> dict[str, float | int | str]:
    outcomes = weather_year.rain.copy()
    if model_index < 2:
        outcomes = rng.permutation(outcomes)
    prior_mean = parameters["prior_mean"]
    prior_strength = parameters["prior_strength"]
    alpha = np.repeat(prior_mean * prior_strength, providers)
    beta = np.repeat((1.0 - prior_mean) * prior_strength, providers)
    memory = np.repeat(np.log(prior_mean / (1.0 - prior_mean)), providers)
    selectivity = np.linspace(-0.6, 0.6, providers)
    event_outcomes = []
    prices = []
    provider_ids = []
    accepted_requests = 0
    requests = 0

    for day in range(len(outcomes) - 7):
        drought = float(weather_year.drought[day])
        dry_spell = float(weather_year.dry_spell[day])
        hazard = (
            float(np.mean(outcomes))
            if model_index < 2
            else float(weather_year.hazard[day])
        )
        if model_index == 0:
            request_probability = parameters["random_request_probability"]
        else:
            request_probability = expit(-3.2 + 0.11 * dry_spell + 0.75 * drought)
        if rng.random() >= request_probability:
            continue
        requests += 1
        provider = int(rng.integers(0, providers))
        if model_index >= 3:
            acceptance_probability = expit(
                parameters["selection_intercept"]
                + parameters["selection_slope"] * (hazard - 0.5)
                + selectivity[provider]
            )
        else:
            acceptance_probability = 0.85
        if rng.random() >= acceptance_probability:
            continue
        accepted_requests += 1
        outcome = int(outcomes[day])
        if model_index < 4:
            price = parameters["fixed_price"]
        else:
            if model_index == 4:
                reputation = alpha[provider] / (alpha[provider] + beta[provider])
            else:
                reputation = expit(memory[provider])
            perceived_delta = max(0.0, reputation - hazard)
            rainfall_value = parameters["rainfall_value"] * (1.0 + 0.5 * drought)
            ability_to_pay = 1.0 / (1.0 + 0.12 * drought**2)
            willingness_to_pay = ability_to_pay * (
                parameters["social_utility"] + rainfall_value * perceived_delta
            )
            price = 0.8 * willingness_to_pay
        event_outcomes.append(outcome)
        prices.append(price)
        provider_ids.append(provider)
        if model_index == 4:
            alpha[provider] += outcome
            beta[provider] += 1 - outcome
        elif model_index == 5:
            increment = (
                parameters["selective_success_weight"]
                if outcome
                else -parameters["selective_failure_weight"]
            )
            memory[provider] = (
                parameters["recency"] * memory[provider] + increment
            )

    event_array = np.asarray(event_outcomes, dtype=float)
    price_array = np.asarray(prices, dtype=float)
    provider_array = np.asarray(provider_ids, dtype=int)
    if len(event_array):
        apparent_success = float(event_array.mean())
        mean_price = float(price_array.mean())
        success_prices = price_array[event_array == 1]
        failure_prices = price_array[event_array == 0]
        price_success_difference = (
            float(success_prices.mean() - failure_prices.mean())
            if len(success_prices) and len(failure_prices)
            else np.nan
        )
        provider_revenues = np.array(
            [price_array[provider_array == index].sum() for index in range(providers)]
        )
        provider_mean_prices = np.array(
            [
                price_array[provider_array == index].mean()
                if np.any(provider_array == index)
                else np.nan
                for index in range(providers)
            ]
        )
        observed_provider_prices = provider_mean_prices[
            ~np.isnan(provider_mean_prices)
        ]
        provider_price_dispersion = (
            float(np.std(observed_provider_prices))
            if len(observed_provider_prices) >= 2
            else np.nan
        )
    else:
        apparent_success = np.nan
        mean_price = np.nan
        price_success_difference = np.nan
        provider_revenues = np.zeros(providers)
        provider_price_dispersion = np.nan
    if model_index == 4:
        reputations = alpha / (alpha + beta)
    elif model_index == 5:
        reputations = 1.0 / (1.0 + np.exp(-memory))
    else:
        reputations = np.repeat(0.5, providers)
    total_expenditure = float(price_array.sum()) if len(price_array) else 0.0
    provider_cost = parameters["provider_cost"]
    social_utility = parameters["social_utility"]
    provider_resource_cost = provider_cost * accepted_requests
    return {
        "region": weather_year.region,
        "requests": requests,
        "events": accepted_requests,
        "apparent_success": apparent_success,
        "mean_price": mean_price,
        "price_success_difference": price_success_difference,
        "provider_price_dispersion": provider_price_dispersion,
        "reputation_dispersion": float(np.std(reputations)),
        "provider_revenue": total_expenditure,
        "community_expenditure": total_expenditure,
        "provider_resource_cost": provider_resource_cost,
        "provider_profit": total_expenditure - provider_resource_cost,
        "community_material_social_utility": (
            social_utility * accepted_requests - total_expenditure
        ),
        "total_social_surplus": (
            (social_utility - provider_cost) * accepted_requests
        ),
        "provider_revenue_dispersion": float(np.std(provider_revenues)),
    }


def summarize(results: pd.DataFrame) -> pd.DataFrame:
    outcomes = [
        "events",
        "apparent_success",
        "mean_price",
        "price_success_difference",
        "provider_price_dispersion",
        "reputation_dispersion",
        "provider_revenue",
        "community_expenditure",
        "provider_resource_cost",
        "provider_profit",
        "community_material_social_utility",
        "total_social_surplus",
        "provider_revenue_dispersion",
    ]
    rows = []
    for model, group in results.groupby("model", sort=False):
        for outcome in outcomes:
            values = group[outcome].dropna()
            rows.append(
                {
                    "model": model,
                    "outcome": outcome,
                    "mean": values.mean(),
                    "sd": values.std(),
                    "ci_low": values.quantile(0.025),
                    "ci_high": values.quantile(0.975),
                    "n": len(values),
                }
            )
    return pd.DataFrame(rows)


def make_figure(summary: pd.DataFrame, fixed_price: float) -> None:
    models = summary["model"].drop_duplicates().tolist()
    positions = np.arange(len(models))
    model_ticks = [model.split("_")[0] for model in models]
    figure, axes_grid = plt.subplots(3, 2, figsize=(7.4, 8.8))
    axes = axes_grid.ravel()

    def plot_metric(
        axis: plt.Axes,
        outcome: str,
        title: str,
        ylabel: str,
        color: str,
    ) -> None:
        part = summary[summary["outcome"] == outcome].set_index("model").loc[models]
        error = np.vstack(
            [part["mean"] - part["ci_low"], part["ci_high"] - part["mean"]]
        )
        axis.errorbar(
            positions,
            part["mean"],
            yerr=error,
            fmt="o-",
            capsize=2.5,
            color=color,
            linewidth=1.2,
            markersize=4,
        )
        axis.set_xticks(positions)
        axis.set_xticklabels(model_ticks, fontsize=8)
        axis.set_title(title, loc="left", fontsize=9.2, pad=5)
        axis.set_ylabel(ylabel, fontsize=8.2)
        axis.tick_params(axis="y", labelsize=8)
        axis.grid(axis="y", alpha=0.25, linewidth=0.6)

    plot_metric(
        axes[0], "events", "A. Accepted-event frequency", "Events", "#0072B2"
    )
    plot_metric(
        axes[1],
        "apparent_success",
        "B. Current apparent success",
        "Success proportion",
        "#009E73",
    )
    plot_metric(
        axes[2],
        "mean_price",
        "C. Mean simulated scenario price",
        "Scenario units",
        "#D55E00",
    )
    axes[2].axhline(
        fixed_price,
        color="#666666",
        linestyle="--",
        linewidth=1,
        label="Fixed-price baseline",
    )
    axes[2].legend(frameon=False, fontsize=7.2, loc="upper left")

    reputation = (
        summary[summary["outcome"] == "reputation_dispersion"]
        .set_index("model")
        .loc[models]
    )
    provider_price = (
        summary[summary["outcome"] == "provider_price_dispersion"]
        .set_index("model")
        .loc[models]
    )
    axes[3].plot(
        positions,
        reputation["mean"],
        "o-",
        color="#009E73",
        label="Reputation SD",
        linewidth=1.2,
        markersize=4,
    )
    axes[3].set_ylabel("Reputation SD", color="#009E73", fontsize=8.2)
    axes[3].tick_params(axis="y", labelcolor="#009E73", labelsize=8)
    price_axis = axes[3].twinx()
    price_axis.plot(
        positions,
        provider_price["mean"],
        "s--",
        color="#CC79A7",
        label="Provider-mean-price SD",
        linewidth=1.2,
        markersize=4,
    )
    price_axis.set_ylabel("Provider price SD", color="#CC79A7", fontsize=8.2)
    price_axis.tick_params(axis="y", labelcolor="#CC79A7", labelsize=8)
    axes[3].set_xticks(positions)
    axes[3].set_xticklabels(model_ticks, fontsize=8)
    axes[3].set_title(
        "D. Reputation and provider price heterogeneity",
        loc="left",
        fontsize=9.2,
        pad=5,
    )
    axes[3].grid(axis="y", alpha=0.25, linewidth=0.6)
    lines = axes[3].get_lines() + price_axis.get_lines()
    axes[3].legend(
        lines,
        [line.get_label() for line in lines],
        frameon=False,
        fontsize=7.2,
        loc="upper left",
    )

    plot_metric(
        axes[4],
        "price_success_difference",
        "E. Price(success) − price(failure)",
        "Scenario units",
        "#CC79A7",
    )
    axes[4].axhline(0, color="#333333", linewidth=1)

    axes[5].axis("off")
    axes[5].set_title(
        "F. Stock–flow interpretation", loc="left", fontsize=9.2, pad=5
    )
    axes[5].text(
        0.5,
        0.78,
        "Past attributed outcomes",
        ha="center",
        va="center",
        fontsize=8.5,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "#E6F4EA"},
    )
    axes[5].annotate(
        "",
        xy=(0.5, 0.59),
        xytext=(0.5, 0.70),
        arrowprops={"arrowstyle": "->", "color": "#333333"},
    )
    axes[5].text(
        0.5,
        0.51,
        "Reputation stock + current hazard\n→ simulated scenario price",
        ha="center",
        va="center",
        fontsize=8,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "#FCE8D5"},
    )
    axes[5].text(
        0.5,
        0.20,
        "Current hazard → natural rainfall\n→ current apparent success",
        ha="center",
        va="center",
        fontsize=8,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "#E5F1FA"},
    )
    axes[5].text(
        0.5,
        0.02,
        "No pseudo-event-to-rainfall effect",
        ha="center",
        va="bottom",
        fontsize=7.5,
        color="#555555",
    )

    for axis in [axes[0], axes[1]]:
        axis.axvline(1.5, color="#777777", linestyle=":", linewidth=1)
    figure.suptitle(
        "Sequential model enrichment under an exact zero rainfall effect",
        fontsize=11.5,
    )
    figure.tight_layout(rect=(0, 0, 1, 0.975), h_pad=1.3, w_pad=1.4)
    figure.savefig(
        FIGURES / "figure4_simulation_decomposition.pdf", bbox_inches="tight"
    )
    figure.savefig(
        FIGURES / "figure4_simulation_decomposition.png",
        dpi=600,
        bbox_inches="tight",
    )
    plt.close(figure)


def run() -> None:
    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    weather_years = load_weather_years()
    rows = []
    replications = int(config["replications_per_model"])
    seed_sequence = np.random.SeedSequence(config["seed"])
    weather_seed, simulation_seed = seed_sequence.spawn(2)
    weather_rng = np.random.default_rng(weather_seed)
    weather_indices = weather_rng.integers(
        0, len(weather_years), size=replications
    )
    simulation_seeds = simulation_seed.spawn(
        replications * len(config["models"])
    )
    for replication, weather_index in enumerate(weather_indices):
        weather_year = weather_years[int(weather_index)]
        for model_index, model in enumerate(config["models"]):
            rng = np.random.default_rng(
                simulation_seeds[
                    replication * len(config["models"]) + model_index
                ]
            )
            row = simulate_one(
                model_index,
                weather_year,
                rng,
                config["parameters"],
                int(config["providers"]),
            )
            row["weather_draw"] = int(weather_index)
            row["model"] = model
            row["replication"] = replication
            rows.append(row)
    results = pd.DataFrame(rows)
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    results.to_csv(
        RESULTS / "simulation_replications.csv.gz",
        index=False,
        compression={"method": "gzip", "compresslevel": 6, "mtime": 0},
    )
    summary = summarize(results)
    summary.to_csv(RESULTS / "simulation_summary.csv", index=False)
    make_figure(summary, float(config["parameters"]["fixed_price"]))
    print(
        f"Completed {len(results):,} simulations "
        f"({replications:,} per model)"
    )


if __name__ == "__main__":
    run()
