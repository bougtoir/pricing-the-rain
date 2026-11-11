from __future__ import annotations

import json
import math
import re
import subprocess
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt
from docx_equation import mathml_to_omml
from latex2mathml.converter import convert as latex_to_mathml


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript"
SUPPLEMENT = ROOT / "supplement"
TABLES = ROOT / "tables"
FIGURES = ROOT / "figures"
RESULTS = ROOT / "results"
METADATA = pd.read_csv(ROOT / "analysis" / "reference_metadata.csv")
VALUES = json.loads((RESULTS / "manuscript_values.json").read_text())

TITLE = (
    "Selected Experience and Rare-Event Risk: Endogenous Observation, "
    "Subjective Transformation, and Reputation under Hidden Counterfactuals"
)
ARTICLE_TYPE = "Research article"
JOURNAL = "Journal of Risk and Uncertainty"
JOURNAL_SHORT = "JRU"
JEL_CODES = "D81; D82; D83; D84"

REFERENCE_ORDER = [
    "10.14989/68028",
    "10.1093/ije/dyh299",
    "10.1086/261849",
    "10.1111/j.2517-6161.1972.tb00899.x",
    "10.1086/374180",
    "10.5751/es-12875-270209",
    "10.1093/qje/qjag026",
    "10.2307/1912352",
    "10.1111/j.1475-4932.2006.00293.x",
    "10.1002/qj.3803",
    "10.1016/0022-0531(82)90030-8",
    "10.1175/1520-0434(1993)008<0281:wiagfa>2.0.co;2",
    "10.1029/2000wr900320",
    "10.1161/circulationaha.107.747873",
    "10.1037/h0055873",
    "10.1126/science.185.4157.1124",
    "10.1001/jama.293.10.1239",
    "10.1111/j.0956-7976.2004.00715.x",
    "10.1037/bul0000115",
    "10.1111/j.1467-9280.2009.02319.x",
    "10.1007/bf00122574",
    "10.2307/2998573",
    "10.3982/ecta12609",
    "10.1257/aer.20161696",
    "10.3982/qe650",
    "10.1016/j.econmod.2015.05.012",
    "10.1016/j.jebo.2012.07.006",
    "10.1016/j.jebo.2016.03.008",
    "10.1287/orsc.12.5.523.10092",
    "10.1037/0033-295x.112.4.951",
    "10.1037/a0023010",
    "10.1037/0033-295x.107.4.659",
    "10.1016/j.tics.2009.09.004",
    "10.1002/bdm.443",
    "10.1023/a:1011111601406",
    "10.2307/3325045",
    "10.1006/cogp.1998.0710",
]

# Every DOI in REFERENCE_ORDER must be cited in the manuscript text. Each entry
# maps the DOI to a surname token that must appear inside a citation.
REFERENCE_CITE_TOKENS = {
    "10.14989/68028": "Akong'a",
    "10.1093/ije/dyh299": "Barnett",
    "10.1086/261849": "Bikhchandani",
    "10.1111/j.2517-6161.1972.tb00899.x": "Cox",
    "10.1086/374180": "Dranove",
    "10.5751/es-12875-270209": "Espín-Sánchez & Gil-Guirado, 2022",
    "10.1093/qje/qjag026": "Espín-Sánchez",
    "10.2307/1912352": "Heckman",
    "10.1111/j.1475-4932.2006.00293.x": "Hensher",
    "10.1002/qj.3803": "Hersbach",
    "10.1016/0022-0531(82)90030-8": "Kreps",
    "10.1175/1520-0434(1993)008<0281:wiagfa>2.0.co;2": "Murphy",
    "10.1029/2000wr900320": "Pattanayak",
    "10.1161/circulationaha.107.747873": "Shahian",
    "10.1037/h0055873": "Skinner",
    "10.1126/science.185.4157.1124": "Tversky",
    "10.1001/jama.293.10.1239": "Werner",
    "10.1111/j.0956-7976.2004.00715.x": "Hertwig",
    "10.1037/bul0000115": "Wulff",
    "10.1111/j.1467-9280.2009.02319.x": "Ungemach",
    "10.1007/bf00122574": "Tversky",
    "10.2307/2998573": "Prelec",
    "10.3982/ecta12609": "Esponda",
    "10.1257/aer.20161696": "Jehiel",
    "10.3982/qe650": "Vespa",
    "10.1016/j.econmod.2015.05.012": "Shea",
    "10.1016/j.jebo.2012.07.006": "Liu",
    "10.1016/j.jebo.2016.03.008": "Matsumoto",
    "10.1287/orsc.12.5.523.10092": "Denrell & March",
    "10.1037/0033-295x.112.4.951": "Denrell, 2005",
    "10.1037/a0023010": "Le Mens",
    "10.1037/0033-295x.107.4.659": "Fiedler",
    "10.1016/j.tics.2009.09.004": "Hertwig & Erev",
    "10.1002/bdm.443": "Barron",
    "10.1023/a:1011111601406": "Kunreuther et al., 2001",
    "10.2307/3325045": "Camerer",
    "10.1006/cogp.1998.0710": "Gonzalez",
}

FIGURE_FILES = {
    "FIGURE_1": FIGURES / "figure1_framework.png",
    "FIGURE_2": FIGURES / "figure2_pseudo_event_success.png",
    "FIGURE_3": FIGURES / "figure3_empirical_hazard.png",
    "FIGURE_4": FIGURES / "figure4_four_probabilities.png",
    "FIGURE_5": FIGURES / "figure5_distortion_decomposition.png",
    "FIGURE_6": FIGURES / "figure6_observational_equivalence.png",
    "FIGURE_7": FIGURES / "figure7_simulation_decomposition.png",
    "FIGURE_8": FIGURES / "figure8_robustness.png",
}

TABLE_FILES = {
    "TABLE_1": TABLES / "table1_proposition_classification.csv",
    "TABLE_2": TABLES / "table2_general_regimes.csv",
    "TABLE_3": TABLES / "table4_observational_equivalence.csv",
    "TABLE_4": TABLES / "table5_pseudo_event_results.csv",
    "TABLE_S9": TABLES / "table3_study_locations.csv",
    "TABLE_S10": TABLES / "table6_simulation_results.csv",
    "TABLE_S1": TABLES / "table_s1_price_models.csv",
    "TABLE_S2": TABLES / "table_s2_threshold_window_sensitivity.csv",
    "TABLE_S3": TABLES / "table_s3_parameter_sensitivity.csv",
    "TABLE_S4": TABLES / "table_s4_simulation_convergence.csv",
    "TABLE_S5": TABLES / "table_s5_permutation_falsification.csv",
    "TABLE_S6": TABLES / "table_s6_accounting.csv",
    "TABLE_S7": TABLES / "table_s7_general_convergence.csv",
    "TABLE_S8": TABLES / "table_s8_probability_layer_detail.csv",
}

