---
type: concept
title: "ATR"
tags:
  - concept
  - indicators
level: 1
prerequisites:
  - "[[moving-average|Moving Average]]"
---

## What It Is

Average True Range is the Wilder-smoothed average of *true range*, a non-parametric per-bar volatility measure that accounts for overnight gaps.

True range for bar $t$ is the max of three candidates:

$$\text{TR}_t = \max\left(H_t - L_t,\; |H_t - C_{t-1}|,\; |L_t - C_{t-1}|\right)$$

The first term is the intra-bar range; the second and third capture moves through the prior close (gaps). Then:

$$\text{ATR}_t = (1 - \alpha)\,\text{ATR}_{t-1} + \alpha \cdot \text{TR}_t, \qquad \alpha = \tfrac{1}{n}$$

Default $n = 14$. ATR is denominated in *price units* — same scale as the asset — which is why ATR-percent ($\text{ATR}_t / P_t$) is what you actually use for cross-asset comparison.

## Why It Matters

- **ATR is the standard input to position sizing.** "Risk 1% of equity per trade with a stop at $2 \cdot \text{ATR}$" turns into $\text{shares} = (0.01 \cdot \text{equity}) / (2 \cdot \text{ATR})$. This is how every chart-based trading book sizes positions and how most discretionary desks operate. The quant generalization is volatility-scaling, where ATR is the simplest realized-vol estimator.
- **It's non-parametric.** ATR makes no distributional assumption — useful in [[fat-tails|fat-tailed]] regimes where standard-deviation-based vol underestimates tail moves. It tracks realized close-to-close vol fairly well in practice but reacts faster to gaps.
- **Stop placement.** A "structural stop + ATR buffer" is the standard combination: identify the invalidation level from price structure (swing low, support), then add a $0.5\text{–}1.0 \cdot \text{ATR}$ buffer so normal noise doesn't take you out before invalidation.
- **Regime detection.** ATR percentile over a rolling window is a clean regime feature. Top quintile = high-vol regime, condition strategy choice on it. Many trend-following systems require ATR expanding to enter — entries during ATR contraction are mostly chop.
- **Keltner channels use ATR for their band width** instead of $k\sigma$ ([[bollinger-bands|Bollinger]] uses standard deviation). ATR-bands are slower to contract on quiet markets, which makes the "Bollinger inside Keltner" condition a stronger squeeze.

## Key Equations

**Chandelier exit** (Charles Le Beau's trailing stop, the classic ATR application):

$$\text{exit}_t^{\text{long}} = \max_{i \le t} H_i - k \cdot \text{ATR}_t, \qquad k \in [2.5, 3.5]$$

A long position trails its stop at $k$-ATRs below the highest high since entry.

**Volatility-scaled position size:**

$$N = \frac{r \cdot E}{m \cdot \text{ATR}}$$

where $r$ is fractional risk per trade (e.g., 0.01), $E$ is account equity, and $m$ is the ATR-multiple for the stop (e.g., 2.0). $N$ is contract / share count.

## Code

```python
import numpy as np, pandas as pd
np.random.seed(7)
n = 60
close = pd.Series(100 * np.exp(np.cumsum(np.random.normal(0.0005, 0.01, n))))
high = close * (1 + np.abs(np.random.normal(0, 0.005, n)))
low = close * (1 - np.abs(np.random.normal(0, 0.005, n)))

prev_close = close.shift(1)
tr = pd.concat([
    high - low,
    (high - prev_close).abs(),
    (low - prev_close).abs(),
], axis=1).max(axis=1)
atr = tr.ewm(alpha=1/14, adjust=False).mean()

print(f"TR={tr.iloc[-1]:.4f}  ATR(14)={atr.iloc[-1]:.4f}  "
      f"ATR%={atr.iloc[-1]/close.iloc[-1]*100:.4f}%")
# TR=2.1210  ATR(14)=1.2625  ATR%=1.2555%
```

ATR% of ~1.26% per bar is a moderate-volatility reading for this synthetic series (annualized $\sigma$ of about 16% if these were daily bars).

## Resources

- J. Welles Wilder Jr. — *New Concepts in Technical Trading Systems* (1978, the originating text)
- Curtis Faith — *Way of the Turtle* (ATR-based "N" for sizing, the original Turtle Traders system)

## Connections

- [[position-sizing|Position Sizing]] — the standard input to risk-per-trade sizing rules
- [[kelly-criterion|Kelly Criterion]] — full-Kelly sizing requires a vol estimate; ATR is the discretionary version
- [[bollinger-bands|Bollinger Bands]] / Keltner — ATR-bands vs. σ-bands; the pair gives a squeeze signal
- [[moving-average|Moving Average]] — ATR is a Wilder EMA ($\alpha = 1/n$) of true range
- [[fat-tails|Fat Tails]] — ATR is more robust to tail bars than rolling close-to-close std
