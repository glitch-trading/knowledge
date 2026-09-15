---
type: concept
title: "Bollinger Bands"
tags:
  - concept
  - indicators
level: 1
prerequisites:
  - "[[moving-average|Moving Average]]"
---

## What It Is

Bollinger Bands wrap a [[moving-average|moving average]] with two volatility envelopes set at a fixed number of rolling standard deviations above and below. The default parameters are a 20-period SMA and $k=2$.

$$\text{mid}_t = \text{SMA}_t^{(n)}, \qquad \sigma_t = \sqrt{\frac{1}{n}\sum_{i=0}^{n-1}(P_{t-i} - \text{mid}_t)^2}$$

$$\text{upper}_t = \text{mid}_t + k\sigma_t, \qquad \text{lower}_t = \text{mid}_t - k\sigma_t$$

Two derived features matter more than the bands themselves:

- **%B** — where price sits inside the channel:
$$\%B_t = \frac{P_t - \text{lower}_t}{\text{upper}_t - \text{lower}_t}$$
$\%B = 0$ at the lower band, $0.5$ at the mid, $1$ at the upper band, and outside $[0,1]$ when price punches through.

- **Bandwidth** — the relative width of the channel, a non-parametric vol gauge:
$$\text{BW}_t = \frac{\text{upper}_t - \text{lower}_t}{\text{mid}_t} = \frac{2k\sigma_t}{\text{mid}_t}$$

## Why It Matters

- **Bandwidth squeeze is a regime feature, not a signal.** When BW drops to a multi-month low, realized vol is unusually compressed; the conditional distribution of the *next* large move's magnitude is wider than usual. The squeeze does not tell you direction — pair it with a directional trigger ([[macd|MACD]] cross, breakout above a horizontal level, [[atr|ATR]] expansion).
- **Band tags are not signals either.** "Touch upper band, sell" loses in a trend (price walks the upper band for weeks). The band tag is a feature whose conditional return depends on [[mean-reversion|regime]]: in range, mean-reverting; in trend, continuation.
- **The Gaussian assumption is wrong but useful.** $k=2$ would contain 95% of observations under normality. Real return distributions are [[fat-tails|fat-tailed]], so band breaks happen more often than 5% of the time — that's *why* the band-tag mean-reversion trade has poor unconditional edge.
- **Bandwidth is comparable across assets** in a way that raw $\sigma$ is not — it's normalized by price level. Use BW percentiles (e.g., bottom-20% historical BW) rather than absolute thresholds when screening across a universe.

## Key Equations

**Wilder-smoothed (EMA) Bollinger variant** — replaces the SMA mid with an EMA, less common but reduces edge effects in low-bar regimes:

$$\text{mid}_t = \text{EMA}_t^{(n)}, \qquad \sigma_t^2 = (1-\alpha)\sigma_{t-1}^2 + \alpha(P_t - \text{mid}_{t-1})^2$$

**Keltner channel** (the close cousin, often paired): replaces $k\sigma$ with $k \cdot \text{ATR}$. Bollinger contracts faster on quiet markets; Keltner contracts less, so a Bollinger-inside-Keltner condition is a stronger squeeze.

## Code

```python
import numpy as np, pandas as pd
np.random.seed(7)
close = pd.Series(100 * np.exp(np.cumsum(np.random.normal(0.0005, 0.01, 60))))

n, k = 20, 2
mid = close.rolling(n).mean()
sd = close.rolling(n).std(ddof=0)
upper, lower = mid + k * sd, mid - k * sd
bw = (upper - lower) / mid
pctb = (close - lower) / (upper - lower)

print(f"mid={mid.iloc[-1]:.4f}  upper={upper.iloc[-1]:.4f}  "
      f"lower={lower.iloc[-1]:.4f}")
print(f"bandwidth={bw.iloc[-1]:.4f}  %B={pctb.iloc[-1]:.4f}")
# mid=98.8702  upper=101.7687  lower=95.9717
# bandwidth=0.0586  %B=0.7912
```

A BW of 0.0586 means the channel spans ~5.9% of price; a $\%B$ of 0.79 means price is about 79% of the way from the lower to the upper band — extended but not punched through.

## Resources

- John Bollinger — *Bollinger on Bollinger Bands* (the originator's text)
- John Murphy — *Technical Analysis of the Financial Markets* (Ch. 14)

## Connections

- [[moving-average|Moving Average]] — the mid band; choice of SMA vs. EMA changes character materially
- [[atr|ATR]] — Keltner channels swap $k\sigma$ for $k \cdot \text{ATR}$; ATR-based bands react less to outliers
- [[mean-reversion|Mean Reversion]] — band-tag fades are a textbook MR setup, only viable in range regimes
- [[fat-tails|Fat Tails]] — why 2σ breaks happen far more often than the Gaussian assumption implies
