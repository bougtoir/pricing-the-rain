from __future__ import annotations

import json
from pathlib import Path

import cairosvg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import yaml
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from PIL import Image
from pptx import Presentation
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches as PptxInches
from pptx.util import Pt as PptxPt


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
TABLES = ROOT / "tables"
RESULTS = ROOT / "results"
ANALYSIS = ROOT / "analysis"
TABLES.mkdir(exist_ok=True)

MODEL_LABELS = {
    "M0_random_timing": "M0 Random timing",
    "M1_drought_demand": "M1 Drought demand",
    "M2_realistic_hazard": "M2 Realistic hazard",
    "M3_strategic_selection": "M3 Selective acceptance",
    "M4_bayesian_reputation": "M4 Bayesian reputation",
    "M5_selective_recency": "M5 Selective/recency memory",
}

FIGURE_CAPTIONS = {
    "Figure 1": (
        "Conceptual framework. Baseline environmental hazard enters demand, provider "
        "acceptance, valuation, attribution, and reputation, while the "
        "pseudo-intervention never changes rainfall."
    ),
    "Figure 2": (
        "Natural rainfall following fictional known-zero-effect stress tests in "
        "2011–2020, shown as apparent success by prospective event-selection rule. "
        "Apparent successes are observed rainfall events; causal attribution to "
        "intervention is false by construction."
    ),
    "Figure 3": (
        "Estimated seven-day rainfall hazards by preceding dry-spell duration and "
        "location in the 1991–2010 training period. The eight locations are "
        "pre-specified mechanism stress tests, not a representative global sample."
    ),
    "Figure 4": (
        "Four-layer separation in the generic rare-event simulation. "
        "Panel A compares the objective probability, experienced frequency, "
        "subjective probability, and price-implied index under endogenous "
        "observation across rarity regimes; panel B "
        "shows the absolute selection gap p_ref − p_obj and the selection ratio "
        "p_ref / p_obj under endogenous versus exogenous observation; panel C "
        "shows relative price distortion against "
        "objective expected-value pricing for models B–D; panel D shows the "
        "contemporaneous price–outcome association under Model D. All quantities "
        "are generated (simulation evidence, not empirical estimates)."
    ),
    "Figure 5": (
        "Frequency distortion versus price distortion across rarity regimes. "
        "Panel A: absolute selection gap (bars, left axis) shrinks with rarity "
        "while the selection ratio (lines, right axis) is stable at "
        "approximately {ratio_endo:.2f} under endogenous observation and "
        "{ratio_exo:.2f} under "
        "exogenous observation—the analytically derived invariance of Lemma 1. "
        "Panel B: relative price distortion under Model "
        "D decomposes into a transformed-frequency part that is "
        "quantitatively dominant in every simulated regime and an additive "
        "reputation part whose share rises as objective expected value "
        "shrinks; neither part is bounded relative to the shrinking "
        "benchmark. The relative-distortion rise is a denominator-scaling "
        "effect in both non-scaling components, not growing frequency bias "
        "and not growing absolute mispricing."
    ),
    "Figure 6": (
        "Mean-performance equivalence map. Mean apparent success among observed "
        "events as true efficacy added on intervened periods varies, under "
        "endogenous (A) "
        "and exogenous (B) observation. Endogenous selection with zero true "
        "efficacy reproduces the MEAN apparent success of positive efficacy under "
        "exogenous observation (first-moment equivalence only)."
    ),
    "Figure 7": (
        "Zero-effect benchmark: sequential Monte Carlo pricing-rule enrichment "
        "under M0–M5 "
        "on fictional rainmaking pseudo-events over observed weather. M0–M1 shuffle "
        "rainfall outcomes within sampled years; M2–M5 retain observed local and "
        "seasonal ordering. Selective acceptance changes accepted-event composition "
        "and current apparent success. In M4–M5, past attributed outcomes accumulate "
        "in reputation stocks that create price premia and provider-price "
        "heterogeneity, while current success remains a natural-rainfall flow "
        "governed by current hazard. Mean price(success) minus price(failure) is "
        "negative in M4–M5. Error bars are 2.5th and 97.5th Monte Carlo percentiles, "
        "not confidence intervals for historical parameters."
    ),
    "Figure 8": (
        "Robustness. Apparent success across rainfall thresholds and windows, selected "
        "parameter sensitivity, and Monte Carlo precision."
    ),
}