MAIN_TABLE_CAPTIONS = {
    "TABLE_1": "Table 1. Proposition classification.",
    "TABLE_2": (
        "Table 2. Generic rare-event simulation: probability layers and "
        "pricing distortion by regime and observation rule."
    ),
    "TABLE_3": (
        "Table 3. Mean-performance equivalence: mean apparent success by true "
        "efficacy, regime, and observation rule."
    ),
    "TABLE_4": "Table 4. Zero-effect benchmark: pseudo-event apparent success.",
}

SUPPLEMENT_TABLE_CAPTIONS = {
    "TABLE_S1": "Table S1. Scenario price models.",
    "TABLE_S2": "Table S2. Rainfall-threshold and attribution-window sensitivity.",
    "TABLE_S3": "Table S3. Simulation parameter sensitivity.",
    "TABLE_S4": "Table S4. Monte Carlo convergence and precision.",
    "TABLE_S5": "Table S5. Permutation falsification.",
    "TABLE_S6": "Table S6. Simulated transfer, cost, profit, and surplus accounting.",
    "TABLE_S7": "Table S7. Generic-simulation Monte Carlo convergence.",
    "TABLE_S8": "Table S8. Generic-simulation subjective and price layer detail.",
    "TABLE_S9": "Table S9. Benchmark environment: study locations and rainfall observations.",
    "TABLE_S10": "Table S10. Zero-effect benchmark: Monte Carlo pricing-rule decomposition.",
}


def f(value: float, digits: int = 3) -> str:
    text = f"{value:.{digits}f}"
    return text[1:] if text.startswith("-") and float(text) == 0 else text


def simulation_value(model: str, outcome: str, field: str = "mean") -> float:
    rows = [
        row
        for row in VALUES["simulation"]["summary"]
        if row["model"] == model and row["outcome"] == outcome
    ]
    if len(rows) != 1:
        raise ValueError(f"Missing simulation value: {model} {outcome}")
    return float(rows[0][field])


def pseudo_value(rule: str, field: str) -> float:
    rows = [
        row
        for row in VALUES["empirical"]["pseudo_events"]
        if row["Selection rule"] == rule
    ]
    if len(rows) != 1:
        raise ValueError(f"Missing pseudo-event value: {rule} {field}")
    return float(rows[0][field])


def model_row(model: str) -> dict:
    rows = [
        row
        for row in VALUES["empirical"]["price_models"]
        if row["model"] == model and row["term"] == "scenario_wtp"
    ]
    if len(rows) != 1:
        raise ValueError(f"Missing price model: {model}")
    return rows[0]


def cluster_row() -> dict:
    rows = [
        row
        for row in VALUES["empirical"]["cluster_robust_price_model"]
        if row["term"] == "scenario_wtp"
    ]
    if len(rows) != 1:
        raise ValueError("Missing clustered scenario WTP estimate")
    return rows[0]


def general_value(
    regime: str, rule: str, metric: str, field: str = "mean"
) -> float:
    rows = [
        row
        for row in VALUES["general"]["summary"]
        if row["regime"] == regime
        and row["obs_rule"] == rule
        and row["metric"] == metric
    ]
    if len(rows) != 1:
        raise ValueError(f"Missing general value: {regime} {rule} {metric}")
    return float(rows[0][field])


def analytic_selection_ratio() -> float:
    """Analytic two-state selection ratio of Lemma 1, computed from
    config/general_simulation.yml (demand x acceptance observation
    probabilities per state)."""
    cfg = yaml.safe_load(
        (ROOT / "config" / "general_simulation.yml").read_text()
    )
    hs = cfg["hazard_state"]
    dem = cfg["demand"]
    acc = cfg["acceptance"]
    expit = lambda x: 1.0 / (1.0 + math.exp(-x))
    selectivity = np.linspace(
        -float(acc["selectivity_spread"]),
        float(acc["selectivity_spread"]),
        int(cfg["providers"]),
    )

    def q_state(state: int) -> float:
        mult = hs["high_multiplier"] if state else hs["low_multiplier"]
        q_d = expit(float(dem["intercept"]) + float(dem["slope"]) * state)
        q_a = float(
            np.mean(
                [
                    expit(
                        float(acc["intercept"])
                        + float(acc["slope"]) * (float(mult) - 1.0)
                        + float(s_j)
                    )
                    for s_j in selectivity
                ]
            )
        )
        return q_d * q_a

    pi = float(hs["high_share"])
    m_l = float(hs["low_multiplier"])
    m_h = float(hs["high_multiplier"])
    q_l = q_state(0)
    q_h = q_state(1)
    mu = pi * m_h + (1 - pi) * m_l
    return (pi * m_h * q_h + (1 - pi) * m_l * q_l) / (
        mu * (pi * q_h + (1 - pi) * q_l)
    )


def endo_selection_ratio_range() -> tuple[float, float]:
    values = [
        float(row["mean"])
        for row in VALUES["general"]["summary"]
        if row["metric"] == "selection_ratio" and row["obs_rule"] == "endogenous"
    ]
    return min(values), max(values)


def equivalent_efficacy(regime: str) -> dict[str, float]:
    """Solved equivalent-efficacy row for a regime from
    results/general_equivalent_efficacy.csv (explicit inverse interpolation
    with MCSE bounds; equivalent_efficacy may be NaN when the target lies
    outside the scanned efficacy grid)."""
    rows = [
        row
        for row in VALUES["general"]["equivalent_efficacy"]
        if row["regime"] == regime
    ]
    if len(rows) != 1:
        raise ValueError(f"Missing equivalent-efficacy row for {regime}")
    return {
        "delta": float(rows[0]["equivalent_efficacy"]),
        "low": float(rows[0]["equivalent_efficacy_low"]),
        "high": float(rows[0]["equivalent_efficacy_high"]),
        "target": float(rows[0]["endo_apparent_zero"]),
    }


