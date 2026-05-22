---
type: concept
title: "Momentum"
tags:
  - concept
  - factor-investing
  - strategies
  - market-anomalies
level: 5
prerequisites:
  - "[[Regression]]"
  - "[[Statistical Arbitrage]]"
---

## What It Is

**Momentum** is the empirical regularity that assets which performed well over the past 3-12 months continue to outperform over the next 3-12 months, and conversely for past underperformers. Established empirically by [[Returns to Buying Winners and Selling Losers — Jegadeesh & Titman|Jegadeesh & Titman (1993)]] and now treated as a standard tradeable factor across asset classes.

The canonical implementation:

1. At each rebalance date, rank assets by their return over a **formation window** (most commonly 6 or 12 months, skipping the most recent month to avoid short-term reversal).
2. Go long the top decile (winners), short the bottom decile (losers), dollar-neutral.
3. Hold for a **holding window** (typically 1-12 months), then rebalance.

The "12-1" convention (formation = months $t-12$ to $t-1$, skip month $t$) is standard because it captures the momentum effect while excluding the short-horizon reversal in the most recent month.

## Why It Matters

Momentum is one of the few academic anomalies that has survived out-of-sample across decades, geographies, and asset classes:

- **Equity momentum** documented in U.S., European, Japanese, and emerging markets. The U.S. effect has been weaker since 2000 but not zero.
- **Cross-asset momentum** works on commodities, currencies, fixed income, and crypto. Time-series momentum (an asset's own past return predicts its future return) is also robust.
- **It survives transaction costs at institutional scale**, unlike many academic factors. Several large funds (AQR, MAN AHL, Winton) run momentum-centric strategies.
- **It is the Carhart fourth factor** added to the [[Fama-French Three-Factor Model]] in 1997, now standard in factor regressions.

The hard part is not finding momentum — it is sizing through its drawdowns. Momentum crashes are real and severe: 2009 saw a -85% drawdown in U.S. equity momentum as the market sharply reversed off the March bottom, with the losers (heavily shorted financials) rallying violently while the winners stalled. Risk management *for* the momentum strategy is the practical research frontier.

## Variants

- **Cross-sectional momentum** (the Jegadeesh-Titman form): rank assets against each other and trade the spread.
- **Time-series momentum** (Moskowitz, Ooi & Pedersen 2012): long an asset if its own trailing return is positive, short if negative. Each asset is treated independently; no cross-sectional comparison.
- **Risk-managed momentum** (Barroso & Santa-Clara 2015): scale momentum exposure by the inverse of its trailing realized volatility. Reduces crash risk substantially without sacrificing average return.
- **Industry / sector momentum** (Moskowitz & Grinblatt 1999): rank sectors instead of stocks; argued to be a significant component of stock-level momentum.

## Key Equations

**Cross-sectional momentum signal** for asset $i$ at time $t$:

$$\text{mom}_{i,t} = R_{i, t-12, t-1}$$

i.e., the cumulative return over months $t-12$ through $t-1$, excluding the most recent month.

**Risk-managed sizing** (Barroso & Santa-Clara):

$$w_t = \frac{\sigma_{\text{target}}}{\hat\sigma_{t}^{\text{mom}}}$$

where $\hat\sigma_t^{\text{mom}}$ is the trailing 6-month realized vol of the momentum portfolio. Cap leverage to prevent extreme allocations during low-vol periods.

## Common Failure Modes

- **Momentum crashes.** The strategy is implicitly short volatility — short losers and long winners both expose you to mean-reverting reversals after large drawdowns. Sizing must account for this.
- **Crowding.** When too many funds run the same momentum sort, signal decays and reversal events become sharper.
- **Cost sensitivity.** Naive monthly rebalancing has high turnover; many real-world implementations use longer holding periods or signal smoothing.
- **Misclassification by [[Survivorship Bias]].** Backtests that exclude delisted names overweight the short leg's actual win rate.

## Resources

- [[Returns to Buying Winners and Selling Losers — Jegadeesh & Titman]] — The founding paper
- Asness, Moskowitz & Pedersen (2013), "Value and Momentum Everywhere" — Cross-asset evidence
- Moskowitz, Ooi & Pedersen (2012), "Time Series Momentum" — The TS variant
- Barroso & Santa-Clara (2015), "Momentum Has Its Moments" — Risk management

## Connections

- [[Returns to Buying Winners and Selling Losers — Jegadeesh & Titman]] — Founding empirical paper
- [[Fama-French Three-Factor Model]] — Momentum is the Carhart fourth factor
- [[CAPM]] — Momentum alpha persists after controlling for market beta
- [[Statistical Arbitrage]] — Momentum is one of the canonical [[Statistical Arbitrage|stat-arb]] signals
- [[Overfitting]] — Momentum is unusual in *not* being a likely overfit; the deflated Sharpe of momentum survives the multiple-testing correction
- [[Position Sizing]] — Drawdown management is the central practical challenge
