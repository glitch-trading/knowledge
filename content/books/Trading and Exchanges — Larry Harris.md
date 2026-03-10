---
type: book
title: "Trading and Exchanges: Market Microstructure for Practitioners"
author: Larry Harris
status: unread
tags:
  - book
  - market-structure
level: 1
topics:
  - "[[Order Book]]"
  - "[[Order Types]]"
  - "[[Market Making]]"
  - "[[Spread]]"
  - "[[Liquidity]]"
---

**THE book for market structure from scratch.**

## Why Read This
Foundation for understanding how all markets work — order types, order books, market making, adverse selection, spread economics. Required before touching the [[Avellaneda-Stoikov]] paper.

## Reading Plan
- **Chapters 1-6:** How markets work (order types, order book, trade mechanics, depth, liquidity)
- **Chapters 7-13:** Market making (what a market maker does, inventory risk, adverse selection, spread as compensation)

## Key Takeaways

- **Market orders demand liquidity; limit orders supply it.** This distinction is the foundation of market microstructure. Market makers (liquidity suppliers) earn the spread; market order traders (liquidity demanders) pay it. Every strategy you build is on one side or the other.
- **The spread compensates for three costs.** Order processing costs (infrastructure), inventory holding costs (risk of adverse price moves while holding), and adverse selection costs (trading against informed counterparties). The last one dominates in practice.
- **Adverse selection is the market maker's enemy.** When informed traders hit your quotes, you systematically lose. The spread must be wide enough to cover losses from informed flow while remaining competitive enough to attract uninformed flow.
- **Liquidity is not a number — it's a function.** It depends on time, order size, urgency, and market conditions. The order book shows depth at each price level, but this depth evaporates in a crisis exactly when you need it most.
- **Order types are tools with trade-offs.** Market orders guarantee execution, not price. Limit orders guarantee price, not execution. Stop orders are triggers. Understanding these mechanics is prerequisite to everything else.


## Connections
- Prerequisite for [[Avellaneda-Stoikov]]
- Concepts used throughout [[Market Structure MOC]]