def config_tokens() -> dict[str, str]:
    """Simulation inputs quoted in Methods, read from the declared config."""
    from simulation.general_rare_event import PRIOR_OBS_STOCK, PRIOR_SUCCESS_STOCK

    cfg = yaml.safe_load(
        (ROOT / "config" / "general_simulation.yml").read_text()
    )
    hs, learn, price = cfg["hazard_state"], cfg["learning"], cfg["pricing"]
    base = {row["name"]: float(row["base_prob"]) for row in cfg["regimes"]}
    grid = [float(x) for x in cfg["efficacy_grid"]]
    from analysis.robustness import N_PERMUTATIONS, SENSITIVITY_REPLICATIONS

    return {
        "CFG_N_PERMUTATIONS": f"{N_PERMUTATIONS:,}",
        "CFG_SENSITIVITY_REPLICATIONS": f"{SENSITIVITY_REPLICATIONS:,}",
        "CFG_PERSISTENCE": f"{float(hs['persistence']):.2f}",
        "CFG_HIGH_SHARE_PCT": f"{100 * float(hs['high_share']):.0f}",
        "CFG_HIGH_MULT": str(float(hs["high_multiplier"])),
        "CFG_LOW_MULT": str(float(hs["low_multiplier"])),
        "CFG_P_COMMON": f"{base['common']:.2f}",
        "CFG_P_MODRARE": f"{base['moderately_rare']:.2f}",
        "CFG_P_RARE": f"{base['rare']:.2f}",
        "CFG_P_VRARE": f"{base['very_rare']:.2f}",
        "CFG_P_MIN": f"{min(base.values()) * float(hs['low_multiplier']):.3f}",
        "CFG_PRIOR_STRENGTH": str(float(learn["prior_strength"])),
        "CFG_RECENCY_DECAY": str(float(learn["recency_decay"])),
        "CFG_SUCCESS_WEIGHT": str(float(learn["selective_success_weight"])),
        "CFG_FAILURE_WEIGHT": str(float(learn["selective_failure_weight"])),
        "CFG_PRIOR_OUTCOMES": f"{PRIOR_OBS_STOCK / (1 - float(learn['recency_decay'])):.0f}",
        "CFG_PRIOR_MEAN": str(PRIOR_SUCCESS_STOCK / PRIOR_OBS_STOCK),
        "CFG_R0": f"{PRIOR_SUCCESS_STOCK:.2f}",
        "CFG_N0": f"{PRIOR_OBS_STOCK:.2f}",
        "CFG_PRELEC": str(float(cfg["weighting"]["prelec_alpha"])),
        "CFG_GAMMA": str(float(price["reputation_gamma"])),
        "CFG_REP_DECAY": str(float(price["reputation_decay"])),
        "CFG_HORIZON": f"{int(cfg['horizon']):,}".replace(",", "{,}"),
        "CFG_EFFICACY_GRID": ", ".join("0" if x == 0 else f"{x:.2f}" for x in grid),
        "CFG_EFFICACY_MAX": f"{max(grid):.2f}",
    }


