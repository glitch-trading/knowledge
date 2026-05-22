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

## Carry-quality filters

Raw funding rate is a misleading ranking signal. The same headline number can be a stable regime or a five-minute spike that disappears the moment you enter. A live allocator should rank candidate trades on **expected captured carry net of execution risk**, not on instantaneous funding:

- **Persistence.** Penalize opportunities whose funding has only been elevated for a few prints. A short EWMA of the rate, or a fraction-of-recent-windows-above-threshold count, filters flashes. The aim is to estimate the funding you will *actually accrue over your minimum hold period*, not the snapshot.
- **Liquidity floor.** Reject any pair where the round-trip cost (spread + impact + fees on both legs) exceeds a meaningful fraction of expected funding over the hold. Tiny markets with juicy rates are usually traps.
- **Position symmetry.** If exchange-specific minimum sizes force the two legs to be materially unequal, the trade is no longer delta-neutral — it is directional with a funding kicker. Either reject, scale to the smaller-min leg, or add a separate hedge.
- **Rotation hysteresis.** Once in a position, do *not* rotate every time a marginally better opportunity appears. The bot pays double round-trip cost to rotate, so the new trade's expected net carry must exceed the current trade's by at least `2 × round_trip_cost / expected_hold`. A flat threshold (e.g. "only rotate if new opportunity beats current by ≥ N bps annualized" or "current opportunity drops below a floor") prevents allocator churn driven by noise. Same logic as a [[mean-reversion|Mean Reversion]] band: the entry and exit thresholds must differ by more than the round-trip cost or the bot trades itself broke.

## Loop cadence

Funding accrues on a venue-defined schedule (hourly, 8-hourly, continuous). The strategy's natural decision cadence is set by that schedule, *not* by how fast the bot can poll. Polling sub-second is pure noise: it creates more failed orders, more rotations, more fee leakage, with no information gain. A loop interval on the order of 5–15 minutes captures essentially all of the carry signal while leaving headroom to react to regime changes. Faster polling makes sense only for the *risk* side (margin headroom, partial-fill reconciliation), not the *allocation* side.

## PnL attribution: funding vs price

The bedrock validation for any carry strategy: decompose realized PnL into the **funding component** and the **price/basis component**.

$$\text{Net PnL} = \underbrace{\sum_i F_i}_{\text{funding}} + \underbrace{\sum_{\text{legs}} (P_{\text{exit}} - P_{\text{entry}}) \cdot q}_{\text{price/basis}} - \text{fees}$$

If the strategy is working as designed, funding PnL should be the dominant, positive term and price PnL should oscillate around zero. If realized profit is dominated by price PnL, the bot got lucky on direction or basis movement — that is not the edge it was built to capture, and the sample is uninformative about whether the carry signal is real. Track both components per closed trade; a strategy with positive net PnL but negative funding PnL is broken even if the dashboard looks green.

```python
def attribute_pnl(legs, fees_per_leg=0.0):
    """legs: list of dicts with size (signed), entry, exit, funding_accrued."""
    funding_pnl = sum(leg["funding_accrued"] for leg in legs)
    price_pnl = sum((leg["exit"] - leg["entry"]) * leg["size"] for leg in legs)
    fees = fees_per_leg * len(legs)
    return {
        "funding_pnl": funding_pnl,
        "price_pnl":   price_pnl,
        "fees":        fees,
        "net_pnl":     funding_pnl + price_pnl - fees,
    }

# Long perp on venue A (low funding), short perp on venue B (high funding).
legs = [
    {"size":  1.0, "entry": 60000.0, "exit": 60050.0, "funding_accrued": -0.40},
    {"size": -1.0, "entry": 60020.0, "exit": 60080.0, "funding_accrued":  1.10},
]
print(attribute_pnl(legs, fees_per_leg=0.05))
# {'funding_pnl': 0.70, 'price_pnl': -10.00, 'fees': 0.10, 'net_pnl': -9.40}
```

The example shows the failure mode the article warns about: funding earned (+0.70) but **basis leakage** (-10.00) dominated. The short leg's mark moved up more than the long leg's, so the "delta-neutral" structure leaked through non-identical exit fills. Realized carry strategies live and die on minimizing this term.

## Key Equations

**Annualized yield (simplified):**
$$\text{Yield} = \frac{\text{Funding Rate} \times 3 \times 365}{\text{Capital Deployed}} \times 100\%$$

(Assuming 8-hour funding periods, 3 per day.)

**Net yield after costs:**
$$\text{Net Yield} = \text{Gross Funding} - \text{Trading Fees} - \text{Borrowing Costs} - \text{Slippage}$$

**Rotation rule of thumb** (current opportunity $c$, candidate $n$, hold horizon $h$, round-trip cost $r$ per leg):
$$\text{Rotate} \iff \mathbb{E}[F_n] - \mathbb{E}[F_c] > \frac{4r}{h}$$

(Factor of 4: closing two legs and opening two new ones.)

## Resources

- Exchange funding rate dashboards (Binance, dYdX, etc.)
- Coinglass — Historical and real-time funding rate data across exchanges

## Connections

- [[statistical-arbitrage|Statistical Arbitrage]] — Funding arb is a specific form of stat arb (probabilistic, not riskless)
- [[spread|Spread]] — The funding rate is a spread between perp and spot pricing
- [[leg-risk|Leg Risk]] — perp/spot or perp/perp leg asymmetry is what produces the basis-leakage term in the attribution above
- [[trading-bot-operations|Trading Bot Operations]] — position reconciliation, reduce-only exits, and session-lifecycle handling are load-bearing for any live carry allocator
- [[mean-reversion|Mean Reversion]] — same hysteresis argument: entry/exit thresholds must clear round-trip cost or the bot churns
