---
type: paper
title: "High-Frequency Trading in a Limit Order Book"
authors:
  - Marco Avellaneda
  - Sasha Stoikov
year: 2008
status: unread
tags:
  - paper
  - market-making
  - core
level: 2
topics:
  - "[[market-making|Market Making]]"
  - "[[inventory-risk|Inventory Risk]]"
  - "[[hjb-equation|HJB Equation]]"
  - "[[poisson-process|Poisson Process]]"
---

**"High-Frequency Trading in a Limit Order Book"**

The core paper of the roadmap. Models optimal bid/ask placement for a market maker under inventory risk.

## Key Results

### Reservation Price (eq. 29)
$$r = s - q\gamma\sigma^2(T-t)$$
- `s` = mid-price, `q` = inventory, `γ` = risk aversion, `σ` = volatility, `T-t` = time remaining
- Shifts the midpoint based on inventory: long inventory → lower reservation price (want to sell)

### Optimal Spread (eq. 30)
$$\delta^a + \delta^b = \gamma\sigma^2(T-t) + \frac{2}{\gamma}\ln\left(1 + \frac{\gamma}{k}\right)$$
- Spread widens with volatility, risk aversion, and time remaining
- `k` = order book parameter from the trading intensity model

## Model Setup
- Mid-price follows [[brownian-motion|Brownian Motion]]: `dS = σdW`
- Order arrivals are [[poisson-process|Poisson Process]]es with intensity `λ(δ) = Ae^(-kδ)`
- Market maker maximizes [[exponential-utility|Exponential Utility]] of terminal wealth
- Solved via [[hjb-equation|HJB Equation]] + ansatz substitution

## Sections to Study
1. **Sections 1-2:** Value function, [[reservation-price|Reservation Price]]s, limit order model, trading intensity
2. **Section 3:** HJB derivation, ansatz, asymptotic expansion, practical formulas
3. **Simulations:** Inventory management reduces variance at cost of slightly lower returns

## Prerequisites
- [[brownian-motion|Brownian Motion]], [[ito-calculus|Itô Calculus]], [[poisson-process|Poisson Process]]
- [[utility-theory|Utility Theory]], [[hjb-equation|HJB Equation]]
- [[order-book|Order Book]], [[market-making|Market Making]] basics

## Connections
- Extended by [[algorithmic-and-high-frequency-trading-cartea-et-al|Algorithmic and High-Frequency Trading — Cartea et al.]]
- Foundation for all market making strategy work in this repo
