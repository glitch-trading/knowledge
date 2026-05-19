---
type: concept
title: "Hidden Markov Models"
tags:
  - concept
  - statistics
  - machine-learning
  - regimes
level: 6
prerequisites:
  - "[[Markov Chain]]"
  - "[[Regime Switching]]"
---

## What It Is

A **Hidden Markov Model (HMM)** is a Markov chain over an *unobservable* state, observed through noisy emissions. Where an observable [[Regime Switching]] model requires the modeler to label each historical bar by hand (bull / bear / sideways from rolling returns, etc.), an HMM learns both the regime sequence and the regime-conditional return distributions jointly from data — without any labels.

Two stochastic processes are running:

- **Hidden state sequence** $Z_1, Z_2, \ldots, Z_T \in \{1, \ldots, K\}$ — a Markov chain over $K$ latent regimes with transition matrix $\mathbf{A}$ where $A_{ij} = P(Z_{t+1} = j \mid Z_t = i)$.
- **Observed sequence** $X_1, X_2, \ldots, X_T$ — each $X_t$ drawn from an **emission distribution** $b_j(x) = P(X_t = x \mid Z_t = j)$ depending only on the current hidden state.

For financial applications, emissions are typically returns (or a vector of returns plus realized vol, credit spread, VIX term-structure slope, etc.) and the emission distribution is Gaussian: $X_t \mid Z_t = j \sim \mathcal{N}(\mu_j, \Sigma_j)$.

The parameter set is $\lambda = (\mathbf{A}, \{(\mu_j, \Sigma_j)\}, \boldsymbol\pi_0)$ where $\boldsymbol\pi_0$ is the initial state distribution.

## Why It Matters

The most important market regimes — credit cycles, monetary policy stance, dealer risk appetite, structural liquidity conditions — are driven by *latent* factors that are not directly visible in price data. An observable regime-switching model that thresholds on 20-day returns will identify a bear regime *after* it has already shown up in prices. An HMM with the right emissions can identify the same regime as it is forming, because the latent factor leaks into multiple observable channels at once (returns *and* vol *and* spreads *and* term structure) and the model combines them probabilistically.

Concretely:

- **No labeling required.** Bypass the brittle threshold definitions of observable regime models.
- **Soft regime probabilities.** At each $t$ you get $P(Z_t = j \mid X_{1:t})$ — a probability distribution over regimes, not a hard label. Position sizing maps naturally to this distribution.
- **Information fusion.** Multivariate emissions integrate signals from different channels in a principled way.
- **Online updating.** The forward algorithm updates regime probabilities one observation at a time — well-suited to live trading.

The cost is non-convex parameter estimation (see Baum-Welch below) and significantly higher sensitivity to misspecification. HMMs reward domain knowledge in emission design more than any other extra hyperparameter.

## Three Canonical Problems

For a fixed model $\lambda$:

1. **Evaluation** — compute $P(X_{1:T} \mid \lambda)$, the likelihood of the observed sequence. Solved by the **forward algorithm** (dynamic programming, $O(K^2 T)$).
2. **Decoding** — find the single most likely hidden sequence $\arg\max_{Z_{1:T}} P(Z_{1:T} \mid X_{1:T}, \lambda)$. Solved by the **Viterbi algorithm** (a max-product variant of forward, also $O(K^2 T)$).
3. **Learning** — estimate $\lambda$ from observed $X_{1:T}$ alone (no labels). Solved by **Baum-Welch**, the EM algorithm specialized to HMMs.

## Key Equations

**Forward recursion** for $\alpha_t(j) = P(X_{1:t}, Z_t = j \mid \lambda)$:

$$\alpha_1(j) = \pi_{0,j}\, b_j(X_1)$$

$$\alpha_{t+1}(j) = b_j(X_{t+1}) \sum_{i=1}^{K} \alpha_t(i)\, A_{ij}$$

**Backward recursion** for $\beta_t(i) = P(X_{t+1:T} \mid Z_t = i, \lambda)$:

$$\beta_T(i) = 1$$

$$\beta_t(i) = \sum_{j=1}^{K} A_{ij}\, b_j(X_{t+1})\, \beta_{t+1}(j)$$

