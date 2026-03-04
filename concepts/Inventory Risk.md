---
type: concept
title: "Inventory Risk"
tags:
  - concept
  - market-making
  - risk
level: 1-2
prerequisites:
  - "[[Market Making]]"
  - "[[Order Book]]"
---

# Inventory Risk

## What It Is
Inventory risk is the risk a [[Market Maker]] faces from holding a net directional position (inventory) in the asset they are making markets in. Since a market maker's bid and ask orders fill at different times and rates, they inevitably accumulate inventory — sometimes long, sometimes short. If the price moves against their position, they lose money.

Example: A market maker has been buying more than selling, accumulating +10 units. If the price drops by $1, they lose $10 — potentially wiping out many spread-capture trades. This is inventory risk.

## Why It Matters
Inventory risk is the central problem that [[Avellaneda-Stoikov]] solves:
- **Without inventory management**: a naive market maker who quotes symmetrically around the midprice will accumulate large positions and eventually suffer catastrophic losses
- **The Avellaneda-Stoikov solution**: shift quotes using the [[Reservation Price]] formula $r = s - q\gamma\sigma^2(T-t)$, which:
  - Skews quotes toward reducing inventory (if long, lower the center to attract sellers)
  - Increases the skew as inventory grows (larger $q$)
  - Increases the skew as volatility rises (larger $\sigma$ means inventory is riskier)
  - Increases the skew as time remaining grows (more time for adverse moves)
- **In practice**: market makers also use hard position limits, hedging with correlated instruments, and time-based inventory decay to manage this risk
- **Crypto-specific**: on [[AMM]]s, inventory risk manifests as impermanent loss — the LP's position drifts from 50/50 as the price moves

## Key Equations

**Reservation price adjustment** (inventory risk correction to midprice):

$$r - s = -q\gamma\sigma^2(T-t)$$

The magnitude of the adjustment is proportional to:
- $|q|$ — how much inventory you hold
- $\gamma$ — how risk-averse you are
- $\sigma^2$ — how volatile the asset is
- $(T - t)$ — how much time remains for the price to move against you

**Inventory P&L variance** (for a position $q$ held over time $\Delta t$):

$$\text{Var}[\Delta \text{P\&L}] = q^2 \sigma^2 \Delta t$$

## Resources
- Avellaneda-Stoikov paper, Sections 2-3 (inventory risk is the core motivation)
- Gueant, Lehalle, Fernandez-Tapia, "Dealing with the Inventory Risk" (2013)

## Connections
- [[Market Making]] — inventory risk is the primary risk of the market-making strategy
- [[Reservation Price]] — the mechanism by which Avellaneda-Stoikov manages inventory risk
- [[Avellaneda-Stoikov]] — the model that provides the optimal solution to the inventory risk problem
