---
type: concept
title: "Maximum Drawdown"
tags:
  - concept
  - risk
level: 3
prerequisites: []
---

# Maximum Drawdown

## What It Is

Maximum Drawdown (MDD) is the largest peak-to-trough decline in portfolio value over a given period. It measures the worst cumulative loss an investor would have experienced if they entered at the worst possible time.

$$MDD = \max_{t \in [0,T]} \left( \frac{\text{Peak}_t - \text{Trough}_t}{\text{Peak}_t} \right)$$

Where $\text{Peak}_t$ is the running maximum of portfolio value up to time $t$, and $\text{Trough}_t$ is the subsequent minimum.

**Example:** Your portfolio goes $100 → $150 → $90 → $120 → $80. The max drawdown is from $150 to $80 = **46.7%**.

## Why It Matters

Maximum drawdown is what actually kills strategies and traders in practice. While [[Sharpe Ratio]] and other return metrics tell you about average behavior, MDD tells you about the worst experience.

**Why it matters more than volatility:**
- **Psychological**: A 50% drawdown requires 100% gain to recover. Most traders quit before recovery.
- **Leverage**: If you're leveraged, drawdowns trigger margin calls and forced liquidation. You can be "right" on the trade but "wrong" on the sizing.
- **Capital allocation**: Allocators (including yourself) pull capital after large drawdowns. The strategy may never get to play out its edge.
- **Path dependency**: Two strategies with identical Sharpe ratios but different max drawdowns have very different survival probabilities.

**Rules of thumb:**
- Full [[Kelly Criterion]] typically produces ~50% max drawdown over long horizons
- Half Kelly reduces expected MDD to ~25%
- Any strategy with >30% MDD is difficult to stick with psychologically
- Historical MDD underestimates future MDD — the worst drawdown is always ahead of you

## Key Equations

**Calmar Ratio:**
$$\text{Calmar} = \frac{\text{Annualized Return}}{\text{Max Drawdown}}$$

A return-to-MDD ratio. Higher = better risk-adjusted performance.

**Recovery time:**
$$T_{\text{recovery}} = \frac{-\ln(1 - \text{DD})}{\mu - \frac{\sigma^2}{2}}$$

Approximate time to recover from drawdown DD given geometric drift $\mu$ and volatility $\sigma$.

## Resources

- Magdon-Ismail & Atiya (2004) — "Maximum Drawdown" (analytical properties)
- [[Quantitative Risk Management — McNeil, Frey & Embrechts]]

## Connections

- [[Position Sizing]] — Proper sizing is the primary defense against catastrophic drawdowns
- [[Sharpe Ratio]] — MDD captures what Sharpe misses: path-dependent risk
- [[Kelly Criterion]] — Kelly fraction directly determines expected drawdown magnitude
