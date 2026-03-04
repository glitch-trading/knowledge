---
type: concept
title: "Market Making"
tags:
  - concept
  - market-structure
  - strategies
level: 1-2
prerequisites:
  - "[[Order Book]]"
  - "[[Spread]]"
  - "[[Order Types]]"
---

# Market Making

## What It Is
Market making is the strategy of continuously posting limit orders on both the bid and ask sides of the [[Order Book]], earning the [[Spread]] as compensation for providing [[Liquidity]]. A market maker does not bet on direction — they profit from the flow of trades crossing their quotes, buying at the bid and selling at the ask.

The fundamental challenge: market makers are always on the wrong side of informed trades ([[Adverse Selection]]) and accumulate inventory that exposes them to directional risk ([[Inventory Risk]]). Successful market making requires managing these risks while capturing enough spread to remain profitable.

## Why It Matters
Market making is one of the most established and well-studied strategies in quantitative trading:
- **Revenue model**: Earn the spread on each round-trip (buy at bid, sell at ask), minus losses from adverse selection and inventory drawdowns
- **[[Avellaneda-Stoikov]]** is the canonical academic model: it derives the optimal bid and ask quotes by maximizing expected utility, accounting for inventory risk through the [[Reservation Price]]
- **Practical implementation** requires decisions beyond the model: how to set $\gamma$, how to estimate $\sigma$ and $k$, position limits, fee structures, multiple venues
- **In crypto/DeFi**: market making also occurs on [[AMM]]s, where the mechanism is different (providing liquidity to a pool rather than posting limit orders)
- **Edge**: comes from speed (latency), better models (more accurate parameter estimates), and risk management (position limits, hedging)

## Key Equations

**Avellaneda-Stoikov optimal quotes** (the core result):

Reservation price: $r = s - q\gamma\sigma^2(T-t)$

Optimal spread around reservation price:

$$\delta^a + \delta^b = \gamma\sigma^2(T-t) + \frac{2}{\gamma}\ln\left(1 + \frac{\gamma}{k}\right)$$

**Simplified P&L per round-trip**: $\text{P\&L} \approx \text{spread} - \text{adverse selection cost} - \text{fees}$

## Resources
- Avellaneda & Stoikov, "High-frequency trading in a limit order book" (2008)
- Gueant, *The Financial Mathematics of Market Making* (2017)
- Harris, *Trading and Exchanges*, Chapter 13

## Connections
- [[Market Maker]] — the entity performing market making
- [[Spread]] — the market maker's gross revenue per round-trip
- [[Inventory Risk]] — the primary risk that market makers face
- [[Adverse Selection]] — trading against informed counterparties
- [[Avellaneda-Stoikov]] — the canonical optimal market-making model
