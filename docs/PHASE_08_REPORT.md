# Phase 8 report: manuscript and submission package

## Outputs

- A fully rendered English manuscript generated from
  `manuscript/manuscript_template.md` and `results/manuscript_values.json`.
- An inline-figure review version in DOCX and PDF.
- A submission-text version in DOCX and PDF with no embedded figures and all five
  legends collected at the end.
- A supplementary appendix in DOCX and PDF with five generated tables.
- A separate title page, highlights file, declarations sheet, and cover-letter draft.
- Twenty references ordered by first appearance and generated from archived Crossref
  records or, for Akong'a (1987), the preserved institutional source.

## Compliance checks

- Main text excluding references: 3,589 words, below the 8,000-word limit.
- Abstract: 214 words, below the 250-word limit.
- Highlights: five; longest is 70 characters, below the 85-character limit.
- Figures: five individually supplied high-resolution files plus an editable PPTX.
- Main tables: four; supplementary tables: five.
- Submission manuscript: 20 pages; inline review manuscript: 22 pages.
- All figures and tables are cited in first-appearance order.
- All 20 references are cited, and no phantom citation or orphan reference remains.
- The submission-text DOCX contains no embedded image media.
- English terminology is consistent across manuscript, captions, figures, and tables.

## Reproducibility

`manuscript/build_manuscript.py` reads the machine-readable result bundle, replaces
all numerical tokens, constructs references from archived metadata, inserts generated
tables, and creates the manuscript and supplement deliverables. Tests enforce journal
limits, ordered figure/table citation, complete reference coverage, and separate-figure
submission packaging.

## Remaining author input

Author names and order, affiliations, corresponding-author details, funding,
competing interests, CRediT contributions, acknowledgements, and confirmation of
exclusive submission remain explicit placeholders. These details are not inferred.
