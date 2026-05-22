---
type: concept
title: "KL Divergence"
tags:
  - concept
  - information-theory
  - probability
level: 3
prerequisites:
  - "[[Shannon Entropy]]"
  - "[[Probability Distributions]]"
---

## What It Is

The Kullback–Leibler divergence (relative entropy) measures how many extra bits per symbol are needed to encode draws from distribution $P$ if the encoder is optimized for distribution $Q$ instead. For discrete $P, Q$:

$$D_{\mathrm{KL}}(P \,\|\, Q) = \sum_i p(x_i)\,\log_2 \frac{p(x_i)}{q(x_i)}$$

**Properties:**

- **Non-negative**, with $D_{\mathrm{KL}} = 0$ iff $P = Q$ everywhere (Gibbs' inequality).
- **Asymmetric**: $D_{\mathrm{KL}}(P \,\|\, Q) \neq D_{\mathrm{KL}}(Q \,\|\, P)$ in general. The first argument is the *true* (or trader's) distribution; the second is the *reference* (or market's).
- **Not a metric** (fails the triangle inequality), but functions as a directed "distance" between distributions.
- **Undefined when $q(x_i) = 0$ and $p(x_i) > 0$**. In practice, clip probabilities to a small $\varepsilon$ (e.g. $[0.01, 0.99]$) for numerical safety.

For a binary market at price $q$ where the trader's estimate is $p$:

$$D_{\mathrm{KL}}(p \,\|\, q) = p\log_2\!\frac{p}{q} + (1-p)\log_2\!\frac{1-p}{1-q}$$

## Why It Matters

**KL divergence is the natural unit of trading edge over a probabilistic counterparty.** This is not analogy — it falls out of Kelly's derivation:

- For a [[Kelly Criterion|full-Kelly]] bettor wagering on a binary event at fair odds $b = q/(1-q)$ implied by market price $q$, when their true belief is $p$, the expected log-growth per bet is exactly $D_{\mathrm{KL}}(p \,\|\, q)$ (in bits if $\log_2$, nats if $\ln$). Over $n$ independent bets, wealth compounds at rate $n \cdot D_{\mathrm{KL}}(p \,\|\, q)$.
- This identifies *edge in bits per trade* with *expected log-return per trade* under optimal sizing.

**Practical workflow on prediction markets:**

1. For each open market, form a probability estimate $p$ (model, base rate, signal fusion via [[Maximum Entropy Principle]], etc.).
2. Compute $D_{\mathrm{KL}}(p \,\|\, q)$ against the market price $q$.
3. Rank markets by edge; trade the top entries subject to fees, liquidity, and capacity.

**Rough thresholds (binary markets, after clipping):**

- $D_{\mathrm{KL}} < 0.05$ bits — likely below fees and slippage; skip.
- $0.05 \le D_{\mathrm{KL}} < 0.10$ bits — marginal; depends on cost structure.
- $0.10 \le D_{\mathrm{KL}} < 0.30$ bits — meaningful edge.
- $D_{\mathrm{KL}} > 0.30$ bits — suspiciously large; double-check the model and check for unmodeled tail outcomes.

**Cross-entropy and ML connection:** the cross-entropy loss used in classification is $H(p, q) = H(p) + D_{\mathrm{KL}}(p \,\|\, q)$. Minimizing cross-entropy of predicted probabilities against labels is minimizing KL divergence to the empirical distribution — the same object that quantifies trading edge.

**What KL doesn't tell you:**

- It is an *ex ante* expected quantity. Realized P&L on any single trade is dominated by variance, not edge.
- High $D_{\mathrm{KL}}$ does not survive bad probability calibration. If your $p$ is systematically wrong, the computed edge is fictional.
- It ignores transaction costs, slippage, and counterparty/credit risk — these are subtracted from realized growth, not from $D_{\mathrm{KL}}$.

## Key Equations

**Discrete KL divergence:**
$$D_{\mathrm{KL}}(P \,\|\, Q) = \sum_i p(x_i)\,\log_2 \frac{p(x_i)}{q(x_i)}$$

**Decomposition via cross-entropy:**
$$D_{\mathrm{KL}}(P \,\|\, Q) = H(P, Q) - H(P), \qquad H(P, Q) = -\sum_i p(x_i)\log_2 q(x_i)$$

**Expected log-growth of a Kelly bettor (binary, betting at market-implied odds):**
$$g^* = D_{\mathrm{KL}}(p \,\|\, q)$$

## Resources

- Cover & Thomas — *Elements of Information Theory*, Ch. 2, 6
- [[A New Interpretation of Information Rate — Kelly]] — derives the growth-rate = KL identity
- [[Advances in Financial Machine Learning — López de Prado]] — entropy and mutual information as feature-selection tools

## Connections

- [[Shannon Entropy]] — KL is the relative-entropy generalization
- [[Kelly Criterion]] — expected log-growth of optimal sizing equals $D_{\mathrm{KL}}$ of beliefs from market
- [[Maximum Entropy Principle]] — chosen distribution is the one with minimum $D_{\mathrm{KL}}$ from the uniform prior subject to constraints
- [[Prediction Markets]] — cleanest venue to compute KL because market prices are explicit probabilities
- [[Bayes' Theorem]] — Bayesian updating monotonically decreases expected KL to the truth as evidence accumulates
