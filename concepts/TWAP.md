---
type: concept
title: "TWAP"
tags:
  - concept
  - execution
level: 4
prerequisites:
  - "[[Market Impact]]"
---

# TWAP (Time-Weighted Average Price)

## What It Is

TWAP is an execution algorithm that splits a large order into equal-sized slices and executes them at regular time intervals over a specified period. The goal is to achieve an average execution price close to the time-weighted average price of the market during the execution window.

**Example**: You want to buy 1,000 ETH over 1 hour. TWAP splits this into 60 slices of ~16.7 ETH, executing one slice every minute.

**Mechanics:**
- Divide total quantity $Q$ into $N$ equal slices: $q = Q/N$
- Execute one slice every $\Delta t = T/N$ time units
- Each slice can be a market order or a limit order with a short time horizon
- If a slice doesn't fill (limit order), it can roll into the next interval or be market-ordered

TWAP is the simplest execution algorithm and serves as a benchmark for more sophisticated approaches.

## Why It Matters

- **Reduces market impact**: By spreading execution over time, TWAP avoids the large instantaneous impact of executing all at once. Each small slice has minimal impact.
- **Simple and robust**: No need to predict volume profiles or model impact functions. Just divide and execute. This simplicity is a feature in uncertain environments.
- **Benchmark**: TWAP is a standard benchmark for execution quality. If your algo can't beat TWAP, something is wrong.
- **DeFi relevance**: On-chain TWAP oracles (Uniswap v2/v3 TWAP) use time-weighted average prices as manipulation-resistant price feeds. Different from TWAP execution, but same underlying concept.

## Key Equations

**TWAP price:**
$$P_{TWAP} = \frac{1}{T} \int_0^T P(t) \, dt$$

In discrete form:
$$P_{TWAP} = \frac{1}{N} \sum_{i=1}^{N} P(t_i)$$

**Slice size:**
$$q = \frac{Q}{N}$$

**Expected impact of TWAP vs. single execution:**

Single execution impact: $\sigma \cdot c \cdot \sqrt{Q/V}$

TWAP impact (approximate): $\sigma \cdot c \cdot \sqrt{q/V} = \sigma \cdot c \cdot \sqrt{Q/(N \cdot V)}$

Impact reduction factor: $1/\sqrt{N}$

**Timing risk (variance of TWAP execution price):**
$$\text{Var}(P_{TWAP}) = \frac{\sigma^2 T}{3N}$$

More slices reduce variance but increase total execution time and risk of information leakage.

## Resources

- Almgren & Chriss — "Optimal Execution of Portfolio Transactions" (TWAP as special case)
- Robert Kissell — algorithmic execution benchmarks
- Uniswap v2/v3 documentation — TWAP oracles

## Connections

- [[VWAP]] — TWAP's volume-aware cousin; weights by volume profile instead of equal time slices
- [[Market Impact]] — TWAP is designed to minimize market impact from large orders
- [[Slippage]] — TWAP reduces slippage by executing in smaller, less impactful chunks
