---
type: concept
title: "Market Maker"
tags:
  - concept
  - market-structure
level: 1
prerequisites: []
---

# Market Maker

## What It Is
A market maker is an entity (individual, firm, or algorithm) that continuously quotes both bid and ask prices for an asset, standing ready to buy or sell at those prices. By doing so, the market maker provides [[Liquidity]] to the market — other participants can always trade immediately by hitting the market maker's quotes.

Market makers can be:
- **Designated**: formally appointed by an exchange with obligations to quote (e.g., NYSE specialists historically)
- **Voluntary**: proprietary trading firms that choose to make markets for profit (e.g., Citadel Securities, Jump Trading)
- **Algorithmic**: automated systems that adjust quotes in real-time based on models like [[Avellaneda-Stoikov]]

## Why It Matters
Market makers are essential infrastructure of financial markets:
- **They create liquidity**: without market makers, traders would have to wait to find a counterparty, making markets slower and more costly
- **They earn the spread**: the bid-ask spread is the market maker's compensation for the service of providing immediacy
- **They bear two key risks**:
  - [[Inventory Risk]]: accumulating a directional position as fills arrive asymmetrically
  - [[Adverse Selection]]: being picked off by traders with better information about where the price is heading
- **The quant problem**: How should a market maker set their bid and ask prices to maximize profit while managing risk? This is exactly what [[Avellaneda-Stoikov]] answers
- In crypto, both centralized exchange market makers and [[AMM]] liquidity providers serve this role

## Key Equations
Not applicable — the market maker is a role, not a formula. See [[Market Making]] for the quantitative framework.

## Resources
- Harris, *Trading and Exchanges*, Chapters 13-14
- Hasbrouck, *Empirical Market Microstructure*

## Connections
- [[Market Making]] — the strategy and quantitative framework for market makers
- [[Spread]] — the market maker's gross revenue per trade
- [[Inventory Risk]] — the primary risk from asymmetric order flow
