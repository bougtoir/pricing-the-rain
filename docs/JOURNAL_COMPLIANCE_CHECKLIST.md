# *Ecological Economics* compliance checklist

Live guide and Elsevier generative-AI policy rechecked on
2026-09-25 at 05:37–05:43 UTC:
https://www.sciencedirect.com/journal/ecological-economics/publish/guide-for-authors
https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals

The live guide remains controlling. Current and prior guide extractions and the
AI-policy HTML snapshot are recorded in `data/raw/journal_acquisition_ledger.csv`.

## Article and review route

| Requirement | Status |
|---|---|
| Article category selected | Analysis |
| Analysis maximum 8,000 words or 25 double-spaced pages | Pass: final generated count recorded in `manuscript/manuscript_metrics.json` |
| Single-anonymized review | Pass: submission text and separate title page supplied |
| Originality, quality, analytical accuracy, importance | Addressed in adversarial review; editorial judgment remains |

## Front matter

| Requirement | Status |
|---|---|
| Concise title | Pass |
| Author names and order | **Author input required** |
| Affiliations and correspondence | **Author input required** |
| ORCIDs | **Author input required if applicable** |
| Corresponding-author postal address, email, and telephone | **Author input required** |
| Abstract no more than 250 words | Pass: final generated count recorded in `manuscript/manuscript_metrics.json` |
| English keywords, 1–7 | Pass: 7 |
| Highlights in separate editable file | Pass: `manuscript/highlights.txt` |
| Highlights, 3–5 bullets | Pass: 5 |
| Each highlight no more than 85 characters | Pass: generated file is checked automatically |
| Graphical abstract | Not supplied; encouraged, not mandatory |

## Manuscript and assets

| Requirement | Status |
|---|---|
| Editable manuscript file | Pass: DOCX supplied |
| Separate title page | Pass: DOCX supplied |
| Separate figure files | Pass: five PDF and five high-resolution PNG files |
| Vector line art | Pass: PDF versions supplied for all figures |
| Figure 4 publication dimensions and legibility | Pass: 526.6 × 625.1 pt (7.31 × 8.68 in), 3 × 2 panels, vector PDF and 600-dpi PNG |
| Editable figures | Pass: PPTX supplied |
| Editable tables | Pass: main and supplementary table DOCX files supplied |
| Figure legends | Pass: legends included in submission text |
| Supplementary material | Pass: DOCX and PDF supplied and cited in the manuscript |
| References | Pass: consistent numeric style is permitted under format-free submission; citations and reference metadata are checked for completeness |
| Upload bundle | Pass: ZIP contains editable article, title page, figures, tables, highlights, cover letter, declarations, supplement, and author-action checklist |

## Statements and policies

| Requirement | Status |
|---|---|
| Data availability statement | Pass: names preserved inputs and lawful exclusions |
| Code availability statement | Pass: links to https://github.com/bougtoir/pricing-the-rain |
| Funding declaration | **Author input required** |
| Competing-interest declaration | **Author input required** |
| CRediT authorship | **Author input required** |
| Acknowledgements | **Author input required** |
| Generative-AI declaration | **Draft present; author must confirm the tool, purpose, human review, and responsibility statement before submission** |
| Generative AI in scientific figures | Pass: no generative-AI image tool used; figures are generated from analysis code |
| Ethics statement | Pass: public data and fictional simulations; no participants |
| Originality/exclusive-submission confirmation | **Author confirmation required** |

## Submission-system actions

1. Complete title-page and declaration placeholders, including the corresponding
   author's telephone number and confirmation of the generative-AI statement after
   final author review.
2. Upload `manuscript/manuscript_text.docx` as the editable article file.
3. Upload `manuscript/title_page.docx` separately.
4. Upload each figure PDF separately; retain PNG alternatives if requested.
5. Upload `manuscript/highlights.txt`, editable table files, and supplement.
6. Paste or upload the completed declarations and data statement.
7. Review the automatically generated submission PDF before approval.