def figure_captions() -> dict[str, str]:
    generic = pd.read_csv(RESULTS / "general_summary.csv")
    ratio = generic.loc[generic["metric"] == "selection_ratio"].groupby(
        "obs_rule"
    )["mean"].mean()
    captions = dict(FIGURE_CAPTIONS)
    captions["Figure 5"] = captions["Figure 5"].format(
        ratio_endo=ratio["endogenous"], ratio_exo=ratio["exogenous"]
    )
    return captions


def read_config() -> tuple[dict, dict]:
    regions = yaml.safe_load((ROOT / "config" / "regions.yml").read_text())
    simulation = yaml.safe_load((ROOT / "config" / "simulation.yml").read_text())
    return regions, simulation


def save_table(frame: pd.DataFrame, stem: str) -> None:
    frame.to_csv(TABLES / f"{stem}.csv", index=False)


def make_tables(regions_config: dict) -> dict[str, pd.DataFrame]:
    weather = pd.read_csv(
        ROOT / "data" / "processed" / "daily_weather_features.csv.gz",
        usecols=["region", "date", "precip_mm"],
    )
    region_rows = []
    for region in regions_config["regions"]:
        subset = weather.loc[weather["region"] == region["id"]]
        region_rows.append(
            {
                "Location": region["name"],
                "Latitude": region["latitude"],
                "Longitude": region["longitude"],
                "Rainfall regime": region["regime"],
                "Region-days": int(len(subset)),
                "Missing precipitation": int(subset["precip_mm"].isna().sum()),
            }
        )
    table1 = pd.DataFrame(region_rows)

    pseudo = pd.read_csv(ANALYSIS / "pseudo_events.csv")
    table2 = (
        pseudo.groupby("rule", observed=True)
        .agg(
            Events=("rule", "size"),
            Apparent_success_1d=("success_1mm_1d", "mean"),
            Apparent_success_3d=("success_1mm_3d", "mean"),
            Apparent_success_7d=("success_1mm_7d", "mean"),
            Apparent_success_14d=("success_1mm_14d", "mean"),
            Mean_scenario_WTP=("scenario_wtp", "mean"),
        )
        .reset_index()
        .rename(columns={"rule": "Selection rule"})
    )

    summary = pd.read_csv(RESULTS / "simulation_summary.csv")
    selected = [
        "events",
        "apparent_success",
        "mean_price",
        "provider_price_dispersion",
        "price_success_difference",
        "reputation_dispersion",
    ]
    table3 = (
        summary.loc[summary["outcome"].isin(selected)]
        .pivot(index="model", columns="outcome", values="mean")
        .reindex(MODEL_LABELS)
        .reset_index()
        .rename(columns={"model": "Model"})
    )
    table3["Model"] = table3["Model"].map(MODEL_LABELS)

    generic = pd.read_csv(RESULTS / "general_summary.csv")
    endo_ratio = generic.loc[
        (generic["obs_rule"] == "endogenous")
        & (generic["metric"] == "selection_ratio"),
        "mean",
    ].mean()
    propositions = pd.DataFrame(
        [
            ("P1 Risk-correlated selection shifts experienced frequency; the "
             "sign is set by Cov(m, s)",
             "Demonstrated (generic simulation and known-zero benchmark, "
             "positive-covariance calibration); derived analytically (Lemma 1)",
             "selection ratio = 1 + Cov(m,s)/(E[m]E[s]); positive covariance "
             "yields selection_gap > 0 under endogenous observation at zero "
             "efficacy; adjusted hazard attenuation in the rainfall benchmark"),
            ("P2a Selection shifts experienced frequency proportionally; "
             "positive-covariance calibration",
             "Demonstrated (generic simulation); derived analytically (Lemma 1)",
             f"selection_ratio = p_ref/p_obj ≈ {endo_ratio:.2f}, analytically independent "
             "of baseline rarity under multiplicative state-dependent "
             "selection; ≈ 1.0 under exogenous observation; record term "
             "B_abs ≈ 0 on the observed support"),
            ("P2b Original hypothesis: rarity amplifies the absolute "
             "selection gap",
             "NOT SUPPORTED (negative result)",
             f"absolute selection gap falls with rarity (≈ {endo_ratio - 1:.2f} × p_obj); the "
             "original rarity-amplification hypothesis for the frequency gap "
             "was driven by scaling of the composition effect with p, not by "
             "a rarity mechanism"),
            ("P2c Rarity changes the relative composition of modeled prices "
             "through nonlinear transformation and non-scaling reputation",
             "Demonstrated (generic simulation); transformed term divergent "
             "analytically (Lemma 2)",
             "D_rel(Model D) rises with rarity through both a nonlinear "
             "transformed-frequency part—the larger share in every simulated "
             "regime, asymptotically unbounded under Prelec weighting—and an "
             "additive reputation part whose share rises with rarity"),
            ("P3 Weighting moves the subjective layer relative to experience",
             "Demonstrated (generic simulation)",
             "B_subj differs across learner rules; selective memory exceeds "
             "experienced frequency"),
            ("P4 Model-implied quotes mix hazard and transformation",
             "Demonstrated (generic simulation)",
             "B_price and D_EV differ across pricing models A–D"),
            ("P5 Reputation decouples price from contemporaneous performance",
             "Demonstrated (generic simulation; sharper in the known-zero "
             "benchmark)",
             "Reputation premia coexist with small or negative contemporaneous "
             "price-success differences"),
            ("P6 Mean-performance equivalence limits inference from raw "
             "performance",
             "Demonstrated (generic simulation; first-moment only)",
             "Zero efficacy under endogenous observation reproduces the MEAN "
             "apparent success of positive efficacy under exogenous "
             "observation in the simulated rare regimes (first-moment only; "
             "regime-dependent, no solution in the common regime)"),
        ],
        columns=["Proposition", "Classification", "Basis"],
    )

    regression = pd.read_csv(ANALYSIS / "price_success_models.csv")
    cluster = pd.read_csv(ANALYSIS / "cluster_robust_price_success.csv")
    permutation = pd.read_csv(ANALYSIS / "price_permutation_falsification.csv")
    table_s1 = pd.concat(
        [
            regression.assign(inference="model-based"),
            cluster.rename(
                columns={"cluster_standard_error": "standard_error"}
            ).assign(
                model="hazard-adjusted",
                inference="two-way clustered: region-year and region-rule",
            ),
        ],
        ignore_index=True,
        sort=False,
    )
    table_s2 = pd.read_csv(ANALYSIS / "threshold_window_sensitivity.csv")
    table_s3 = pd.read_csv(RESULTS / "simulation_sensitivity_summary.csv")
    table_s4 = pd.read_csv(RESULTS / "simulation_convergence.csv")
    table_s5 = permutation
    accounting = [
        "provider_revenue",
        "community_expenditure",
        "provider_resource_cost",
        "provider_profit",
        "community_material_social_utility",
        "total_social_surplus",
        "provider_revenue_dispersion",
    ]
    table_s6 = (
        summary.loc[summary["outcome"].isin(accounting)]
        .pivot(index="model", columns="outcome", values="mean")
        .reindex(MODEL_LABELS)
        .reset_index()
        .rename(columns={"model": "Model"})
    )
    table_s6["Model"] = table_s6["Model"].map(MODEL_LABELS)

    tables = {
        "table1_proposition_classification": propositions,
        "table3_study_locations": table1,
        "table5_pseudo_event_results": table2,
        "table6_simulation_results": table3,
        "table_s1_price_models": table_s1,
        "table_s2_threshold_window_sensitivity": table_s2,
        "table_s3_parameter_sensitivity": table_s3,
        "table_s4_simulation_convergence": table_s4,
        "table_s5_permutation_falsification": table_s5,
        "table_s6_accounting": table_s6,
    }

    general_summary_path = RESULTS / "general_summary.csv"
    if general_summary_path.exists():
        general = pd.read_csv(general_summary_path)
        regime_order = ["common", "moderately_rare", "rare", "very_rare"]
        pivot = general.pivot_table(
            index=["regime", "obs_rule"], columns="metric", values="mean"
        ).reindex(
            [(r, o) for r in regime_order
             for o in ["endogenous", "exogenous"]]
        )
        general_metrics = [
            "p_objective", "p_ref_observed", "p_experienced",
            "selection_gap", "selection_ratio", "B_abs", "B_rel",
            "B_subj_bayesian", "B_price_D_reputation",
            "D_rel_prob_D_reputation", "D_rel_rep_D_reputation",
            "D_rel_D_reputation",
            "price_success_diff_D_reputation", "reputation_hazard_corr",
            "provider_rank_distortion",
        ]
        table2 = pivot[general_metrics].reset_index()
        total = table2["D_rel_D_reputation"]
        table2["prob_share_D_reputation"] = (
            table2["D_rel_prob_D_reputation"] / total
        )
        table2["rep_share_D_reputation"] = (
            table2["D_rel_rep_D_reputation"] / total
        )
        tables["table2_general_regimes"] = table2.rename(
            columns={"regime": "Regime", "obs_rule": "Observation rule"}
        )
        equivalence = pd.read_csv(
            RESULTS / "general_observational_equivalence.csv"
        )
        tables["table4_observational_equivalence"] = equivalence.pivot_table(
            index=["regime", "obs_rule"], columns="efficacy",
            values="apparent_success_mean",
        ).reset_index().rename(columns={
            "regime": "Regime", "obs_rule": "Observation rule",
        })
        tables["table_s7_general_convergence"] = pd.read_csv(
            RESULTS / "general_convergence.csv"
        )
        learner_metrics = [
            "selection_gap", "selection_ratio", "B_abs", "B_rel",
            "B_subj_naive", "B_subj_bayesian", "B_subj_recency",
            "B_subj_selective", "B_price_A_objective", "B_price_B_experienced",
            "B_price_C_weighted", "B_price_D_reputation",
            "D_prob_abs_D_reputation", "D_rep_abs_D_reputation",
        ]
        tables["table_s8_probability_layer_detail"] = (
            pivot[learner_metrics].reset_index()
            .rename(columns={"regime": "Regime", "obs_rule": "Observation rule"})
        )
    for stem, frame in tables.items():
        save_table(frame, stem)
    return tables