def replacements() -> dict[str, str]:
    naive = model_row("naive")
    adjusted = model_row("hazard-adjusted")
    cluster = cluster_row()
    permutation = VALUES["empirical"]["permutation_falsification"][0]
    max_mcse = max(
        float(row["monte_carlo_se"])
        for row in VALUES["simulation"]["convergence"]
        if row["sample_size"] == max(
            r["sample_size"] for r in VALUES["simulation"]["convergence"]
        )
        and row["outcome"] == "apparent_success"
    )
    rules = {
        "DEFICIT": "30-day deficit threshold",
        "DRYSPELL": "dry-spell threshold",
        "HAZARD": "high prospective hazard",
        "RANDOM": "random drought day",
        "PLACEBO": "season-matched placebo",
    }
    output = {
        **config_tokens(),
        "TOTAL_REGION_DAYS": f"{int(VALUES['study']['region_days']):,}",
        "TOTAL_PSEUDO_EVENTS": str(
            sum(int(row["Events"]) for row in VALUES["empirical"]["pseudo_events"])
        ),
        "SIM_REPLICATIONS": f"{VALUES['simulation']['replications_per_model']:,}",
        "NAIVE_WTP_COEF": f(float(naive["coefficient"])),
        "NAIVE_CI_LOW": f(float(naive["ci_low"])),
        "NAIVE_CI_HIGH": f(float(naive["ci_high"])),
        "ADJUSTED_WTP_COEF": f(float(adjusted["coefficient"])),
        "ADJUSTED_CI_LOW": f(float(adjusted["ci_low"])),
        "ADJUSTED_CI_HIGH": f(float(adjusted["ci_high"])),
        "CLUSTER_CI_LOW": f(float(cluster["ci_low"])),
        "CLUSTER_CI_HIGH": f(float(cluster["ci_high"])),
        "CLUSTERS": str(int(cluster["clusters"])),
        "RULE_CLUSTERS": str(int(cluster["region_rule_clusters"])),
        "REGRESSION_N": str(int(cluster["n"])),
        "PERM_OBSERVED": f(float(permutation["observed_adjusted_ols_coefficient"]), 4),
        "PERM_MEAN": f(float(permutation["permutation_mean"]), 4),
        "PERMUTATION_P": f(float(permutation["permutation_p_two_sided"])),
        "M0_EVENTS": f(simulation_value("M0_random_timing", "events"), 2),
        "M1_EVENTS": f(simulation_value("M1_drought_demand", "events"), 2),
        "M3_EVENTS": f(simulation_value("M3_strategic_selection", "events"), 2),
        "M0_SUCCESS": f(simulation_value("M0_random_timing", "apparent_success")),
        "M1_SUCCESS": f(simulation_value("M1_drought_demand", "apparent_success")),
        "M2_SUCCESS": f(simulation_value("M2_realistic_hazard", "apparent_success")),
        "M3_SUCCESS": f(
            simulation_value("M3_strategic_selection", "apparent_success")
        ),
        "M4_PRICE": f(simulation_value("M4_bayesian_reputation", "mean_price")),
        "M5_PRICE": f(simulation_value("M5_selective_recency", "mean_price")),
        "FIXED_PRICE": f(float(VALUES["simulation"]["parameters"]["fixed_price"])),
        "M4_PRICE_PREMIUM": f(
            simulation_value("M4_bayesian_reputation", "mean_price")
            - float(VALUES["simulation"]["parameters"]["fixed_price"])
        ),
        "M5_PRICE_PREMIUM": f(
            simulation_value("M5_selective_recency", "mean_price")
            - float(VALUES["simulation"]["parameters"]["fixed_price"])
        ),
        "M4_PROVIDER_PRICE_DISPERSION": f(
            simulation_value(
                "M4_bayesian_reputation", "provider_price_dispersion"
            )
        ),
        "M5_PROVIDER_PRICE_DISPERSION": f(
            simulation_value(
                "M5_selective_recency", "provider_price_dispersion"
            )
        ),
        "M4_REPUTATION": f(
            simulation_value("M4_bayesian_reputation", "reputation_dispersion")
        ),
        "M5_REPUTATION": f(
            simulation_value("M5_selective_recency", "reputation_dispersion")
        ),
        "M4_PRICE_SUCCESS": f(
            simulation_value(
                "M4_bayesian_reputation", "price_success_difference"
            )
        ),
        "M5_PRICE_SUCCESS": f(
            simulation_value("M5_selective_recency", "price_success_difference")
        ),
        "MAX_SUCCESS_MCSE": f(max_mcse, 4),
        "GEN_REPLICATIONS": f"{max(int(row['sample_size']) for row in VALUES['general']['convergence']):,}",
        "SEL_GAP_ENDO_COMMON": f(general_value("common", "endogenous", "selection_gap")),
        "SEL_GAP_ENDO_MOD": f(general_value("moderately_rare", "endogenous", "selection_gap")),
        "SEL_GAP_ENDO_RARE": f(general_value("rare", "endogenous", "selection_gap")),
        "SEL_GAP_ENDO_VRARE": f(general_value("very_rare", "endogenous", "selection_gap")),
        "SEL_RATIO_ENDO_COMMON": f(
            general_value("common", "endogenous", "selection_ratio"), 2
        ),
        "SEL_RATIO_ENDO_VRARE": f(
            general_value("very_rare", "endogenous", "selection_ratio"), 2
        ),
        "B_ABS_EXO_RARE": f(general_value("rare", "exogenous", "B_abs")),
        "B_SUBJ_SELECTIVE_ENDO_RARE": f(
            general_value("rare", "endogenous", "B_subj_selective")
        ),
        "P_SUBJ_SELECTIVE_ENDO_RARE": f(
            general_value("rare", "endogenous", "p_subj_selective")
        ),
        "P_EXP_ENDO_RARE": f(
            general_value("rare", "endogenous", "p_experienced")
        ),
        "D_REL_B_ENDO_COMMON": f(
            general_value("common", "endogenous", "D_rel_B_experienced"), 2
        ),
        "D_REL_B_ENDO_VRARE": f(
            general_value("very_rare", "endogenous", "D_rel_B_experienced"), 2
        ),
        "D_REL_C_ENDO_COMMON": f(
            general_value("common", "endogenous", "D_rel_C_weighted"), 2
        ),
        "D_REL_C_ENDO_VRARE": f(
            general_value("very_rare", "endogenous", "D_rel_C_weighted"), 2
        ),
        "D_REL_D_ENDO_COMMON": f(
            general_value("common", "endogenous", "D_rel_D_reputation"), 2
        ),
        "D_REL_D_ENDO_RARE": f(
            general_value("rare", "endogenous", "D_rel_D_reputation"), 2
        ),
        "D_EV_D_ENDO_COMMON": f(
            general_value("common", "endogenous", "D_EV_D_reputation")
        ),
        "D_EV_D_ENDO_VRARE": f(
            general_value("very_rare", "endogenous", "D_EV_D_reputation")
        ),
        "D_REL_D_ENDO_VRARE": f(
            general_value("very_rare", "endogenous", "D_rel_D_reputation"), 2
        ),
        "D_REL_REP_VRARE": f(
            general_value("very_rare", "endogenous", "D_rel_rep_D_reputation"), 2
        ),
        "D_REL_PROB_VRARE": f(
            general_value("very_rare", "endogenous", "D_rel_prob_D_reputation"), 2
        ),
        "PROB_SHARE_ENDO_COMMON": f(
            100
            * general_value("common", "endogenous", "D_rel_prob_D_reputation")
            / general_value("common", "endogenous", "D_rel_D_reputation"),
            1,
        ),
        "PROB_SHARE_ENDO_VRARE": f(
            100
            * general_value("very_rare", "endogenous", "D_rel_prob_D_reputation")
            / general_value("very_rare", "endogenous", "D_rel_D_reputation"),
            1,
        ),
        "PROB_SHARE_EXO_VRARE": f(
            100
            * general_value("very_rare", "exogenous", "D_rel_prob_D_reputation")
            / general_value("very_rare", "exogenous", "D_rel_D_reputation"),
            1,
        ),
        "REP_HAZARD_CORR_ENDO_RARE": f(
            general_value("rare", "endogenous", "reputation_hazard_corr")
        ),
        "PRICE_DIFF_D_ENDO_RARE": f(
            general_value("rare", "endogenous", "price_success_diff_D_reputation")
        ),
        "RANK_DIST_ENDO_COMMON": f(
            general_value("common", "endogenous", "provider_rank_distortion")
        ),
        "SEL_RATIO_ANALYTIC": f(analytic_selection_ratio(), 4),
        "SEL_RATIO_ANALYTIC_2DP": f(analytic_selection_ratio(), 2),
        "SEL_RATIO_ENDO_MIN": f(endo_selection_ratio_range()[0]),
        "SEL_RATIO_ENDO_MAX": f(endo_selection_ratio_range()[1]),
        "EQUIV_DELTA_MOD": f(equivalent_efficacy("moderately_rare")["delta"], 3),
        "EQUIV_DELTA_RARE": f(equivalent_efficacy("rare")["delta"], 3),
        "EQUIV_DELTA_VRARE": f(equivalent_efficacy("very_rare")["delta"], 4),
    }
    for token, rule in rules.items():
        output[f"{token}_SUCCESS_7D"] = f(
            pseudo_value(rule, "Apparent_success_7d")
        )
    return output


def crossref_message(doi: str) -> dict:
    slug = doi.lower().replace("/", "_").replace(".", "-")
    path = ROOT / "data" / "raw" / "literature" / f"crossref_{slug}.json"
    return json.loads(path.read_text())["message"]


def apa_author_list(message: dict) -> str:
    """APA7 author list: up to 20 authors; else first 19, ellipsis, last."""
    authors = message.get("author", [])

    def name(author: dict) -> str:
        family = author.get("family", "").strip()
        if family.isupper():
            family = family.title()
        initials = ". ".join(
            part[0].upper()
            for part in re.findall(r"[A-Za-zÀ-ÿ]+", author.get("given", ""))
        )
        return f"{family}, {initials}." if initials else family

    if len(authors) <= 20:
        names = [name(author) for author in authors]
    else:
        names = [name(author) for author in authors[:19]] + [
            "…",
            name(authors[-1]),
        ]
    if len(names) == 1:
        return names[0]
    joined = ", ".join(names)
    if "…" not in names:
        joined = ", ".join(names[:-1]) + ", & " + names[-1]
    return joined


def apa_first_family(message: dict) -> str:
    authors = message.get("author", [])
    family = authors[0].get("family", "").strip() if authors else ""
    return family.title() if family.isupper() else family


def apa_sort_key(doi: str) -> tuple:
    if doi == "10.14989/68028":
        return (("Akong'a",), 1987)
    if doi == "10.1093/ije/dyh299":
        return (("Barnett", "van der Pols", "Dobson"), 2005)
    message = crossref_message(doi)
    issued = (
        message.get("published-print")
        or message.get("published-online")
        or message.get("issued")
    )
    # APA: same first author -> fewer/alphabetical co-authors first, then year.
    families = tuple(
        (a.get("family", "").strip().title() if a.get("family", "").isupper() else a.get("family", "").strip())
        for a in message.get("author", [])
    )
    return (families, issued["date-parts"][0][0])


