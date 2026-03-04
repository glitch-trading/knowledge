---
type: paper
title: "Uniswap v3 Core"
authors:
  - Hayden Adams
  - Noah Zinsmeister
  - Moody Salem
  - River Keefer
  - Dan Robinson
year: 2021
status: unread
tags:
  - paper
  - DeFi
  - AMM
topics:
  - "[[AMM]]"
  - "[[Impermanent Loss]]"
---

# Uniswap v3 Whitepaper

**Concentrated liquidity, tick math, virtual reserves, fee tiers. The most capital-efficient AMM design.**

## Summary

Uniswap v3 introduces **concentrated liquidity**: instead of providing liquidity across the entire price range (0, infinity) like v2, LPs choose a specific price range $[p_a, p_b]$ to concentrate their capital. Within that range, the LP's capital acts as if it were a much larger v2 position. Outside that range, the position is inactive (100% in one token).

This is a fundamental upgrade — v3 can be up to 4000x more capital efficient than v2 for tight ranges.

## Key Results

**Virtual reserves:**

A v3 position in range $[p_a, p_b]$ behaves like a v2 pool with virtual reserves:
$$x_{\text{virtual}} = \frac{L}{\sqrt{p}} \quad \text{and} \quad y_{\text{virtual}} = L \sqrt{p}$$

Where $L = \sqrt{k}$ is the liquidity parameter. The constant product invariant applies to virtual reserves:
$$x_{\text{virtual}} \cdot y_{\text{virtual}} = L^2$$

**Tick math:**

Prices are discretized into **ticks**. Each tick represents a 0.01% (1 basis point) price change:
$$p(i) = 1.0001^i$$

Tick spacing varies by fee tier (e.g., 10 ticks for 0.05% fee, 60 ticks for 0.3% fee). This discretization makes the math tractable for on-chain computation.

**Fee tiers:**
- 0.01% — stablecoin pairs
- 0.05% — correlated pairs
- 0.30% — standard pairs
- 1.00% — exotic/volatile pairs

**Key implications:**
- **LP positions are non-fungible**: Each position has unique range parameters, represented as an NFT rather than ERC-20
- **Active management required**: LPs must rebalance ranges as price moves, or their capital sits idle. LPing becomes an active strategy, not a passive one.
- **[[Impermanent Loss]] is concentrated**: Tighter ranges amplify both fee income and IL. A tight range earns more fees per dollar but suffers more IL per price move.
- **JIT (just-in-time) liquidity**: Sophisticated LPs can add concentrated liquidity right before a large trade and remove it after, capturing fees while minimizing IL exposure. This is a form of MEV.

## Connections

- [[AMM]] — v3 is the current state of the art in AMM design
- [[Impermanent Loss]] — Concentrated liquidity amplifies IL, making it the central risk for v3 LPs
