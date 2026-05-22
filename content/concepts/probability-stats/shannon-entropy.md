---
type: concept
title: "Shannon Entropy"
tags:
  - concept
  - information-theory
  - probability
level: 3
prerequisites:
  - "[[probability-distributions|Probability Distributions]]"
  - "[[logarithms-and-exponentials|Logarithms and Exponentials]]"
---

## What It Is

Shannon entropy is the average amount of information (in bits, when using $\log_2$) carried by a random variable. Equivalently, it is the minimum number of bits per symbol required to losslessly encode draws from the variable's distribution. For a discrete random variable $X$ with distribution $p$:

$$H(X) = -\sum_i p(x_i)\,\log_2 p(x_i)$$

**Properties:**

- **Non-negative**, with $H = 0$ iff one outcome has probability 1 (no uncertainty).
- **Maximum at the uniform distribution**: for $n$ outcomes, $H_{\max} = \log_2 n$. For a binary variable, max is 1 bit at $p = 0.5$.
- **Concave** in $p$ and **additive over independent variables**: $H(X, Y) = H(X) + H(Y)$ if independent.

For a binary market quoting price $q$ (interpreted as $\mathbb{P}[\text{YES}]$):

$$H(q) = -q\log_2 q - (1-q)\log_2(1-q)$$

The closer $q$ is to $0.5$, the more uncertainty the market is pricing in, and the more information the eventual resolution will reveal.

## Why It Matters

Entropy is the unit in which **information** is measured. Everything downstream — [[kl-divergence|KL Divergence]], [[maximum-entropy-principle|Maximum Entropy Principle]], cross-entropy loss, [[kelly-criterion|Kelly Criterion]] growth rates — is defined relative to it.

**Uses in trading:**

- **Pricing uncertainty**: $H$ of a [[prediction-markets|prediction market]] price quantifies the remaining uncertainty the market is pricing. A market at 0.50 holds 1 bit; at 0.95, only ~0.29 bits.
- **Signal information content**: the conditional entropy $H(Y \mid X)$ measures how much uncertainty about the target $Y$ remains after observing signal $X$. Mutual information $I(X;Y) = H(Y) - H(Y \mid X)$ is the amount the signal reveals.
- **Anomaly / regime detection**: tracking $H(t)$ of a price-implied distribution over time and watching its derivative $dH/dt$ flags abrupt collapses in uncertainty (large directional moves, possible information leakage). Thresholding $|dH/dt|$ at $k \cdot \sigma_H$ (e.g. $k = 3$) gives a simple change-point detector; the events still need to be triaged against public news before claiming insider activity.
- **Distribution-free feature scoring**: entropy-based criteria (information gain, mutual information) rank features without assuming a functional form, useful in ML pipelines where linear correlation is misleading.

**Caveats:**

- Entropy in bits requires $\log_2$; using $\ln$ gives nats. Be consistent.
- Estimating $H$ from a small sample is biased downward (Miller-Madow correction etc.); matters for short rolling windows.
- A market's *implied* entropy is the entropy under the market's *risk-neutral* / equilibrium distribution, not the true one. See [[interpreting-prediction-market-prices-manski|Interpreting Prediction Market Prices — Manski]].

## Key Equations

**Discrete entropy:**
$$H(X) = -\sum_i p(x_i)\,\log_2 p(x_i)$$

**Binary entropy function:**
$$H_2(p) = -p\log_2 p - (1-p)\log_2(1-p), \qquad H_2(0.5) = 1$$

**Joint, conditional, mutual:**
$$H(X, Y) = H(X) + H(Y \mid X), \qquad I(X; Y) = H(X) + H(Y) - H(X, Y)$$

## Resources

- Shannon, C.E. (1948) — "A Mathematical Theory of Communication"
- Cover & Thomas — *Elements of Information Theory* (canonical reference)
- [[a-new-interpretation-of-information-rate-kelly|A New Interpretation of Information Rate — Kelly]] — Kelly derives optimal bet sizing from Shannon's information rate

## Connections

- [[kl-divergence|KL Divergence]] — relative entropy; measures distance between two distributions in bits
- [[maximum-entropy-principle|Maximum Entropy Principle]] — choose the highest-entropy distribution consistent with known constraints
- [[kelly-criterion|Kelly Criterion]] — expected log-growth of a Kelly bettor equals the [[kl-divergence|KL Divergence]] of their beliefs from market-implied probabilities
- [[logarithmic-market-scoring-rule|Logarithmic Market Scoring Rule]] — LMSR's cost function is literally a log-sum-exp; prices come from the same family as the softmax used in cross-entropy
- [[prediction-markets|Prediction Markets]] — natural venue for entropy / KL analysis because prices map directly to probabilities
