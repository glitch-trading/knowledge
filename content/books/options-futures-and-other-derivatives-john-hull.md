---
type: book
title: "Options, Futures, and Other Derivatives"
author: John C. Hull
status: unread
tags:
  - book
  - derivatives
  - options
level: 2, 4
topics:
  - "[[geometric-brownian-motion|Geometric Brownian Motion]]"
  - "[[itos-lemma|Itô's Lemma]]"
  - "[[black-scholes-equation|Black-Scholes Equation]]"
  - "[[greeks|Greeks]]"
  - "[[implied-volatility|Implied Volatility]]"
---

**The standard derivatives textbook. Covers Black-Scholes, Greeks, and pricing from first principles.**

## Why Read This

Even if you're not trading options directly, derivatives theory permeates quantitative finance. LP positions on AMMs are economically equivalent to selling options (short gamma). Delta hedging, the Greeks, and implied volatility are the language of risk. Hull's treatment is the clearest path from basic concepts to the Black-Scholes framework and beyond.

The Greeks chapter is essential for understanding how to decompose and manage exposure — Delta (directional), Gamma (convexity), Theta (time decay), Vega (vol sensitivity).

## Key Takeaways

- **[[black-scholes-equation|Black-Scholes derivation]].** Delta hedging argument → riskless portfolio → PDE → closed-form solution. Understand the logic, not just the formula.
- **The [[greeks|Greeks]].** Delta, Gamma, Theta, Vega, Rho — each quantifies a different dimension of option risk. Taylor expansion connects them: `dV ≈ Δ·dS + ½Γ·(dS)² + Θ·dt`.
- **[[implied-volatility|Implied Volatility]].** The market's consensus forecast of future volatility, backed out from option prices. The vol smile/skew tells you about tail risk expectations.
- **Risk-neutral pricing.** Price derivatives by taking expectations under the risk-neutral measure, not the real-world measure. This is the theoretical foundation.
- **[[put-call-parity|Put-Call Parity]].** Model-free no-arbitrage identity between call and put on the same strike — the universal sanity check.


## Connections

- [[black-scholes-equation|Black-Scholes Equation]] — The PDE this book derives and applies
- [[greeks|Greeks]] — Standalone treatment of the Greeks
- [[implied-volatility|Implied Volatility]] — The vol surface chapter
- [[put-call-parity|Put-Call Parity]] — Model-free identity used throughout
- [[itos-lemma|Itô's Lemma]] — The mathematical tool behind Black-Scholes
- [[level-4-mev-and-algorithmic-trading|Level 4 — MEV & Algorithmic Trading]] — Greeks section
- [[impermanent-loss|Impermanent Loss]] — LP as short gamma connects to options theory
