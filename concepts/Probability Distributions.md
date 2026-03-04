---
type: concept
title: "Probability Distributions"
tags:
  - concept
  - probability
level: 1
prerequisites: []
---

# Probability Distributions

## What It Is

A **probability distribution** describes how the probability of a random variable is spread across its possible values. There are three key functions:

- **PMF (Probability Mass Function)**: For discrete random variables. $P(X = x)$ gives the probability of each specific outcome.
- **PDF (Probability Density Function)**: For continuous random variables. $f(x)$ gives the density at $x$; probabilities come from integrating: $P(a \le X \le b) = \int_a^b f(x)\,dx$.
- **CDF (Cumulative Distribution Function)**: $F(x) = P(X \le x)$. Works for both discrete and continuous. Monotonically non-decreasing from 0 to 1.

Key relationships:
- For continuous distributions: $F(x) = \int_{-\infty}^{x} f(t)\,dt$ and $f(x) = F'(x)$
- For discrete distributions: $F(x) = \sum_{x_i \le x} P(X = x_i)$

A distribution is fully characterized by either its PMF/PDF, its CDF, or its moment generating function $M(t) = E[e^{tX}]$.

## Why It Matters

Every model in quant finance is built on probability distributions:

- **Return modeling**: Choosing the right distribution for asset returns determines everything — risk estimates, option prices, portfolio weights. The [[Normal Distribution]] is the starting point, but real markets have [[Fat Tails]].
- **Order flow modeling**: The [[Poisson Distribution]] models order arrival counts; the [[Exponential Distribution]] models times between orders. Both are central to market-making models like Avellaneda-Stoikov.
- **Risk management**: VaR and Expected Shortfall are quantiles and tail expectations of the P&L distribution. Getting the tail distribution wrong can be catastrophic.
- **Price modeling**: Asset prices (not returns) tend to follow the [[Log-Normal Distribution]], which ensures prices stay positive.
- **Extreme events**: [[Power Law Distribution]]s capture the heavy tails seen in real market data — large moves happen far more often than a normal distribution predicts.

## Key Equations

$$\text{PMF: } \sum_{x} P(X = x) = 1$$

$$\text{PDF: } \int_{-\infty}^{\infty} f(x)\,dx = 1, \quad f(x) \ge 0$$

$$\text{CDF: } F(x) = P(X \le x)$$

$$E[X] = \int_{-\infty}^{\infty} x\, f(x)\,dx \quad \text{(continuous)}$$

## Resources

- *Probability and Statistics for Engineering and the Sciences* by Jay Devore
- *All of Statistics* by Larry Wasserman — concise and rigorous
- Khan Academy: Random Variables and Distributions

## Connections

- [[Normal Distribution]] — the most common continuous distribution, foundation of classical finance
- [[Log-Normal Distribution]] — models asset prices (positive support)
- [[Exponential Distribution]] — models inter-arrival times
- [[Poisson Distribution]] — models event counts in fixed intervals
- [[Power Law Distribution]] — models heavy-tailed phenomena like large trades and crashes
