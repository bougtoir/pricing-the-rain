# Final quality-control report

## Verdict

The scientific and computational package passes final QC for public release and
editorial submission preparation. It is **not administratively submission-ready**
until the author-specific placeholders listed below are resolved.

## Scientific QC

| Domain | Verdict | Evidence and residual limitation |
|---|---|---|
| Scope | Pass | Claims are limited to a zero-effect mechanism stress test; no actual ritual effect is estimated. |
| Novelty | Pass with narrowing | Closest QJE work is treated as prior art for endogenous timing. Novelty is the integrated selection–valuation–reputation system. |
| Valuation substance | Pass | WTP, price, causal rainfall value, social utility, expenditure, revenue, profit, and surplus are separated. Monetary quantities remain calibrated scenarios. |
| Causal language | Pass | “Apparent success” is defined as future rain; intervention status never changes rainfall. Regression results are exploratory associations. |
| Robustness | Pass with boundary result | Thresholds, windows, selection slopes, priors, memory weights, permutation falsification, and convergence are reported. Positive price–success is not supported. |
| Generalizability | Pass with limitation | Eight locations are climate stress tests, not communities or a global sample. |
| Statistical assumptions | Pass with disclosure | Logit and linear-probability checks are descriptive; clustered inference and simulation assumptions are explicit. |
| Dependence | Pass with limitation | Two-way clustering addresses region-year and region-rule dependence; overlapping windows remain disclosed. |
| Multiplicity | Pass with limitation | No correction is claimed; p-values are exploratory and not the sole classification rule. |
| Leakage | Pass | Drought and dry-spell states are lagged, event-day rain is unavailable, success begins on the next day, hazards use 1991–2010 only, and follow-up is complete. |
| Missingness | Pass | Raw analytical ERA5 precipitation is complete; invalid all-null ERA5-Land snapshots are excluded and retained. Sparse hazard cells use training-only location-month fallback. Undefined no-event simulation quantities remain missing rather than zero-filled. |
| Convergence | Pass | Principal models use 10,000 replications each; convergence tables report Monte Carlo standard errors at increasing sample sizes. |
| Citation correctness | Pass | Twenty references are generated in first-appearance order; DOI-role mismatches and the Akong'a title discrepancy are documented. |
| Historical evidence | Pass | Historical claims are separated from theoretical provider, observer, and price mechanisms. |
| Cultural framing | Pass with care | Plural and relational value are not collapsed into WTP; no historical belief is inferred from simulation. |

## Numerical consistency

- 87,664 region-days and 2,595 fictional pseudo-events.
- Principal simulation: 60,000 replications, 10,000 for each M0–M5 model.
- Sensitivity simulation: 18,000 replications.
- Regression dataset: 2,595 complete pseudo-events.
- Naive price coefficient: 0.1237; 95% model-based interval 0.0855–0.1619.
- Adjusted price coefficient: 0.0360; two-way clustered interval −0.0388–0.1109.
- Within-stratum permutation coefficient: −0.0319; two-sided \(p=0.0020\).
- Manuscript: 3,589 words excluding references; abstract 186 words.
- Package: 5 figures, 4 main tables, 5 supplementary tables, 20 references.
- Highlights: 5; longest 70 characters.

All manuscript values are rendered from `results/manuscript_values.json`; no manual
numerical transcription is required.

## Computational QC

The full offline pipeline was run twice consecutively after the final statistical
repair. Both runs:

- validated 46 archived raw-input records;
- produced the same 33-output reproduction manifest;
- passed all 20 automated tests.

An exact public-sync copy with the five restricted audit paths removed was then rebuilt
end to end. It validated 43 redistributable raw-input records, produced the same
33-output manifest hash, and passed all 20 tests.

Stable manifest SHA-256:

```text
3bd0665313a4ef89226d522f81ca369e5fe65ffd3ee786278133630c372e9bca
```

Required verification commands:

```bash
PYTHONPATH=. .venv/bin/python run_all.py
PYTHONPATH=. .venv/bin/python -m compileall -q run_all.py src simulation analysis manuscript tests
git diff --check
PYTHONPATH=. .venv/bin/python -m pytest tests -q
```

## Public-release QC

- No credential-like file or hard-coded secret was detected.
- No tracked project file exceeds common GitHub single-file limits; the largest
  release artifact is the compressed principal simulation output.
- Archived weather and Crossref metadata are eligible for synchronization under their
  source terms and are not relicensed by the project.
- The institutional article, repository landing snapshot, captured publisher guide,
  and their restricted audit ledgers are excluded from public synchronization because
  redistribution permission is unclear.
- Source URLs, acquisition methods, sizes, and checksums remain documented.
- No raw snapshot is deleted or overwritten.

## Administrative blockers

The following require author decisions and must not be inferred:

1. author names and order;
2. affiliations, corresponding author, postal address, email, and ORCIDs;
3. funding statement;
4. competing-interest statement;
5. CRediT roles;
6. acknowledgements;
7. confirmation of originality and exclusive consideration;
8. optional suggested reviewers.
