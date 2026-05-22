---
type: book
title: "Continuous-time Stochastic Control and Optimization with Financial Applications"
author: "Huyên Pham"
status: not-started
tags:
  - book
  - optimization
  - stochastic-control
level: 2
topics:
  - "[[dynamic-programming|Dynamic Programming]]"
  - "[[hjb-equation|HJB Equation]]"
  - "[[stochastic-differential-equations|Stochastic Differential Equations]]"
---

## Key Takeaways

- The HJB equation is the continuous-time analogue of the Bellman equation — both express optimality as a recursive condition
- Viscosity solutions handle cases where classical solutions don't exist (common in finance)
- Verification theorems connect candidate solutions back to true optimality — essential for proving the Avellaneda-Stoikov result is actually optimal
- Singular and impulse control handle transaction costs and discrete trading decisions

## What It Covers

Chapters 1-3: stochastic calculus review, dynamic programming principle, HJB equations and verification theorems. The mathematical machinery behind optimal control problems like the [[avellaneda-stoikov|Avellaneda-Stoikov]] market making model. More rigorous than Cartea et al. on the control theory side.

## Resources

- [[convex-optimization-boyd-and-vandenberghe|Convex Optimization — Boyd & Vandenberghe]] — Optimization foundations
- [[algorithmic-and-high-frequency-trading-cartea-et-al|Algorithmic and High-Frequency Trading — Cartea et al.]] — Applied control theory for trading
- [[level-2-basic-probabilistic-arbitrage|Level 2 — Basic Probabilistic Arbitrage]] — HJB and optimization section
