---
type: concept
title: "Poisson Process"
tags:
  - concept
  - probability
  - stochastic-processes
level: 1-2
prerequisites: []
---

# Poisson Process

## What It Is

A **Poisson process** is a continuous-time stochastic process that counts the number of events occurring over time, where events happen independently at a constant average rate $\lambda$. A counting process $\{N(t), t \ge 0\}$ is a Poisson process with rate $\lambda$ if:

1. $N(0) = 0$
2. The process has **independent increments**: the numbers of events in non-overlapping intervals are independent
3. The number of events in any interval of length $t$ follows a Poisson distribution: $N(t+s) - N(s) \sim \text{Poisson}(\lambda t)$

Equivalently, a Poisson process is defined by its inter-arrival times being i.i.d. exponential: $T_i \sim \text{Exp}(\lambda)$.

Key properties:
- **Event counts**: $E[N(t)] = \lambda t$, $\text{Var}(N(t)) = \lambda t$
- **Inter-arrival times**: $T_i \sim \text{Exp}(\lambda)$, independent of each other
- **Merging**: Two independent Poisson processes with rates $\lambda_1, \lambda_2$ merge into one with rate $\lambda_1 + \lambda_2$
- **Thinning**: Each event independently kept with probability $p$ gives a Poisson process with rate $p\lambda$
- **Conditional arrival times**: Given $N(t) = n$, the $n$ event times are uniformly distributed on $[0, t]$

**Inhomogeneous (non-homogeneous) Poisson process**: The rate $\lambda(t)$ varies over time. The number of events in $[s, t]$ is Poisson with mean $\int_s^t \lambda(u)\,du$.

## Why It Matters

The Poisson process is the standard model for event arrivals in market microstructure:

- **Avellaneda-Stoikov core assumption**: The A-S model assumes that buy and sell market orders arrive according to independent Poisson processes. The key innovation is that the arrival rate depends on the market maker's quote distance from the mid-price: $\Lambda(\delta) = A e^{-k\delta}$. This is an inhomogeneous Poisson process where the rate is controlled by the market maker's quoting strategy.
- **Limit order fills**: The probability that a limit order at distance $\delta$ from mid is filled in a small time interval $dt$ is approximately $\Lambda(\delta)\,dt$. The probability of being filled before time $T$ is $1 - e^{-\Lambda(\delta)(T-t)}$.
- **Trade arrival modeling**: The simplest model for trade arrivals at an exchange. In reality, trade arrivals exhibit clustering (bursts of activity) that a homogeneous Poisson process cannot capture — this motivates Hawkes processes.
- **Thinning for order types**: You can model buy and sell arrivals as thinned versions of a total order arrival process. Each arriving order is independently a buy with probability $p$ or a sell with probability $1-p$.
- **Inventory dynamics**: Under Poisson fill assumptions, the market maker's inventory $q_t$ is a continuous-time Markov chain that jumps by $+1$ (buy fill) or $-1$ (sell fill) at rates determined by the bid/ask distances.

## Key Equations

$$N(t) \sim \text{Poisson}(\lambda t)$$

$$P(N(t) = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}$$

Inter-arrival time: $T_i \sim \text{Exp}(\lambda)$, so $P(T_i > t) = e^{-\lambda t}$

Avellaneda-Stoikov fill intensity:

$$\Lambda(\delta) = A e^{-k\delta}$$

Probability of fill by time $T$:

$$P(\text{fill before } T) = 1 - \exp\!\left(-\int_t^T \Lambda(\delta(s))\,ds\right)$$

## Resources

- *Introduction to Probability Models* by Sheldon Ross — Chapter 5 (the standard reference)
- *Stochastic Processes* by Sheldon Ross — more depth
- Avellaneda & Stoikov (2008) — application to market making
- *Probability and Random Processes* by Grimmett & Stirzaker — Chapter 6

## Connections

- [[Poisson Distribution]] — the distribution of counts in any interval
- [[Exponential Distribution]] — the distribution of inter-arrival times
- [[Avellaneda-Stoikov]] — Poisson order arrivals are the core modeling assumption
