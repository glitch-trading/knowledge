---
type: concept
title: "Spatial Arbitrage"
tags:
  - concept
  - strategies
  - arbitrage
level: 2
prerequisites: []
---

# Spatial Arbitrage

## What It Is

Spatial arbitrage exploits price differences for the same asset across different venues. Buy low on exchange A, sell high on exchange B, pocket the spread. The simplest form of arbitrage — conceptually trivial, operationally demanding.

**Example:** BTC is $60,000 on Binance and $60,150 on Coinbase. Buy on Binance, sell on Coinbase, earn $150 minus fees and transfer costs.

**Two execution modes:**
- **Transfer-based**: Actually move the asset between exchanges. Slow (depends on block confirmations), exposes you to price risk during transfer.
- **Pre-positioned inventory**: Hold balances on both exchanges. Execute simultaneously. No transfer delay, but requires capital on each venue. This is how most real spatial arb works.

## Why It Matters

Spatial arbitrage is the simplest edge to understand but one of the hardest to profit from sustainably:

- **Latency-sensitive**: By the time you see the spread, so has everyone else. Winning requires faster data feeds, faster execution, and colocation.
- **Highly competitive**: This is the most crowded arbitrage. Spreads are typically pennies and shrinking.
- **Fee-dominated**: After maker/taker fees, withdrawal fees, and spread costs, many apparent opportunities are negative EV.
- **Capital-intensive**: Pre-positioning inventory on N exchanges requires N times the capital.
- **Still educational**: Understanding spatial arb builds intuition for all other arbitrage types. If you can't reason about simple price discrepancies, you won't reason about complex ones.

## Resources

- Start with CEX pairs (e.g., BTC/USDT across exchanges)
- Monitor via websocket feeds for real-time spreads
- Account for all costs: taker fee both sides, withdrawal fee, slippage

## Connections

- [[CEX-DEX Arbitrage]] — Spatial arb extended to on-chain/off-chain venue pairs
- [[Statistical Arbitrage]] — When spatial arb becomes probabilistic rather than deterministic
