---
type: concept
title: "Poisson Distribution"
tags:
  - concept
  - probability
  - distributions
level: 1
prerequisites: []
---

## What It Is

The **Poisson distribution** models the number of events occurring in a fixed interval of time (or space), when events happen independently at a constant average rate. If $X \sim \text{Poisson}(\lambda)$:

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots$$

Key properties:
- **Mean**: $E[X] = \lambda$
- **Variance**: $\text{Var}(X) = \lambda$ — mean equals variance (this is a defining characteristic)
- **Additivity**: If $X \sim \text{Poisson}(\lambda_1)$ and $Y \sim \text{Poisson}(\lambda_2)$ are independent, then $X + Y \sim \text{Poisson}(\lambda_1 + \lambda_2)$
- Arises as a limit of the Binomial distribution when $n \to \infty$, $p \to 0$, and $np = \lambda$
- The Poisson distribution is the discrete counterpart of the [[Exponential Distribution]]: Poisson counts events, exponential measures gaps

## Why It Matters

The Poisson distribution is central to modeling order flow and trade arrivals:

- **Order arrival modeling**: In the Avellaneda-Stoikov framework, the number of buy/sell orders arriving in a time interval is modeled as Poisson with rate $\Lambda(\delta) = A e^{-k\delta}$, where $\delta$ is the distance from mid-price. This is the core assumption that makes the model tractable.
- **Trade counting**: The number of trades in a 1-second window, the number of cancellations per minute — these are naturally modeled as Poisson counts.
- **Overdispersion in practice**: Real order flow is often **overdispersed** (variance > mean), violating the Poisson assumption. This is because order arrival rates are not truly constant — they vary with volatility, time of day, and market events. More sophisticated models use inhomogeneous Poisson processes or Hawkes processes.
- **Rare event modeling**: The Poisson distribution also models rare events: number of flash crashes per year, number of extreme moves per month.
- **Mean-variance relationship**: The Poisson property $\text{Var} = \text{Mean}$ provides a quick diagnostic: if your event count data has variance much larger than the mean, a simple Poisson model is inadequate.

## Key Equations

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

$$E[X] = \text{Var}(X) = \lambda$$

Avellaneda-Stoikov fill intensity:

$$\Lambda(\delta) = A e^{-k\delta}$$

where $A$ is the baseline arrival rate and $k$ is the decay parameter.

## Resources

- *Introduction to Probability Models* by Sheldon Ross — Chapter 5
- *All of Statistics* by Larry Wasserman
- Avellaneda & Stoikov (2008) — Poisson arrival assumption for limit order fills

## Connections

- [[Poisson Process]] — the underlying process that generates Poisson-distributed counts
- [[Exponential Distribution]] — inter-arrival times between Poisson events
- [[Avellaneda-Stoikov]] — Poisson order arrivals are a core modeling assumption
