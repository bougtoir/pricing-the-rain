from __future__ import annotations

import json
import re
import subprocess
import zipfile
from pathlib import Path

import pandas as pd
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
    "Apparent Performance under Selective Environmental Risk: Strategic "
    "Acceptance and Reputation under a Zero-Effect Rainfall Null"
)
ARTICLE_TYPE = "Original Research"
JOURNAL = "Risk Analysis"

REFERENCE_ORDER = [
    "10.14989/68028",
    "10.1093/ije/dyh299",
    "10.1086/261849",
    "10.1016/j.ecolecon.2011.11.011",
    "10.1111/j.2517-6161.1972.tb00899.x",
    "10.1086/374180",
    "10.5751/es-12875-270209",
    "10.1093/qje/qjag026",
    "10.2307/1912352",
    "10.1111/j.1475-4932.2006.00293.x",
    "10.1002/qj.3803",
    "10.1016/j.cosust.2018.09.005",
    "10.1016/j.ecolecon.2015.01.006",
    "10.1016/0022-0531(82)90030-8",
    "10.1175/1520-0434(1993)008<0281:wiagfa>2.0.co;2",
    "10.1016/j.cosust.2016.12.006",
    "10.1029/2000wr900320",
    "10.1016/j.ecolecon.2024.108425",
    "10.4102/hts.v69i1.1175",
    "10.1161/circulationaha.107.747873",
    "10.1037/h0055873",
    "10.1126/science.185.4157.1124",
    "10.1001/jama.293.10.1239",
]

# Every DOI in REFERENCE_ORDER must be cited in the manuscript text. Each entry
# maps the DOI to a surname token that must appear inside a citation.
REFERENCE_CITE_TOKENS = {
    "10.14989/68028": "Akong'a",
    "10.1093/ije/dyh299": "Barnett",
    "10.1086/261849": "Bikhchandani",
    "10.1016/j.ecolecon.2011.11.011": "Chan",
    "10.1111/j.2517-6161.1972.tb00899.x": "Cox",
    "10.1086/374180": "Dranove",
    "10.5751/es-12875-270209": "Espín-Sánchez & Gil-Guirado, 2022",
    "10.1093/qje/qjag026": "Espín-Sánchez",
    "10.2307/1912352": "Heckman",
    "10.1111/j.1475-4932.2006.00293.x": "Hensher",
    "10.1002/qj.3803": "Hersbach",
    "10.1016/j.cosust.2018.09.005": "Himes",
    "10.1016/j.ecolecon.2015.01.006": "Kenter",
    "10.1016/0022-0531(82)90030-8": "Kreps",
    "10.1175/1520-0434(1993)008<0281:wiagfa>2.0.co;2": "Murphy",
    "10.1016/j.cosust.2016.12.006": "Pascual",
    "10.1029/2000wr900320": "Pattanayak",
    "10.1016/j.ecolecon.2024.108425": "Schrieks",
    "10.4102/hts.v69i1.1175": "Semenya",
    "10.1161/circulationaha.107.747873": "Shahian",
    "10.1037/h0055873": "Skinner",
    "10.1126/science.185.4157.1124": "Tversky",
    "10.1001/jama.293.10.1239": "Werner",
}

FIGURE_FILES = {
    "FIGURE_1": FIGURES / "figure1_framework.png",
    "FIGURE_2": FIGURES / "figure2_empirical_hazard.png",
    "FIGURE_3": FIGURES / "figure3_pseudo_event_success.png",
    "FIGURE_4": FIGURES / "figure4_simulation_decomposition.png",
    "FIGURE_5": FIGURES / "figure5_robustness.png",
}

TABLE_FILES = {
    "TABLE_1": TABLES / "table1_study_locations.csv",
    "TABLE_2": TABLES / "table2_pseudo_event_results.csv",
    "TABLE_3": TABLES / "table3_simulation_results.csv",
    "TABLE_4": TABLES / "table4_hypothesis_classification.csv",
    "TABLE_S1": TABLES / "table_s1_price_models.csv",
    "TABLE_S2": TABLES / "table_s2_threshold_window_sensitivity.csv",
    "TABLE_S3": TABLES / "table_s3_parameter_sensitivity.csv",
    "TABLE_S4": TABLES / "table_s4_simulation_convergence.csv",
    "TABLE_S5": TABLES / "table_s5_permutation_falsification.csv",
    "TABLE_S6": TABLES / "table_s6_accounting.csv",
}

