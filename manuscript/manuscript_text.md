# Selected Experience and Rare-Event Risk: Endogenous Observation, Subjective Transformation, and Reputation under Hidden Counterfactuals

## Abstract

Risky decisions about rare events—insurance against uncommon losses,
credit for rare defaults, low-frequency professional services—often rest on
histories that are selectively generated: an outcome enters the record only
when someone participated and observed it. This paper studies how such
endogenous observation changes experienced risk, how subjective probability
transformation and reputation act on that selected experience, and what can
and cannot be inferred about underlying efficacy when counterfactuals are
hidden. It separates four objects: the objective probability, the
experienced frequency on the selected record, a transformed subjective
probability, and a price-implied index from a reduced-form quote rule. A
standard selection identity gives the ratio of experienced to objective
risk as one plus a scaled covariance between state risk and observation; in
the calibrated simulation the ratio is approximately
1.71 and does not depend on baseline rarity, while the
absolute gap shrinks with rarity. Rarity instead changes the composition of
the quote: the relative distortion of the reputation-augmented quote rises
from 1.12 to 11.61 as objective expected
value falls, through probability weighting and an additive reputation stock
that is decoupled from current hazard. In simulated rare regimes,
zero-efficacy selection matches the mean apparent performance of positive
efficacy under exogenous observation. A weather benchmark with zero causal
efficacy by construction—rainmaking pseudo-events over
87,664 region-days—shows apparent success of
0.853 and model reputation premia alongside negative
price–success differences.

**Keywords:** decisions from experience; endogenous observation; rare
events; probability weighting; reputation; selection

**JEL classification:** D81; D82; D83; D84

## 1. Introduction

Many economically consequential transactions price the occurrence of rare,
partly controllable events: surgical outcomes for uncommon conditions,
catastrophe insurance, drought interventions, disaster-recovery contracts, and
the advertised efficacy of low-frequency professional services. These
transactions share three structural features that standard pricing analysis
usually treats separately. The event is rare, so both buyers and sellers learn
from sparse positive outcomes. The counterfactual is hidden, because the would-be outcome
without intervention is not observed for accepted cases. And observation is
endogenous: which interventions occur—and which are recorded—depends on the
same risk state that generates outcomes. Humans have long attributed causal
efficacy to coincident outcomes under exactly these conditions (Skinner,
1948), and forecast evaluation has long required scoring performance relative
to the difficulty of the task (Murphy, 1993). The question motivating this
paper is deceptively simple: when these three features hold, what does a
posted quote actually encode?

The answer requires distinguishing four objects that are often conflated. The
objective probability \(p_t\) is the data-generating risk state. The
experienced probability \(\hat{p}_{exp,t}\) is the frequency of apparent
success in the cases that were actually observed. The subjective probability
\(\hat{p}_{subj,t}\) applies a transformation—Bayesian updating, selective
memory, or a parameterized probability-weighting scenario—to that
experienced frequency. The fourth
object, \(\hat{q}_{price,t}\), is a price-implied index: the value an
expected-value benchmark would have to place on success to rationalize the
quoted price. It is deliberately not called a probability: under
reputation-mediated pricing it includes an additive stock term and can
exceed one, so it is a composite index rather than a quantity constrained
to \([0,1]\). Throughout, "price" and "pricing" refer to this
model-implied quote formation under a reduced-form pricing rule, not to
market-clearing equilibrium prices. Under exogenous
observation the objective and experienced layers coincide in expectation
when defined on the same support; subjective transformation and reputation
can still separate the later layers. Endogenous observation introduces an
additional composition gap between the objective and experienced
probabilities, and a price can be simultaneously inflated relative to
objective risk and deflated relative to experienced frequency.

A second question follows: what can an outsider infer about true efficacy from
observed prices? We show that endogenous selection can create a
mean-performance equivalence—in the simulated rare regimes, environments
with exactly zero true efficacy generate the same MEAN apparent performance
as positive efficacy under exogenous observation—so mean apparent
performance alone cannot distinguish the two environments without
auxiliary structure. The equivalence
is first-moment only: it does not equate the joint distribution of outcomes,
prices, provider identities, or histories. Model-implied quotes transmit a
mixture of baseline hazard, selection, transformation, and reputation rather
than a clean probability signal, so observed quote data do not
automatically solve the problem either. The paper contains no
human-subject or market-transaction data: its claims concern what
model-implied quotes can encode, which is a statement about information
structure rather than estimated behavior.

The paper makes three contributions, each a result rather than a
combination of components. First, it formalizes the four-layer structure and
proves a matched-support decomposition: the experienced-frequency gap
splits into a selection/composition term and a same-support record term,
and under the model's multiplicative hazard the selection ratio equals
one plus a scaled covariance between state risk and the observation
weight, analytically independent of baseline rarity, with its sign set by
that covariance (Lemma 1)—the simulated ratio near
1.71 is the positive-selection calibration, not a
universal constant. Second, it separates probability distortion from price-composition
distortion: a generic simulation varying rarity, observation rules, learning
rules, and pricing models shows that rarity leaves the frequency structure
essentially unchanged while the relative composition of modeled prices
shifts through two non-scaling channels—a nonlinear probability-transformation
term and an additive, history-dependent reputation term—both of which can
grow relative to the objective-EV benchmark as that benchmark shrinks.
In the simulated finite regimes the transformed-frequency term is
quantitatively the larger share of the total relative distortion, which
rises from 1.12 to 11.61 while the
absolute price deviation stays flat; reputation's distinct role is a
stock–flow decoupling in which reputation premia coexist with
zero or negative contemporaneous price-success differences. The simulation also
establishes a first-moment equivalence between zero-efficacy selection and positive
efficacy. Third, it benchmarks the mechanism against a real stochastic
process with known-zero causal efficacy: rainmaking pseudo-events over
87,664 archived region-days of observed rainfall and
2595 synthetic pseudo-events, where every causal efficacy
attribution is false by construction and the selection, attribution, and
reputation mechanisms still produce elevated apparent performance.

