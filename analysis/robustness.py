from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import yaml

from simulation.run_simulation import load_weather_years, simulate_one


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"
RESULTS = ROOT / "results"


def empirical_robustness() -> None:
    events = pd.read_csv(ANALYSIS / "pseudo_events.csv")
    events["region_year"] = events["region"] + "_" + events["year"].astype(str)
    events["region_rule"] = events["region"] + "_" + events["rule"]
    data = events.dropna(
        subset=[
            "success_1mm_7d",
            "scenario_wtp",
            "success_1mm_7d_mean",
            "drought_severity",
        ]
    ).reset_index(drop=True)
    cluster_groups = np.column_stack(
        [
            pd.Categorical(data["region_year"]).codes,
            pd.Categorical(data["region_rule"]).codes,
        ]
    )
    model = smf.logit(
        "success_1mm_7d ~ scenario_wtp + success_1mm_7d_mean + "
        "drought_severity + C(region) + C(month) + C(rule)",
        data=data,
    ).fit(
        disp=False,
        maxiter=200,
        cov_type="cluster",
        cov_kwds={"groups": cluster_groups},
    )
    rows = []
    for term in ["scenario_wtp", "success_1mm_7d_mean", "drought_severity"]:
        rows.append(
            {
                "term": term,
                "coefficient": model.params[term],
                "cluster_standard_error": model.bse[term],
                "ci_low": model.conf_int().loc[term, 0],
                "ci_high": model.conf_int().loc[term, 1],
                "p_value": model.pvalues[term],
                "clusters": data["region_year"].nunique(),
                "region_rule_clusters": data["region_rule"].nunique(),
                "n": len(data),
            }
        )
    pd.DataFrame(rows).to_csv(
        ANALYSIS / "cluster_robust_price_success.csv", index=False
    )

    outcome_columns = [
        column
        for column in events.columns
        if column.startswith("success_")
        and not column.endswith("_mean")
        and column.rsplit("_", 1)[-1].endswith("d")
    ]
    sensitivity = (
        events.groupby("rule", observed=True)[outcome_columns]
        .mean()
        .reset_index()
        .melt(id_vars="rule", var_name="outcome", value_name="apparent_success")
    )
    sensitivity.to_csv(
        ANALYSIS / "threshold_window_sensitivity.csv", index=False
    )

    strata = [
        indices.to_numpy()
        for _, indices in data.groupby(["region", "month", "rule"]).groups.items()
    ]

    def within_strata(values: np.ndarray) -> np.ndarray:
        centered = values.copy()
        for indices in strata:
            centered[indices] -= centered[indices].mean()
        return centered

    matrix = np.column_stack(
        [
            within_strata(data["success_1mm_7d_mean"].to_numpy(dtype=float)),
            within_strata(data["drought_severity"].to_numpy(dtype=float)),
        ]
    )
    inverse = np.linalg.pinv(matrix)
    outcome = within_strata(data["success_1mm_7d"].to_numpy(dtype=float))
    price = data["scenario_wtp"].to_numpy(dtype=float)
    outcome_residual = outcome - matrix @ (inverse @ outcome)

    def coefficient(values: np.ndarray) -> float:
        centered = within_strata(values)
        residual = centered - matrix @ (inverse @ centered)
        return float(
            np.dot(residual, outcome_residual) / np.dot(residual, residual)
        )

    observed = coefficient(price)
    rng = np.random.default_rng(20260924)
    permutations = []
    for _ in range(1000):
        permuted = price.copy()
        for indices in strata:
            permuted[indices] = rng.permutation(permuted[indices])
        permutations.append(coefficient(permuted))
    permutation_array = np.asarray(permutations)
    pd.DataFrame(
        {
            "observed_adjusted_ols_coefficient": [observed],
            "permutation_mean": [permutation_array.mean()],
            "permutation_sd": [permutation_array.std(ddof=1)],
            "permutation_p_two_sided": [
                (np.sum(np.abs(permutation_array) >= abs(observed)) + 1) / 1001
            ],
            "permutations": [1000],
        }
    ).to_csv(ANALYSIS / "price_permutation_falsification.csv", index=False)


def convergence() -> None:
    simulations = pd.read_csv(RESULTS / "simulation_replications.csv.gz")
    rows = []
    for model, group in simulations.groupby("model", sort=False):
        for sample_size in [500, 1000, 2500, 5000, 10000]:
            subset = group.iloc[:sample_size]
            for outcome in [
                "apparent_success",
                "mean_price",
                "reputation_dispersion",
            ]:
                values = subset[outcome].dropna()
                rows.append(
                    {
                        "model": model,
                        "sample_size": sample_size,
                        "outcome": outcome,
                        "mean": values.mean(),
                        "monte_carlo_se": values.std() / np.sqrt(len(values)),
                    }
                )
    pd.DataFrame(rows).to_csv(RESULTS / "simulation_convergence.csv", index=False)


