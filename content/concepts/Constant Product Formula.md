---
type: concept
title: "Constant Product Formula"
tags:
  - concept
  - DeFi
  - AMM
level: 1
prerequisites: []
---

## What It Is

The constant product formula is the invariant used by Uniswap v2 and many AMM forks:

$$x \cdot y = k$$

Where $x$ and $y$ are the reserves of two tokens in a liquidity pool, and $k$ is a constant that only changes when liquidity is added or removed (not during swaps).

When a trader swaps token X for token Y, they add $\Delta x$ to the pool and receive $\Delta y$ such that the product remains constant:

$$(x + \Delta x)(y - \Delta y) = k$$

This creates a hyperbolic bonding curve. The price is the ratio of reserves, and it moves along the curve with each trade. The curve never reaches zero on either axis — it is impossible to drain a pool completely, but prices become extreme as reserves become imbalanced.

## Why It Matters

- **Simplicity**: The constant product formula is the simplest viable AMM design. Understanding it is the foundation for understanding all other AMM variants.
- **Price impact is mechanical**: Larger trades move the price more. This is [[Slippage]] — and it's deterministic, so you can calculate it exactly before trading.
- **Arbitrage pricing**: Because the price is just $y/x$, any deviation from external market prices creates a risk-free arbitrage opportunity. This is what keeps AMM prices aligned with the broader market.
- **Impermanent loss derivation**: [[Impermanent Loss]] can be derived analytically from the constant product invariant.

## Key Equations

**Invariant:**
$$x \cdot y = k$$

**Marginal price of X in terms of Y:**
$$P = \frac{y}{x}$$

**Output amount for a swap of $\Delta x$ (ignoring fees):**
$$\Delta y = y - \frac{k}{x + \Delta x} = \frac{y \cdot \Delta x}{x + \Delta x}$$

**Output amount with fee $\gamma$ (e.g., $\gamma = 0.003$ for 0.3%):**
$$\Delta y = \frac{y \cdot \Delta x \cdot (1 - \gamma)}{x + \Delta x \cdot (1 - \gamma)}$$

**Price impact (percentage):**
$$\text{Impact} = \frac{\Delta x}{x + \Delta x}$$

**Arbitrage trade size to move price from $P_0$ to $P_1$:**
$$\Delta x = x \left(\sqrt{\frac{P_1}{P_0}} - 1\right)$$

## Resources

- Uniswap v2 Whitepaper
- Vitalik Buterin — "On Path Independence" (early AMM theory)
- Paradigm — "An Analysis of Uniswap Markets"

## Connections

- [[AMM]] — The constant product formula is the canonical AMM invariant
- [[Impermanent Loss]] — Derived directly from how the constant product curve rebalances reserves
- [[Slippage]] — Price impact on constant product pools is deterministic and calculable
- [[Curve Stableswap]] — A more complex invariant designed to improve on constant product for pegged assets