Two clarifications frame the contribution. The selection mechanism is
GENERAL—it operates for common events too; what is specifically rare-event
about this paper is the economic scaling: as objective expected value
shrinks, non-scaling price components become relatively dominant and
successful outcomes become sparser, while inference from raw frequencies
weakens. The ingredients are established and are cited as such. Endogenous
sampling biases experience-based estimates because observation depends on
the learner's own state or choices (Denrell & March, 2001; Fiedler, 2000;
Denrell, 2005), and the bias survives Bayesian updating (Le Mens & Denrell,
2011). Selected-sample means differ from population means by a covariance
term (Heckman, 1979), and selective acceptance distorts provider report
cards (Dranove et al., 2003; Werner & Asch, 2005). Rare events are
underweighted when experienced through sampling rather than described
(Barron & Erev, 2003; Hertwig et al., 2004; Hertwig & Erev, 2009; Wulff et
al., 2018), stated probabilities differ from experienced ones (Ungemach et
al., 2009), and low probabilities are hard to use in decisions at all
(Camerer & Kunreuther, 1989; Kunreuther et al., 2001). Berk–Nash equilibrium
(Esponda & Pouzo, 2016), analogy-based expectations (Jehiel, 2018), and
laboratory evidence (Esponda & Vespa, 2018) show that endogenous feedback
can make mislearning persistent. Probability weighting supplies the
transformation layer (Tversky & Kahneman, 1992; Prelec, 1998; Gonzalez &
Wu, 1999). The selection ratio below is a standard selection identity
applied to the observation of a rare binary event, and the divergence of
the transformed relative term is a known property of the Prelec function.
The incremental contribution is the combination: an accounting
decomposition of a reduced-form quote into objective, experienced,
subjective, and reputation layers; the comparative static that separates
rarity-invariant relative distortion from shrinking absolute distortion; a
simulated stock–flow decoupling of reputation from current hazard; a
first-moment equivalence between selection and positive efficacy; and a
benchmark in which causal efficacy is zero by construction.

Section 2 defines the four probability
objects. Section 3 states the theory, including the analytic selection-ratio
lemma. Section 4 describes the generic
simulation. Section 5 introduces the zero-effect environmental benchmark.
Section 6 reports results. Section 7 discusses what prices can and cannot
reveal, candidate application domains, and limitations. Section 8 concludes.

## 2. Conceptual framework

Figure 1 represents the data-generating system shared by the generic
simulation and the environmental benchmark. A risk state enters demand,
provider acceptance, valuation, attribution of outcomes, and reputation, while
the intervention itself may or may not change the outcome. In the benchmark
environment the causal arrow is deleted by construction; in the generic
simulation its strength is a parameter swept from zero to positive values.



### 2.1. Four probability layers

For a case \(i\) in period \(t\), let \(S_{it} \in \{0,1\}\) indicate the risk
state (e.g., high hazard), \(D_{it}\) the demand decision, \(A_{it}\) the
provider's acceptance decision, \(O_{it}\) whether the case enters the observed
record, and \(Y_{it}\) the attributed outcome. Four probability objects are
defined on this structure:

\[
p_t = P(Y_{it}=1 \mid S_{it}), \quad
\hat{p}_{exp,t} = \frac{\sum_i Y_{it} O_{it}}{\sum_i O_{it}}, \quad
\hat{p}_{subj,t} = w(\hat{p}_{exp,t}), \quad
\hat{q}_{price,t} = \frac{P_t}{\alpha v},
\]

where \(w(\cdot)\) is a transformation (Bayesian updating, selective memory,
or a probability-weighting function), \(P_t\) is the quote produced by a
pricing rule (no market clearing, bargaining, or equilibrium demand is
modeled), and \(v\) is the value of a successful outcome scaled by the
pricing coefficient \(\alpha\). The first three objects are probabilities.
The fourth is a price-implied index: under an additive reputation rule
\(P_t = \alpha \hat{w}_t v + \gamma R_t\) it equals
\(\hat{w}_t + \gamma R_t/(\alpha v)\), a composite that is not constrained
to \([0,1]\) and is not interpretable as a probability in general.
Objective success probability \(p_t\) and the success
probability for accepted cases \(P(Y=1 \mid A=1)\) differ whenever acceptance
correlates with the risk state; experienced frequency adds the observation
filter \(O_{it}\); and the price-implied index absorbs reputation, margins,
and the provider's selectivity.

The quote rule itself has a minimal reduced-form interpretation. If an
agent quotes a share of perceived gross surplus, and perceived benefit is
the transformed probability times the value of a success, then the
probability part of the quote is \(\alpha\,\hat{w}_t\,v\), where
\(\alpha\) is the share of perceived gross surplus the quote recovers.
Reputation enters as a separable trust/amenity component \(\gamma R_t\),
where \(\gamma\) is the exchange rate between accumulated reputation and
quote units. The reputation-mediated rule
\(P_t = \alpha \hat{w}_t v + \gamma R_t\) is therefore a reduced-form
mapping from perceived gross benefit plus a separable reputation
component to a posted quote; it makes no equilibrium, bargaining, or
welfare-optimality claim, and the objective-EV benchmark used below is
normative only in the limited sense of objective expected value under the
model, not a welfare optimum.

### 2.2. Reputation as a stock, performance as a flow

Provider reputation \(R_{jt}\) is a decaying success rate over the
provider's own attributed outcomes before \(t\):

\[
R_{jt} = \frac{r_0 + \sum_{\tau<t} (1-\rho)\rho^{\,t-1-\tau}\, O_{\tau} Y_{\tau}\,\mathbb{1}[j_\tau = j]}
{n_0 + \sum_{\tau<t} (1-\rho)\rho^{\,t-1-\tau}\, O_{\tau}\,\mathbb{1}[j_\tau = j]},
\]

with decay \(\rho\) and prior stocks \(r_0, n_0\) (Section 4),

while contemporaneous apparent success is a flow driven by the current risk
state and the current case mix. Because the stock and the flow answer
different questions, a reputation-mediated price premium can coexist with
weak, zero, or negative mean contemporaneous price-success differences—a
decoupling that the benchmark environment makes measurable. This stock–flow
separation is the framework's central testable implication: where prices
encode reputation, the contemporaneous correlation between what was paid and
what was delivered need not be positive.

### 2.3. The mean-performance equivalence problem

An outside observer sees prices, attributed outcomes, and the accepted case
mix, but not the rejected cases or the counterfactual. If endogenous
selection concentrates interventions in high-risk states, apparent success
rises even when efficacy is exactly zero. Formally, let \(\delta\) denote true
efficacy and \(\sigma\) the strength of selection. Mean-performance
equivalence holds when \((\delta = 0, \sigma > 0)\) under endogenous
observation produces the same MEAN apparent success as
\((\delta > 0, \sigma = 0)\) under exogenous observation. The equivalence is
deliberately first-moment: it makes no claim about the joint distribution of
outcomes, prices, provider identities, event timing, or reputation
trajectories, which can differ substantially across the two environments.
Section 6 quantifies the equivalent \(\delta\) implied by selection alone.

## 3. Theory

Propositions P1–P6 organize the framework; P2 is split into a supported
form (P2a), an explicitly historical claim that failed (P2b), and the
corrected comparative-statics statement (P2c). Lemma 1 supplies the
analytic core of P2a. Table 1 classifies each by
evidentiary status: demonstrated in the generic simulation, demonstrated in
the zero-effect benchmark, or a theoretical implication not directly tested.

{{TABLE_1}}

