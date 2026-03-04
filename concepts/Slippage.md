---
type: concept
title: "Slippage"
tags:
  - concept
  - market-structure
  - execution
level: 1
prerequisites:
  - "[[Order Book]]"
  - "[[Liquidity]]"
---

# Slippage

## What It Is
Slippage is the difference between the expected execution price and the actual execution price of a trade. It occurs when a market order (or aggressive limit order) is large enough to consume multiple price levels in the [[Order Book]], resulting in a worse average fill price than the top-of-book quote.

Example: if the best ask shows 10 units at $100 and the next level has 10 units at $100.05, a market buy of 15 units would fill 10 at $100 and 5 at $100.05, giving an average price of $100.017 — the $0.017 above the quoted ask is slippage.

## Why It Matters
Slippage is one of the most important real-world frictions in trading:
- **Backtesting vs. live trading gap**: Many strategies look profitable in backtests that assume execution at midprice, but fail live because of slippage. Accounting for slippage is essential for realistic strategy evaluation
- **Scales with order size**: Larger orders cause more slippage, which limits strategy capacity
- **Particularly relevant in crypto/DeFi**: [[AMM]]-based markets have explicit slippage determined by the bonding curve, making it calculable in advance
- **Market making context**: In [[Avellaneda-Stoikov]], market makers use limit orders and typically do not experience slippage themselves — but their counterparties (market-order users) do. Wider spreads increase the slippage for takers
- **Optimal execution**: Algorithms like TWAP and VWAP exist specifically to minimize slippage by breaking large orders into smaller pieces over time

## Key Equations

**Simple slippage**:

$$\text{slippage} = p_{\text{actual}} - p_{\text{expected}}$$

**For AMMs** (constant product, e.g., Uniswap v2):

$$\text{slippage} = \frac{\Delta x}{x + \Delta x}$$

Where $\Delta x$ is the trade size relative to pool reserve $x$.

## Resources
- Harris, *Trading and Exchanges*, Chapter 6
- Almgren & Chriss, "Optimal Execution of Portfolio Transactions" (2001)

## Connections
- [[Liquidity]] — slippage is inversely related to liquidity
- [[Order Book]] — slippage comes from consuming multiple levels of the book
- [[Market Impact]] — slippage is a component of market impact
- [[AMM]] — AMMs have deterministic, calculable slippage
