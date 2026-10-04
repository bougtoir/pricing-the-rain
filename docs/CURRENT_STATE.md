# Current state

- Completed phase: 10
- Scientific release checkpoint:
  `ef8c25a5a96e757aa7787fffb2c3b1d4d635c8e8`
- Reproduction-manifest SHA-256:
  `3bd0665313a4ef89226d522f81ca369e5fe65ffd3ee786278133630c372e9bca`
- Verification: two final full builds and one restricted-source-excluded public-copy
  build produced the same manifest and passed all 20 tests
- Release route: branch `devin/1790232699-pricing-the-rain` synchronizes the
  `pricing-the-rain` subdirectory to `bougtoir/pricing-the-rain`
- Administrative hold: author identity and order, affiliations, correspondence,
  ORCIDs, funding, competing interests, CRediT roles, acknowledgements,
  exclusive-submission confirmation, and optional reviewers remain unresolved
- Next action: review the pull request, complete author placeholders, and submit through
  the journal system
- Resume:
  1. `cd pricing-the-rain`
  2. `PYTHONPATH=. .venv/bin/python run_all.py --validate-only`
  3. inspect `FINAL_REPORT.md`, `docs/FINAL_QC_REPORT.md`, and
     `docs/JOURNAL_COMPLIANCE_CHECKLIST.md`
  4. replace every `[AUTHOR INPUT REQUIRED]` and
     `[AUTHOR CONFIRMATION REQUIRED]` marker
  5. rerun `PYTHONPATH=. .venv/bin/python run_all.py`