**P1 (Risk-correlated selection shifts experienced frequency; the sign is
set by the covariance).** If observation weights covary positively with
the state risk multiplier, \(E[p_t \mid O_t = 1] > E[p_t]\) for the
selected record even when efficacy is zero; negative covariance produces
the opposite sign. This is the selection-on-gains channel of Heckman
(1979) applied to experienced frequencies, generalized by Lemma 1 to an
arbitrary state distribution: the composition shift is
\(\mathrm{Cov}(m,s)/(E[m]E[s])\), and in the calibrated simulation the
covariance is positive, converting baseline hazard into apparent
performance.

**Lemma 1 (Selection ratio under multiplicative state risk and
state-dependent observation).** Let the risk state be a random variable
\(X\) with multiplier \(m(X) > 0\), and write the objective probability as
\(p(X) = p_0\,m(X)\) where valid. Let the observation weight
\(s(X) \ge 0\)—the probability that a case in state \(X\) enters the
observed record—be independent of the baseline rarity scale \(p_0\). Then
population risk is \(E[p] = p_0 E[m(X)]\), the selected-support risk is
\(p_{ref} = p_0\,E[m(X)s(X)]/E[s(X)]\), and the selection ratio is

\[
R \;=\; \frac{p_{ref}}{E[p]}
\;=\; \frac{E[m(X)\,s(X)]}{E[m(X)]\,E[s(X)]}
\;=\; 1 + \frac{\mathrm{Cov}\big(m(X),\,s(X)\big)}{E[m(X)]\,E[s(X)]},
\]

which is independent of the baseline \(p_0\): the rarity scale cancels in
the ratio, and the absolute selection gap
\(p_{ref} - E[p] = p_0 E[m](R-1)\) is proportional to \(p_0\). The identity
also determines the SIGN of the shift: positive
\(\mathrm{Cov}(m,s)\) inflates the experienced frequency, zero covariance
leaves the composition unchanged, and negative covariance deflates it—so
risk-correlated selection need not inflate apparent success in general.
The condition fails if observation responds to the absolute level \(p(X)\)
rather than to the state or relative hazard, in which case \(s\) is not
independent of \(p_0\).

The simulation's two-state process is the special case
\(X \in \{L, H\}\) with prevalence \(\pi = P(X = H)\), multipliers
\(m_L < m_H\), mean multiplier \(\mu = \pi m_H + (1-\pi) m_L\), and
state-dependent observation probabilities \(q_L, q_H\) (demand depends on
the state; acceptance responds to the relative hazard
\(p_t/p_0 - 1 = m(S_t) - 1\)). With \(q_L = q_{D,L}q_{A,L}\) and
\(q_H = q_{D,H}q_{A,H}\),

\[
R \;=\; \frac{\pi m_H q_H + (1-\pi) m_L q_L}{\mu\,(\pi q_H + (1-\pi) q_L)},
\]

which evaluates to \(R \approx 1.7115\) under the simulation's positive
selection parameters; the simulated ratios (1.708–1.713) match within
Monte Carlo error. The value 1.71 is parameter-specific, not universal,
and the calibrated case is the positive-covariance example of the general
identity.

**P2a (Selection shifts experienced frequency proportionally; the
simulation calibrates the positive-selection case).** Holding selection
strength fixed, the selection ratio is constant across rarity regimes by
Lemma 1, so the absolute selection gap shrinks with rarity at the same
rate as \(p\) itself; the calibrated simulation is the positive-covariance
case. Moreover, the record term
\(E[Y\mid O=1]-E[p_t\mid O=1]\) is near zero at zero true efficacy: the
shift is a composition effect on the selected support, not bias in the
record itself.

**P2b (Original hypothesis—not supported: rarity amplifies the absolute
selection gap).** The earlier formulation of this project predicted that
the experienced-frequency gap would grow monotonically with rarity. The
matched-estimand decomposition rejects it: the absolute gap falls as fast
as \(p\) and the ratio is flat. Reported as a negative result.

**Lemma 2 (Unboundedness of the transformed relative term under Prelec
weighting).** Under the assumed one-parameter Prelec weighting
\(w(p) = \exp(-(-\ln p)^\alpha)\) with \(0 < \alpha < 1\), write
\(L = \ln(1/p)\). Then
\(w(p)/p = \exp(L - L^\alpha) \to \infty\) as \(p \to 0\), because
\(L - L^\alpha = L(1 - L^{\alpha-1}) \to \infty\) for \(\alpha < 1\). Hence
\((w(p)-p)/p \to \infty\) as well: the transformed-frequency relative term
is itself unbounded in rarity—it is not a bounded component. The finite
simulation grid therefore compares two divergent terms at finite \(p\),
and which component is larger is a calibration fact, not an asymptotic one.

**P2c (Rarity changes the relative composition of modeled prices through
nonlinear transformation and non-scaling reputation).** For a price
\(P = \alpha \hat{w} V + \gamma R\),
\((P - \alpha p V)/(\alpha p V) = (\hat{w}-p)/p + \gamma R/(\alpha p V)\).
Under the assumed Prelec weighting the first term diverges as \(p \to 0\)
(Lemma 2), and the second diverges provided the reputation stock \(R\)
does not itself vanish proportionally with \(p\)—the condition the
simulation parameterizes. Both components therefore fail to scale with
objective expected value: rarity changes which components dominate the
price signal relative to the objective-EV benchmark, not how large the
frequency distortion is in absolute terms. In the simulated finite regimes
the transformed-frequency term is the larger of the two; reputation's
distinct contribution is the stock–flow decoupling of P5.

**P3 (Nonlinear transformation moves the subjective layer relative to
experience).** For rare events, an inverse-S probability-weighting
function \(w(p)\) overweights \(p\) (Prelec, 1998; Tversky & Kahneman,
1992), which can move \(\hat{p}_{subj}\) away from the experienced
frequency in either direction. The Prelec transformation used here is one
parameterized scenario, not an estimated behavioral law and not the same
mechanism as the description–experience underweighting documented for
learned frequencies (Hertwig et al., 2004; Ungemach et al., 2009; Wulff
et al., 2018); Bayesian updating, recency weighting, and selective memory
are alternative transformations that the simulation compares separately.

**P4 (Model-implied quotes mix hazard and transformation).** Under expected-value pricing
with linear transformation, the price-implied index tracks
\(\hat{p}_{subj}\). Under reputation-mediated pricing it additionally loads
on the reputation stock, so \(\hat{q}_{price}\) is no longer interpretable
as a probability at all but a composite of hazard, transformed frequency,
and accumulated attribution. Misspecified-feedback equilibria make the persistence of this
composite systematic rather than transient (Esponda & Pouzo, 2016; Jehiel,
2018; Esponda & Vespa, 2018), and bounded learning on endogenous
variables can degrade inference further (Shea, 2015).

