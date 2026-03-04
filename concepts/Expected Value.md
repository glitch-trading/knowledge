---
type: concept
title: "Expected Value"
tags:
  - concept
  - probability
level: 1
prerequisites: []
---

# Expected Value

## What It Is

The **expected value** (or **mean**) of a random variable $X$ is the probability-weighted average of all possible outcomes:

- **Discrete**: $E[X] = \sum_x x \cdot P(X = x)$
- **Continuous**: $E[X] = \int_{-\infty}^{\infty} x \, f(x)\,dx$

Key properties:
- **Linearity**: $E[aX + bY] = aE[X] + bE[Y]$ — always holds, regardless of dependence between $X$ and $Y$. This is extremely powerful.
- **Law of the Unconscious Statistician (LOTUS)**: $E[g(X)] = \int g(x) f(x)\,dx$ — you don't need the distribution of $g(X)$, just the distribution of $X$.
- **Conditional expectation**: $E[X \mid Y] = \int x\, f_{X|Y}(x|y)\,dx$ — the expected value of $X$ given information about $Y$.
- **Law of iterated expectations**: $E[E[X \mid Y]] = E[X]$ — averaging conditional expectations over the conditioning variable gives the unconditional mean.

## Why It Matters

Expected value is the central concept in decision-making under uncertainty:

- **Trading edge**: A trade has positive expected value if $E[\text{P\&L}] > 0$. But expected value alone is not sufficient — you also need to consider [[Variance]] and tail risk.
- **Kelly criterion**: The [[Kelly Criterion]] maximizes $E[\ln(W)]$, the expected log wealth. This turns out to maximize long-run geometric growth rate.
- **Risk-neutral pricing**: Option prices are expected values of discounted payoffs under the risk-neutral measure: $V = e^{-rT} E^{\mathbb{Q}}[\text{payoff}]$.
- **Utility theory**: Rational agents maximize $E[U(W)]$, expected utility of wealth. The choice of utility function $U$ encodes risk preferences.
- **Inventory penalties**: In Avellaneda-Stoikov, the market maker's objective involves $E[-e^{-\gamma W_T}]$, the expected exponential utility of terminal wealth.

## Key Equations

$$E[X] = \sum_x x \cdot P(X = x) \quad \text{or} \quad E[X] = \int_{-\infty}^{\infty} x\, f(x)\,dx$$

$$E[aX + bY] = aE[X] + bE[Y]$$

$$\text{Var}(X) = E[X^2] - (E[X])^2$$

$$E[E[X \mid Y]] = E[X]$$

## Resources

- *Probability and Statistics for Engineering and the Sciences* by Jay Devore
- *All of Statistics* by Larry Wasserman — Chapter 3
- *Thinking, Fast and Slow* by Kahneman — expected value vs. human intuition

## Connections

- [[Variance]] — the second central moment, measures dispersion around the mean
- [[Utility Theory]] — rational agents maximize expected utility, not expected wealth
- [[Kelly Criterion]] — maximizes expected logarithmic growth