def format_reference(doi: str) -> str:
    if doi == "10.14989/68028":
        return (
            "Akong'a, J. (1987). Rainmaking rituals: A comparative study of "
            "two Kenyan societies. *African Study Monographs*, *8*(2), "
            "71–85. https://doi.org/10.14989/68028"
        )
    if doi == "10.1093/ije/dyh299":
        # CrossRef lists only the first author and the online date; PubMed
        # 15333621 (data/raw/literature/pubmed_15333621_esummary.json) gives
        # three authors and the 2005 print issue.
        return (
            "Barnett, A. G., van der Pols, J. C., & Dobson, A. J. (2005). "
            "Regression to the mean: What it is and how to deal with it. "
            "*International Journal of Epidemiology*, *34*(1), 215–220. "
            "https://doi.org/10.1093/ije/dyh299"
        )
    if doi == "10.1001/jama.293.10.1239":
        # CrossRef lists only the first author and the first page; the article
        # is by Werner and Asch, pages 1239–1244.
        return (
            "Werner, R. M., & Asch, D. A. (2005). The unintended consequences "
            "of publicly reporting quality information. *JAMA*, *293*(10), "
            "1239–1244. https://doi.org/10.1001/jama.293.10.1239"
        )
    message = crossref_message(doi)
    title = message.get("title", [""])[0].rstrip(".*")
    container = message.get("container-title", [""])[0]
    issued = (
        message.get("published-print")
        or message.get("published-online")
        or message.get("issued")
    )
    year = issued["date-parts"][0][0]
    volume = message.get("volume", "")
    issue = message.get("issue", "")
    pages = message.get("page", "")
    tail = ""
    if volume:
        tail += f", *{volume}*"
        if issue:
            tail += f"({issue})"
    if pages:
        tail += f", {pages}"
    journal_part = f" *{container}*{tail}." if container else f"{tail}."
    sep = "" if title.endswith(("?", "!")) else "."
    return (
        f"{apa_author_list(message)} ({year}). {title}{sep}{journal_part} "
        f"https://doi.org/{doi}"
    )


def reference_block() -> str:
    ordered = sorted(REFERENCE_ORDER, key=apa_sort_key)
    return "\n\n".join(format_reference(doi) for doi in ordered)


def render_template(source: Path, destination: Path) -> str:
    text = source.read_text()
    for token, value in replacements().items():
        text = text.replace(f"{{{{{token}}}}}", value)
    text = text.replace("{{REFERENCES}}", reference_block())
    unresolved = re.findall(r"\{\{[A-Z0-9_]+\}\}", text)
    allowed = set(FIGURE_FILES) | set(TABLE_FILES)
    unexpected = [token for token in unresolved if token[2:-2] not in allowed]
    if unexpected:
        raise ValueError(f"Unresolved manuscript tokens: {unexpected}")
    if source.name == "manuscript_template.md":
        body = text.split("## References", maxsplit=1)[0]
        uncited = [
            doi
            for doi, token in REFERENCE_CITE_TOKENS.items()
            if token not in body
        ]
        if uncited:
            raise ValueError(f"References not cited in manuscript: {uncited}")
    destination.write_text(text)
    return text


def add_omml(paragraph, latex: str) -> None:
    paragraph._element.append(
        mathml_to_omml(latex_to_mathml(latex))
    )


def add_inline_runs(paragraph, text: str) -> None:
    parts = re.split(r"(\*\*.*?\*\*|\\\(.*?\\\)|\*[^*]+\*)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith(r"\(") and part.endswith(r"\)"):
            add_omml(paragraph, part[2:-2])
        elif part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif (
            part.startswith("*")
            and part.endswith("*")
            and len(part) > 2
        ):
            run = paragraph.add_run(part[1:-1])
            run.italic = True
        else:
            paragraph.add_run(part)


def set_cell_shading(cell, fill: str) -> None:
    properties = cell._tc.get_or_add_tcPr()
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), fill)
    properties.append(shading)


def add_table(document: Document, marker: str) -> None:
    frame = pd.read_csv(TABLE_FILES[marker])
    caption_text = MAIN_TABLE_CAPTIONS.get(
        marker, SUPPLEMENT_TABLE_CAPTIONS.get(marker, marker.replace("_", " "))
    )
    caption = document.add_paragraph()
    caption.paragraph_format.space_before = Pt(16)
    caption.paragraph_format.space_after = Pt(6)
    caption_run = caption.add_run(caption_text)
    caption_run.bold = True
    table = document.add_table(rows=1, cols=len(frame.columns))
    table.style = "Table Grid"
    table.autofit = True
    header = table.rows[0]
    header._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
    for cell, column in zip(header.cells, frame.columns):
        cell.text = str(column).replace("_", " ")
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        set_cell_shading(cell, "D9EAF7")
        for run in cell.paragraphs[0].runs:
            run.bold = True
            run.font.size = Pt(7)
    for row in frame.itertuples(index=False, name=None):
        table_row = table.add_row()
        row_properties = table_row._tr.get_or_add_trPr()
        row_properties.append(OxmlElement("w:cantSplit"))
        cells = table_row.cells
        for cell, value in zip(cells, row):
            if isinstance(value, float):
                cell.text = f"{value:.3f}"
            else:
                cell.text = str(value)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(7)


def add_figure(document: Document, marker: str) -> None:
    number = marker.split("_")[1]
    document.add_picture(str(FIGURE_FILES[marker]), width=Inches(6.25))
    image_paragraph = document.paragraphs[-1]
    image_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    caption = document.add_paragraph()
    caption.paragraph_format.space_before = Pt(12)
    caption.paragraph_format.space_after = Pt(8)
    run = caption.add_run(
        "Fig. {} {}".format(
            number,
            jru_caption(VALUES["figure_captions"]["Figure " + str(number)]),
        )
    )
    run.bold = True


def configure_document(document: Document) -> None:
    section = document.sections[0]
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    styles = document.styles
    normal = styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)
    normal.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    normal.paragraph_format.space_after = Pt(0)
    from docx.shared import RGBColor
    for name in ["Title", "Heading 1", "Heading 2", "Heading 3"]:
        styles[name].font.name = "Times New Roman"
        styles[name].font.color.rgb = RGBColor(0, 0, 0)
    if "Figure Caption" not in styles:
        style = styles.add_style("Figure Caption", WD_STYLE_TYPE.PARAGRAPH)
        style.font.name = "Times New Roman"
        style.font.size = Pt(10)


