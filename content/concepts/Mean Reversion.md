---
type: concept
title: "Mean Reversion"
tags:
  - concept
  - strategies
level: 2
prerequisites: []
---

## What It Is

Mean reversion is the tendency of a price series — or a spread between series — to return to a long-run average after deviating from it. A mean-reverting strategy bets on that pullback: enter when the series is far from its mean, exit when it returns.

**Variants:**

- **Single-asset mean reversion**: price deviations from a rolling mean / VWAP / TWAP / band (Bollinger, Keltner). Most fragile — most "mean reverting" individual assets are actually trending plus noise.
- **Spread mean reversion (pairs trading)**: two assets are [[Cointegration|cointegrated]]; trade the spread when its z-score is extreme. Robust to drift in either leg.
- **Range extremity plays**: discretionary version — identify a range, fade taps of the high/low when there is no breakout context.
- **Cross-venue mean reversion**: same asset on two venues drifts apart for microstructural reasons and converges. Closely related to [[Spatial Arbitrage]] / [[CEX-DEX Arbitrage]] but with timing risk.

**Required conditions:**

- The series must actually be [[Stationarity|stationary]] (or the spread must be). Test, don't assume.
- The mean and variance must be stable enough to estimate from history.
- The HTF context must not be a regime in which the "mean" itself is moving (e.g., fading a strong trend).

## Why It Matters

Mean reversion is one of the two fundamental strategy archetypes (the other being trend following / momentum). Most quant edges in liquid markets are some form of mean reversion at some horizon — market making is mean reversion on microstructure noise; stat arb pairs are mean reversion on a cointegrated spread; funding-rate harvest is mean reversion of basis.

**Why it fails when it fails:**

- **Regime change**: the mean moves and never comes back. Cointegrated pairs decointegrate.
- **Fading the trend**: short-horizon mean reversion against a strong HTF trend is a structurally losing trade.
- **Fat tails**: a 3σ deviation is supposed to be rare; if returns are fat-tailed, 3σ events happen often enough to ruin a naive sizing model. See [[Fat Tails]].
- **No stop discipline**: "it'll come back" is the famous last words of mean reversion traders without invalidation rules.

**Pairing with HTF context:** even when running a mean-reversion playbook, alignment with the HTF trend matters. A range-extreme fade taken *against* the HTF trend should be sized smaller (or skipped) than the same setup taken *with* the HTF trend.

## Key Equations

**Z-score entry signal** (same as in [[Statistical Arbitrage]]):

$$z = \frac{x_t - \mu}{\sigma}$$

Enter when $|z|$ exceeds a threshold, exit when it returns toward zero.

**Ornstein-Uhlenbeck process** (continuous-time model of mean-reverting dynamics):

$$dX_t = \theta(\mu - X_t)\,dt + \sigma\,dW_t$$

$\theta$ is the speed of reversion, $\mu$ the long-run mean, $\sigma$ the noise scale. Half-life of mean reversion: $\ln(2)/\theta$.

## Resources

- [[Algorithmic Trading — Ernie Chan]] — practical mean reversion implementation
- Avellaneda & Lee (2010) — "Statistical Arbitrage in the U.S. Equities Market"

## Connections

- [[Statistical Arbitrage]] — mean reversion is the dominant stat-arb engine
- [[Cointegration]] — the property that makes a spread tradeable as mean-reverting
- [[Stationarity]] — the underlying statistical requirement
- [[Market Making]] — quoting is mean reversion at the microstructure level
- [[Funding Rate Arbitrage]] — basis mean reversion in perpetual futures
- [[Fat Tails]] — the main reason mean reversion blows up when it does