**Posterior regime probability** (smoothed):

$$\gamma_t(j) = P(Z_t = j \mid X_{1:T}, \lambda) = \frac{\alpha_t(j)\,\beta_t(j)}{\sum_i \alpha_t(i)\,\beta_t(i)}$$

**Viterbi recursion** (max-product, for the most-likely path):

$$\delta_{t+1}(j) = b_j(X_{t+1}) \max_i \left[\delta_t(i)\, A_{ij}\right]$$

**Baum-Welch** is EM with these as the E-step; the M-step updates $\mathbf{A}$, $\boldsymbol\mu$, $\boldsymbol\Sigma$ from expected sufficient statistics under $\gamma$ and $\xi_t(i,j) = P(Z_t = i, Z_{t+1} = j \mid X_{1:T}, \lambda)$.

## Fitting in Code

`hmmlearn` provides Baum-Welch and Viterbi out of the box:

```python
from hmmlearn import hmm
import numpy as np, pandas as pd

def fit_market_hmm(returns: pd.Series, n_states: int = 3, n_restarts: int = 10):
    X = returns.values.reshape(-1, 1)
    best = None
    for seed in range(n_restarts):                       # Baum-Welch finds a local max
        m = hmm.GaussianHMM(n_components=n_states,       # always run multiple restarts
                            covariance_type="full",
                            n_iter=1000, random_state=seed).fit(X)
        if best is None or m.score(X) > best.score(X):
            best = m
    return best
```

Online regime forecast for live trading:

```python
def hmm_signal(model, returns: pd.Series, lookback: int = 252) -> pd.Series:
    sigs = []
    for i in range(lookback, len(returns)):
        window = returns.iloc[i - lookback:i].values.reshape(-1, 1)
        posterior = model.predict_proba(window)[-1]      # P(Z_t = j | X_{1:t})
        next_dist = posterior @ model.transmat_          # one-step-ahead forecast
        sigs.append(next_dist[0] - next_dist[1])         # bull − bear (after sorting states)
    return pd.Series(sigs, index=returns.index[lookback:])
```

After fitting, re-label hidden states by economic interpretation (e.g., sort by emission mean so state 0 = highest-mean = bull). Baum-Welch returns arbitrary state indices; the post-processing step is mandatory.

## Implementation Pitfalls

- **Local optima.** Baum-Welch maximizes a non-convex likelihood and gets stuck. Always run $\geq 10$ restarts from random initializations and keep the highest-likelihood fit. The default single initialization frequently produces a noticeably worse regime assignment.
- **Emission design dominates.** Returns alone carry limited regime information. Returns combined with realized vol, credit spreads, VIX term-structure slope, dealer-positioning indicators — any of these add real lift. This is where domain knowledge compounds the math.
- **Number of states.** Pick $K$ by economic reasoning first, then validate with BIC or held-out likelihood. More states fit the training data better but generalize worse; $K=2$ or $K=3$ is typical for monthly/daily macro regimes.
- **Underflow.** Forward probabilities underflow for moderately long sequences. Production implementations scale $\alpha$ at each step or work in log-space throughout. `hmmlearn` handles this; rolling your own does not unless you remember to.
- **Stationarity assumption.** Like any [[Markov Chain]], the HMM assumes time-homogeneous transitions. The same rolling-window discipline from [[Regime Switching]] applies.

## Resources

- Rabiner (1989) — "A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition" (still the clearest exposition of the three problems and their algorithms)
- *Pattern Recognition and Machine Learning* by Bishop — Ch. 13 on sequential data, derives Baum-Welch as a special case of EM
- *Inference in Hidden Markov Models* by Cappé, Moulines & Rydén — comprehensive monograph
- Hamilton (1989) — the regime-switching paper that introduced HMM-style models to econometrics

## Connections

- [[Markov Chain]] — the latent process inside an HMM is a Markov chain
- [[Regime Switching]] — the observable-state cousin of HMMs
- [[Time Series Analysis]] — broader methodological context
- [[Maximum Drawdown]] / [[Position Sizing]] — natural consumers of soft regime probabilities
- [[Trading Strategies MOC]] — where HMM-driven strategies live