def make_robustness_figure() -> None:
    sensitivity = pd.read_csv(ANALYSIS / "threshold_window_sensitivity.csv")
    sensitivity[["threshold", "window"]] = sensitivity["outcome"].str.extract(
        r"success_([0-9.]+)mm_([0-9]+)d"
    )
    sensitivity["window"] = sensitivity["window"].astype(int)
    heat = (
        sensitivity.groupby(["threshold", "window"], observed=True)[
            "apparent_success"
        ]
        .mean()
        .unstack()
        .reindex(["0.1", "1", "5"])
    )

    parameter = pd.read_csv(RESULTS / "simulation_sensitivity_summary.csv")
    parameter = parameter.loc[
        ((parameter["scenario"].str.startswith("M3_")) & (parameter["outcome"] == "apparent_success"))
        | (
            parameter["scenario"].str.startswith(("M4_", "M5_"))
            & (parameter["outcome"] == "mean_price")
        )
    ].copy()
    parameter["label"] = (
        parameter["scenario"]
        .str.replace("M3_selection_slope_", "M3 slope ", regex=False)
        .str.replace("M4_prior_mean_", "M4 prior ", regex=False)
        .str.replace("M5_", "M5 ", regex=False)
        .str.replace("_memory", "", regex=False)
        .str.replace("_", " ", regex=False)
    )

    convergence = pd.read_csv(RESULTS / "simulation_convergence.csv")
    convergence = convergence.loc[
        (convergence["outcome"] == "apparent_success")
        & convergence["model"].isin(
            ["M0_random_timing", "M3_strategic_selection", "M5_selective_recency"]
        )
    ].copy()
    convergence["model"] = convergence["model"].map(MODEL_LABELS)

    sns.set_theme(style="whitegrid", context="paper")
    figure, axes = plt.subplots(1, 3, figsize=(13.2, 4.4))
    sns.heatmap(
        heat,
        annot=True,
        fmt=".2f",
        cmap="Blues",
        vmin=0,
        vmax=1,
        cbar_kws={"label": "Apparent success"},
        ax=axes[0],
    )
    axes[0].set_title("A. Threshold and window sensitivity")
    axes[0].set_xlabel("Post-event window (days)")
    axes[0].set_ylabel("Rainfall threshold (mm)")

    sns.barplot(data=parameter, x="mean", y="label", hue="outcome", ax=axes[1])
    axes[1].set_title("B. Parameter sensitivity")
    axes[1].set_xlabel("Mean apparent success or price")
    axes[1].set_ylabel("")
    axes[1].legend(title="", loc="lower right", fontsize=7)

    sns.lineplot(
        data=convergence,
        x="sample_size",
        y="monte_carlo_se",
        hue="model",
        marker="o",
        ax=axes[2],
    )
    axes[2].set_title("C. Monte Carlo precision")
    axes[2].set_xlabel("Replications")
    axes[2].set_ylabel("Monte Carlo standard error")
    axes[2].legend(title="", fontsize=7)
    figure.tight_layout()
    figure.savefig(FIGURES / "figure8_robustness.pdf", bbox_inches="tight")
    figure.savefig(
        FIGURES / "figure8_robustness.png", dpi=600, bbox_inches="tight"
    )
    plt.close(figure)


