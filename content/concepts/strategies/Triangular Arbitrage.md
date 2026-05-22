---
type: concept
title: "Triangular Arbitrage"
tags:
  - concept
  - strategies
  - arbitrage
level: 2
prerequisites: []
---

## What It Is

Triangular arbitrage exploits cross-rate inconsistencies within a single exchange. You cycle through three (or more) trading pairs — A to B to C back to A — and end up with more A than you started with.

**Example:** On one exchange:
- BTC/USDT = 60,000
- ETH/BTC = 0.05
- ETH/USDT = 3,100

Implied ETH/USDT via BTC: 60,000 x 0.05 = 3,000. But the direct ETH/USDT market quotes 3,100. So: buy ETH via BTC (pay $3,000 equivalent), sell ETH for USDT directly ($3,100). Profit = $100 per ETH, minus fees.

**The arbitrage condition:**
$$\frac{P_{A/B} \cdot P_{B/C}}{P_{A/C}} \neq 1$$

If this ratio deviates from 1 by more than the round-trip fee, there's an opportunity.

## Why It Matters

- **Math-heavy**: Requires real-time monitoring of all pair combinations. For $n$ assets, there are $O(n^3)$ triangular paths to check (or more for longer cycles).
- **Highly competitive**: Exchanges and other arbers correct these discrepancies in milliseconds. Speed and co-location matter.
- **Low risk per trade**: All legs execute on the same exchange, so no transfer or counterparty risk. But fees eat most of the edge.
- **Good training ground**: Builds intuition for multi-leg execution, fee modeling, and order book depth analysis.
- **Extends to N-gons**: The principle generalizes beyond triangles. A→B→C→D→A (quadrangular) and longer cycles can sometimes capture opportunities that triangles miss.

## Key Equations

**Profit condition (three pairs):**
$$\prod_{i=1}^{3} (1 - f_i) \cdot \prod_{i=1}^{3} r_i > 1$$

Where $f_i$ = fee on leg $i$ and $r_i$ = exchange rate on leg $i$.

## Resources

- Implement with exchange websocket APIs for real-time orderbook data
- Bellman-Ford algorithm can detect negative cycles (= arb opportunities) in the exchange rate graph

## Connections

- [[Spatial Arbitrage]] — Single-asset, multi-venue; triangular is multi-asset, single-venue
