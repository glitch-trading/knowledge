---
type: paper
title: "StableSwap - Efficient Mechanism for Stablecoin Liquidity"
authors:
  - Michael Egorov
year: 2019
status: unread
tags:
  - paper
  - DeFi
  - AMM
topics:
  - "[[Curve Stableswap]]"
  - "[[AMM]]"
---

# Curve Whitepaper — Michael Egorov

**StableSwap invariant. Amplification parameter. Optimal AMM design for stablecoins and pegged assets.**

## Summary

Curve's StableSwap invariant is a hybrid between a constant sum ($x + y = k$, zero slippage but can be drained) and a constant product ($x \cdot y = k$, infinite liquidity but high slippage). By blending these two formulas, Curve creates an AMM that offers extremely low slippage for assets that should trade near parity (stablecoins, wrapped assets, LSDs).

The key insight: if two assets are expected to trade at a 1:1 ratio, you don't need a constant product curve that prices the entire range from 0 to infinity. You need something that's nearly flat around 1:1 (low slippage for normal trades) but still has the constant product "guardrails" for extreme depegs.

## Key Results

**The StableSwap invariant:**

$$A \cdot n^n \sum x_i + D = A \cdot D \cdot n^n + \frac{D^{n+1}}{n^n \prod x_i}$$

Where:
- $x_i$ = reserve of token $i$
- $n$ = number of tokens in the pool
- $D$ = total deposit value (when all tokens at equal value)
- $A$ = **amplification parameter** (the key knob)

**The amplification parameter $A$:**
- $A = 0$: Reverts to constant product (like Uniswap). High slippage, infinite liquidity.
- $A \to \infty$: Approaches constant sum. Zero slippage near parity, but pool can be fully drained.
- $A$ in practice (50-2000): Sweet spot. Low slippage near parity, reasonable protection at extreme deviations.

**Why this works for stablecoins:**
- USDC/USDT trades should have minimal slippage — they're both $1.00. The high-$A$ curve delivers this.
- During a depeg (e.g., USDC drops to $0.90), the constant product component kicks in, preventing complete pool drainage and providing price discovery.
- The result: 10-100x better slippage than Uniswap for same-peg swaps, while still functioning (albeit with high slippage) during extreme events.

**Curve v2 (tricrypto):**
Egorov later extended the StableSwap concept to non-pegged assets using an internal price oracle and dynamic repricing. The invariant adjusts its "center point" to track the current market price, allowing concentrated liquidity for volatile pairs without manual LP rebalancing.

## Connections

- [[Curve Stableswap]] — The invariant and its mathematical properties
- [[AMM]] — Curve is a specialized AMM optimized for correlated assets