def add_docx_table(document: Document, title: str, frame: pd.DataFrame) -> None:
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(16)
    run = paragraph.add_run(title)
    run.bold = True
    table = document.add_table(rows=1, cols=len(frame.columns))
    table.style = "Table Grid"
    for cell, column in zip(table.rows[0].cells, frame.columns):
        cell.text = str(column).replace("_", " ")
    for row in frame.itertuples(index=False, name=None):
        cells = table.add_row().cells
        for cell, value in zip(cells, row):
            if isinstance(value, float):
                cell.text = f"{value:.3f}"
            else:
                cell.text = str(value)


def make_tables_docx(tables: dict[str, pd.DataFrame]) -> None:
    document = Document()
    section = document.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width, section.page_height = section.page_height, section.page_width
    title = document.add_heading(
        "Apparent Performance under Selective Environmental Risk — Editable Tables", level=0
    )
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    main_titles = {
        "table1_proposition_classification": "Table 1. Proposition classification",
        "table2_general_regimes": "Table 2. Generic rare-event simulation: "
            "probability layers and pricing distortion by regime and "
            "observation rule",
        "table4_observational_equivalence": "Table 3. Mean-performance "
            "equivalence: mean apparent success by true efficacy, regime, and "
            "observation rule",
        "table5_pseudo_event_results": "Table 4. Zero-effect benchmark: "
            "pseudo-event apparent success",
        "table3_study_locations": "Table S9. Benchmark environment: study "
            "locations and rainfall observations",
        "table6_simulation_results": "Table S10. Zero-effect benchmark: Monte "
            "Carlo pricing-rule decomposition",
    }
    for stem, title_text in main_titles.items():
        add_docx_table(document, title_text, tables[stem])
        document.add_page_break()
    document.save(TABLES / "main_tables_editable.docx")

    supplement = Document()
    supplement.sections[0].orientation = WD_ORIENT.LANDSCAPE
    supplement.sections[0].page_width, supplement.sections[0].page_height = (
        supplement.sections[0].page_height,
        supplement.sections[0].page_width,
    )
    supplement.add_heading(
        "Apparent Performance under Selective Environmental Risk — Editable Supplementary Tables",
        level=0,
    )
    for stem in [
        "table_s1_price_models",
        "table_s2_threshold_window_sensitivity",
        "table_s3_parameter_sensitivity",
        "table_s4_simulation_convergence",
        "table_s5_permutation_falsification",
        "table_s6_accounting",
        "table_s7_general_convergence",
        "table_s8_probability_layer_detail",
    ]:
        add_docx_table(
            supplement,
            stem.replace("_", " ").replace("table s", "Table S").title(),
            tables[stem],
        )
        supplement.add_page_break()
    supplement.save(TABLES / "supplementary_tables_editable.docx")