**P5 (Reputation decouples price from performance).** Because reputation is a
stock, periods of high current hazard with undelivered outcomes can coincide
with high prices built on earlier attributed successes. The contemporaneous
price-success association can therefore be zero or negative while a
reputation premium is strongly positive.

**P6 (Mean-performance equivalence limits inference from raw
performance).** Endogenous selection under zero efficacy can
reproduce—and in some regimes exceed—the MEAN apparent performance
generated by positive efficacy under exogenous observation: mean apparent
performance alone cannot distinguish the two environments in several
simulated rarity regimes. The equivalence is first-moment and
regime-dependent: it does not equate distributions, and in the simulated
common regime no efficacy in the scanned grid reproduces the endogenous
apparent success, so it is not universal. Observed quote data do not
automatically solve the problem either, because in the model quotes
themselves load on transformed beliefs and reputation—a caution, not a
proved identification theorem. Within the present framework, separating
selection from efficacy can be aided by additional information such as
rejected-case disclosure, an exogenous observation rule, pre-event risk
information, or a known-zero benchmark; other identification strategies
may also be possible.

## 4. Generic simulation

The generic simulation implements the framework as a discrete-time stochastic
system. A two-state risk process \(S_t\) persists with transition probability
\(0.97\) and spends \(30\%\) of periods in the high-hazard state, in which the
success probability is multiplied by \(2.0\) relative to baseline (by \(0.6\) in the
low-hazard state). Four rarity
regimes set the baseline success probability \(p\) to \(0.30\) (common),
\(0.10\) (moderately rare), \(0.03\) (rare), and \(0.01\) (very rare). Demand
increases in the current risk state; provider acceptance increases in the
relative hazard \(p_t/\bar{p}-1\) with provider-specific selectivity;
accepted cases enter the observed record (endogenous rule), while an
exogenous comparator requests interventions at the same marginal rate and
accepts at a constant rate, so demand and acceptance are both independent of
the state. Every learner state, reputation stock, and quote at period
\(t\) is computed from the observed record through \(t-1\) only, so no
quote conditions on the outcome it prices. The naive learner reports the raw
experienced frequency
\(\hat{p}_{exp,t-1} = \sum_{\tau<t} Y_\tau O_\tau / \sum_{\tau<t} O_\tau\);
before the first observation, where this ratio is undefined, it is
initialized at the pre-specified prior mean \(\bar{p}\) (an
initialization, not smoothing). The subjective-learning variants are
Bayesian updating with a Beta prior of mean \(\bar{p}\) and strength
\(2.0\), exponential recency weighting with decay \(0.995\), and
selective memory that weights attributed successes at \(1.0\) and failures
at \(0.35\); the recency, selective-memory, and reputation stocks start from
a prior weight equivalent to 20 attributed outcomes at mean \(0.5\).
Subjective probabilities for models C and D apply a Prelec weighting
function with \(\alpha = 0.65\) to the Bayesian estimate, a parameterized
scenario drawn from the literature, not an estimate from human subjects or
market data in this paper.
Prices are computed under four
pricing rules—each produces a model-implied quote, and none models market
clearing: A, expected value on the objective probability; B, expected value on
the raw experienced frequency \(\hat{p}_{exp,t-1}\); C, a
probability-weighted quote; and D,
a reputation-mediated rule that adds a fraction \(0.5\) of the provider's
reputation stock to the quote base. Reputation decays at \(\rho = 0.995\)
per period from prior stocks \(r_0 = 0.05\), \(n_0 = 0.10\), and it enters
the quote in periods whose case is observed for that provider; in other
periods the model D quote equals the model C quote. Each cell uses
2,000 independent replications of a \(4{,}000\)-period horizon
after burn-in; true efficacy \(\delta\) is swept over
\(\{0, 0.02, 0.05, 0.10\}\).

Metrics are defined per layer and averaged over replications with Monte Carlo
error bands. The estimands are matched by construction (estimand audit in
the project documentation): \(p_{ref} = E[p_t \mid O_t = 1]\) is the
objective probability on the observed support; the selection gap
\(p_{ref} - E[p_t]\) and selection ratio \(p_{ref}/E[p_t]\) measure the
composition shift produced by endogenous observation; the matched record
bias \(B_{abs} = \hat{p}_{exp} - p_{ref}\) and \(B_{rel} = B_{abs}/p_{ref}\)
compare the experienced frequency to its own estimand; under exogenous
observation demand and acceptance are both state-independent, so
\(p_{ref} = E[p_t]\) and all three selection quantities are zero.
the subjective and price layers are measured against the objective
probability, \(B_{subj} = \hat{p}_{subj} - p\) and
\(B_{price} = \hat{q}_{price} - p\), averaged over all periods (increments
between adjacent layers follow by differencing the layer means reported in
Table 2 and Table S8, and are not labeled \(B\));
\(D_{EV} = \text{price} - \alpha v\,p\) is the deviation from expected
value; and \(D_{rel}\) is the period mean of \(D_{EV}/(\alpha v p)\), the
relative price distortion. Because \(p_t \geq 0.006\) in every regime, the
denominator is bounded away from zero in every simulated cell. Event-level
price-success differences compare mean price on attributed successes against
attributed failures; provider-rank distortion correlates simulated price
ranks with outcome ranks. Table 2 summarizes the regimes and the four
probability layers by rule; Table S7 in Online Resource 1 reports convergence
diagnostics and Table S8 the full per-layer detail.

{{TABLE_2}}

## 5. Zero-effect environmental benchmark

The benchmark environment instantiates the framework where efficacy is known
exactly: rainmaking—payment for interventions intended to produce rainfall.
The benchmark imposes a zero causal effect of rainmaking on rainfall by
construction, so every causal efficacy attribution is
false by construction (apparent successes are still observed events; what is
false is the attribution to intervention). Any performance pricing that emerges is
generated by selection, attribution, and reputation alone. This makes the
setting a known-zero-effect environmental benchmark rather than the
substantive object of the paper: it serves as a known-zero
negative-control benchmark, bounding what the mechanisms can produce in the
absence of any true effect. The benchmark has two layers that must not be
conflated. The OBSERVED-WEATHER layer—actual rainfall, fictional event
timings, baseline-hazard selection, and the resulting apparent-success
rates—is an empirical demonstration: real weather shows that
selection/timing can generate large apparent-success differences under
known zero causal efficacy. The MODEL-OVERLAY layer—willingness to pay,
quotes, reputation, and selective memory—remains calibrated and
simulated: it demonstrates that the same mechanisms produce the
stock–flow pattern when overlaid on real weather, but it measures neither
observed market prices, actual willingness to pay, actual reputation
formation, nor human probability weighting. The empirical strength of the
benchmark is the first layer.

