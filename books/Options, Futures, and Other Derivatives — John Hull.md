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
  - "[[Geometric Brownian Motion]]"
  - "[[Itô's Lemma]]"
---

# Options, Futures, and Other Derivatives — John Hull

**The standard derivatives textbook. Covers Black-Scholes, Greeks, and pricing from first principles.**

## Why Read This

Even if you're not trading options directly, derivatives theory permeates quantitative finance. LP positions on AMMs are economically equivalent to selling options (short gamma). Delta hedging, the Greeks, and implied volatility are the language of risk. Hull's treatment is the clearest path from basic concepts to the Black-Scholes framework and beyond.

The Greeks chapter is essential for understanding how to decompose and manage exposure — Delta (directional), Gamma (convexity), Theta (time decay), Vega (vol sensitivity).

## Key Takeaways

- **Black-Scholes derivation.** Delta hedging argument → riskless portfolio → PDE → closed-form solution. Understand the logic, not just the formula.
- **The Greeks.** Delta, Gamma, Theta, Vega, Rho — each quantifies a different dimension of option risk. Taylor expansion connects them: `dV ≈ Δ·dS + ½Γ·(dS)² + Θ·dt`.
- **Implied volatility.** The market's consensus forecast of future volatility, backed out from option prices. The vol smile/skew tells you about tail risk expectations.
- **Risk-neutral pricing.** Price derivatives by taking expectations under the risk-neutral measure, not the real-world measure. This is the theoretical foundation.


## Connections

- [[Itô's Lemma]] — The mathematical tool behind Black-Scholes
- [[Level 4 — MEV & Algorithmic Trading]] — Greeks section
- [[Impermanent Loss]] — LP as short gamma connects to options theory
