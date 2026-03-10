---
type: book
title: "Algorithmic Trading: Winning Strategies and Their Rationale"
author: Ernie Chan
status: unread
tags:
  - book
  - stat-arb
  - backtesting
level: 3
topics:
  - "[[Cointegration]]"
  - "[[Statistical Arbitrage]]"
  - "[[Overfitting]]"
---

**The best practical backtesting guide with code. Code-first approach to stat arb.**

## Why Read This
Bridges theory and practice. Covers cointegration strategies, backtesting pitfalls, and practical implementation. The antidote to theory-only learning.

## Key Takeaways

- **Mean reversion is the practical edge.** Most retail-accessible alpha comes from mean-reverting relationships — cointegrated pairs, cross-venue spreads, funding rate convergence. Momentum strategies require faster infrastructure and more capital.
- **Cointegration, not correlation.** Two assets can be highly correlated but not cointegrated (both trend up together). Cointegration means the *spread* is mean-reverting even if individual prices are random walks. Test with Augmented Dickey-Fuller or Johansen.
- **Transaction costs kill paper profits.** The #1 reason backtested strategies fail live. Model realistic fees, slippage, market impact, and funding costs. If the edge is < 2x transaction costs, it's probably not real.
- **Backtest with paranoia.** Survivorship bias (only testing assets that still exist), lookahead bias (accidentally using future data), and overfitting (curve-fitting historical noise) are the three graveyard gates. Walk-forward testing is non-negotiable.
- **Kelly sizing in practice.** Full Kelly is too aggressive for noisy edge estimates. Use half-Kelly or quarter-Kelly. The cost of under-betting is linear (lower returns), but the cost of over-betting is catastrophic (ruin).


## Connections
- Pairs with [[Introduction to Statistical Learning (ISLR)]] for ML foundations
- Practical application of [[Cointegration]] and [[Time Series Analysis]]