The environmental data are daily precipitation series from the ERA5
reanalysis (Hersbach et al., 2019), comprising 87,664
region-days across 80 climate clusters; Table 3 reports the study
locations and coverage. Prospective hazards are estimated with standard
baseline-hazard methods (Cox, 1972) on a 1991–2010 training period, and the
calibrated willingness-to-pay range follows environmental-valuation and
stated-choice practice (Pattanayak & Kramer, 2001; Hensher et al., 2006). Rainmaking institutions are cross-culturally documented, which
supplies institutional plausibility for the pricing scenarios without
committing the paper to any claim about observed historical fees:
ethnographic and historical accounts describe specialized roles, stated
payments, and responses to unreliable rainfall
(Akong'a, 1987; Espín-Sánchez & Gil-Guirado, 2022; Espín-Sánchez et al.,
2026). Prices and acceptance strategies are
calibrated scenarios, not reconstructed history.

2595 synthetic pseudo-events are generated under five
attribution rules—random dates in qualifying drought conditions, drought
dates, preceding dry spells, rolling precipitation deficit, and
high-prospective-hazard dates—plus calendar-matched placebos. Figure 2 shows the resulting apparent
success rates for the 7-day attribution window at the 1 mm threshold: apparent
success differs across event rules purely because baseline hazard differs.
The study locations and coverage are reported in Online Resource 1 (Table S9);
Figure 3 maps the empirical hazard structure.





The benchmark Monte Carlo mirrors the generic architecture. Six pricing rules span
fixed pricing, naive demand, hazard-adjusted demand, and strategic acceptance
with and without reputation-mediated pricing and probability weighting.
Because efficacy is exactly zero by construction, observed differences in
apparent performance arise only from baseline hazard, selection, attribution,
and learning—the precise mechanisms the generic simulation parameterizes.

## 6. Results

### 6.1. Risk-correlated selection shifts experienced frequency proportionally, not increasingly with rarity

We decompose the experienced-frequency gap into a matched composition term
and a record term: \(p_{exp}-p_{obj} = (p_{ref}-p_{obj}) + (p_{exp}-p_{ref})\),
where \(p_{ref} = E[p_t \mid O_t=1]\) is the objective probability on the
observed support (Figure 4, panel B; Figure 5, panel A). Under endogenous
observation the absolute selection gap falls with rarity—0.216
under common events, 0.072 under moderately rare events,
0.022 under rare events, and 0.007 under
very rare events—while the selection ratio is stable at approximately
1.71 to 1.71. This stability is not
coincidental: Lemma 1 shows the ratio is exactly independent of baseline
rarity under the model's multiplicative hazard and state-dependent
selection, and its analytic value 1.7115—the positive-covariance
calibration of the general identity—matches the simulated means within
Monte Carlo error. The record term
\(p_{exp}-p_{ref}\) is approximately zero in every regime
(0.000 under exogenous observation in the rare regime), so the
experienced-frequency inflation is a composition effect: observation selects
higher-hazard events, but the record itself is unbiased on the observed
support. The earlier formulation of this project—"experienced-frequency
bias grows monotonically with rarity"—is therefore corrected: rarity
amplifies neither the absolute gap nor the selection ratio.



### 6.2. The four layers separate

Figure 4, panel A, displays all four layers by regime. The
subjective layer under selective memory sits above experienced frequency
(mean estimate 0.341 against an experienced
frequency of 0.052 in the rare regime, so
\(B_{subj}\) relative to the objective probability is
0.311), while
Bayesian updating shrinks experienced frequencies toward the prior; recency
weighting tracks the experienced layer closely. The price-implied index under
reputation-mediated pricing separates from every probability layer: \(D_{rel}\)
for model D rises from 1.12 under common events to
11.61 under very rare events. Model A has \(D_{rel}=0\) by
construction; model B, which prices the experienced frequency, stays near
1.24–1.24 with no trend in rarity, as the rarity invariance of
the selection ratio implies; model C rises from 1.03 to 9.45, which is
exactly the transformed-frequency part of model D. Figure 5, panel B, decomposes this rise into the two
non-scaling components of P2c. The transformed-frequency term is
quantitatively the larger share in every simulated regime
(9.45 of the 11.61 total in the
very-rare regime under endogenous observation—81.4\%
of the total, down from 91.4\% under common events),
while the additive reputation term grows to 2.16 and its
share rises with rarity. Under exogenous observation the pattern is the
same with a larger reputation share throughout (58.8\%
probability share in the very-rare regime). Neither component is bounded:
under the assumed Prelec weighting the transformed-frequency relative term
itself diverges as \(p \to 0\) (Lemma 2), and the reputation term diverges
whenever the reputation stock does not vanish proportionally with \(p\).

Two qualifications keep this from being a denominator tautology. First, the
absolute deviation \(D_{EV}\) under model D stays approximately flat
across regimes (0.175 to 0.129 under
endogenous observation): the relative ratio rises because the
expected-value benchmark in its denominator shrinks, not because the
absolute deviation grows. Second, the economically meaningful statement is about
composition: rarity changes which components dominate the price signal
relative to the objective-EV benchmark. Rarity therefore changes the
relative composition of the price signal through two non-scaling
channels—nonlinear probability transformation, quantitatively dominant on
the finite grid, and additive reputation, whose share rises with
rarity—not through larger frequency bias and not through a larger absolute
deviation. Reputation's distinct result is not the size of its share but
the stock–flow decoupling of Section 6.3.



### 6.3. Reputation decouples price from contemporaneous performance

The reputation stock and the contemporaneous outcome flow answer different
questions, and the simulation makes the decoupling measurable. The
correlation between provider reputation and current hazard is
-0.159 in the rare regime—weak and negative, so
reputation does not track the current hazard state—
while event-level mean price-success differences under model D are small and
positive (0.013 in the rare regime) rather than the
large positive association a naive performance-pricing account predicts.
Provider-rank distortion—the Spearman correlation between price ranks and
outcome ranks—is -0.357 under common events, negative
because reputation concentrates among providers whose attributed histories
pre-date the current hazard cycle. The controlled benchmark below sharpens
this result: there, contemporaneous price-success differences are negative.

### 6.4. Mean-performance equivalence

Figure 6 and Table 3 report the equivalence map, defined on the mean of
apparent success only. Under endogenous selection
at zero efficacy, mean apparent success in the rare regime matches what an
exogenous-observation environment with efficacy of approximately
0.022 would produce (inverse interpolation on the efficacy
grid; 0.072 and 0.0075 in the moderately rare
and very-rare regimes). In the common regime no efficacy in the scanned
grid reproduces the endogenous apparent success—selection alone exceeds
what efficacy up to 0.10 explains. The equivalence is first-moment: the
matched quantities are mean apparent-success rates, and the joint
distribution of outcomes, prices, provider identities, and reputation
trajectories is not shown to coincide. A naive observer who regresses outcomes
on prices—or compares priced interventions with unpriced periods—recovers a
positive "effect" that is entirely generated by selection. The valid
inference is narrower than a price-based identification bound: mean
apparent performance alone cannot distinguish zero-efficacy endogenous
selection from positive-efficacy exogenous observation in the simulated
rare regimes, and observed quote data do not automatically solve the
problem because quotes themselves load on transformed beliefs and
reputation.



