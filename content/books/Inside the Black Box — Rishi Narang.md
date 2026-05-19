---
type: book
title: "Inside the Black Box"
author: Rishi K. Narang
status: unread
tags:
  - book
  - industry
  - quant-strategies
level:
topics: []
---

**Plain-English guided tour of how systematic and quantitative funds are actually built.**

## Why Read This

Most quant introductions are textbooks (math-first) or memoirs (people-first). Narang sits between the two: a working practitioner walking through the moving parts of a real quant fund — alpha models, risk models, transaction-cost models, portfolio construction, execution, infrastructure — without equations. Good as a structural map before you dive into [[Stochastic Calculus for Finance II — Steven Shreve]] or [[Algorithmic Trading — Ernie Chan]].

## Key Takeaways

- A quant fund is not "the model" — it's a stack: alpha model + risk model + transaction-cost model + portfolio construction + execution. Each layer can destroy the layer above it.
- Alpha sources are usually a small menu: trend, reversion, value, carry, quality, behavioral. The interesting variation is in implementation, not invention.
- The hard problems are often not in the alpha but in the [[Portfolio Optimization]] and execution layers — sizing, [[Market Impact]], capacity, leverage.
- HFT and statistical arbitrage and global macro look totally different from the outside but share the same architecture under the hood.
- [[Overfitting]] is the industry's universal failure mode and most public "edge" claims do not survive realistic transaction costs.

## Connections

- [[The Quants — Scott Patterson]] — Same era, narrative angle instead of structural
- [[The Man Who Solved the Market — Gregory Zuckerman]] — Specific case study (Renaissance) of what Narang generalizes
- [[Statistical Arbitrage]] — The strategy family Narang spends the most time on
