# Final finishing report

## Git state

- Starting Git hash: `8399dfcda03ff432dfa22c4b2f778721b6daf212`
- Ending implementation/package Git hash:
  `56382828be41f78d76bdf0bea95e6e39e56224e5`
- The finishing report itself is added in a documentation-only follow-up commit; the
  hash above is the exact end of the manuscript, package, code, and generated-output
  changes.

## Analysis freeze

The scientific analysis remained frozen. No raw or processed scientific data,
pseudo-event definition, hazard estimate, M0–M5 specification, random seed, Monte
Carlo output, robustness result, falsification result, coefficient, interval,
p-value, or calibrated parameter was rerun or changed.

SHA-256 manifests covering the scientific analytical inputs and outputs were generated
before and after the finishing build and were identical. The finishing build consumed
the committed frozen CSV, CSV.GZ, JSON, and configuration outputs. No numerical
inconsistency was found.

## Exact textual changes

1. Table 4 and its machine-readable source now classify strategic provider selection
   as `demonstrated in model using observed weather`, with the unchanged basis
   `M3 versus M2 and selection-slope sensitivity`.
2. The Discussion now states:
   “In the model, a provider who selectively accepts high-hazard requests can monetize
   information about nature without producing rainfall.”
3. The manuscript and supplement explicitly distinguish observed-weather natural
   rainfall evidence from model-contingent strategic selection.
4. The data/code statement now names
   `https://github.com/bougtoir/pricing-the-rain`, identifies the public reproducibility
   assets, and distinguishes legally redistributable inputs from restricted sources
   represented by provenance ledgers.
5. The generative-AI declaration now follows the current Elsevier disclosure structure
   while retaining an explicit author-confirmation gate for final human review,
   editing, and responsibility.
6. The title page and author-action list now include the corresponding author's
   telephone number and enumerate all remaining submission-system actions.

## Figure 4 presentation changes

Only presentation was changed. The figure now uses a 3 × 2 panel arrangement at
7.31 × 8.68 inches, explicit type sizes, improved panel spacing, compact legends,
clearer line and marker sizes, a vector PDF, and a 600-dpi PNG. The six panels,
underlying values, analytical definitions, and stock–flow interpretation are
unchanged. The final figure was inspected at publication scale and at 100% viewing.

## Journal-compliance recheck

The live *Ecological Economics* Guide for Authors and Elsevier generative-AI policy
were rechecked on 2026-09-25. The final package satisfies the Analysis article limit,
abstract and keyword limits, highlights rules, single-anonymized route, editable file
requirements, figure/table and supplement requirements, data/code statement, and AI
disclosure requirements, subject to the author-only gates below.

The journal permits a consistent reference format at initial submission. The existing
numeric citation system was therefore retained rather than changed solely for style;
all 20 citations and references are complete and internally consistent.

## Public repository status

The finishing implementation/package commit was pushed to PR
`https://github.com/bougtoir/wip/pull/517`. GitHub Actions synchronized the public
repository to:

`https://github.com/bougtoir/pricing-the-rain/commit/2fa09adc19cf8a812a556a7799c71bc9c718b0bb`

The public manuscript source, generated inline manuscript, submission ZIP,
classification table, Figure 4, and provenance ledger were compared by Git blob hash
with the WIP finishing commit and matched. Restricted journal and literature snapshots
remain excluded; their public ledgers retain provenance and status information.

## Clean build and QC

The following build-only commands were run in a clean linked worktree at the ending
implementation/package commit:

```bash
PYTHONPATH=. /home/ubuntu/repos/wip/pricing-the-rain/.venv/bin/python analysis/build_manuscript_assets.py
PYTHONPATH=. /home/ubuntu/repos/wip/pricing-the-rain/.venv/bin/python manuscript/build_manuscript.py
PYTHONPATH=. /home/ubuntu/repos/wip/pricing-the-rain/.venv/bin/python analysis/final_audit.py
PYTHONPATH=. /home/ubuntu/repos/wip/pricing-the-rain/.venv/bin/python -c 'import run_all; run_all.validate_raw_inputs(); run_all.validate_outputs(); run_all.write_manifest()'
PYTHONPATH=. /home/ubuntu/repos/wip/pricing-the-rain/.venv/bin/python -m pytest tests -q
unzip -t manuscript/pricing_apparent_environmental_performance_submission.zip
```

Result:

- Final audit passed.
- 52 archived raw-input records validated.
- 21 tests passed.
- Submission ZIP integrity passed.
- Machine-readable manuscript values and final-audit output reproduced byte-for-byte.
- DOCX document XML reproduced byte-for-byte; container hashes differ only because
  office files carry regenerated package metadata.
- No internal path, task prompt, TODO, debug string, or author identity was found in
  the submission manuscript files.
- The final ZIP contains exactly the intended 26 files.

## Final manuscript metrics

- Main text excluding references: 3,979 words.
- Abstract: 188 words.
- References: 20.
- Figures: 5.
- Main tables: 4.
- Supplementary tables: 6.
- Highlights: 5; maximum length 67 characters.

## Unresolved author-only actions

1. Confirm author names, order, affiliations, correspondence address, email, telephone
   number, and ORCIDs where applicable.
2. Provide acknowledgements or confirm that none are required.
3. Provide funding sources and grant numbers or confirm no specific funding.
4. Provide the competing-interests declaration.
5. Assign CRediT roles to every author.
6. Confirm originality and exclusive submission.
7. Confirm every author's approval of the final manuscript and submission.
8. Confirm final human review, editing, and responsibility for AI-assisted content.
9. Select the journal article type and confirm data/code responses in the submission
   system.
10. Review the cover letter, select suggested or opposed reviewers if desired, and
    approve the journal-generated submission PDF.

## Exact final filenames

- Inline manuscript DOCX: `manuscript/manuscript_blinded.docx`
- Submission package ZIP:
  `manuscript/pricing_apparent_environmental_performance_submission.zip`
- Finishing report: `FINAL_FINISHING_REPORT.md`