{{TABLE_3}}

### 6.5. Benchmark: apparent performance under exact zero efficacy

The environmental benchmark reproduces the generic mechanisms at extreme
clarity. Apparent success reaches 0.853 for
high-prospective-hazard events—versus 0.600 for matched
placebos and 0.593 for random dates—under exactly zero
efficacy (Figure 2). These apparent successes are observed rainfall events;
what is false by construction is their causal attribution to the
intervention.

Overlaying the calibrated pricing and reputation rules on the same weather
benchmark reproduces the stock–flow pattern of Section 6.3 in sharpened
form: reputation-mediated premia persist while mean contemporaneous
price–success differences are negative. This overlay is a model result,
not observed pricing—the empirical content of the benchmark is the
selection/apparent-success demonstration above. The scenario WTP
regressions, permutation falsification, and M4/M5 quote-reputation
decomposition are reported in Online Resource 1 (Section S15); Table 4
reports the pseudo-event summary. Figure 7 shows the full Monte Carlo
decomposition (detail in Online Resource 1, Table S10), and Figure 8 reports
robustness.

{{TABLE_4}}





## 7. Discussion

### 7.1. What prices reveal

The framework's main output is a diagnostic: a rare-event price is a
composite signal, and the composition changes with rarity. The
selection/composition mechanism is already fully present under common
events—a selection ratio of approximately 1.71 and a
relative price distortion of 1.12 under model D—so
rarity does not create the separation. What rarity changes is the scaling
and composition of the price signal. Under the positive risk–observation covariance calibration used here, endogenous selection inflates the
experienced layer, transformation pushes the subjective layer away from it in
either direction, and reputation loads the price-implied index with a stock
that is
nearly orthogonal to contemporaneous performance. In the benchmark
environment the composite is extreme—prices remain elevated while mean
contemporaneous price-success differences are negative—demonstrating that the
sign of the price-performance correlation is not a test of whether pricing
works.

What is uniquely rare-event about the paper is therefore not the selection
mechanism, which is general and operates identically in common regimes
(Lemma 1). It is the economics of scale: as objective expected value
shrinks, both non-scaling components—nonlinear probability transformation
and additive reputation stocks—grow relative to the objective-EV
benchmark, successful outcomes become sparser, and the equivalent-efficacy
interpretation of a raw apparent-success rate shrinks with the selection
gap: the mean performance that zero-efficacy selection produces falls with
the baseline probability, so the equivalent efficacy scales downward
(0.072 to 0.0075 across the simulated rare
regimes) rather than staying inflated. Rarity changes the interpretation
of the price, not the existence of the distortion.

### 7.2. Identification

The mean-performance equivalence result suggests concrete routes to separating
selection from efficacy within the present framework: (i) disclosure of the
rejected case mix, which would break the observation filter; (ii) an
exogenous observation rule, so that experienced frequencies are generated
independently of the risk state; (iii) pre-event risk information, which
would let the case mix be adjusted directly; or (iv) a known-zero benchmark
that calibrates what the mechanisms alone produce. The benchmark
environment supplies (iv); the others are design routes for markets that
price rare interventions, and other identification strategies may also be
possible. These routes parallel the case-mix adjustments developed for surgeon report cards, where
baseline risk and selection contaminate raw performance comparisons
(Shahian & Normand, 2008; Werner & Asch, 2005; Barnett et al., 2005), and the
information-aggregation concerns of cascade models in which endogenous
signals transmit distorted states (Bikhchandani et al., 1992; Dranove et
al., 2003; Kreps & Wilson, 1982), and expert advice embeds
similar adverse-selection and reputation forces (Liu & Sanyal, 2012).

### 7.3. Candidate application domains

The framework is a structural analogy, not a validated account of any
particular market. It applies as a candidate model only where four
ingredients jointly hold: a rare priced outcome, endogenous observation
(case selection correlated with the risk state), a hidden counterfactual,
and prices or reputations built on the observed record. Medical reputation
markets plausibly satisfy all four—low-frequency outcomes, hidden
counterfactuals, selected case loads—and surgeon report cards already
document the raw-comparison problem the framework formalizes (Shahian &
Normand, 2008; Werner & Asch, 2005), although their information structure,
regulation, and price-setting institutions differ from the stylized model.
The direction of the composition shift is domain-specific: by Lemma 1 it
is determined by \(\mathrm{Cov}(m,s)\), so provider cherry-picking of
low-risk cases can inflate apparent success while adverse selection can
move it in the opposite direction. Catastrophe insurance, credit for rare
default events, and low-frequency
professional services are candidate domains to the extent that providers
or buyers select endogenously on risk and histories accumulate into
reputation—experienced price distributions demonstrably shape
subsequent consumer beliefs (Matsumoto & Spence, 2016); whether each ingredient holds—and which sign the covariance
takes—is an empirical question this
paper does not answer. Where the ingredients do hold, the framework
predicts (a) experienced-frequency inflation under positive risk–observation
covariance (deflation under negative), concentrated in the
observation-selected segment, (b) price-implied indices that track
reputation stocks rather than contemporaneous flows, and (c) attenuation
of apparent efficacy once hazard is controlled—the pattern the benchmark
environment exhibits in its extreme form.

### 7.4. Limitations

Three limitations bound the claims. The simulation demonstrates what the
mechanisms can produce, not what actual people or markets do; no claim is
made about observed historical rainmaking prices, universal probability
weighting, actual consumer willingness-to-pay relationships, or observed
market pricing of rare events. The generic model is stylized: one risk state,
stationary rarity regimes, and specific functional forms for demand,
acceptance, and learning, although sensitivity checks vary the key slopes.
The benchmark uses fictional pseudo-events over real weather; it demonstrates
the feasibility of the mechanisms under a true zero but measures neither
market prices nor human beliefs in any real domain. The quote rule is one
reduced-form mapping—other pricing institutions could shift magnitudes
though not the decomposition itself—and the reputation stock follows
exponential smoothing of attributed outcomes, one accumulation rule among
others; the stock–flow decoupling it demonstrates is a possibility result,
not a claim about every reputation mechanism.

## 8. Conclusion

