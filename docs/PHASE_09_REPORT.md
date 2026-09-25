# Phase 9 report: one-command reproducibility

## Outputs

- Root-level project overview and interpretation boundaries in `README.md`.
- A `Makefile` with setup, full reproduction, validation, test, manuscript, and
  optional acquisition targets.
- An offline-by-default `run_all.py` orchestration script.
- A detailed stage and determinism guide in `docs/REPRODUCIBILITY.md`.
- A machine-readable journal-guide acquisition ledger.
- A generated hypothesis-classification stage rather than a manually retained CSV.
- Deterministic gzip metadata for processed weather and simulation-replication files.
- `results/reproduction_manifest.json`, containing the pinned execution environment
  and SHA-256 values for 33 processed and machine-readable outputs.

## Full-build verification

`PYTHONPATH=. .venv/bin/python run_all.py` completed from the archived raw inputs and:

- validated 46 raw-input ledger records;
- analyzed 87,664 region-days and 2,595 fictional pseudo-events;
- ran 60,000 principal simulations and 18,000 parameter-sensitivity simulations;
- regenerated robustness results, figures, tables, editable assets, manuscript,
  supplement, title page, highlights, declarations, and cover letter;
- retained a 3,589-word main text and 186-word abstract;
- passed all 20 automated tests.

The end-to-end build took approximately 84 seconds on the recorded two-core VM.
Two consecutive full builds produced the identical reproduction-manifest SHA-256:

```text
3bd0665313a4ef89226d522f81ca369e5fe65ffd3ee786278133630c372e9bca
```

This verifies deterministic processed and machine-readable results under the pinned
environment. Office and PDF containers are regenerated successfully but are not
byte-stability targets because their internal creation timestamps can vary.

The committed Phase 9 checkpoint was also checked out into a clean detached worktree
and rebuilt with the same command. The final Phase 10 code was subsequently rebuilt
twice in the persistent project VM with the same 33-output manifest hash and all 20
tests passing. Office and PDF containers remain outside byte-stability targets.

## Raw-data safety

The default pipeline contains no acquisition step. Acquisition remains an explicit
networked target and only fetches absent files. The weather acquisition interface no
longer exposes an overwrite switch, and existing retrieval timestamps are preserved
when ledgers are refreshed. Invalid all-null ERA5-Land responses remain archived and
excluded.

## Checks

```text
20 passed
compileall passed
git diff --check passed
```

The next phase is adversarial reviewer-oriented QC, current journal-guide rechecking,
final release packaging, and pull-request creation.
