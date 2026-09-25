# Reproducibility guide

## Scope

The default pipeline rebuilds all derived results from preserved raw snapshots. It does
not call weather, Crossref, publisher, or repository APIs. Acquisition is a separate,
optional command.

## Full command

```bash
make reproduce
```

The ordered stages are:

1. Validate all archived raw files against machine-readable byte counts and SHA-256
   checksums.
2. Rebuild the zero-effect framework diagram.
3. Recompute weather features, prospective hazards, fictional pseudo-events, apparent
   success, and descriptive scenario-WTP models.
4. Run 10,000 replications for each of M0–M5.
5. Run clustered inference, 1,000 permutations, threshold/window sensitivity,
   convergence analysis, and 18,000 parameter-sensitivity replications.
6. Recreate hypothesis classifications, figures, tables, editable assets, and
   `results/manuscript_values.json`.
7. Render manuscript, supplement, title page, highlights, declarations, and cover
   letter.
8. Write SHA-256 hashes for machine-readable outputs to
   `results/reproduction_manifest.json`.
9. Run the full test suite.

## Expected runtime and resources

The full run is CPU-bound during Monte Carlo simulation. It was validated on Python
3.10 with two logical CPU cores and 7.8 GiB RAM. LibreOffice is required only for PDF
rendering. Exact Python package versions are pinned in `requirements.txt`.

## Determinism

Principal and sensitivity simulations use fixed seeds in `config/simulation.yml` and
`analysis/robustness.py`. Fictional placebo and random-drought selections also use a
fixed seed. Machine-readable numerical outputs are deterministic for the pinned
environment. DOCX/PPTX/PDF containers may have different internal timestamps across
runs; manuscript numbers are sourced from deterministic JSON/CSV outputs rather than
from those containers.

## Raw-input preservation

Raw files are immutable inputs. Acquisition scripts skip existing snapshots, validate
content, and record source URL, retrieval information, size, SHA-256, usage, and status.
Invalid all-null ERA5-Land responses are preserved separately and excluded from
analysis. The Akong'a repository landing response and verified institutional PDF are
both retained.

## Verification commands

```bash
make validate
make test
PYTHONPATH=. .venv/bin/python -m compileall -q src simulation analysis manuscript tests
git diff --check
```

The manuscript tests enforce the abstract, main-text, and highlight limits; ordered
figure/table citations; complete citation/reference correspondence; and the absence of
embedded figures from the submission-text DOCX.