MAIN_TABLE_CAPTIONS = {
    "TABLE_1": "Table 1. Study locations and rainfall observations.",
    "TABLE_2": "Table 2. Observed-weather zero-effect stress-test results.",
    "TABLE_3": "Table 3. Monte Carlo model decomposition.",
    "TABLE_4": "Table 4. Analytic proposition classification.",
}

SUPPLEMENT_TABLE_CAPTIONS = {
    "TABLE_S1": "Table S1. Scenario price models.",
    "TABLE_S2": "Table S2. Rainfall-threshold and attribution-window sensitivity.",
    "TABLE_S3": "Table S3. Simulation parameter sensitivity.",
    "TABLE_S4": "Table S4. Monte Carlo convergence and precision.",
    "TABLE_S5": "Table S5. Permutation falsification.",
    "TABLE_S6": "Table S6. Simulated transfer, cost, profit, and surplus accounting.",
}


def f(value: float, digits: int = 3) -> str:
    return f"{value:.{digits}f}"


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


def replacements() -> dict[str, str]:
    naive = model_row("naive")
    adjusted = model_row("hazard-adjusted")
    cluster = cluster_row()
    permutation = VALUES["empirical"]["permutation_falsification"][0]
    max_mcse = max(
        float(row["monte_carlo_se"])
        for row in VALUES["simulation"]["convergence"]
        if row["sample_size"] == 10000 and row["outcome"] == "apparent_success"
    )
    rules = {
        "DEFICIT": "30-day deficit threshold",
        "DRYSPELL": "dry-spell threshold",
        "HAZARD": "high prospective hazard",
        "RANDOM": "random drought day",
        "PLACEBO": "season-matched placebo",
    }
    output = {
        "TOTAL_REGION_DAYS": str(VALUES["study"]["region_days"]),
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
        return ("Akong'a", 1987)
    message = crossref_message(doi)
    issued = (
        message.get("published-print")
        or message.get("published-online")
        or message.get("issued")
    )
    return (apa_first_family(message), issued["date-parts"][0][0])


def format_reference(doi: str) -> str:
    if doi == "10.14989/68028":
        return (
            "Akong'a, J. (1987). Rainmaking rituals: A comparative study of "
            "two Kenyan societies. *African Study Monographs*, *8*(2), "
            "71–85. https://doi.org/10.14989/68028"
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
    number = int(marker.split("_")[1])
    document.add_picture(str(FIGURE_FILES[marker]), width=Inches(6.25))
    image_paragraph = document.paragraphs[-1]
    image_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    caption = document.add_paragraph()
    caption.paragraph_format.space_before = Pt(12)
    caption.paragraph_format.space_after = Pt(8)
    run = caption.add_run(
        f"Figure {number}. {VALUES['figure_captions'][f'Figure {number}']}"
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
    ]:
        paragraph = document.add_paragraph()
        run = paragraph.add_run(f"{label}: ")
        run.bold = True
        paragraph.add_run(value)
    document.save(MANUSCRIPT / "title_page.docx")


def make_supporting_files(word_count: int, abstract_count: int) -> None:
    location_count = int(VALUES["study"]["locations"])
    cover = f"""# Cover letter draft

Dear Editors,

Please consider my Original Research manuscript, "{TITLE}," for publication
in *{JOURNAL}*.

The manuscript addresses a general problem in performance evaluation: when
baseline environmental hazard is heterogeneous and providers can select their
exposure to that risk, raw observed performance may reflect risk composition
and selective acceptance rather than causal provider performance. The
untreated counterfactual is unobserved, so the components cannot be separated
by outcome rates alone.

The study uses rainmaking as a deliberately sharp known-ground-truth stress
test in which the intervention's causal effect on rainfall is fixed exactly at
zero. Because true efficacy is not ambiguous, apparent performance generated
by baseline hazard, selective exposure, attribution, and learning can be
measured directly. Using archived ERA5 rainfall at {location_count}
contrasting rainfall regimes, I show that selective acceptance can materially
raise apparent performance without changing rainfall: seven-day apparent
success ranges from 0.593 under random drought timing to 0.853 under high
prospective hazard.

A second result concerns dynamics. Past attributed outcomes accumulate into a
provider-specific reputation stock, whereas current apparent performance
remains a flow governed by current environmental hazard. Reputation and price
premia therefore need not imply superior contemporaneous performance; in the
simulation the contemporaneous price-success association is negative even
while premia persist.

The paper separates each component—baseline hazard, endogenous demand,
selective acceptance, attribution, and reputation learning—through a staged
Monte Carlo decomposition, and stress-tests the conclusions across thresholds,
parameters, replication counts, and a pre-specified permutation falsification.
Willingness-to-pay and price results are presented as calibrated and simulated
consequences of attributed performance, not as historical estimates, and the
positive contemporaneous price-success proposition is explicitly reported as
unsupported.

I believe this question sits within the scope of *Risk Analysis*: performance
inference under heterogeneous risk, selective exposure, hidden
counterfactuals, risk adjustment, reputation, and decision-making under
uncertainty. Espín-Sánchez, Gil-Guirado, and Ryan establish the rain-prayer
timing, hazard, and persuasion foundation and its historical evidence; this
manuscript asks a different risk-analysis question—what raw provider
performance means once requests, selective acceptance, provider-specific
reputation, and risk-conditioned outcomes are separated.

The practical implication is restrained but consequential: raw performance
measures may reward favorable exposure rather than causal improvement, which
motivates prospective risk adjustment and disclosure of rejected cases as
candidate safeguards for provider scorecards and performance contracts.

[AUTHOR CONFIRMATION REQUIRED: The manuscript is original and is not under
consideration elsewhere.] It uses no human participants or confidential data.
All redistributable analytical inputs, code, acquisition records, checksums,
simulation outputs, and manuscript values accompany the submission; exact
retrieval records are supplied for audit sources that are not redistributed.

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
- **Data and code:** Public code, legally redistributable inputs, frozen outputs, and
  acquisition ledgers: https://github.com/bougtoir/pricing-the-rain.
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
        "supplementary_tables": 6,
        "keywords": 5,
    }
    (MANUSCRIPT / "manuscript_metrics.json").write_text(
        json.dumps(metrics, indent=2) + "\n"
    )


def make_submission_archive() -> None:
    archive_path = MANUSCRIPT / (
        "pricing_apparent_environmental_performance_submission.zip"
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
        ROOT / "docs" / "RISK_ANALYSIS_COMPLIANCE_CHECKLIST.md",
        ROOT / "docs" / "FINAL_RISK_ANALYSIS_REPORT.md",
        ROOT / "docs" / "FINAL_RISK_ANALYSIS_FINISHING_REPORT.md",
    ]
    figure_files = [
        FIGURES / f"{stem}.{ext}"
        for stem in [
            "figure1_framework",
            "figure2_empirical_hazard",
            "figure3_pseudo_event_success",
            "figure4_simulation_decomposition",
            "figure5_robustness",
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
                "table1_study_locations.csv",
                "table2_pseudo_event_results.csv",
                "table3_simulation_results.csv",
                "table4_hypothesis_classification.csv",
            ]
        }
    )
    readme = """# Submission package — Risk Analysis

- manuscript_blinded.docx/.pdf: double-blind manuscript, title-only first page,
  figures and tables inline.
- manuscript_text.docx/.pdf: text-only manuscript with figure legends.
- title_page.docx: separate title page (article type: Original Research).
- cover_letter.docx/.pdf, declarations.md: cover letter and declarations with
  author-action placeholders.
- supplement.docx/.pdf: supplementary material (Tables S1–S6).
- figures/: journal figure files (vector PDF + 600-dpi PNG).
- tables/: main tables as CSV.
- figures_editable.pptx, tables/*_editable.docx: editable figure/table decks.
- AUTHOR_ACTIONS_REQUIRED.md, RISK_ANALYSIS_COMPLIANCE_CHECKLIST.md, and
  FINAL_RISK_ANALYSIS_REPORT.md are included for the author's records, not
  for upload.
"""
    package["README.md"] = readme
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


def make_submission_text(rendered: str) -> str:
    text = rendered
    for marker in FIGURE_FILES:
        text = text.replace(f"{{{{{marker}}}}}", "")
    legends = "\n\n".join(
        f"**Figure {number}.** {VALUES['figure_captions'][f'Figure {number}']}"
        for number in range(1, 6)
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
    words = manuscript_word_count(rendered)
    abstract_words = abstract_word_count(rendered)
    make_supporting_files(words, abstract_words)
    make_submission_archive()
    print(
        f"Built manuscript ({words} words; abstract {abstract_words} words), "
        "supplement, title page, cover letter, and submission archive"
    )


if __name__ == "__main__":
    main()
