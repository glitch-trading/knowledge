---
type: concept
title: "Position Sizing"
tags:
  - concept
  - risk
level: 3
prerequisites: []
---

## What It Is

Position sizing determines how much capital to allocate to a given trade or strategy. It is the most underrated component of a trading system. You can have a positive-edge strategy and still go broke with wrong sizing.

**The core question:** Given your edge, your bankroll, and your risk tolerance, how large should each bet be?

**Common approaches:**
- **Fixed fractional**: Risk a fixed percentage of capital per trade (e.g., 1% per trade)
- **[[Kelly Criterion]]**: Optimal fraction based on edge and odds — maximizes geometric growth
- **Volatility-based**: Size inversely to recent volatility (e.g., target a fixed dollar volatility per position)
- **Risk parity**: Allocate so each position contributes equal risk to the portfolio
- **Fixed dollar**: Same dollar amount per trade regardless of account size (naive, doesn't scale)

## Why It Matters

Position sizing is where theory meets survival. Wrong sizing ruins even positive-edge strategies:

- **Too large**: A string of losses wipes you out before the edge plays out. Ruin probability increases exponentially with bet size beyond Kelly.
- **Too small**: You underutilize your edge and capital. Opportunity cost is real.
- **Not adjusting for correlation**: Five "independent" positions that are all long crypto is really one big position.

**Key principles:**
1. **Never risk ruin.** No single trade or correlated set of trades should be able to end you.
2. **Size to your worst case, not your expected case.** Plan for drawdowns, not average outcomes.
3. **Your edge estimate is probably wrong.** Size as if your edge is half what you think (fractional Kelly).
4. **Adjust dynamically.** After drawdowns, reduce size. After profits, you can increase (but carefully).

## Key Equations

**Probability of ruin (simplified):**
$$P(\text{ruin}) = \left(\frac{q}{p}\right)^{n}$$

Where $n$ = number of betting units in bankroll. More units → lower ruin probability.

**Volatility-targeting position size:**
$$\text{Position Size} = \frac{\text{Target Volatility}}{\text{Asset Volatility}} \times \text{Capital}$$

## Resources

- [[Kelly Criterion]] — The theoretical foundation
- Van Tharp — *Trade Your Way to Financial Freedom* (position sizing focused)
- [[A Man for All Markets — Ed Thorp]]

## Connections

- [[Kelly Criterion]] — Theoretical optimal sizing framework
- [[Maximum Drawdown]] — The constraint that makes position sizing necessary
- [[Risk Aversion]] — Your sizing reflects your risk tolerance