def make_figures_pptx() -> None:
    png1 = FIGURES / "figure1_framework.png"
    cairosvg.svg2pdf(
        url=str(FIGURES / "figure1_framework.svg"),
        write_to=str(FIGURES / "figure1_framework.pdf"),
    )
    cairosvg.svg2png(
        url=str(FIGURES / "figure1_framework.svg"),
        write_to=str(png1),
        output_width=2400,
    )
    figure_paths = [
        (png1, "1"),
        (FIGURES / "figure2_pseudo_event_success.png", "2"),
        (FIGURES / "figure3_empirical_hazard.png", "3"),
        (FIGURES / "figure4_four_probabilities.png", "4"),
        (FIGURES / "figure5_distortion_decomposition.png", "5"),
        (FIGURES / "figure6_observational_equivalence.png", "6"),
        (FIGURES / "figure7_simulation_decomposition.png", "7"),
        (FIGURES / "figure8_robustness.png", "8"),
    ]
    presentation = Presentation()
    presentation.slide_width = PptxInches(13.333)
    presentation.slide_height = PptxInches(7.5)
    for path, index in figure_paths:
        slide = presentation.slides.add_slide(presentation.slide_layouts[6])
        title_box = slide.shapes.add_textbox(
            PptxInches(0.5), PptxInches(0.15), PptxInches(12.3), PptxInches(0.45)
        )
        title = title_box.text_frame.paragraphs[0]
        title.text = f"Figure {index}"
        title.font.size = PptxPt(22)
        title.font.bold = True
        title.alignment = PP_ALIGN.CENTER
        image_width, image_height = Image.open(path).size
        image_ratio = image_width / image_height
        box_width, box_height = 11.93, 5.65
        if image_ratio >= box_width / box_height:
            width = box_width
            height = width / image_ratio
        else:
            height = box_height
            width = height * image_ratio
        left = 0.7 + (box_width - width) / 2
        top = 0.7 + (box_height - height) / 2
        slide.shapes.add_picture(
            str(path),
            PptxInches(left),
            PptxInches(top),
            width=PptxInches(width),
            height=PptxInches(height),
        )
        caption_box = slide.shapes.add_textbox(
            PptxInches(0.65), PptxInches(6.45), PptxInches(12.03), PptxInches(0.8)
        )
        caption = caption_box.text_frame.paragraphs[0]
        caption.text = figure_captions()[f"Figure {index}"]
        caption.font.size = PptxPt(11)
    presentation.save(FIGURES / "figures_editable.pptx")


