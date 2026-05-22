---
type: concept
title: "Bayes' Theorem"
tags:
  - concept
  - probability
level: 1
prerequisites: []
---

## What It Is

**Bayes' Theorem** provides a way to update the probability of a hypothesis given new evidence. It inverts conditional probabilities:

$$P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B)}$$

The components:
- $P(A)$ — **prior**: your belief about $A$ before seeing evidence $B$
- $P(B \mid A)$ — **likelihood**: how probable the evidence is if $A$ is true
- $P(B)$ — **marginal likelihood** (or **evidence**): the total probability of observing $B$
- $P(A \mid B)$ — **posterior**: your updated belief about $A$ after seeing $B$

Using the law of total probability for the denominator:

$$P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B \mid A)P(A) + P(B \mid \neg A)P(\neg A)}$$

The theorem generalizes to continuous distributions, where priors and posteriors become density functions.

## Why It Matters

Bayes' theorem is the mathematically correct way to update beliefs, making it central to quant trading:

- **Signal combination**: When you have multiple alpha signals, Bayesian updating provides a principled framework for combining them. Each new signal updates your posterior estimate of fair value.
- **Market making**: A market maker implicitly performs Bayesian updating — each trade reveals information about whether the counterparty is informed. The posterior estimate of the true price shifts after each fill.
- **Parameter estimation**: Bayesian estimation of model parameters (volatility, drift, mean-reversion speed) incorporates prior knowledge and updates as data arrives. This is especially valuable with limited data, which is the norm in crypto.
- **Prediction markets**: Prediction market prices can be interpreted as posterior probabilities. Price changes reflect Bayesian updates as new information arrives.
- **Regime detection**: $P(\text{regime} \mid \text{recent data})$ — estimating whether the market is in a trending, mean-reverting, or volatile regime is a Bayesian inference problem.
- **Overfitting prevention**: Bayesian priors act as regularizers, penalizing extreme parameter values and reducing overfitting in strategy development.

## Key Equations

$$P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}$$

Continuous form:

$$f(\theta \mid \text{data}) = \frac{f(\text{data} \mid \theta) \, f(\theta)}{f(\text{data})} \propto \text{likelihood} \times \text{prior}$$

**Odds form** (often more intuitive):

$$\frac{P(A \mid B)}{P(\neg A \mid B)} = \frac{P(B \mid A)}{P(B \mid \neg A)} \cdot \frac{P(A)}{P(\neg A)}$$

$$\text{posterior odds} = \text{likelihood ratio} \times \text{prior odds}$$

## Worked Example: Informed-Trader Posterior

A market maker quotes a two-sided book. Suppose 20% of incoming orders come from informed traders ($I$) who know the true price direction; the rest are uninformed. An informed trader buys 80% of the time when fair value is above mid; an uninformed trader buys 50% of the time regardless. We just observed a buy ($B$) at the offer. What is $P(I \mid B)$?

```python
p_I        = 0.20                                     # prior: 20% informed
p_B_given_I = 0.80                                    # informed buys 80% when overvalued
p_B_given_U = 0.50                                    # uninformed: 50/50

p_B = p_B_given_I * p_I + p_B_given_U * (1 - p_I)     # marginal: 0.56
p_I_given_B = (p_B_given_I * p_I) / p_B               # posterior

print(f"P(informed | buy) = {p_I_given_B:.3f}")       # 0.286
```

The posterior jumps from 20% to 28.6%, and the maker should widen the offer or skew the mid down: each buy is mild evidence that fair value sits above the current quote.

The same calculation done one buy at a time *is* the Glosten-Milgrom market-making model. Spread is the maker's compensation for being repeatedly Bayes-updated by informed flow — see [[Adverse Selection]].

## Sequential Updating

Each new observation $B_n$ updates the posterior from the previous round:

```python
def update(prior: float, p_B_given_H: float, p_B_given_not_H: float) -> float:
    num = p_B_given_H * prior
    den = num + p_B_given_not_H * (1 - prior)
    return num / den

posterior = 0.20
for _ in range(5):                                    # five buys in a row
    posterior = update(posterior, 0.80, 0.50)
print(f"P(informed | 5 buys) = {posterior:.3f}")      # 0.724
```

Five consecutive buys drag the posterior from 20% to ~72%. Order flow autocorrelation is informative because of exactly this dynamic.

## Resources

- *Probability Theory: The Logic of Science* by E.T. Jaynes — the Bayesian bible
- *Bayesian Data Analysis* by Gelman et al. — practical Bayesian methods
- *The Signal and the Noise* by Nate Silver — Bayesian thinking applied
- 3Blue1Brown: *Bayes' Theorem* (YouTube)
- **MIT Quant Bible** (MIT Sloan Business Club PDF) §2.1 — Tversky-Kahneman cab problem, the Steve-the-librarian problem, and the "1000 coins / one double-headed / 10 heads in a row" classic. All three drill the base-rate-neglect failure mode that shows up in phone screens.

## Connections

- [[Conditional Probability]] — Bayes' theorem is derived from the definition of conditional probability
- Prediction markets — prices as posterior probabilities
- Bayesian methods — prior/posterior framework for parameter estimation and model selection
