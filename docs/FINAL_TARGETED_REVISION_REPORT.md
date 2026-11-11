> SUPERSEDED — retained only for provenance. Current final reports: FINAL_DECOMPOSITION_REVISION_REPORT.md, PRICE_DECOMPOSITION_FINAL_AUDIT.md, FINAL_SUBMISSION_PASS_REPORT.md.

# Final targeted-revision report — rare-event pricing (Economic Modelling)

Scope: generic rare-event simulation and its interpretation only. Rainfall /
rainmaking validation is frozen; no rainfall quantity was recomputed or
changed. Safety checkpoint: `checkpoint-pre-targeted-revision-29781ff64`.
Companion docs: GENERIC_PROBABILITY_ESTIMAND_AUDIT.md,
EXOGENOUS_BENCHMARK_AUDIT.md, RARE_EVENT_TARGETED_REVISION_LOG.md.

## 1. The inconsistency that triggered the revision

The manuscript stated that experienced-frequency bias "grows monotonically
with rarity," while the reported absolute gap under endogenous observation
decreased (0.216 → 0.072 → 0.021 → 0.007) across common → very-rare regimes.
The statement conflated two different estimands.

## 2. Estimand audit (Phase 1)

`p_objective` was a time-weighted marginal E[p_t]; `p_experienced` an
observation-weighted conditional E[Y|O=1]. Their difference is a composition
(selection) gap, not a record bias. Resolved by the decomposition

    p_exp − p_bar = (p_ref − p_bar) + (p_exp − p_ref)
                  = selection_gap   +  B_abs

with p_ref = E[p_t | O=1]. "Bias" is now used only for same-support
comparisons (B_abs, B_rel); the composition difference is called the
selection gap / selection ratio. Full table of every probability-like
quantity: docs/GENERIC_PROBABILITY_ESTIMAND_AUDIT.md.

## 3. Exogenous-benchmark audit (Phase 2)

The previous exogenous rule made demand state-independent but left
acceptance state-dependent (relative-hazard slope), so the "exogenous"
support was still selected — this is why p_experienced exceeded p_objective
under exogenous observation. Fixed: under exogenous, acceptance is constant,
so O ⊥ p_t. Endogenous rule untouched. Unit tests
(tests/test_generic_estimands.py) verify: exogenous unbiasedness for
homogeneous and heterogeneous p; positive gap under increasing-state
selection; negative gap under decreasing-state selection.

## 4. Corrected metrics (Phase 3)

New columns in results/general_summary.csv and Table 2/S8:
p_ref_observed, selection_gap, selection_ratio, B_abs, B_rel (matched record
bias), and the exact model-D split D_EV = D_prob_abs + D_rep_abs,
D_rel = D_rel_prob + D_rel_rep. Near-zero denominators guarded by ε floors.

## 5. Rarity mechanism audit (Phase 4) — headline finding

| Regime | sel. gap (endo) | sel. ratio (endo) | sel. ratio (exo) | B_abs (endo) |
|---|---|---|---|---|
| common | 0.216 | 1.713 | 0.999 | ≈ 0.000 |
| moderately_rare | 0.072 | 1.711 | 1.000 | ≈ −0.000 |
| rare | 0.022 | 1.710 | 1.000 | ≈ −0.001 |
| very_rare | 0.007 | 1.708 | 1.000 | ≈ −0.000 |

- The selection gap is ≈ 0.72 × p_obj: it shrinks with rarity at the same
  rate as p itself — a composition effect scaled by p, not a rarity
  mechanism.
- The selection ratio is stable at ≈ 1.71 across all regimes.
- B_abs ≈ 0 everywhere: the record is unbiased on its own support.
- Exogenous is now a clean benchmark: gap ≈ 0, ratio ≈ 1.

**Verdict: the rarity-amplification-of-frequency-bias hypothesis fails.** It
was driven by scaling of the composition effect with p. Reported as a
negative result in §6.1 and Table 1 (P2b), not buried.

## 6. Price-distortion decomposition (Phase 5)

Model D: P = α·ŵ·V + γ·R ⇒ (P−αpV)/(αpV) = (ŵ−p)/p + γR/(αpV) exactly.
Measured split (endogenous, D_rel): common 1.03 + 0.10 = 1.12; very_rare
9.45 + 2.08 = 11.54. The additive reputation part grows from 0.10 to 5.01
because the reputation stock does not scale with objective EV; the same rise
appears under exogenous observation (0.20 → 5.01), confirming the mechanism
is the denominator/additive structure, not frequency bias. Absolute
distortion D_EV stays ≈ 0.13–0.19 across regimes. No asymptotic-divergence
claim beyond the finite regimes simulated.

## 7. Proposition revisions (Phase 6)

Original P2 ("rarity amplifies the gap") → failed, disclosed. Replaced by:
- P2a: selection inflates experienced frequency proportionally (ratio ≈ 1.7
  stable) — supported.
- P2b: record near-unbiased on observed support — supported; the original
  claim reported as failed.
- P2c: rarity amplifies relative price distortion via non-scaling additive
  components — supported, with the analytic identity in §3.
