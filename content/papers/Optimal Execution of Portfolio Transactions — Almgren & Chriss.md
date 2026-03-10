---
type: paper
title: "Optimal Execution of Portfolio Transactions"
authors: "Robert Almgren & Neil Chriss"
year: 2000
status: not-started
tags:
  - paper
  - execution
  - market-impact
level: 6
topics:
  - "[[Market Impact]]"
  - "[[TWAP]]"
  - "[[VWAP]]"
---

## Key Takeaways

- Trading creates both temporary impact (transient price displacement) and permanent impact (information content shifts equilibrium)
- Optimal execution is a tradeoff: trade fast to reduce timing risk vs trade slow to reduce market impact
- The efficient frontier of execution: expected cost vs variance of cost, parameterized by risk aversion
- Square-root law: impact scales as √(order_size / daily_volume), not linearly

## What It Covers

The standard model for optimal trade execution. Decomposes market impact into permanent and temporary components, formulates execution as a mean-variance optimization, and derives closed-form optimal trading trajectories. The model produces TWAP-like strategies modified by risk aversion and impact estimates.

## Resources

- [[Algorithmic and High-Frequency Trading — Cartea et al.]] — Extends this to continuous-time settings
- [[Level 6 — Advanced Topics]] — Advanced market microstructure section
