---
type: concept
title: "Market Impact"
tags:
  - concept
  - execution
  - microstructure
level: 3-4
prerequisites: []
---

# Market Impact

## What It Is

Market impact is the price movement caused by your own trading activity. When you buy, you push the price up; when you sell, you push it down. The larger your order relative to available liquidity, the more you move the price against yourself.

Market impact has two components:

1. **Temporary impact**: The transient price displacement from consuming liquidity. It partially reverts as the order book replenishes. This is the "mechanical" cost of eating through resting orders.

2. **Permanent impact**: The lasting price change caused by the information content of your trade. If you're buying because you have alpha, the price should stay at the new level — your trade revealed information to the market.

**The fundamental tradeoff in execution**: Trade quickly (high impact, low risk of price moving against you) vs. trade slowly (low impact, but the market may move before you're done). This is the **urgency-impact tradeoff** at the heart of optimal execution theory.

## Why It Matters

- **It's your biggest cost**: For any strategy trading meaningful size, market impact typically dwarfs commissions and fees. Reducing impact is often the difference between a profitable and unprofitable strategy.
- **It limits strategy capacity**: Every alpha signal has a capacity — the point where market impact from trading on the signal consumes the expected profit. Understanding impact lets you size strategies correctly.
- **Execution algorithms exist to minimize it**: [[TWAP]], [[VWAP]], and more sophisticated algorithms (Almgren-Chriss, IS) are all designed to optimally manage the urgency-impact tradeoff.
- **Square-root law**: Empirically, market impact scales with the square root of order size relative to volume — a universal relationship observed across markets.

## Key Equations

**Square-root law of market impact:**
$$\Delta P \approx \sigma \cdot c \cdot \sqrt{\frac{Q}{V}}$$

Where:
- $\Delta P$ = price impact
- $\sigma$ = daily volatility
- $Q$ = order size (shares/contracts)
- $V$ = daily volume
- $c$ = constant (empirically ~0.5-1.5 depending on market)

**Almgren-Chriss optimal execution framework:**

Minimize:
$$\text{Cost} = \underbrace{\text{Expected impact cost}}_{\text{decreases with slower trading}} + \underbrace{\lambda \times \text{Timing risk (variance)}}_{\text{increases with slower trading}}$$

Where $\lambda$ is the risk aversion parameter controlling the urgency-impact tradeoff.

**Temporary vs. permanent impact decomposition:**
$$\Delta P_{\text{total}} = \underbrace{g(v)}_{\text{permanent}} + \underbrace{h(v)}_{\text{temporary}}$$

Where $v$ is the trading rate. Permanent impact $g$ is typically linear in $v$; temporary impact $h$ is concave.

**Implementation shortfall:**
$$IS = P_{\text{decision}} - P_{\text{average execution}}$$

The total cost of implementing a trading decision, capturing both impact and timing.

## Resources

- Almgren & Chriss (2000) — "Optimal Execution of Portfolio Transactions"
- Bouchaud, Farmer & Lillo — "How Markets Slowly Digest Changes in Supply and Demand" (square-root law)
- Robert Kissell — *The Science of Algorithmic Trading and Portfolio Management*
- Kyle (1985) — permanent price impact and information

## Connections

- [[Liquidity]] — Market impact is inversely related to available liquidity
- [[TWAP]] — Simplest algorithm for reducing market impact over time
- [[VWAP]] — Volume-weighted execution to align with natural liquidity
- [[Slippage]] — Market impact is the primary driver of slippage on large orders
- [[Adverse Selection]] — Permanent impact reflects information content; market makers face it as adverse selection