def json_records(frame: pd.DataFrame) -> list[dict[str, object]]:
    clean = frame.replace({np.nan: None})
    return clean.to_dict(orient="records")


def make_values(tables: dict[str, pd.DataFrame], regions: dict, simulation: dict) -> None:
    payload = {
        "study": {
            "start": regions["study_period"]["start"],
            "end": regions["study_period"]["end"],
            "training_end": regions["training_end"],
            "rain_threshold_mm": regions["primary_rain_threshold_mm"],
            "success_windows_days": regions["success_windows_days"],
            "locations": len(regions["regions"]),
            "region_days": int(tables["table3_study_locations"]["Region-days"].sum()),
        },
        "simulation": {
            "seed": simulation["seed"],
            "replications_per_model": simulation["replications_per_model"],
            "providers": simulation["providers"],
            "models": simulation["models"],
            "parameters": simulation["parameters"],
            "summary": json_records(
                pd.read_csv(RESULTS / "simulation_summary.csv")
            ),
            "sensitivity": json_records(
                pd.read_csv(RESULTS / "simulation_sensitivity_summary.csv")
            ),
            "convergence": json_records(
                pd.read_csv(RESULTS / "simulation_convergence.csv")
            ),
        },
        "empirical": {
            "pseudo_events": json_records(tables["table5_pseudo_event_results"]),
            "price_models": json_records(
                pd.read_csv(ANALYSIS / "price_success_models.csv")
            ),
            "cluster_robust_price_model": json_records(
                pd.read_csv(ANALYSIS / "cluster_robust_price_success.csv")
            ),
            "permutation_falsification": json_records(
                pd.read_csv(ANALYSIS / "price_permutation_falsification.csv")
            ),
            "threshold_window_sensitivity": json_records(
                pd.read_csv(ANALYSIS / "threshold_window_sensitivity.csv")
            ),
        },
        "hypotheses": json_records(
            pd.read_csv(RESULTS / "hypothesis_classification.csv")
        ),
        "figure_captions": figure_captions(),
    }
    general_summary_path = RESULTS / "general_summary.csv"
    if general_summary_path.exists():
        payload["general"] = {
            "summary": json_records(pd.read_csv(general_summary_path)),
            "equivalence": json_records(
                pd.read_csv(RESULTS / "general_observational_equivalence.csv")
            ),
            "convergence": json_records(
                pd.read_csv(RESULTS / "general_convergence.csv")
            ),
            "equivalent_efficacy": json_records(
                pd.read_csv(RESULTS / "general_equivalent_efficacy.csv")
            ),
            "regimes": tables.get(
                "table2_general_regimes"
            ).to_dict(orient="records")
            if "table2_general_regimes" in tables
            else [],
        }
    (RESULTS / "manuscript_values.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    )


def main() -> None:
    regions, simulation = read_config()
    tables = make_tables(regions)
    make_robustness_figure()
    make_tables_docx(tables)
    make_figures_pptx()
    make_values(tables, regions, simulation)
    print("Built manuscript figures, tables, and machine-readable values")


if __name__ == "__main__":
    main()
