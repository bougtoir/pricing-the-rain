# Price-Decomposition Final Audit

Date: 2026-10-13
Source prompt: `Economic_Modelling_PRICE_DECOMPOSITION_FINAL_REVISION.txt`
Baseline: 51a71594f (`checkpoint-pre-decomp-revision-51a71594f`)
Purpose: audit the interpretation of the relative price-distortion
decomposition before revising text. All simulation and rainfall numbers are
frozen; this audit only re-reads frozen outputs and adds one analytic
derivation.

## 1. Component shares of D_rel under Model D (frozen outputs)

Pointwise split P − αpV = αV(wsubj − p) + γR, so
D_rel = D_rel_prob + D_rel_rep exactly.

### Endogenous observation

| Regime | D_rel_prob | D_rel_rep | Total | Prob share | Rep share |
|---|---|---|---|---|---|
| common | 1.0264 | 0.0958 | 1.1222 | 91.5% | 8.5% |
| moderately rare | 2.0723 | 0.2332 | 2.3054 | 89.9% | 10.1% |
| rare | 4.6661 | 0.7135 | 5.3796 | 86.7% | 13.3% |
| very rare | 9.4542 | 2.0838 | 11.5380 | 81.9% | 18.1% |

### Exogenous observation

| Regime | D_rel_prob | D_rel_rep | Total | Prob share | Rep share |
|---|---|---|---|---|---|
| common | 0.4275 | 0.2026 | 0.6300 | 67.9% | 32.1% |
| moderately rare | 1.3519 | 0.5329 | 1.8849 | 71.7% | 28.3% |
| rare | 3.4964 | 1.6937 | 5.1901 | 67.4% | 32.6% |
| very rare | 7.3910 | 5.0088 | 12.3998 | 59.6% | 40.4% |

**Finding.** The transformed-frequency (probability) component is the
larger component of D_rel in EVERY simulated regime, under both observation
rules. The reputation component's share rises with rarity (endogenous
8.5%→18.1%; exogenous 32.1%→40.4%) but does not overtake the probability
component anywhere on the grid. The previous characterization ("additive
reputation drives the rise; transformed-frequency part stays bounded") is
not supported by the frozen numbers and is corrected.

Absolute terms (frozen): D_EV(Model D) is approximately flat
(0.176 → 0.128 endogenous); D_prob_abs declines with rarity
(0.118 → 0.088 endogenous); D_rep_abs is small and roughly flat
(0.058 → 0.040 endogenous). The relative rise is a denominator-scaling
phenomenon for BOTH components, not growing absolute mispricing.

## 2. Prelec asymptotics (analytic derivation)

Implemented transformation (simulation/general_rare_event.py):
w(p) = exp(−(−ln p)^α), α = 0.65 (one-parameter Prelec, β = 1).

Let L = ln(1/p) → ∞ as p → 0. Then

  w(p)/p = exp(−L^α) / exp(−L) = exp(L − L^α).

For 0 < α < 1, L − L^α = L(1 − L^{α−1}) → ∞ because L^{α−1} → 0.
Therefore

  w(p)/p → ∞   and   (w(p) − p)/p = w(p)/p − 1 → ∞   as p → 0.

**Consequence.** The transformed-frequency relative term is itself
asymptotically unbounded under the assumed Prelec weighting; it is NOT
bounded in any rarity-independent sense. Both components of D_rel are
asymptotically non-scaling:
- transformation term: diverges because w(p)/p diverges (Prelec, α < 1);
- reputation term: diverges provided the reputation stock R does not
  vanish proportionally with p (γR/(αpV) with R bounded below).

Finite-grid evidence must therefore be reported as a comparison of two
divergent components at finite p, not as "bounded vs unbounded." On the
finite grid the probability component is larger in every simulated regime.

## 3. Corrections implied

1. P2c restated: both nonlinear transformation and non-scaling reputation
   make the relative deviation rise as p falls; conditions stated.
2. Abstract, §6.2, §7.1, Conclusion, Table 1, Figure 4 caption, cover
   letter: transformed-frequency component reported as quantitatively
   dominant on the finite grid; reputation's distinct role stated as the
   stock–flow decoupling (history-dependence, premia under weak current
   performance, non-probability price-implied index).
3. "Bounded transformed-frequency part" removed everywhere.
4. Discussion: "four layers stay close under common events" replaced —
   common regime already shows selection ratio ≈ 1.71 and D_rel ≈ 1.12.
5. Equivalence wording: equivalent efficacy shrinks with rarity
   (0.072 → 0.0075); no "bind more tightly"/"stays inflated" claims.
6. "Placebo arm" → "known-zero negative-control benchmark"; residual
   "validation" labels in Table 1 → "known-zero benchmark".