def markdown_to_docx(
    markdown: str, destination: Path, journal_layout: bool = False
) -> None:
    document = Document()
    configure_document(document)
    blocks = re.split(r"\n\s*\n", markdown.strip())
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        if lines[0].startswith("- "):
            items = []
            current = ""
            for line in lines:
                if line.startswith("- "):
                    if current:
                        items.append(current)
                    current = line[2:]
                else:
                    current += " " + line
            if current:
                items.append(current)
            for item in items:
                paragraph = document.add_paragraph(style="List Bullet")
                add_inline_runs(paragraph, item)
            continue
        if re.match(r"^\d+\. ", lines[0]):
            items = []
            current = ""
            for line in lines:
                if re.match(r"^\d+\. ", line):
                    if current:
                        items.append(current)
                    current = line
                else:
                    current += " " + line
            if current:
                items.append(current)
            for item in items:
                paragraph = document.add_paragraph()
                paragraph.paragraph_format.left_indent = Inches(0.25)
                paragraph.paragraph_format.first_line_indent = Inches(-0.25)
                add_inline_runs(paragraph, item)
            continue
        if lines[0] == r"\[" and lines[-1] == r"\]":
            paragraph = document.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            latex = " ".join(
                line.strip() for line in lines[1:-1] if line.strip()
            )
            add_omml(paragraph, latex)
            continue
        line = " ".join(lines)
        marker_match = re.fullmatch(r"\{\{([A-Z0-9_]+)\}\}", line)
        if marker_match:
            marker = marker_match.group(1)
            if marker in FIGURE_FILES:
                add_figure(document, marker)
            elif marker in TABLE_FILES:
                add_table(document, marker)
            continue
        if line.startswith("# "):
            paragraph = document.add_paragraph(style="Title")
            add_inline_runs(paragraph, line[2:])
            if journal_layout:
                # Double-blind layout: page 1 holds the title only.
                paragraph.add_run().add_break(WD_BREAK.PAGE)
            continue
        if line.startswith("## "):
            paragraph = document.add_heading(level=1)
            add_inline_runs(paragraph, line[3:])
            continue
        if line.startswith("### "):
            paragraph = document.add_heading(level=2)
            add_inline_runs(paragraph, line[4:])
            continue
        paragraph = document.add_paragraph()
        add_inline_runs(paragraph, line)
        if journal_layout and line.startswith("**Keywords:**"):
            # Page 2 holds the abstract and keywords; main text starts page 3.
            paragraph.add_run().add_break(WD_BREAK.PAGE)
    document.save(destination)


def manuscript_word_count(text: str) -> int:
    body = text.split("## References", maxsplit=1)[0]
    body = re.sub(r"\{\{[A-Z0-9_]+\}\}", "", body)
    return len(re.findall(r"\b[\w’'-]+\b", body))


def keyword_count(text: str) -> int:
    line = text.split("**Keywords:**", 1)[1].split("\n\n", 1)[0]
    return len([item for item in line.split(";") if item.strip()])


def pdf_pages(path: Path) -> int:
    info = subprocess.run(
        ["pdfinfo", str(path)], check=True, capture_output=True, text=True
    ).stdout
    return int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))


def abstract_word_count(text: str) -> int:
    abstract = text.split("## Abstract", 1)[1].split("**Keywords:**", 1)[0]
    return len(re.findall(r"\b[\w’'-]+\b", abstract))


def make_title_page() -> None:
    document = Document()
    configure_document(document)
    title = document.add_paragraph(style="Title")
    title.add_run(TITLE)
    for label, value in [
        ("Article type", ARTICLE_TYPE),
        ("Author(s)", "[AUTHOR INPUT REQUIRED]"),
        ("Affiliation(s)", "[AUTHOR INPUT REQUIRED]"),
        ("Corresponding author", "[AUTHOR INPUT REQUIRED]"),
        ("Email and postal address", "[AUTHOR INPUT REQUIRED]"),
        ("Telephone number", "[AUTHOR INPUT REQUIRED]"),
        ("ORCID(s)", "[AUTHOR INPUT REQUIRED, if applicable]"),
        ("JEL classification", JEL_CODES),
    ]:
        paragraph = document.add_paragraph()
        run = paragraph.add_run(f"{label}: ")
        run.bold = True
        paragraph.add_run(value)
    document.save(MANUSCRIPT / "title_page.docx")