When the event being priced is rare, the counterfactual hidden, and
observation endogenous, the signal embedded in a modeled quote is not
generally the objective risk. The framework separates the objective probability, the
experienced frequency on the selected record, the transformed subjective
probability, and a price-implied index that need not be a probability at
all; under the positive risk–observation covariance calibration used here,
endogenous selection inflates experienced frequencies by a selection ratio
that is analytically independent of baseline rarity under multiplicative
scaling, while
reputation-mediated pricing decouples price from contemporaneous performance
and produces a relative distortion that rises with rarity through two
non-scaling channels—a nonlinear probability-transformation term that
carries the larger share in the simulated regimes and an additive
reputation term whose share grows—an absolute deviation that stays flat
even as the relative ratio grows;
and the zero-effect environmental benchmark demonstrates that elevated
apparent performance, reputation premia, and negative mean contemporaneous
price-success differences all arise under exactly zero efficacy. Prices of
rare events track a composite of baseline hazard, selection, transformation,
and accumulated attribution—and observed model-implied quotes do not by
themselves reveal how much of the signal reflects each component. Within the present framework, evaluation of rare-event pricing
can be aided by case-mix disclosure, exogenous observation, pre-event risk
information, or known-zero benchmarks—several routes rather than an
exclusive requirement; the framework supplies the language, and the
benchmark supplies the zero effect.

## Acknowledgements

[AUTHOR INPUT REQUIRED: provide acknowledgements or confirm that none are
required.]

## Statements and Declarations

### Data and code availability

Code, frozen analytical outputs, acquisition ledgers, and
manuscript-generation files are publicly available at
https://github.com/bougtoir/pricing-the-rain. The ERA5 precipitation data
(Copernicus Climate Change Service) are not redistributed. They are publicly
available through the Open-Meteo Historical Weather API, and the repository
provides the exact request URLs, retrieval code, and checksums of the derived
files. Other sources whose redistribution rights are unclear are likewise
not redistributed. Fictional pseudo-events and all simulation outputs are
reproducible from the re-acquired rainfall series and the declared seeds.

### Funding

[AUTHOR INPUT REQUIRED: identify funding sources or state that no specific
funding was received.]

### Competing interests

[AUTHOR INPUT REQUIRED: declare competing interests or state that none exist.]

### Author contributions

[AUTHOR INPUT REQUIRED: provide CRediT roles for each author.]

### Ethics

The study uses public environmental data, bibliographic metadata, and
simulated fictional events. It includes no human participants, personal data,
or animal research.

### Generative AI disclosure

During preparation of this work, the authors used Devin (Cognition AI) to
assist with code development, manuscript drafting, and language organization.
[AUTHOR CONFIRMATION REQUIRED: after using this tool, the authors reviewed and
edited the content as needed and take full responsibility for the content of
the publication.] No generative-AI image tool was used to create or alter the
scientific figures, and no generative AI was used to fabricate data or
references.

## References

Akong'a, J. (1987). Rainmaking rituals: A comparative study of two Kenyan societies. *African Study Monographs*, *8*(2), 71–85. https://doi.org/10.14989/68028

Barnett, A. G., van der Pols, J. C., & Dobson, A. J. (2005). Regression to the mean: What it is and how to deal with it. *International Journal of Epidemiology*, *34*(1), 215–220. https://doi.org/10.1093/ije/dyh299

Barron, G., & Erev, I. (2003). Small feedback‐based decisions and their limited correspondence to description‐based decisions. *Journal of Behavioral Decision Making*, *16*(3), 215-233. https://doi.org/10.1002/bdm.443

Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades. *Journal of Political Economy*, *100*(5), 992-1026. https://doi.org/10.1086/261849

Camerer, C. F., & Kunreuther, H. (1989). Decision Processes for Low Probability Events: Policy Implications. *Journal of Policy Analysis and Management*, *8*(4), 565. https://doi.org/10.2307/3325045

Cox, D. R. (1972). Regression Models and Life-Tables. *Journal of the Royal Statistical Society Series B: Statistical Methodology*, *34*(2), 187-202. https://doi.org/10.1111/j.2517-6161.1972.tb00899.x

Denrell, J. (2005). Why Most People Disapprove of Me: Experience Sampling in Impression Formation. *Psychological Review*, *112*(4), 951-978. https://doi.org/10.1037/0033-295x.112.4.951

Denrell, J., & March, J. G. (2001). Adaptation as Information Restriction: The Hot Stove Effect. *Organization Science*, *12*(5), 523-538. https://doi.org/10.1287/orsc.12.5.523.10092

Dranove, D., Kessler, D., McClellan, M., & Satterthwaite, M. (2003). Is More Information Better? The Effects of “Report Cards” on Health Care Providers. *Journal of Political Economy*, *111*(3), 555-588. https://doi.org/10.1086/374180

Esponda, I., & Pouzo, D. (2016). Berk-Nash Equilibrium: A Framework for Modeling Agents With Misspecified Models. *Econometrica*, *84*(3), 1093-1130. https://doi.org/10.3982/ecta12609

Esponda, I., & Vespa, E. (2018). Endogenous sample selection: A laboratory study. *Quantitative Economics*, *9*(1), 183-216. https://doi.org/10.3982/qe650

Espín-Sánchez, J. A., & Gil-Guirado, S. (2022). Praying for rain, resilience, and social stability in Murcia (southeast Spain). *Ecology and Society*, *27*(2). https://doi.org/10.5751/es-12875-270209

Espín-Sánchez, J. A., Gil-Guirado, S., & Ryan, N. (2026). Praying for Rain. *The Quarterly Journal of Economics*, *141*(3), 2363-2422. https://doi.org/10.1093/qje/qjag026

Fiedler, K. (2000). Beware of samples! A cognitive-ecological sampling approach to judgment biases. *Psychological Review*, *107*(4), 659-676. https://doi.org/10.1037/0033-295x.107.4.659

Gonzalez, R., & Wu, G. (1999). On the Shape of the Probability Weighting Function. *Cognitive Psychology*, *38*(1), 129-166. https://doi.org/10.1006/cogp.1998.0710

Heckman, J. J. (1979). Sample Selection Bias as a Specification Error. *Econometrica*, *47*(1), 153. https://doi.org/10.2307/1912352

Hensher, D., Shore, N., & Train, K. (2006). Water Supply Security and Willingness to Pay to Avoid Drought Restrictions. *Economic Record*, *82*(256), 56-66. https://doi.org/10.1111/j.1475-4932.2006.00293.x

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., Muñoz‐Sabater, J., Nicolas, J., Peubey, C., Radu, R., Schepers, D., Simmons, A., Soci, C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, G., Bidlot, J., Bonavita, M., …, Thépaut, J. N. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, *146*(730), 1999-2049. https://doi.org/10.1002/qj.3803

Hertwig, R., Barron, G., Weber, E. U., & Erev, I. (2004). Decisions from Experience and the Effect of Rare Events in Risky Choice. *Psychological Science*, *15*(8), 534-539. https://doi.org/10.1111/j.0956-7976.2004.00715.x