def parameter_sensitivity() -> None:
    config = yaml.safe_load(
        (ROOT / "config" / "simulation.yml").read_text(encoding="utf-8")
    )
    base = config["parameters"]
    weather_years = load_weather_years()
    scenarios = [
        ("M3_selection_slope_2", 3, {"selection_slope": 2.0}),
        ("M3_selection_slope_5", 3, {"selection_slope": 5.0}),
        ("M3_selection_slope_8", 3, {"selection_slope": 8.0}),
        ("M4_prior_mean_0.25", 4, {"prior_mean": 0.25}),
        ("M4_prior_mean_0.50", 4, {"prior_mean": 0.50}),
        ("M4_prior_mean_0.75", 4, {"prior_mean": 0.75}),
        (
            "M5_balanced_memory",
            5,
            {"selective_success_weight": 1.0, "selective_failure_weight": 1.0},
        ),
        (
            "M5_base_memory",
            5,
            {"selective_success_weight": 1.5, "selective_failure_weight": 0.6},
        ),
        (
            "M5_strong_selective_memory",
            5,
            {"selective_success_weight": 2.0, "selective_failure_weight": 0.3},
        ),
    ]
    seed_sequence = np.random.SeedSequence(20260925)
    weather_seed, simulation_seed = seed_sequence.spawn(2)
    weather_rng = np.random.default_rng(weather_seed)
    weather_indices = weather_rng.integers(0, len(weather_years), size=2000)
    simulation_seeds = simulation_seed.spawn(2000 * len(scenarios))
    rows = []
    for replication, weather_index in enumerate(weather_indices):
        weather_year = weather_years[int(weather_index)]
        for scenario_index, (scenario, model_index, changes) in enumerate(
            scenarios
        ):
            parameters = {**base, **changes}
            rng = np.random.default_rng(
                simulation_seeds[
                    replication * len(scenarios) + scenario_index
                ]
            )
            row = simulate_one(
                model_index,
                weather_year,
                rng,
                parameters,
                int(config["providers"]),
            )
            row["weather_draw"] = int(weather_index)
            row["scenario"] = scenario
            row["replication"] = replication
            rows.append(row)
    results = pd.DataFrame(rows)
    results.to_csv(
        RESULTS / "simulation_sensitivity_replications.csv.gz",
        index=False,
        compression={"method": "gzip", "compresslevel": 6, "mtime": 0},
    )
    summary_rows = []
    for scenario, group in results.groupby("scenario", sort=False):
        for outcome in [
            "events",
            "apparent_success",
            "mean_price",
            "price_success_difference",
            "reputation_dispersion",
            "provider_revenue",
        ]:
            values = group[outcome].dropna()
            summary_rows.append(
                {
                    "scenario": scenario,
                    "outcome": outcome,
                    "mean": values.mean(),
                    "ci_low": values.quantile(0.025),
                    "ci_high": values.quantile(0.975),
                    "n": len(values),
                }
            )
    pd.DataFrame(summary_rows).to_csv(
        RESULTS / "simulation_sensitivity_summary.csv", index=False
    )


def hypothesis_classification() -> None:
    rows = [
        {
            "hypothesis": (
                "Natural rainfall can generate substantial apparent success under "
                "zero efficacy"
            ),
            "classification": "demonstrated with observed weather",
            "basis": "Observed-weather pseudo-events and all simulation models",
        },
        {
            "hypothesis": "Drought-driven demand increases intervention frequency",
            "classification": "demonstrated in model",
            "basis": "M1 versus M0 under the specified demand function",
        },
        {
            "hypothesis": "Drought can increase scenario WTP",
            "classification": "demonstrated in calibrated scenario",
            "basis": (
                "Calibrated rainfall-loss term raises WTP over intermediate drought "
                "severity but is offset at extremes by ability to pay"
            ),
        },
        {
            "hypothesis": (
                "Strategic provider selection increases apparent success"
            ),
            "classification": "demonstrated in model using observed weather",
            "basis": "M3 versus M2 and selection-slope sensitivity",
        },
        {
            "hypothesis": (
                "Higher prices are positively associated with apparent success"
            ),
            "classification": "not supported",
            "basis": (
                "Two-way clustered logit interval includes zero; within-stratum "
                "permutation estimate and M4-M5 differences are negative"
            ),
        },
        {
            "hypothesis": (
                "Reputation learning creates persistent provider differentiation"
            ),
            "classification": "demonstrated in model",
            "basis": "M4-M5 reputation dispersion under specified update rules",
        },
        {
            "hypothesis": (
                "Selective and recency-weighted memory raises price premia"
            ),
            "classification": "demonstrated in model",
            "basis": "M5 versus M4 and memory sensitivity",
        },
        {
            "hypothesis": (
                "Zero meteorological efficacy implies zero social value"
            ),
            "classification": "logical distinction; not empirically tested",
            "basis": (
                "Positive social utility is modeled separately from causal "
                "rainfall benefit"
            ),
        },
    ]
    pd.DataFrame(rows).to_csv(
        RESULTS / "hypothesis_classification.csv", index=False
    )


def run() -> None:
    empirical_robustness()
    convergence()
    parameter_sensitivity()
    hypothesis_classification()
    print("Completed empirical and simulation robustness analyses")


if __name__ == "__main__":
    run()