def make_supporting_files(
    word_count: int, abstract_count: int, keyword_count: int
) -> None:
    location_count = int(VALUES["study"]["locations"])
    cover = f"""# Cover letter draft

Dear Editors,

Please consider my research article, "{TITLE}," for publication
in *{JOURNAL}*.

The paper studies how economic inference and model-implied quotes are
shaped when the histories people price from are selectively generated.
When participation and observation depend on the same risk state that
generates outcomes, experienced frequencies diverge from objective risk;
subjective transformation of that selected experience and
history-dependent reputation then determine what a posted quote encodes.
I formalize this separation analytically and quantify it in a generic
simulation and a controlled known-zero benchmark.

The building blocks are established, and the paper presents them as
such: endogenous sampling biases experience-based estimates, the
selected/unselected risk ratio is a standard selection identity (one plus a
scaled covariance between state risk and the observation weight), and the
divergence of the transformed relative term is a known property of the
Prelec function. The incremental contributions are four. First, a simple
comparative static: under multiplicative state risk the selection ratio does
not depend on baseline rarity, while the absolute gap shrinks with it.
Second, an accounting decomposition of a reduced-form quote into objective,
experienced, subjective, and reputation layers, with every layer measured
relative to objective risk. Third, a simulated stock–flow decoupling:
reputation premia coexist with weak or negative contemporaneous
price–success differences—including negative mean contemporaneous
price-success differences in the controlled benchmark—so the sign of the
price-performance correlation is not a test of whether pricing works.
Fourth, a first-moment equivalence: in several simulated rare regimes,
zero-efficacy endogenous selection reproduces the mean apparent performance
of positive efficacy under exogenous observation.

The quote rule is given an explicit reduced-form interpretation—a share
of perceived gross surplus plus a separable reputation component—with no
equilibrium, bargaining, or welfare-optimality claim. As supporting
evidence, a known-zero-effect benchmark places fictional rainmaking
pseudo-events over {location_count} archived region-days of observed
rainfall: selection and timing alone generate elevated apparent success
under exactly zero causal efficacy. The pricing and reputation overlay on
that benchmark is a calibrated model result, not observed market pricing,
estimated willingness to pay, or human probability weighting; the paper
contains no human-subject or market transaction data and makes no claim
to estimate behavior.

The paper fits the *Journal of Risk and Uncertainty* because it is about
decision making under uncertainty when the counterfactual is hidden: how
endogenous observation changes experienced risk, how subjective
probability transformation and reputation act on that selected
experience, and what can and cannot be inferred about underlying efficacy
from the resulting record. It builds on work on decisions from
experience and low-probability risk, including work published in this
journal.

[AUTHOR CONFIRMATION REQUIRED: The manuscript is original and is not under
consideration elsewhere.] It uses no human participants or confidential data.
All code, acquisition records, checksums, machine-readable results, and
reproducibility materials are available through the accompanying public
repository. ERA5 rainfall data are not redistributed but can be re-acquired
through the public Open-Meteo archive with the recorded requests.

[AUTHOR INPUT REQUIRED: corresponding author name, affiliation, contact details,
funding, competing interests, acknowledgements, and any suggested reviewers.]

Sincerely,

[AUTHOR INPUT REQUIRED]
"""
    (MANUSCRIPT / "cover_letter.md").write_text(cover)
    cover_docx = MANUSCRIPT / "cover_letter.docx"
    markdown_to_docx(cover, cover_docx)
    convert_to_pdf(cover_docx)
    declarations = """# Submission declarations

- **Funding:** [AUTHOR INPUT REQUIRED]
- **Competing interests:** [AUTHOR INPUT REQUIRED]
- **CRediT authorship:** [AUTHOR INPUT REQUIRED]
- **Acknowledgements:** [AUTHOR INPUT REQUIRED]
- **Ethics:** Public environmental data, bibliographic metadata, and fictional
  simulations only; no human participants, personal data, or animal research.
- **Data and code:** Public code, frozen outputs, and acquisition ledgers:
  https://github.com/bougtoir/pricing-the-rain. ERA5 data are not
  redistributed; they are re-acquired from the public Open-Meteo archive.
- **Generative AI:** During preparation of this work, the authors used Devin
  (Cognition AI) to assist with code development, manuscript drafting, and language
  organization. [AUTHOR CONFIRMATION REQUIRED: after using this tool, the authors
  reviewed and edited the content as needed and take full responsibility for the
  content of the publication.] No generative-AI image tool was used to create or alter
  scientific figures.
"""
    (MANUSCRIPT / "declarations.md").write_text(declarations)
    metrics = {
        "journal": JOURNAL,
        "article_type": ARTICLE_TYPE,
        "main_text_words_excluding_references": word_count,
        "abstract_words": abstract_count,
        "references": len(REFERENCE_ORDER),
        "figures": len(FIGURE_FILES),
        "main_tables": 4,
        "supplementary_tables": 10,
        "keywords": keyword_count,
        "pages_blinded_pdf": pdf_pages(MANUSCRIPT / "manuscript_blinded.pdf"),
        "jel": JEL_CODES,
    }
    (MANUSCRIPT / "manuscript_metrics.json").write_text(
        json.dumps(metrics, indent=2) + "\n"
    )


