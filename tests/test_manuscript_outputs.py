import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript"


def test_submission_limits_and_no_numeric_placeholders() -> None:
    metrics = json.loads((MANUSCRIPT / "manuscript_metrics.json").read_text())
    text = (MANUSCRIPT / "manuscript.md").read_text()
    allowed_markers = {
        *(f"FIGURE_{number}" for number in range(1, 6)),
        *(f"TABLE_{number}" for number in range(1, 5)),
    }
    unresolved = {
        token
        for token in re.findall(r"\{\{([A-Z0-9_]+)\}\}", text)
        if token not in allowed_markers
    }
    assert not unresolved
    assert metrics["main_text_words_excluding_references"] <= 8000
    assert metrics["abstract_words"] <= 250
    assert metrics["max_highlight_characters"] <= 85


def test_figures_and_tables_are_cited_in_order() -> None:
    text = (MANUSCRIPT / "manuscript.md").read_text()
    figure_positions = [text.index(f"Figure {number}") for number in range(1, 6)]
    table_positions = [text.index(f"Table {number}") for number in range(1, 5)]
    assert figure_positions == sorted(figure_positions)
    assert table_positions == sorted(table_positions)
    for number in range(1, 6):
        assert text.index(f"Figure {number}") < text.index(f"{{{{FIGURE_{number}}}}}")
    for number in range(1, 5):
        marker = "{{TABLE_" + str(number) + "}}"
        assert text.index(f"Table {number}") < text.index(marker)


def test_references_are_complete_and_sequential() -> None:
    text = (MANUSCRIPT / "manuscript.md").read_text()
    references = text.split("## References", maxsplit=1)[1]
    numbers = [
        int(match)
        for match in re.findall(r"(?m)^(\d+)\. ", references)
    ]
    assert numbers == list(range(1, 21))
    cited = set()
    body = text.split("## References", maxsplit=1)[0]
    for citation in re.findall(r"\[([0-9,–-]+)\]", body):
        for item in citation.split(","):
            if "–" in item or "-" in item:
                low, high = re.split(r"[–-]", item)
                cited.update(range(int(low), int(high) + 1))
            else:
                cited.add(int(item))
    assert cited == set(numbers)


def test_submission_manuscript_keeps_figures_separate() -> None:
    text = (MANUSCRIPT / "manuscript_text.md").read_text()
    assert "{{FIGURE_" not in text
    assert text.count("**Figure ") == 5
    with zipfile.ZipFile(MANUSCRIPT / "manuscript_text.docx") as archive:
        assert not any(name.startswith("word/media/") for name in archive.namelist())


def test_submission_figures_include_vector_pdfs() -> None:
    stems = [
        "figure1_framework",
        "figure2_empirical_hazard",
        "figure3_pseudo_event_success",
        "figure4_simulation_decomposition",
        "figure5_robustness",
    ]
    for stem in stems:
        assert (ROOT / "figures" / f"{stem}.pdf").exists()


def test_submission_archive_contains_editable_and_separate_assets() -> None:
    archive_path = MANUSCRIPT / (
        "pricing_apparent_environmental_performance_submission.zip"
    )
    with zipfile.ZipFile(archive_path) as archive:
        names = set(archive.namelist())
    required = {
        "manuscript/manuscript_text.docx",
        "manuscript/title_page.docx",
        "manuscript/highlights.txt",
        "figures/figures_editable.pptx",
        "tables/main_tables_editable.docx",
        "tables/supplementary_tables_editable.docx",
        "supplement/supplement.docx",
        "AUTHOR_ACTIONS_REQUIRED.md",
    }
    assert required <= names
    stems = [
        "figure1_framework",
        "figure2_empirical_hazard",
        "figure3_pseudo_event_success",
        "figure4_simulation_decomposition",
        "figure5_robustness",
    ]
    assert all(f"figures/{stem}.pdf" in names for stem in stems)
