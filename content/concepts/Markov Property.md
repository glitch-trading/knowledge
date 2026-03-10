---
type: concept
title: "Markov Property"
tags:
  - concept
  - probability
  - stochastic-processes
level: 1
prerequisites: []
---

## What It Is

A stochastic process $\{X_t\}$ has the **Markov property** if the future state depends only on the present state, not on the history of how it got there:

$$P(X_{t+1} = x \mid X_t, X_{t-1}, \ldots, X_0) = P(X_{t+1} = x \mid X_t)$$

In words: given the present, the future is independent of the past. The process is **memoryless** — all relevant information is encoded in the current state.

Key concepts:
- **Markov chain**: A discrete-time, discrete-state Markov process. Defined by a transition matrix $P_{ij} = P(X_{t+1} = j \mid X_t = i)$.
- **Continuous-time Markov process**: States can change at any time; defined by transition rates rather than probabilities.
- **State space**: Can be discrete (Markov chain) or continuous (e.g., Brownian motion).
- **Strong Markov property**: The Markov property holds not just at fixed times but also at random stopping times. Brownian motion satisfies this.
- **Non-Markov processes**: Processes with memory (e.g., fractional Brownian motion, GARCH) require the full history. These can sometimes be made Markov by expanding the state space.

## Why It Matters

The Markov property is a simplifying assumption that makes most financial models tractable:

- **Dynamic programming**: The [[Dynamic Programming]] approach (Bellman equation) requires the Markov property. The optimal strategy at time $t$ depends only on the current state $(S_t, q_t, t)$, not the history. The Avellaneda-Stoikov HJB equation is built on this assumption.
- **Brownian motion is Markov**: $W_t$ given $W_s$ (for $s < t$) depends only on $W_s$, not on the path before $s$. This makes Itô calculus and PDE-based option pricing possible.
- **Order book models**: Many market microstructure models treat the order book state as Markov — the current bid/ask/depth is all you need to predict short-term dynamics.
- **When it fails**: Real markets have memory effects:
  - **Momentum**: Past returns predict future returns (violates Markov at the price level)
  - **Volatility clustering**: GARCH, stochastic volatility — volatility has memory
  - **Order flow autocorrelation**: Trades are not independent; large orders are split and arrive in clusters
  - The fix is usually to expand the state space (include past returns, volatility estimates, inventory, etc.) until the augmented process is approximately Markov.
- **Model tractability vs. realism**: The Markov assumption is almost always wrong in detail but often approximately right for the relevant time scale. It's a controlled simplification that enables analytical and computational solutions.

## Key Equations

$$P(X_{t+1} \mid X_t, X_{t-1}, \ldots, X_0) = P(X_{t+1} \mid X_t)$$

Transition matrix (discrete):

$$\mathbf{P} = [P_{ij}], \quad P_{ij} = P(X_{t+1} = j \mid X_t = i), \quad \sum_j P_{ij} = 1$$

Chapman-Kolmogorov equation:

$$P_{ij}^{(n+m)} = \sum_k P_{ik}^{(n)} P_{kj}^{(m)}$$

## Resources

- *Introduction to Probability Models* by Sheldon Ross — Chapter 4 on Markov Chains
- *Stochastic Calculus for Finance I* by Shreve — Markov property in discrete models
- *Markov Chains and Mixing Times* by Levin, Peres & Wilmer — deeper theory

## Connections

- [[Random Walk]] — the simplest Markov process
- [[Brownian Motion]] — a continuous-state, continuous-time Markov process
- [[Dynamic Programming]] — requires the Markov property to define value functions