Hertwig, R., & Erev, I. (2009). The description–experience gap in risky choice. *Trends in Cognitive Sciences*, *13*(12), 517-523. https://doi.org/10.1016/j.tics.2009.09.004

Jehiel, P. (2018). Investment Strategy and Selection Bias: An Equilibrium Perspective on Overoptimism. *American Economic Review*, *108*(6), 1582-1597. https://doi.org/10.1257/aer.20161696

Kreps, D. M., & Wilson, R. (1982). Reputation and imperfect information. *Journal of Economic Theory*, *27*(2), 253-279. https://doi.org/10.1016/0022-0531(82)90030-8

Kunreuther, H., Novemsky, N., & Kahneman, D. (2001). Making Low Probabilities Useful. *Journal of Risk and Uncertainty*, *23*(2), 103-120. https://doi.org/10.1023/a:1011111601406

Le Mens, G., & Denrell, J. (2011). Rational learning and information sampling: On the “naivety” assumption in sampling explanations of judgment biases. *Psychological Review*, *118*(2), 379-392. https://doi.org/10.1037/a0023010

Liu, Y. F., & Sanyal, A. (2012). When second opinions hurt: A model of expert advice under career concerns. *Journal of Economic Behavior &amp; Organization*, *84*(1), 1-16. https://doi.org/10.1016/j.jebo.2012.07.006

Matsumoto, B., & Spence, F. (2016). Price beliefs and experience: Do consumers’ beliefs converge to empirical distributions with repeated purchases? *Journal of Economic Behavior &amp; Organization*, *126*, 243-254. https://doi.org/10.1016/j.jebo.2016.03.008

Murphy, A. H. (1993). What Is a Good Forecast? An Essay on the Nature of Goodness in Weather Forecasting. *Weather and Forecasting*, *8*(2), 281-293. https://doi.org/10.1175/1520-0434(1993)008<0281:wiagfa>2.0.co;2

Pattanayak, S. K., & Kramer, R. A. (2001). Pricing ecological services: Willingness to pay for drought mitigation from watershed protection in eastern Indonesia. *Water Resources Research*, *37*(3), 771-778. https://doi.org/10.1029/2000wr900320

Prelec, D. (1998). The Probability Weighting Function. *Econometrica*, *66*(3), 497. https://doi.org/10.2307/2998573

Shahian, D. M., & Normand, S. L. T. (2008). Comparison of “Risk-Adjusted” Hospital Outcomes. *Circulation*, *117*(15), 1955-1963. https://doi.org/10.1161/circulationaha.107.747873

Shea, P. (2015). Red herrings and revelations: does learning about a new variable worsen forecasts? *Economic Modelling*, *49*, 395-406. https://doi.org/10.1016/j.econmod.2015.05.012

Skinner, B. F. (1948). 'Superstition' in the pigeon. *Journal of Experimental Psychology*, *38*(2), 168-172. https://doi.org/10.1037/h0055873

Tversky, A., & Kahneman, D. (1974). Judgment under Uncertainty: Heuristics and Biases. *Science*, *185*(4157), 1124-1131. https://doi.org/10.1126/science.185.4157.1124

Tversky, A., & Kahneman, D. (1992). Advances in prospect theory: Cumulative representation of uncertainty. *Journal of Risk and Uncertainty*, *5*(4), 297-323. https://doi.org/10.1007/bf00122574

Ungemach, C., Chater, N., & Stewart, N. (2009). Are Probabilities Overweighted or Underweighted When Rare Outcomes Are Experienced (Rarely)? *Psychological Science*, *20*(4), 473-479. https://doi.org/10.1111/j.1467-9280.2009.02319.x

Werner, R. M., & Asch, D. A. (2005). The unintended consequences of publicly reporting quality information. *JAMA*, *293*(10), 1239–1244. https://doi.org/10.1001/jama.293.10.1239

Wulff, D. U., Mergenthaler-Canseco, M., & Hertwig, R. (2018). A meta-analytic review of two modes of learning and the description-experience gap. *Psychological Bulletin*, *144*(2), 140-176. https://doi.org/10.1037/bul0000115

## Figure legends

**Fig. 1** Conceptual framework. Baseline environmental hazard enters demand, provider acceptance, valuation, attribution, and reputation, while the pseudo-intervention never changes rainfall

**Fig. 2** Natural rainfall following fictional known-zero-effect stress tests in 2011–2020, shown as apparent success by prospective event-selection rule. Apparent successes are observed rainfall events; causal attribution to intervention is false by construction

**Fig. 3** Estimated seven-day rainfall hazards by preceding dry-spell duration and location in the 1991–2010 training period. The eight locations are pre-specified mechanism stress tests, not a representative global sample

**Fig. 4** Four-layer separation in the generic rare-event simulation. Panel A compares the objective probability, experienced frequency, subjective probability, and price-implied index under endogenous observation across rarity regimes; panel B shows the absolute selection gap p_ref − p_obj and the selection ratio p_ref / p_obj under endogenous versus exogenous observation; panel C shows relative price distortion against objective expected-value pricing for models B–D; panel D shows the contemporaneous price–outcome association under Model D. All quantities are generated (simulation evidence, not empirical estimates)

**Fig. 5** Frequency distortion versus price distortion across rarity regimes. Panel A: absolute selection gap (bars, left axis) shrinks with rarity while the selection ratio (lines, right axis) is stable at approximately 1.71 under endogenous observation and 1.00 under exogenous observation—the analytically derived invariance of Lemma 1. Panel B: relative price distortion under Model D decomposes into a transformed-frequency part that is quantitatively dominant in every simulated regime and an additive reputation part whose share rises as objective expected value shrinks; neither part is bounded relative to the shrinking benchmark. The relative-distortion rise is a denominator-scaling effect in both non-scaling components, not growing frequency bias and not growing absolute mispricing

**Fig. 6** Mean-performance equivalence map. Mean apparent success among observed events as true efficacy added on intervened periods varies, under endogenous (A) and exogenous (B) observation. Endogenous selection with zero true efficacy reproduces the MEAN apparent success of positive efficacy under exogenous observation (first-moment equivalence only)

**Fig. 7** Zero-effect benchmark: sequential Monte Carlo pricing-rule enrichment under M0–M5 on fictional rainmaking pseudo-events over observed weather. M0–M1 shuffle rainfall outcomes within sampled years; M2–M5 retain observed local and seasonal ordering. Selective acceptance changes accepted-event composition and current apparent success. In M4–M5, past attributed outcomes accumulate in reputation stocks that create price premia and provider-price heterogeneity, while current success remains a natural-rainfall flow governed by current hazard. Mean price(success) minus price(failure) is negative in M4–M5. Error bars are 2.5th and 97.5th Monte Carlo percentiles, not confidence intervals for historical parameters

**Fig. 8** Robustness. Apparent success across rainfall thresholds and windows, selected parameter sensitivity, and Monte Carlo precision
