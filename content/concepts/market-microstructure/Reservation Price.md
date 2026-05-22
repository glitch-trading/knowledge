---
type: concept
title: "Reservation Price"
tags:
  - concept
  - market-making
level: 2
prerequisites:
  - "[[Utility Theory]]"
  - "[[Avellaneda-Stoikov]]"
---

## What It Is
The reservation price (also called the indifference price) is the price at which a market maker is equally happy trading or not trading. It is the price that makes the expected utility of executing a trade equal to the expected utility of standing pat.

In Avellaneda-Stoikov (Definition 1), the reservation price adjusts the midprice based on current inventory: if the market maker is long, the reservation price is *below* the midprice (eager to sell), and if short, it is *above* the midprice (eager to buy). This creates a natural inventory-reversion mechanism.

## Why It Matters
The reservation price is the central output of the Avellaneda-Stoikov model:
- It replaces the midprice as the center of the market maker's quotes
- The bid and ask are placed symmetrically around the reservation price (not the midprice)
- It provides a principled, utility-based answer to: "How should I adjust my quotes based on inventory?"
- The formula makes the tradeoffs explicit: inventory $q$, risk aversion $\gamma$, volatility $\sigma$, and time remaining $T - t$ all appear directly

## Key Equations

**Reservation price** (Avellaneda-Stoikov, Definition 1):

$$r(s, q, t) = s - q \gamma \sigma^2 (T - t)$$

Where:
- $s$ = current midprice
- $q$ = current inventory (positive = long, negative = short)
- $\gamma$ = risk aversion parameter
- $\sigma$ = volatility of the midprice
- $T - t$ = time remaining until terminal time

**Intuition for each term**:
- $q > 0$ (long): reservation price < midprice (want to sell, so lower your center)
- $\gamma$ large: bigger adjustment (more risk-averse, more eager to reduce inventory)
- $\sigma$ large: bigger adjustment (more volatile asset, inventory is riskier)
- $T - t$ large: bigger adjustment (more time for things to go wrong)

## Resources
- Avellaneda-Stoikov paper, Definition 1 and Section 3
- Gueant, Lehalle, Fernandez-Tapia, "Dealing with the Inventory Risk"

## Connections
- [[Avellaneda-Stoikov]] — the reservation price is the key result of the model
- [[Utility Theory]] — derived from the indifference condition under expected utility
- [[Inventory Risk]] — the reservation price is the mechanism for managing inventory risk
