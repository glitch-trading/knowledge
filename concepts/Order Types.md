---
type: concept
title: "Order Types"
tags:
  - concept
  - market-structure
level: 1
prerequisites: []
---

# Order Types

## What It Is
Orders are instructions to buy or sell an asset. The two fundamental types are:

- **Market order**: Execute immediately at the best available price. You get certainty of execution but uncertainty of price. Market orders *consume* liquidity from the order book.
- **Limit order**: Execute only at a specified price or better. You get certainty of price but uncertainty of execution — your order may never fill. Limit orders *provide* liquidity to the order book.

Other common types include stop orders (trigger a market order when price reaches a level), stop-limit orders (trigger a limit order), and iceberg orders (hide the full size).

## Why It Matters
The market order vs. limit order distinction is foundational to understanding market making and trading costs:
- **Market makers** use limit orders to provide liquidity and earn the spread
- **Aggressive traders** use market orders, paying the spread as a cost
- In [[Avellaneda-Stoikov]], the market maker posts limit orders at distances $\delta^a$ and $\delta^b$ from the [[Reservation Price]]
- The probability of a limit order being filled depends on how far it is from the current price — this is the fill-rate function in Avellaneda-Stoikov
- [[Slippage]] occurs when market orders are large enough to consume multiple price levels

## Key Equations
Not applicable — order types are definitional rather than mathematical.

## Resources
- Harris, *Trading and Exchanges*, Chapters 4-5
- Any exchange documentation (e.g., CME, Binance, NYSE)

## Connections
- [[Order Book]] — the data structure where limit orders reside
- [[Market Making]] — market makers operate primarily through limit orders
- [[Slippage]] — caused by market orders consuming depth from the order book
