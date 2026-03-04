---
type: concept
title: "Backrunning"
tags:
  - concept
  - MEV
level: 4
prerequisites:
  - "[[MEV]]"
---

# Backrunning

## What It Is

Backrunning is placing your transaction immediately after a large trade (or other state-changing transaction) to profit from the price displacement it creates. Unlike [[Frontrunning]], you don't trade before the victim — you trade after, capturing the reversion or arbitrage opportunity their trade creates.

**How it works:**
1. A large swap on an AMM moves the price significantly away from the true market price.
2. The backrunner places a transaction in the very next position to arbitrage the AMM price back toward the fair price.
3. The profit comes from the temporary mispricing created by the large trade.

**Common backrunning targets:**
- Large AMM swaps that create price dislocations (CEX-DEX arb)
- Oracle updates that make DeFi positions liquidatable
- New pool deployments or liquidity additions
- Governance actions that change protocol state

## Why It Matters

- **Less adversarial than frontrunning**: Backrunning doesn't worsen the victim's execution. It captures value that would otherwise go to the next arbitrageur. Some consider it a "benign" form of MEV.
- **CEX-DEX arbitrage is mostly backrunning**: The largest MEV category by dollar value involves backrunning AMM trades to correct prices against CEX reference prices.
- **Highly competitive**: Because backrunning is profitable and relatively simple, it is extremely competitive. Searchers compete on latency, builder relationships, and bundle optimization.
- **Foundation of MEV searching**: Most beginning MEV searchers start with backrunning strategies before moving to more complex approaches.

## Key Equations

**Backrunning arbitrage profit:**
$$\pi = |P_{AMM,\text{post-trade}} - P_{\text{fair}}| \times Q - \text{gas} - \text{tip}$$

**Optimal backrun size (constant product AMM):**

After a trade moves the AMM price to $P_{AMM}$ while the fair price is $P_{\text{fair}}$:
$$Q^* = \sqrt{x \cdot y \cdot P_{\text{fair}}} - x$$

Where $x, y$ are the post-trade reserves.

## Resources

- Flashbots documentation — backrunning bundles
- "Quantifying Blockchain Extractable Value" — Flashbots research
- MEV-Share — protocol for sharing backrunning profits with users

## Connections

- [[MEV]] — Backrunning is a fundamental MEV strategy
- [[Frontrunning]] — The more adversarial counterpart to backrunning
- [[Sandwich Attack]] — Combines frontrunning and backrunning
- [[CEX-DEX Arbitrage]] — Most CEX-DEX arb is structured as backrunning
