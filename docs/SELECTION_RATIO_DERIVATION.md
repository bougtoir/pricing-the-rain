# Analytic selection-ratio derivation (generalized, Issue 6 + hostile review)

## General result

Let the risk state be a random variable X with multiplier m(X) > 0 and
objective probability p(X) = p0·m(X) where valid. Let the observation
weight s(X) ≥ 0 — the probability that a case in state X enters the
observed record — be independent of the baseline rarity scale p0.

Then:

  Population risk:        E[p]   = p0·E[m(X)]
  Selected-support risk:  p_ref  = p0·E[m(X)s(X)] / E[s(X)]

  Selection ratio:

  R = p_ref / E[p]
    = E[m s] / (E[m]·E[s])
    = 1 + Cov(m, s) / (E[m]·E[s])

Consequences:

- R is independent of baseline rarity p0 under multiplicative scaling.
- The absolute gap p_ref − E[p] = p0·E[m]·(R−1) is proportional to p0.
- Positive Cov(m,s) ⇒ experienced-frequency INFLATION (R > 1).
- Zero covariance ⇒ no composition shift (R = 1).
- Negative Cov(m,s) ⇒ DEFLATION (R < 1): risk-correlated selection does
  not necessarily inflate apparent success.
- The invariance fails if s responds to the absolute level p(X) rather
  than the state or relative hazard, since s is then not independent of
  p0.

## Two-state special case (the simulated calibration)

Two-state latent hazard S_t ∈ {L, H} with stationary prevalence π = P(S=H).
Multiplicative risk: p_t = b·m(S_t), m_L < m_H, so E[p_t] = b·μ with
μ = π·m_H + (1−π)·m_L.

Endogenous observation O_t = D_t ∧ A_t where

- demand depends only on the state: q_D(S) = expit(β_0 + β_1·1[S=H]);
- acceptance depends only on the RELATIVE hazard: providers observe
  p_t/b − 1 = m(S_t) − 1 plus a provider-specific selectivity term s_j, so
  q_A(S) = E_j[expit(α_0 + α_1·(m(S)−1) + s_j)].

Define q_S = q_D(S)·q_A(S) = P(O=1 | S).

## Derivation

E[p_t | O=1] = b·[π·m_H·q_H + (1−π)·m_L·q_L] / [π·q_H + (1−π)·q_L]

Selection ratio:

  R = E[p_t | O=1] / E[p_t]
    = [π·m_H·q_H + (1−π)·m_L·q_L] / [μ·(π·q_H + (1−π)·q_L)]

The baseline b cancels EXACTLY. R is independent of baseline rarity whenever
(i) risk is multiplicative in the state, p_t = b·m(S_t), and (ii) demand and
acceptance respond to the state or to the relative hazard p_t/b rather than
to p_t itself. The absolute selection gap E[p|O=1] − E[p] = b·μ·(R−1) is
therefore proportional to b and shrinks linearly with rarity.

## Parameter values in the generic simulation

π=0.30, m_L=0.6, m_H=2.0 → μ = 1.02.
β_0=−1.9, β_1=2.4 → q_D(L)=expit(−1.9)=0.1301, q_D(H)=expit(0.5)=0.6225.
α_0=1.4, α_1=4.0, s_j ∈ {−0.7,…,0.7} (6 providers) →
q_A(L)=mean_j expit(−0.2+s_j)=0.4528, q_A(H)=mean_j expit(5.4+s_j)=0.9950.

R = (0.3·2.0·0.6196 + 0.7·0.6·0.0589) / (1.02·(0.3·0.6196 + 0.7·0.0589))
  = 1.7115.

Simulated means: 1.713 / 1.711 / 1.710 / 1.708 across the four regimes;
analytic gaps b·μ·(R−1) = 0.218 / 0.073 / 0.022 / 0.007 vs simulated
0.216 / 0.072 / 0.022 / 0.007. Residuals are Monte Carlo error.

1.71 is therefore a PARAMETER-SPECIFIC value of the general ratio, not a
universal constant: it changes with π, m, the demand slope, and the
acceptance slope. If acceptance depended on the absolute level p_t rather
than p_t/b, b would not cancel and the ratio would vary with rarity.
