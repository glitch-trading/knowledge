---
type: book
title: "Trades, Quotes and Prices: Financial Markets Under the Microscope"
author: "Jean-Philippe Bouchaud, Julius Bonart, Jonathan Donier, Martin Gould"
status: unread
tags:
  - book
  - microstructure
level: 6
topics:
  - "[[Market Impact]]"
  - "[[Order Book]]"
---

**The best book on empirical market microstructure.**

## Why Read This
Data-driven approach to understanding how markets actually work at the microscopic level. Covers order flow, market impact, and high-frequency patterns with real data.

## Key Takeaways

- **Market impact follows a square-root law.** Price impact scales as `√(Q/V)` where Q is order size and V is daily volume. This is empirically robust across markets and time periods — and it means large orders are disproportionately expensive.
- **Order flow is predictive.** The imbalance between buy and sell market orders predicts short-term price movements. Toxic flow (informed traders) moves prices permanently; noise flow reverts.
- **The order book is a queue, not a snapshot.** Understanding order book dynamics — placement, cancellation, and execution rates at each price level — reveals more than static depth. Most of the visible book is noise; the flow tells the story.
- **Volatility clustering is universal.** Big moves follow big moves (GARCH effects). This is not a model assumption — it's an empirical fact across all liquid markets. Auto-correlation of absolute returns decays slowly (long memory).
- **Price formation is a feedback loop.** Trades impact prices, which affect order placement, which affects future trades. Models that treat these as independent miss the core mechanism.

