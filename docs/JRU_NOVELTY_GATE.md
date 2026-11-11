# JRU novelty gate

Inputs: `docs/JRU_CLOSEST_PRIOR_STUDIES_MATRIX.md` (14 rows, 19 studies).
Rule: no contribution is called novel unless that audit supports it.

| # | Contribution as stated in the manuscript | Classification | Supporting / limiting prior work | Allowed wording |
|---|---|---|---|---|
| C1 | Selection ratio \(E[ms]/(E[m]E[s]) = 1+\operatorname{Cov}(m,s)/(E[m]E[s])\) and its sign rule (Lemma 1) | **Established** (algebraic identity); **Known application** to experienced risk | Heckman (1979); Denrell & March (2001); Fiedler (2000) | "a standard selection identity, applied to observation of a rare binary event" — never "we show for the first time" |
| C2 | Ratio invariant to baseline rarity under multiplicative scaling; absolute gap shrinks with \(p\) (Corollary) | **New comparative static** (minor, one-line corollary of C1) | Not stated in rows 1–10 for rare-event observation | "a simple corollary that separates relative from absolute distortion" |
| C3 | Divergence of the transformed relative term under Prelec weighting (Lemma 2) | **Known application** (property of the Prelec function) | Prelec (1998); Gonzalez & Wu (1999) | "a known property of the Prelec function, stated for completeness" |
| C4 | Four-layer separation objective → experienced → subjective → price-implied, with objective-relative gaps \(B\) and adjacent-layer increments \(\Delta\) | **New decomposition** (organising framework; components individually established) | Rows 1–11 cover the layers separately; none combines them in one quote | "an accounting decomposition"; not a structural or identified model |
| C5 | Reputation stock decouples from current hazard and inflates quotes relative to price-implied success (simulation, t−1 information) | **New simulation result** (modest size after the look-ahead correction) | Dranove et al. (2003); Denrell (2005) cover selection-shaped reputation, not rare-event quotes | "in the simulation"; report the corrected magnitudes; no welfare claim |
| C6 | First-moment observational equivalence between selection and positive efficacy | **New simulation result** (first moment only) | Identification under selection is established (Heckman, 1979); the specific equivalence map is not in rows 1–14 | "first-moment equivalence"; must not claim non-identification in general |
| C7 | Known-zero-efficacy weather benchmark (ERA5) with hazard-timed pseudo-events | **New benchmark** | Espín-Sánchez et al. (2026) use rain prayer historically; they do not build a zero-efficacy pseudo-event test of a quote decomposition | "a benchmark in which causal efficacy is zero by construction"; WTP/quotes are model overlays |
| C8 | Endogenous observation biases experienced frequency (qualitative statement) | **Not novel** | Rows 1–4, 7, 9, 10 | Cite as background only |

## Verdict: **ADEQUATE INCREMENTAL NOVELTY**

The analytical results (C1, C3) are established or known applications and
must be presented that way. C2 is a minor new comparative static. The JRU
contribution rests on C4 (a decomposition), C5–C6 (simulation results under
a reduced-form quote rule, not an equilibrium), and C7 (a zero-efficacy
benchmark). These are incremental, not a new theory. The verdict is
conditional on the manuscript (title, abstract, introduction, contribution
list) using the "Allowed wording" column and citing rows 1–4, 8, 10 and 11
where C1, C3 and C8 appear. Any stronger novelty claim fails this gate.
