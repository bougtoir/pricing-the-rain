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
        *(f"FIGURE_{number}" for number in range(1, 9)),
        *(f"TABLE_{number}" for number in range(1, 5)),
        *(f"TABLE_S{number}" for number in range(1, 11)),
    }
    unresolved = {
        token
        for token in re.findall(r"\{\{([A-Z0-9_]+)\}\}", text)
        if token not in allowed_markers
    }
    assert not unresolved
    assert metrics["pages_blinded_pdf"] <= 50
    assert 150 <= metrics["abstract_words"] <= 250
    assert 4 <= metrics["keywords"] <= 6


def test_figures_and_tables_are_cited_in_order() -> None:
    text = (MANUSCRIPT / "manuscript.md").read_text()
    figure_positions = [text.index(f"Figure {number}") for number in range(1, 9)]
    table_positions = [text.index(f"Table {number}") for number in range(1, 5)]
    assert figure_positions == sorted(figure_positions)
    assert table_positions == sorted(table_positions)
    for number in range(1, 9):
        assert text.index(f"Figure {number}") < text.index(f"{{{{FIGURE_{number}}}}}")
    for number in range(1, 5):
        marker = "{{TABLE_" + str(number) + "}}"
        assert text.index(f"Table {number}") < text.index(marker)


def test_references_are_apa_and_complete() -> None:
    text = (MANUSCRIPT / "manuscript.md").read_text()
    references = text.split("## References", maxsplit=1)[1].strip()
    entries = [
        block.strip()
        for block in references.split("\n\n")
        if block.strip()
    ]
    from manuscript.build_manuscript import REFERENCE_ORDER

    assert len(entries) == len(REFERENCE_ORDER)
    # APA: every entry is author-year with a DOI URL, alphabetically ordered.
    surnames = []
    for entry in entries:
        assert re.match(r"^[A-ZÀ-Þ][^\(]*\(\d{4}\)\.", entry), entry
        assert "https://doi.org/" in entry
        surnames.append(entry.split(",", maxsplit=1)[0])
    assert surnames == sorted(surnames, key=str.casefold)
    # No numbered citations remain in the body.
    body = text.split("## References", maxsplit=1)[0]
    assert not re.findall(r"\[[0-9]+\]", body)
    # Every reference surname is cited in the body.
    uncited = [
        surname
        for surname in surnames
        if surname not in body
    ]
    assert not uncited


def test_submission_manuscript_keeps_figures_separate() -> None:
    text = (MANUSCRIPT / "manuscript_text.md").read_text()
    assert "{{FIGURE_" not in text
    assert text.count("**Fig. ") == 8
    with zipfile.ZipFile(MANUSCRIPT / "manuscript_text.docx") as archive:
        assert not any(name.startswith("word/media/") for name in archive.namelist())


def test_submission_figures_include_vector_pdfs() -> None:
    stems = [
        "figure1_framework",
        "figure3_empirical_hazard",
        "figure2_pseudo_event_success",
        "figure7_simulation_decomposition",
        "figure8_robustness",
        "figure4_four_probabilities",
        "figure6_observational_equivalence",
        "figure5_distortion_decomposition",
    ]
    for stem in stems:
        assert (ROOT / "figures" / f"{stem}.pdf").exists()


def test_submission_archive_contains_editable_and_separate_assets() -> None:
    archive_path = MANUSCRIPT / (
        "pricing_rare_events_jru_submission.zip"
    )
    with zipfile.ZipFile(archive_path) as archive:
        names = set(archive.namelist())
    required = {
        "manuscript_blinded.docx",
        "manuscript_text.docx",
        "title_page.docx",
        "cover_letter.docx",
        "figures_editable.pptx",
        "main_tables_editable.docx",
        "supplementary_tables_editable.docx",
        "supplement.docx",
        "AUTHOR_ACTIONS_REQUIRED.md",
        "ECONOMIC_MODELLING_COMPLIANCE_CHECKLIST.md",
        "README.md",
    }
    assert required <= names
    stems = [
        "figure1_framework",
        "figure3_empirical_hazard",
        "figure2_pseudo_event_success",
        "figure7_simulation_decomposition",
        "figure8_robustness",
        "figure4_four_probabilities",
        "figure6_observational_equivalence",
        "figure5_distortion_decomposition",
    ]
    assert all(f"figures/{stem}.pdf" in names for stem in stems)
    assert all(f"figures/{stem}.png" in names for stem in stems)
    for number in range(1, 7):
        assert any(
            name.startswith("tables/") and name.endswith(".csv")
            for name in names
        )
