---
type: concept
title: "Exponential Distribution"
tags:
  - concept
  - probability
  - distributions
level: 1
prerequisites: []
---

# Exponential Distribution

## What It Is

The **exponential distribution** models the time between events in a process where events occur continuously and independently at a constant average rate. If $X \sim \text{Exp}(\lambda)$:

$$f(x) = \lambda e^{-\lambda x}, \quad x \ge 0$$

$$F(x) = 1 - e^{-\lambda x}$$

Key properties:
- **Mean**: $E[X] = 1/\lambda$ — average waiting time is the reciprocal of the rate
- **Variance**: $\text{Var}(X) = 1/\lambda^2$
- **Memoryless property**: $P(X > s + t \mid X > s) = P(X > t)$. Given that you've already waited $s$ time units, the remaining waiting time has the same distribution as if you just started. The exponential distribution is the **only** continuous distribution with this property.
- **Minimum of exponentials**: If $X_1 \sim \text{Exp}(\lambda_1)$ and $X_2 \sim \text{Exp}(\lambda_2)$ are independent, then $\min(X_1, X_2) \sim \text{Exp}(\lambda_1 + \lambda_2)$. Rates add.

## Why It Matters

The exponential distribution is the natural model for timing in quant trading:

- **Inter-arrival times**: In the [[Poisson Process]], the time between consecutive events is exponentially distributed. If orders arrive at rate $\lambda$ per second, the time to the next order is $\text{Exp}(\lambda)$.
- **Avellaneda-Stoikov order fill model**: The probability of a limit order being filled within time $\Delta t$ is modeled using exponential inter-arrival times. The fill intensity $\Lambda(\delta) = A e^{-k\delta}$ gives the rate at which orders arrive that would fill a quote placed at distance $\delta$ from the mid-price.
- **Memoryless property in trading**: The memoryless property means "the market doesn't remember how long you've been waiting." This simplifies dynamic programming formulations because the optimal strategy doesn't depend on elapsed time since the last event.
- **Queue models**: Time in queue at an exchange's matching engine, time to execution — exponential distributions appear throughout market microstructure.
- **Hazard rate**: The exponential has constant hazard rate $\lambda$, meaning the instantaneous probability of the event occurring doesn't change over time.

## Key Equations

$$f(x) = \lambda e^{-\lambda x}, \quad x \ge 0$$

$$P(X > t) = e^{-\lambda t}$$

$$E[X] = \frac{1}{\lambda}, \quad \text{Var}(X) = \frac{1}{\lambda^2}$$

$$P(X > s + t \mid X > s) = P(X > t) = e^{-\lambda t}$$

## Resources

- *Introduction to Probability Models* by Sheldon Ross — Chapter 5
- *All of Statistics* by Larry Wasserman
- *Probability and Random Processes* by Grimmett & Stirzaker

## Connections

- [[Poisson Process]] — exponential inter-arrival times define a Poisson process
- [[Poisson Distribution]] — the Poisson distribution counts events; the exponential models the gaps between them
