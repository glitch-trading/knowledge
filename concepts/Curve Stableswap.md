---
type: concept
title: "Curve Stableswap"
tags:
  - concept
  - DeFi
  - AMM
level: 4
prerequisites:
  - "[[Constant Product Formula]]"
  - "[[AMM]]"
---

# Curve Stableswap

## What It Is

The Curve Stableswap invariant is a hybrid between the constant sum formula ($x + y = k$) and the [[Constant Product Formula]] ($x \cdot y = k$). It is specifically designed for assets that should trade near parity — stablecoins (USDC/USDT), wrapped assets (ETH/stETH), etc.

The key innovation is the **amplification parameter $A$**, which controls how "flat" the bonding curve is near the equilibrium point. When reserves are balanced, the curve behaves like a constant sum (near-zero slippage). As reserves become imbalanced, it transitions smoothly toward constant product behavior (increasing slippage to prevent drain).

This gives Curve pools dramatically better capital efficiency for correlated assets — trades near parity experience far less slippage than on a Uniswap-style pool of the same size.

## Why It Matters

- **Dominant venue for stablecoin swaps**: Curve pools handle the majority of stablecoin-to-stablecoin volume on-chain because of their superior pricing for pegged assets.
- **The $A$ parameter is a risk lever**: Higher $A$ = flatter curve = less slippage near parity, but more vulnerability if the peg breaks. Choosing $A$ is a governance decision with real risk implications.
- **Depeg dynamics**: When a stablecoin starts to depeg, the Curve pool is where the action happens. The invariant's behavior under stress determines whether LPs get crushed or the pool absorbs the shock.
- **Arbitrage opportunities**: The transition between constant-sum and constant-product behavior creates unique arbitrage dynamics, especially during depeg events.

## Key Equations

**Curve StableSwap invariant (simplified for 2 tokens):**

$$A \cdot n^n \cdot (x + y) + D = A \cdot D \cdot n^n + \frac{D^{n+1}}{n^n \cdot x \cdot y}$$

Where:
- $A$ = amplification coefficient (higher = flatter curve near equilibrium)
- $n$ = number of tokens (2 for a pair)
- $D$ = total deposit value when pool is balanced (the invariant's "anchor")
- $x, y$ = reserve quantities

**Limiting behavior:**
- $A \to \infty$: invariant approaches constant sum ($x + y = D$), zero slippage
- $A \to 0$: invariant approaches constant product ($x \cdot y = (D/n)^n$)

**Typical $A$ values:**
- Stablecoin pools: $A = 100$ to $2000$
- ETH/stETH pools: $A = 50$ to $200$

## Resources

- Curve Finance Whitepaper — Michael Egorov (2019)
- "Understanding the Curve AMM" — detailed invariant analysis
- Curve DAO documentation

## Connections

- [[AMM]] — Curve is a specialized AMM design for correlated assets
- [[Constant Product Formula]] — Curve's invariant reduces to constant product when $A = 0$
- [[Impermanent Loss]] — IL dynamics differ on Curve due to the flatter curve near parity
