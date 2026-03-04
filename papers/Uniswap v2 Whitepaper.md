---
type: paper
title: "Uniswap v2 Core"
authors:
  - Hayden Adams
  - Noah Zinsmeister
  - Dan Robinson
year: 2020
status: unread
tags:
  - paper
  - DeFi
  - AMM
topics:
  - "[[AMM]]"
  - "[[Constant Product Formula]]"
---

# Uniswap v2 Whitepaper

**5 pages. Constant product AMM. $x \cdot y = k$. The most readable introduction to AMM design.**

## Summary

The Uniswap v2 whitepaper describes the canonical constant product automated market maker. It is short (5 pages), clear, and foundational. If you read one AMM paper, read this one.

**Core mechanism:** A liquidity pool holds reserves of two tokens ($x$ and $y$). The invariant $x \cdot y = k$ determines pricing. When a trader swaps token A for token B, the product of reserves must remain constant (minus fees). This simple rule creates a fully on-chain, permissionless exchange.

## Key Results

**Constant product invariant:**
$$x \cdot y = k$$

After a trade of $\Delta x$ tokens in:
$$y_{\text{out}} = y - \frac{k}{x + \Delta x} = \frac{y \cdot \Delta x}{x + \Delta x}$$

**Marginal price:**
$$P = \frac{y}{x}$$

The price is simply the ratio of reserves. As you buy token A (increasing $x$), you get less token B per unit — slippage is built into the curve.

**Key design decisions in v2:**
- **0.3% fee** on every trade, accruing to LPs
- **Flash swaps**: Borrow any amount from the pool, execute arbitrary logic, and repay within the same transaction (or revert)
- **Price oracle**: Cumulative price tracking allows time-weighted average price (TWAP) computation
- **ERC-20 LP tokens**: Liquidity positions are fungible tokens, composable with other DeFi protocols

**What v2 gets right:**
- Extreme simplicity — the entire pricing logic is one equation
- Permissionless listing — anyone can create a pool for any token pair
- Always-on liquidity — no market maker needed, the pool is always available

**What v2 gets wrong:**
- Capital inefficiency — liquidity is spread across the entire price curve from 0 to infinity, but most trades happen in a narrow range
- [[Impermanent Loss]] — LPs systematically lose to informed arbitrageurs (see [[CEX-DEX Arbitrage]])
- No concentrated liquidity — fixed to v3

## Connections

- [[AMM]] — Uniswap v2 is the canonical AMM implementation
- [[Constant Product Formula]] — The mathematical invariant underlying v2
