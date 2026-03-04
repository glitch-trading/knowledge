---
type: concept
title: "Liquidity"
tags:
  - concept
  - market-structure
level: 1
prerequisites:
  - "[[Order Book]]"
  - "[[Spread]]"
---

# Liquidity

## What It Is
Liquidity measures how easily an asset can be traded without significantly affecting its price. It has three dimensions:

- **Tightness**: how narrow the [[Spread]] is (cost of a small trade)
- **Depth**: how much volume sits at or near the best bid/ask (capacity before price moves)
- **Resilience**: how quickly the order book recovers after a large trade

A highly liquid market (e.g., S&P 500 futures) has tight spreads, deep order books, and fast recovery. An illiquid market (e.g., small-cap altcoins) has wide spreads, thin books, and slow recovery.

## Why It Matters
Liquidity is both the product that market makers sell and a key constraint on all trading strategies:
- **Market makers provide liquidity**: by posting limit orders on both sides of the book. In return, they earn the spread
- **Liquidity determines trading costs**: low liquidity means high [[Slippage]] and [[Market Impact]], making strategies less profitable
- **Liquidity varies over time**: it dries up during high-volatility events (flash crashes, news), exactly when you most need it
- **Liquidity and strategy capacity**: a highly profitable strategy in an illiquid market may not scale because large orders move the price too much
- In [[Avellaneda-Stoikov]], the fill rate parameter $k$ captures how frequently limit orders are hit — a proxy for how liquid the market is

## Key Equations

There is no single formula for liquidity. Common measures include:

**Bid-ask spread** (tightness): $\text{spread} = p_{\text{ask}} - p_{\text{bid}}$

**Kyle's lambda** (price impact per unit volume): $\Delta p = \lambda \cdot Q$

**Amihud illiquidity ratio**: $\text{ILLIQ} = \frac{|r_t|}{V_t}$ (return per dollar volume)

## Resources
- Kyle, "Continuous Auctions and Insider Trading" (1985)
- Amihud, "Illiquidity and Stock Returns" (2002)
- Harris, *Trading and Exchanges*, Chapter 19

## Connections
- [[Order Book]] — liquidity is determined by the state of the order book
- [[Spread]] — the spread is the most direct measure of liquidity cost
- [[Slippage]] — consequence of insufficient liquidity for your order size
- [[Market Impact]] — how your own trading reduces liquidity for subsequent trades
