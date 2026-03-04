---
type: concept
title: "Liquidation Botting"
tags:
  - concept
  - MEV
  - DeFi
  - strategies
level: 4-5
prerequisites:
  - "[[MEV]]"
---

# Liquidation Botting

## What It Is

Liquidation botting is the practice of monitoring DeFi lending protocols (Aave, Compound, Maker, etc.) for undercollateralized positions and triggering their liquidation for a bonus/discount.

**How DeFi lending works:**
- Borrowers deposit collateral (e.g., ETH) and borrow against it (e.g., USDC).
- Each position has a health factor: if collateral value drops below a threshold (liquidation ratio), the position can be liquidated.
- Anyone can call the liquidation function — you repay some of the borrower's debt and receive their collateral at a discount (the liquidation bonus, typically 5-15%).

**How liquidation bots work:**
1. **Monitor oracle prices** in real-time (Chainlink, Uniswap TWAP, etc.).
2. **Track all open positions** and their health factors.
3. **Predict which positions will become liquidatable** as prices move.
4. **Submit liquidation transactions** as fast as possible when positions cross the threshold.
5. **Optimize gas and routing** — use flash loans to avoid capital requirements, route through optimal DEX paths, bid efficiently to builders.

## Why It Matters

- **Protocol health**: Liquidation bots are essential infrastructure. Without them, lending protocols would accumulate bad debt and become insolvent. Bots keep the system healthy.
- **Competitive MEV niche**: Liquidation botting is highly competitive. Searchers compete on:
  - Latency (monitoring oracle updates, mempool watching)
  - Capital efficiency (flash loans to avoid upfront capital)
  - Gas optimization (efficient contract calls, bundle construction)
  - Coverage (monitoring multiple protocols across multiple chains)
- **Significant profit potential**: During market crashes, liquidation cascades create massive MEV. The 2020 and 2022 crashes generated millions in liquidation profits.
- **Integration with broader MEV stack**: Liquidation bots typically submit through Flashbots or directly to builders, competing in the MEV supply chain like any other searcher.

## Key Equations

**Health factor (Aave-style):**
$$HF = \frac{\sum(\text{collateral}_i \times P_i \times LT_i)}{\text{total debt value}}$$

Where $LT_i$ is the liquidation threshold for collateral asset $i$. Position is liquidatable when $HF < 1$.

**Liquidation profit:**
$$\pi = \text{collateral received} \times (1 + \text{bonus}) - \text{debt repaid} - \text{gas} - \text{tip}$$

**Flash loan liquidation (zero capital required):**
1. Flash borrow USDC
2. Repay borrower's debt
3. Receive discounted collateral
4. Swap collateral to USDC
5. Repay flash loan + fee
6. Keep the difference

## Resources

- Aave Liquidation Documentation
- Compound Protocol Liquidation Mechanics
- "Liquidations: DeFi on a Knife-Edge" — Qin et al.
- Flashbots — liquidation bundle examples

## Connections

- [[MEV]] — Liquidation botting is a major MEV category
- [[Avellaneda-Stoikov]] — Risk management frameworks apply to managing liquidation bot inventory
- [[AMM]] — Liquidation bots often route through AMMs to convert seized collateral
