---
type: concept
title: "Spread"
tags:
  - concept
  - market-structure
level: 1
prerequisites:
  - "[[Order Book]]"
---

## What It Is
The spread (or bid-ask spread) is the difference between the best ask price and the best bid price in the [[Order Book]]:

$$\text{spread} = p_{\text{best ask}} - p_{\text{best bid}}$$

It represents the cost of immediately round-tripping (buying and then selling, or vice versa). The spread exists because limit order providers demand compensation for the risks of providing liquidity — primarily [[Adverse Selection]] and [[Inventory Risk]].

A tighter spread means a more liquid market. A wider spread means higher trading costs for market-order users but higher potential profit per trade for market makers.

## Why It Matters
The spread is the market maker's primary source of revenue:
- Every time a market maker buys at the bid and sells at the ask, they earn approximately the spread
- In [[Avellaneda-Stoikov]], the optimal spread is derived from first principles:

$$\delta^a + \delta^b = \gamma \sigma^2 (T - t) + \frac{2}{\gamma} \ln\left(1 + \frac{\gamma}{k}\right)$$

- The spread must be wide enough to compensate for:
  - **Inventory risk**: holding a position in a volatile asset
  - **Adverse selection**: trading against informed counterparties
  - **Operational costs**: fees, infrastructure, etc.
- In practice, competitive pressure pushes the spread to the minimum viable level

## Key Equations

**Simple spread**:

$$\text{spread} = p_{\text{ask}} - p_{\text{bid}}$$

**Relative spread** (useful for cross-asset comparison):

$$\text{relative spread} = \frac{p_{\text{ask}} - p_{\text{bid}}}{s} \quad \text{where } s = \frac{p_{\text{ask}} + p_{\text{bid}}}{2}$$

**Avellaneda-Stoikov optimal spread** (symmetric case, $q = 0$):

$$\delta^* = \gamma \sigma^2 (T - t) + \frac{2}{\gamma} \ln\left(1 + \frac{\gamma}{k}\right)$$

## Resources
- Avellaneda-Stoikov paper, Proposition 1
- Harris, *Trading and Exchanges*, Chapter 6

## Connections
- [[Order Book]] — the spread is directly observable from the top of the book
- [[Market Making]] — the spread is the market maker's gross revenue per round-trip
- [[Adverse Selection]] — informed traders cause losses that the spread must compensate for
- [[Avellaneda-Stoikov]] — derives the optimal spread from utility maximization