def make_submission_archive() -> None:
    archive_path = MANUSCRIPT / (
        "pricing_rare_events_jru_submission.zip"
    )
    main_files = [
        MANUSCRIPT / "manuscript_blinded.docx",
        MANUSCRIPT / "manuscript_blinded.pdf",
        MANUSCRIPT / "manuscript_text.docx",
        MANUSCRIPT / "manuscript_text.pdf",
        MANUSCRIPT / "title_page.docx",
        MANUSCRIPT / "cover_letter.docx",
        MANUSCRIPT / "cover_letter.pdf",
        MANUSCRIPT / "declarations.md",
        SUPPLEMENT / "supplement.docx",
        SUPPLEMENT / "supplement.pdf",
        FIGURES / "figures_editable.pptx",
        TABLES / "main_tables_editable.docx",
        TABLES / "supplementary_tables_editable.docx",
        ROOT / "AUTHOR_ACTIONS_REQUIRED.md",
        ROOT / "docs" / "JRU_COMPLIANCE_CHECKLIST.md",
        ROOT / "docs" / "JRU_CLOSEST_PRIOR_STUDIES_MATRIX.md",
        ROOT / "docs" / "JRU_NOVELTY_GATE.md",
        ROOT / "docs" / "JRU_CITATION_ECOLOGY.md",
        ROOT / "docs" / "JRU_RETARGETING_REPORT.md",
        ROOT / "docs" / "JRU_SEMANTIC_CODE_AUDIT.md",
        ROOT / "docs" / "JRU_CODE_MANUSCRIPT_CROSSWALK.md",
        ROOT / "docs" / "JRU_LOOKAHEAD_CORRECTION_AUDIT.md",
        ROOT / "docs" / "JRU_NUMERIC_HARDCODE_AUDIT.md",
        ROOT / "docs" / "JRU_PUBLIC_REPRODUCIBILITY_AUDIT.md",
        ROOT / "docs" / "JRU_RESULT_TRACEABILITY.md",
        ROOT / "docs" / "JRU_DATA_TEXT_FIGURE_CONSISTENCY.md",
        ROOT / "docs" / "JRU_CITATION_AUDIT.md",
        ROOT / "docs" / "JRU_HOSTILE_REVIEW_REPORT.md",
        ROOT / "docs" / "JRU_FINAL_SUBMISSION_AUDIT.md",
        ROOT / "docs" / "JEBO_COMPLIANCE_CHECKLIST.md",
        ROOT / "docs" / "JEBO_CITATION_ECOLOGY.md",
        ROOT / "docs" / "JEBO_RETARGETING_REPORT.md",
        ROOT / "docs" / "JEBO_HOSTILE_REVIEW_REPORT.md",
        ROOT / "docs" / "JEBO_NUMERIC_HARDCODE_AUDIT.md",
        ROOT / "docs" / "JEBO_PUBLIC_REPRODUCIBILITY_AUDIT.md",
        ROOT / "docs" / "JEBO_RESULT_TRACEABILITY.md",
        ROOT / "docs" / "JEBO_DATA_TEXT_FIGURE_CONSISTENCY.md",
        ROOT / "docs" / "JEBO_CITATION_AUDIT.md",
        ROOT / "docs" / "JEBO_FINAL_SUBMISSION_AUDIT.md",
        ROOT / "docs" / "ECONOMIC_MODELLING_COMPLIANCE_CHECKLIST.md",
        ROOT / "docs" / "QREF_COMPLIANCE_CHECKLIST.md",
        ROOT / "docs" / "QREF_CITATION_ECOLOGY.md",
        ROOT / "docs" / "QREF_RETARGETING_REPORT.md",
        ROOT / "docs" / "QREF_HOSTILE_REVIEW_REPORT.md",
        ROOT / "docs" / "QREF_NUMERIC_HARDCODE_AUDIT.md",
        ROOT / "docs" / "QREF_FINAL_RETARGETING_AUDIT_REPORT.md",
        ROOT / "docs" / "QREF_CITATION_AUDIT.md",
        ROOT / "docs" / "QREF_FINAL_CLOSURE_REPORT.md",
        ROOT / "docs" / "ARCHIVED_PRE_TARGETED_REVISION_REPORT.md",
        ROOT / "docs" / "GENERALIZATION_DECISION_LOG.md",
        ROOT / "docs" / "FINAL_TARGETED_REVISION_REPORT.md",
        ROOT / "docs" / "FINAL_ECONOMIC_MODELLING_FINISHING_REPORT.md",
        ROOT / "docs" / "RARE_EVENT_TARGETED_REVISION_LOG.md",
        ROOT / "docs" / "GENERIC_PROBABILITY_ESTIMAND_AUDIT.md",
        ROOT / "docs" / "EXOGENOUS_BENCHMARK_AUDIT.md",
        ROOT / "docs" / "SELECTION_RATIO_DERIVATION.md",
        ROOT / "docs" / "CRITICAL_REVIEW_RESPONSE_LOG.md",
        ROOT / "docs" / "FINAL_CRITICAL_REVIEW_REVISION_REPORT.md",
        ROOT / "docs" / "PRICE_DECOMPOSITION_FINAL_AUDIT.md",
        ROOT / "docs" / "FINAL_DECOMPOSITION_REVISION_REPORT.md",
        ROOT / "docs" / "FINAL_SUBMISSION_PASS_REPORT.md",
        ROOT / "docs" / "HOSTILE_REVIEW_RESPONSE_LOG.md",
        ROOT / "docs" / "ECONOMIC_MODELLING_CITATION_ECOLOGY.md",
        ROOT / "docs" / "FINAL_HOSTILE_REVIEW_REPORT.md",
        ROOT / "docs" / "FINAL_TWO_SENTENCE_MICRO_PASS_REPORT.md",
        RESULTS / "general_equivalent_efficacy.csv",
    ]
    figure_files = [
        FIGURES / f"{stem}.{ext}"
        for stem in [
            "figure1_framework",
            "figure3_empirical_hazard",
            "figure2_pseudo_event_success",
            "figure7_simulation_decomposition",
            "figure8_robustness",
            "figure4_four_probabilities",
            "figure6_observational_equivalence",
            "figure5_distortion_decomposition",
        ]
        for ext in ("pdf", "png")
    ]
    package: dict[str, Path] = {
        f"{source.name}": source for source in main_files
    }
    package.update(
        {f"figures/{source.name}": source for source in figure_files}
    )
    package.update(
        {
            f"tables/{source}": TABLES / source
            for source in [
                "table1_proposition_classification.csv",
                "table2_general_regimes.csv",
                "table3_study_locations.csv",
                "table4_observational_equivalence.csv",
                "table5_pseudo_event_results.csv",
                "table6_simulation_results.csv",
            ]
        }
    )
    readme = """# Submission package — Journal of Risk and Uncertainty

- manuscript_blinded.docx/.pdf: manuscript without author identification,
  figures (Fig. 1–8) and tables placed in the text; the title page is a
  separate file.
- manuscript_text.docx/.pdf: text-only manuscript with figure captions.
- title_page.docx: title page (article type, authors, affiliations,
  corresponding author, ORCID, JEL codes).
- cover_letter.docx/.pdf, declarations.md: cover letter and Statements and
  Declarations with author-action placeholders.
- supplement.docx/.pdf: Online Resource 1 (Tables S1–S10).
- figures/: figure files (vector PDF + 600-dpi PNG).
- tables/: main tables as CSV; tables/*_editable.docx and
  figures_editable.pptx are editable versions.
- AUTHOR_ACTIONS_REQUIRED.md and the JRU_* audit reports are for the
  author's records, not for upload. JEBO_*, QREF_*, FINAL_* and
  ECONOMIC_MODELLING_* reports are superseded and kept for provenance.
"""
    package["README.md"] = readme
    package.update(
        {
            f"replication/{name}": ROOT / name
            for name in ("README.md", "README.docx", "README.pdf")
        }
    )
    package["replication/REPLICATION_README_AUDIT.md"] = (
        ROOT / "docs" / "REPLICATION_README_AUDIT.md"
    )
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, source in package.items():
            if isinstance(source, Path):
                if not source.exists():
                    raise FileNotFoundError(
                        f"Missing submission artifact: {source}"
                    )
                payload = source.read_bytes()
            else:
                payload = source.encode("utf-8")
            info = zipfile.ZipInfo(name)
            info.date_time = (1980, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, payload)


def jru_caption(text: str) -> str:
    """JRU style: no punctuation after the figure number or at caption end."""
    return text.strip().rstrip(".;:")


def make_submission_text(rendered: str) -> str:
    text = rendered
    for marker in FIGURE_FILES:
        text = text.replace(f"{{{{{marker}}}}}", "")
    legends = "\n\n".join(
        "**Fig. {}** {}".format(
            number, jru_caption(VALUES["figure_captions"][f"Figure {number}"])
        )
        for number in (marker.split("_")[1] for marker in FIGURE_FILES)
    )
    return text.rstrip() + "\n\n## Figure legends\n\n" + legends + "\n"


def convert_to_pdf(path: Path) -> None:
    subprocess.run(
        [
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(path.parent),
            str(path),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def main() -> None:
    rendered = render_template(
        MANUSCRIPT / "manuscript_template.md", MANUSCRIPT / "manuscript.md"
    )
    supplement = render_template(
        SUPPLEMENT / "supplement_template.md", SUPPLEMENT / "supplement.md"
    )
    main_docx = MANUSCRIPT / "manuscript_blinded.docx"
    submission_docx = MANUSCRIPT / "manuscript_text.docx"
    supplement_docx = SUPPLEMENT / "supplement.docx"
    markdown_to_docx(rendered, main_docx, journal_layout=True)
    submission_text = make_submission_text(rendered)
    (MANUSCRIPT / "manuscript_text.md").write_text(submission_text)
    markdown_to_docx(submission_text, submission_docx, journal_layout=True)
    markdown_to_docx(supplement, supplement_docx)
    make_title_page()
    convert_to_pdf(main_docx)
    convert_to_pdf(submission_docx)
    convert_to_pdf(supplement_docx)
    readme_docx = ROOT / "README.docx"
    markdown_to_docx((ROOT / "README.md").read_text(encoding="utf-8"), readme_docx)
    convert_to_pdf(readme_docx)
    words = manuscript_word_count(rendered)
    abstract_words = abstract_word_count(rendered)
    make_supporting_files(words, abstract_words, keyword_count(rendered))
    make_submission_archive()
    print(
        f"Built manuscript ({words} words; abstract {abstract_words} words), "
        "supplement, title page, cover letter, and submission archive"
    )


if __name__ == "__main__":
    main()