Table 1 now lists seven propositions.

## 8. Observational-equivalence retest (Phase 7)

Explicit inverse solution (linear inverse interpolation on the exogenous
efficacy grid) with ±1-MCSE bounds, machine-readable at
results/general_equivalent_efficacy.csv: moderately_rare δ* = 0.072
[0.0719, 0.0725]; rare δ* = 0.022 [0.0216, 0.0219]; very_rare δ* = 0.0075
[0.0074, 0.0076]. In the common regime no efficacy in the scanned grid (up
to 0.10) reproduces the endogenous apparent success — disclosed in §6.4.
The equivalent apparent efficacy shrinks with rarity proportionally to the
selection gap.

## 9. Figure changes (Phases 8–9)

- Figure 4 (figure6_four_probabilities): panel A adds the matched p_ref
  series; panel B now shows absolute selection gap + selection ratio
  (dual axis).
- Figure 5 (NEW, figure8_distortion_decomposition): panel A absolute gap vs
  selection ratio; panel B exact D_rel split (transformed-frequency part +
  additive reputation part), endogenous vs exogenous.
- Figure 6: observational-equivalence map (renumbered).
- Figures 7–8: rainfall validation figures (renumbered, unchanged content).

## 10. Text changes (Phase 10)

Abstract, introduction contributions, §3 propositions, §4 methods (exogenous
rule described correctly), §5 metrics paragraph (matched-estimand
definitions), §6.1 rewritten as composition-vs-record result with the
failure disclosed, §6.2 rewritten with the decomposition, §6.4 per-regime
equivalent efficacy + unsolved common case, conclusion, highlights, cover
letter, Table 1/2/S8, and figure captions all updated. No surviving claim
asserts any quantity "increases with rarity" whose numbers decrease.

## 11. Journal fit (Phase 11)

Economic Modelling retained as provisional primary target: the revision
strengthens model-first positioning (analytic decomposition, matched
estimands, propositions) and does not change the citation neighborhood.
Journal of Risk and Uncertainty remains the backup.

## 12. QC rerun (Phase 12)

Only the generic pipeline was rerun: simulation/general_rare_event.py (same
seed 20261012; seeds derive from a single SeedSequence), downstream
build_manuscript_assets.py, build_manuscript.py. Rainfall module untouched.
Verification: 25/25 tests pass (incl. new estimand unit tests);
final_audit.py passes; manuscript 4,589 words; abstract 245 words; all
revised values come from code (manuscript_values.json).

## 13. Negative-result discipline (Phase 13)

The failed rarity-amplification hypothesis is stated explicitly in §6.1
("the earlier formulation … is therefore corrected"), in Table 1 (P2b
classified "Failed (reported as a negative result)"), in the decision log,
and in this report. It is not moved to the supplement.

## 14. Adversarial review answers (Phase 14)

1. *Are p_obj and p_exp the same estimand?* No — time-weighted vs
   observation-weighted; decomposed (Section 2 above).
2. *Is the exogenous benchmark truly exogenous?* It was not (acceptance
   remained state-dependent); fixed and unit-tested.
3. *Is the inflation record bias or composition?* Composition; B_abs ≈ 0 in
   every regime, both rules.
4. *Which rarity effect is genuine?* Only the selection ratio's stability
   and the D_rel decomposition are genuine structure; the absolute gap's
   shrink is p-scaling of a composition effect.
5. *Does the D_rel rise need selection?* No — it appears under exogenous too
   (denominator + additive reputation); stated in §6.2.
6. *Is the equivalent efficacy eyeballed?* No — explicit inverse
   interpolation with MCSE bounds, saved to a machine-readable CSV.
7. *Any remaining "increases with rarity" claims on decreasing numbers?*
   None — grep-audited; the only increasing claims are D_rel and its
   reputation part, whose numbers increase.
8. *Near-zero denominators?* ε floors on all ratios; D_rel flagged where
   the denominator approaches zero; B_rel uses p_ref > ε.
9. *Could exogenous D_rel_prob rising mean residual selection?* Checked:
   exo selection ratio = 1.000; the prob-part rise is the learner/Prelec
   transformation's own relative distortion, reported as such.
10. *Were metrics chosen post hoc?* The decomposition identity was derived
    analytically before rerunning; the metric change is disclosed in the
    revision log and manuscript (P2b/§6.1), satisfying the "explicit
    disclosure" condition.
11. *Monte Carlo adequacy?* 2,000 replications/cell; convergence scan at
    250–2,000 in Table S7; equivalent-efficacy bounds propagate MCSE.
12. *Is the abstract honest now?* Yes — it states the stable selection
    ratio, the shrinking absolute gap, the failed hypothesis, and the
    denominator-driven D_rel rise.

## Deliverables regenerated

manuscript (blinded + text + title page + cover letter + declarations +
highlights), supplement, figures (8, PDF+PNG), tables (6 + S1–S8),
figures_editable.pptx, submission zip
(pricing_rare_events_economic_modelling_submission.zip),
results/general_equivalent_efficacy.csv, tests, audit docs, revision log.
Final checkpoint commit follows this report.
