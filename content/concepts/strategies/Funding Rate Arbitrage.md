---
type: concept
title: "Funding Rate Arbitrage"
tags:
  - concept
  - strategies
  - carry
level: 2-5
prerequisites: []
---

## What It Is

Funding rate arbitrage is a delta-neutral carry trade that captures the funding rate differential between perpetual futures and spot (or between perps on different exchanges).

Perpetual futures have no expiry — instead, they use a **funding rate** mechanism to keep the perp price tethered to spot. When perp price > spot price (contango / longs pay shorts), funding is positive. When perp < spot (backwardation / shorts pay longs), funding is negative.

**Basic trade (positive funding):**
1. Buy spot (or a different perp with lower funding)
2. Short the perp with high funding
3. Collect funding payments (typically every 8 hours)
4. Net exposure: delta-neutral (long spot + short perp cancel out)

You earn the funding rate while being market-neutral.

## Why It Matters

- **One of the most accessible "edges" in crypto**: Funding rates in crypto are often persistently positive (retail is structurally long). Annualized funding rates of 10-30% are not uncommon during bull markets.
- **Capital-intensive**: You need capital for both the spot position and the margin for the short perp. Effective yield is halved because you deploy 2x capital for the delta-neutral structure.
- **Not risk-free**: Despite being "delta-neutral," risks include:
  - **Funding rate reversal**: Rates can flip negative, turning carry into bleed
  - **Liquidation risk**: If the perp moves against your short, you may face margin calls before funding accrues
  - **Exchange risk**: Counterparty risk on the CEX holding your funds
  - **Basis risk**: Spot and perp don't always move in perfect lockstep
  - **Execution slippage**: Entry/exit costs eat into carry

**Cross-exchange variant:** Short the perp on exchange A (high funding), long the perp on exchange B (low funding). Same principle, but now you have counterparty risk on two exchanges.

## Key Equations

**Annualized yield (simplified):**
$$\text{Yield} = \frac{\text{Funding Rate} \times 3 \times 365}{\text{Capital Deployed}} \times 100\%$$

(Assuming 8-hour funding periods, 3 per day.)

**Net yield after costs:**
$$\text{Net Yield} = \text{Gross Funding} - \text{Trading Fees} - \text{Borrowing Costs} - \text{Slippage}$$

## Resources

- Exchange funding rate dashboards (Binance, dYdX, etc.)
- Coinglass — Historical and real-time funding rate data across exchanges

## Connections

- [[Statistical Arbitrage]] — Funding arb is a specific form of stat arb (probabilistic, not riskless)
- [[Spread]] — The funding rate is a spread between perp and spot pricing
