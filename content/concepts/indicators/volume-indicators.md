---
type: concept
title: "Volume Indicators"
tags:
  - concept
  - indicators
level: 1
prerequisites:
  - "[[liquidity|Liquidity]]"
---

## What It Is

Volume indicators turn the size dimension of trades into features. Three forms are foundational.

**On-Balance Volume (OBV).** Running sum of volume signed by candle direction:

$$\text{OBV}_t = \text{OBV}_{t-1} + \text{sgn}(P_t - P_{t-1}) \cdot V_t$$

The level is arbitrary; only the *shape* matters. Divergence between price and OBV (price up, OBV flat) is the classical reading.

**Volume Profile.** Histogram of traded volume across price bins over a window. Two derived references:
- **POC** (Point of Control) — the price bin with the most traded volume.
- **Value Area** — the contiguous range around POC containing 70% of total volume.

Volume profile is *price-axis*, not time-axis — it answers "at what prices did transactions happen" rather than "when". Complementary to [[market-profile|Market Profile]], which is time-axis (TPO).

**Cumulative Volume Delta (CVD).** Running sum of *signed-by-trade-aggressor* volume:

$$\text{CVD}_t = \sum_{i \le t} (V_i^{\text{buy}} - V_i^{\text{sell}})$$

Requires per-trade taker side from the exchange (or a tick-rule estimator like Lee-Ready when only OHLCV is available). The candle-direction-signed proxy used in OBV is a poor substitute for CVD when you have access to the real aggressor flag.

## Why It Matters

- **Volume validates moves.** A breakout on weak volume reverts more often than a breakout on heavy volume. Quant version: condition entry-bar return on a volume z-score; the conditional Sharpe is meaningfully higher in the top decile.
- **POC and value area are real intraday reference levels.** Market makers fade the edges of value, takers chase outside it. Order-flow desks anchor stops and targets to these levels; they're the volume analogue of pivot levels.
- **CVD is the cleanest taker-flow gauge available without full L3 data.** Divergence (price ↑, CVD ↓) means takers are selling into a price rise that's being absorbed by passive bids — a classic exhaustion read. Useful as a *feature*, not as a standalone trigger.
- **OBV is mostly historical.** It predates per-trade aggressor data. If you have aggressor flags, prefer CVD; if not, OBV is a noisy approximation. Don't use both — they're nearly collinear.
- **Crypto specifics.** Wash trading inflates exchange-reported volume on smaller venues. Filter by venue (Binance/Bybit/Coinbase USD pairs are mostly clean; many altcoin pairs on lower-tier exchanges are not). On-chain DEX volume is harder to wash but suffers from MEV inflation.

## Key Equations

**Volume-weighted price (the same identity as [[vwap|VWAP]])** — included here because it's the natural "average price" derived from volume:

$$\text{VWAP}_t = \frac{\sum_{i \le t} P_i V_i}{\sum_{i \le t} V_i}$$

**Volume z-score** (the most useful single derived feature):

$$z_t^V = \frac{V_t - \mu_V^{(n)}}{\sigma_V^{(n)}}$$

with rolling mean and std over $n$ bars. Threshold $z_t^V > 2$ flags a volume anomaly.

## Code

```python
import numpy as np, pandas as pd
np.random.seed(7)
n = 60
close = pd.Series(100 * np.exp(np.cumsum(np.random.normal(0.0005, 0.01, n))))
volume = pd.Series(np.random.lognormal(10, 0.5, n))

# OBV
sign = np.sign(close.diff()).fillna(0)
obv = (sign * volume).cumsum()

# Volume profile (5 price bins)
bins = np.linspace(close.min(), close.max(), 6)
vp = volume.groupby(pd.cut(close, bins=bins, include_lowest=True),
                    observed=False).sum()
poc = vp.idxmax()

print(f"OBV[-1]={obv.iloc[-1]:.0f}")
# OBV[-1]=116632
print(f"POC bin={poc}, volume={vp.max():.0f}")
# POC bin=(99.589, 101.096], volume=643720
```

For real CVD you'd replace `sign` with per-trade aggressor side from the exchange feed (Binance `isBuyerMaker`, Bybit `side`, etc.) before aggregating to bar volume.

## Resources

- Joseph Granville — *Granville's New Key to Stock Market Profits* (OBV originator)
- J. Peter Steidlmayer — *Markets and Market Logic* (volume / market profile)
- Lee & Ready (1991) — "Inferring Trade Direction from Intraday Data" (the tick rule for trade-side classification)

## Connections

- [[vwap|VWAP]] — volume-weighted price as benchmark and execution algorithm
- [[liquidity|Liquidity]] — volume is one dimension of liquidity; spread and depth are the others
- [[market-profile|Market Profile]] — TPO complement to volume profile; same value-area / POC vocabulary on a time axis
- [[vpin|VPIN]] — volume-clock-based informed-flow estimator; conceptually downstream of CVD
- [[order-book|Order Book]] — CVD aggregates the trade-execution side of book events
