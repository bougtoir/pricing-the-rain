# JEBO Data–Text–Figure consistency audit

Date: 2026-10-20. HARD GATE. Method: all manuscript numbers are
`{{TOKEN}}` placeholders resolved at build from
`results/manuscript_values.json`; tables are rendered from the same
registry-derived CSVs; figures are generated from the same canonical
results by `analysis/build_manuscript_assets.py`. There is no manual copy
path between canonical outputs and any manuscript-facing artifact.

## Checks performed

- [x] No stale QREF/Economic-Modelling-era artifacts: the archive is
      regenerated wholesale by `build_manuscript.py`; tables/figures are
      rewritten each build from canonical CSVs/PNGs; the old
      `pricing_rare_events_qref_submission.zip` is replaced by
      `pricing_rare_events_jebo_submission.zip` (old name removed).
- [x] Table cells: generated from `tables/*.csv` which are written by
      `analysis/build_manuscript_assets.py` from `results/` canonical
      files — single source.
- [x] Figure-internal numbers: annotations are drawn from the same
      result frames; verified for the five main figures in prior
      numeric-audit pass (printed values = registry values).
- [x] Caption vs plotted values: captions are authored text without
      embedded result literals; in-text numbers citing figures resolve
      from the same registry.
- [x] Rounding: one display precision per quantity via `f()` and token
      formatting; text/table rounding consistent.
- [x] Signs/directions: prose sign statements (selection gap positive
      under calibrated positive covariance; price–success differences
      negative in benchmark) match the signed values in the registry
      (negative price-success diffs retained and disclosed).
- [x] Denominators/sample sizes: 87,664 region-days / 2,595 pseudo-events
      / 2,000 reps per cell identical across abstract, §4–6, tables,
      supplement.
- [x] JEBO-delta prose: the two new text edits contain no numeric
      results; the cover letter's only number ({location_count} region-days)
      is injected from the registry.
- [x] Reference list ↔ in-text citations: every REFERENCE_ORDER entry
      requires its cite token in the rendered text (build enforces);
      author–year order preserved by `apa_sort_key`.

## Result

**PASS** — zero unresolved manuscript-facing inconsistencies.
Visual inspection of the built DOCX/PDF (Phase 17) confirmed: no
clipping, legible numbers, correct panel labels, captions and in-text
citation order correct, supplementary numbering S1–S10 / S1–S3 correct,
no QREF remnants in submission-facing files.
