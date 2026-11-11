# Adversarial review — generalized rare-event pricing manuscript

15 anticipated referee attacks and the current defenses.

1. **"This is just selection bias restated."** The selection mechanism is
   Heckman-type, but the contribution is the layered decomposition plus the
   observational-equivalence bound plus a controlled zero benchmark — none of
   which follows from selection alone. Stated explicitly in §1 and §3.
2. **"Berk–Nash / analogy-based equilibria already cover mislearning."** They
   formalize persistence, not rarity regimes, price-layer separation, or a
   zero-effect validation. Novelty boundary documented in
   GENERALIZATION_NOVELTY_AUDIT.md.
3. **"The simulation only shows what you put in."** True for any structural
   simulation; the validation environment disciplines it because efficacy is
   exactly zero there, so mechanism magnitudes are calibrated to a real
   environmental process rather than chosen freely.
4. **"Rainmaking is not a real market."** It is not claimed to be — it is a
   known-zero benchmark, the analogue of a placebo arm. Claims limited to
   what a zero-efficacy environment produces.
5. **"B_exp is small in absolute terms."** Relative distortion, not absolute,
   is the estimand (P2); D_rel shows the price-layer effect is large where
   absolute probabilities are small. Near-zero denominators are flagged.
6. **"Observational equivalence is obvious."** It is stated as a bound, not a
   surprise: it converts a qualitative suspicion into a quantitative mapping
   (Table 4) that identifies the disclosure requirements in §7.2.
7. **"Prelec alpha = 0.65 is arbitrary."** It is a labeled assumption drawn
   from the standard literature; robustness varies weighting and learners.
   P3 is flagged as the weakest proposition in the final report.
8. **"Learner rules are cherry-picked."** Four distinct rules (naive,
   Bayesian, recency, selective) bound the plausible space; Table S8 reports
   all of them rather than a selected one.
9. **"Price-success differences are positive in the generic model but
   negative in the validation — contradiction."** Not a contradiction: the
   generic model's model-D association is small positive, the validation's is
   negative; both support P5's decoupling claim, which is about the
   stock–flow separation, not a universal sign. Wording in §6.3/§7.1 states
   this precisely (decision D8).
10. **"Provider-rank distortion is negative in the common regime."** Reported
    honestly (Table 2); the claim is that reputation ordering decouples from
    outcome ordering, not that the correlation has a fixed sign.
11. **"Exogenous comparator is contrived."** Its marginal request rate equals
    the endogenous rule's, so it isolates the state-dependence of
    observation rather than the level — the cleanest available contrast.
12. **"Fictional pseudo-events cannot validate anything."** They validate the
    *mechanism magnitudes* under a known zero, which is exactly what a
    validation environment is for; no historical claim is made.
13. **"Cross-domain claims are speculative."** Framed as implications with
    explicit transfer conditions (rare + hidden counterfactual + endogenous
    observation), §7.3; limitations §7.4 bound them.
14. **"Word choice 'priced' implies real WTP."** Claim discipline enforced:
    'the simulation demonstrates', 'the rainfall benchmark demonstrates';
    prohibited phrasings audited. WTP is a calibrated scenario quantity.
15. **"Reproducibility of a two-layer simulation is fragile."** Declared
    seeds (20261012 / frozen rainfall seed), 2,000 replications with MCSE
    convergence tables, manifest hashing of all outputs, and a --validate-only
    pipeline mode; both simulation layers rerun deterministically.
