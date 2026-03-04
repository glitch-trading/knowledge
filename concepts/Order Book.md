---
type: concept
title: "Order Book"
tags:
  - concept
  - market-structure
level: 1
prerequisites: []
---

# Order Book

## What It Is
The order book (also called the limit order book or LOB) is a real-time, sorted list of all outstanding limit orders for a given asset. It has two sides:

- **Bid side**: buy limit orders, sorted highest to lowest. The top (highest) bid is the best price someone is willing to pay.
- **Ask side**: sell limit orders, sorted lowest to highest. The top (lowest) ask is the best price someone is willing to sell at.

**Depth** refers to the quantity of orders at each price level. A "deep" book has large quantities near the best bid/ask, meaning large trades can execute without moving the price much.

The order book is the mechanism through which price discovery occurs in most modern electronic markets.

## Why It Matters
The order book is the environment in which market makers operate:
- The [[Spread]] (best ask minus best bid) is directly observable from the order book
- [[Market Making]] involves placing limit orders on both sides of the book
- Order book depth determines [[Liquidity]] — how much you can trade without moving the price
- In [[Avellaneda-Stoikov]], the market maker's limit orders sit in the order book at distances $\delta^a$ and $\delta^b$ from the midprice
- The fill probability of limit orders depends on order flow, which interacts with order book dynamics
- Real-world market making requires modeling the order book's microstructure (queue position, cancellations, hidden orders)

## Key Equations
Not applicable — the order book is a data structure rather than a mathematical formula. However, the **midprice** is defined from the order book:

$$s = \frac{p_{\text{best bid}} + p_{\text{best ask}}}{2}$$

This midprice $s$ is the starting point for all calculations in Avellaneda-Stoikov.

## Resources
- Harris, *Trading and Exchanges*, Chapters 4-6
- Gould et al., "Limit Order Books" (2013) — survey paper

## Connections
- [[Order Types]] — market orders consume from the book; limit orders add to it
- [[Spread]] — the gap between best bid and best ask in the book
- [[Liquidity]] — determined by the depth and resilience of the order book
- [[Market Making]] — market makers are the primary providers of order book liquidity
