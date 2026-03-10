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

## Resources

- *Probability Theory: The Logic of Science* by E.T. Jaynes — the Bayesian bible
- *Bayesian Data Analysis* by Gelman et al. — practical Bayesian methods
- *The Signal and the Noise* by Nate Silver — Bayesian thinking applied
- 3Blue1Brown: *Bayes' Theorem* (YouTube)

## Connections

- [[Conditional Probability]] — Bayes' theorem is derived from the definition of conditional probability
- Prediction markets — prices as posterior probabilities
- Bayesian methods — prior/posterior framework for parameter estimation and model selection
