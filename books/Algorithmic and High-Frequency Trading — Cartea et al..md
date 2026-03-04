---
type: book
title: "Algorithmic and High-Frequency Trading"
author: "Alvaro Cartea, Sebastian Jaimungal, José Penalva"
status: unread
tags:
  - book
  - market-making
  - optimal-execution
level: 3-6
topics:
  - "[[Avellaneda-Stoikov]]"
  - "[[Market Impact]]"
  - "[[HJB Equation]]"
  - "[[TWAP]]"
  - "[[VWAP]]"
---

# Algorithmic and High-Frequency Trading — Cartea et al.

**Extends Avellaneda-Stoikov. Covers optimal control for market making and execution.**

## Why Read This
Takes the [[Avellaneda-Stoikov]] framework and extends it significantly. Covers optimal execution algorithms, market impact modeling, and advanced market making. The academic reference for algorithmic trading.

## Key Takeaways

- **Avellaneda-Stoikov is the starting point, not the endpoint.** This book extends the A-S framework to handle multiple assets, ambiguity aversion, adverse selection, and optimal execution — the realistic complications that the original paper simplified away.
- **Optimal execution minimizes implementation shortfall.** The gap between the decision price and the actual execution price is the true cost of trading. Almgren-Chriss and extensions balance urgency (risk of price drift) against patience (market impact).
- **Market impact has temporary and permanent components.** Temporary impact reverts after your trade; permanent impact shifts the equilibrium (your trade contained information). Modeling both correctly is critical for sizing.
- **HJB equations are the universal tool.** Every optimal control problem in this book — market making, execution, inventory management — reduces to an HJB PDE. The ansatz trick (guess the solution form) makes these tractable.
- **Inventory management is the core trade-off.** Aggressive quoting earns more spread but accumulates inventory risk. The optimal strategy always skews quotes away from accumulated inventory — exactly the A-S reservation price adjustment.


## Connections
- Direct extension of [[Avellaneda-Stoikov]]
- Covers [[TWAP]], [[VWAP]], [[Market Impact]] in depth
