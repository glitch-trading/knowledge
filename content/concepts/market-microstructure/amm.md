---
type: concept
title: "AMM"
tags:
  - concept
  - DeFi
  - market-structure
level: 1
prerequisites: []
---

## What It Is

An Automated Market Maker is a smart contract that provides liquidity through a deterministic mathematical formula rather than a traditional order book. Instead of matching buyers and sellers, an AMM holds reserves of two (or more) tokens and prices trades according to a bonding curve that relates the reserve quantities.

Anyone can become a liquidity provider (LP) by depositing tokens into the pool's reserves. Traders swap against the pool, and the formula automatically adjusts the price based on how reserves change. There is no bid/ask, no order book, no counterparty matching — just math.

**Major AMM designs:**
- **Uniswap v2**: [[constant-product-formula|Constant Product Formula]] ($x \cdot y = k$)
- **Uniswap v3**: Concentrated liquidity — LPs choose price ranges
- **Curve**: [[curve-stableswap|Curve Stableswap]] — hybrid constant sum/product, optimized for pegged assets
- **Balancer**: Weighted pools with arbitrary token ratios

## Why It Matters

AMMs are the dominant trading venue in DeFi. Understanding them is essential because:

- **They are your trading venue**: If you're trading on-chain, you're likely routing through AMMs.
- **They create arbitrage opportunities**: AMM prices lag CEX prices, creating [[cex-dex-arbitrage|CEX-DEX Arbitrage]] opportunities — a major MEV source.
- **LPing is a trading strategy**: Providing liquidity is economically similar to selling options (short gamma). Understanding when LPing is profitable requires understanding [[impermanent-loss|Impermanent Loss]], fee income, and the adverse selection from arbitrageurs.
- **They define on-chain price discovery**: AMM reserves and their formulas determine on-chain prices, which oracles may reference.

## Key Equations

**General AMM invariant:**
$$f(x, y) = k$$

Where $x$ and $y$ are reserve quantities, and $k$ is a constant maintained by the invariant.

**Marginal price (for constant product):**
$$P = \frac{y}{x}$$

The price is simply the ratio of reserves.

**Price after a trade of $\Delta x$:**
$$P_{\text{after}} = \frac{y - \Delta y}{x + \Delta x}$$

Where $\Delta y$ is determined by the invariant.

## Resources

- Uniswap v2 Whitepaper
- Uniswap v3 Whitepaper — concentrated liquidity
- Curve Stableswap Paper — hybrid invariant
- Paradigm — "An Analysis of Uniswap Markets"
- Dan Robinson & Dave White — various research on AMM theory

## Connections

- [[constant-product-formula|Constant Product Formula]] — The most fundamental AMM invariant ($x \cdot y = k$)
- [[curve-stableswap|Curve Stableswap]] — Specialized AMM design for correlated assets
- [[impermanent-loss|Impermanent Loss]] — The core risk of providing liquidity to an AMM
- [[liquidity|Liquidity]] — AMMs are a mechanism for providing and accessing liquidity on-chain
- [[adverse-selection|Adverse Selection]] — LP losses to arbitrageurs are a form of adverse selection
- [[mev|MEV]] — AMMs are the primary venue where MEV is extracted
