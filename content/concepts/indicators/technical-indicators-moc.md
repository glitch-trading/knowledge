---
title: "Technical Indicators — Map of Content"
type: MOC
tags:
  - MOC
  - indicators
---

Indicators are deterministic transforms of OHLCV history. They compress price/volume into a small number of features that downstream rules consume — entries, exits, regime filters, sizing overlays. None of them carry edge on their own; the edge is in how the feature is used, what timeframe it is computed on, and what regime conditions you apply it under.

## Trend / Smoothing
- [[moving-average|Moving Average]] (SMA, EMA, WMA) — the foundational smoother; basis for almost every other indicator
- [[macd|MACD]] — difference of two EMAs with a signal-line EMA on top

## Volatility / Bands
- [[bollinger-bands|Bollinger Bands]] — rolling mean ± $k\sigma$; used for mean-reversion bands and "squeeze" regime detection
- [[atr|ATR]] — Average True Range; the standard non-parametric volatility scale used for stops and position sizing

## Momentum / Oscillators
- [[rsi|RSI]] — bounded momentum oscillator over a fixed lookback
- [[macd|MACD]] — momentum *and* trend; the signal-line cross is the most common discretionary trigger

## Volume
- [[volume-indicators|Volume Indicators]] — OBV, volume profile, cumulative volume delta
- [[vwap|VWAP]] — volume-weighted average price; both a benchmark and an intraday reference

## How to think about indicators in a quant context
- **They are features, not strategies.** A 14-period RSI < 30 is not a buy signal — it is a feature whose conditional return distribution you have to measure.
- **Lookback choice dominates.** The same indicator on a 5m chart vs. a 1d chart is effectively a different feature. Sweep lookbacks; don't accept defaults.
- **Most indicators are correlated.** RSI, stochastic, Williams %R, CCI — high pairwise correlation. Use one momentum, one trend, one volatility, one volume; stacking redundant ones is overfitting.
- **Path-dependence matters.** EMA-based features depend on the entire history before your backtest window; truncate the warmup or your early bars are garbage.
- **Indicators interact with regime.** A mean-reversion band fade and a trend-following EMA cross are *opposite* trades on the same price. Use [[bollinger-bands|Bollinger Bands]] squeeze or [[atr|ATR]] expansion to condition which playbook is active.

## Related
- [[mean-reversion|Mean Reversion]] — Bollinger Bands and RSI extremes are canonical inputs
- [[momentum|Momentum]] — MACD and price-vs-MA crosses are the canonical trend signals
- [[market-profile|Market Profile]] — TPO-based structural reference, complementary to volume profile
- [[overfitting|Overfitting]] — indicator parameter sweeps are a primary source of in-sample overfit
