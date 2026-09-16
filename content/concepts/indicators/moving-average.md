---
type: concept
title: "Moving Average"
tags:
  - concept
  - indicators
level: 1
prerequisites: []
---

## What It Is

A moving average is a rolling smoother of a price series. It trades responsiveness for stability — a longer window filters more noise but lags more behind the current price. Three forms dominate.

**Simple Moving Average (SMA).** Equal weight to the last $n$ closes.

$$\text{SMA}_t^{(n)} = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}$$

**Exponential Moving Average (EMA).** Recursive, geometrically decaying weights — the most recent observation gets the most weight and older observations decay smoothly to zero.

$$\text{EMA}_t = \alpha P_t + (1-\alpha)\,\text{EMA}_{t-1}, \qquad \alpha = \frac{2}{n+1}$$

The $\alpha = 2/(n+1)$ convention makes the EMA's *center of mass* equal to the SMA's center of mass for the same $n$ — comparable smoothing strength, different lag profile.

**Weighted Moving Average (WMA).** Linear weights $1, 2, \dots, n$ over the last $n$ closes.

$$\text{WMA}_t^{(n)} = \frac{\sum_{i=0}^{n-1} (n-i)\,P_{t-i}}{\sum_{i=1}^{n} i}$$

## Why It Matters

- **The foundation of almost every other indicator.** [[bollinger-bands|Bollinger Bands]] is an SMA ± $k\sigma$. [[macd|MACD]] is the difference of two EMAs. [[atr|ATR]] is an EMA of true range. RSI's "smoothed gain / loss" is an EMA (Wilder form, $\alpha = 1/n$).
- **EMA vs. SMA lag.** SMA lag is roughly $(n-1)/2$ bars. EMA effective lag is similar in expectation but the EMA reacts to new observations immediately (no cliff at $t-n$), which is why crossover systems and live signal generation almost always use EMAs.
- **Path dependence.** The EMA at bar $t$ depends on every bar back to $t=0$. In a backtest, you must either burn in long enough for the recursion to converge (a few hundred bars at most $n$) or seed it from the SMA of the first $n$ bars. Cutting the warmup is a silent source of biased early P&L.
- **Crossover signals.** "Fast MA crosses slow MA" (e.g., 50/200 golden cross) is the canonical [[momentum|momentum]] trigger. It works because the difference of two MAs is a low-pass-filtered first derivative of price.
- **Where they fail.** In a range, every MA cross is a whipsaw. MA systems lose continuously in chop and recoup on a small number of large trending moves — sizing has to assume long losing streaks.

## Key Equations

**SMA recursive update** (useful for streaming):

$$\text{SMA}_t = \text{SMA}_{t-1} + \frac{P_t - P_{t-n}}{n}$$

**EMA recursive form** (the one you actually implement):

$$\text{EMA}_t = \alpha\,(P_t - \text{EMA}_{t-1}) + \text{EMA}_{t-1}$$

**Center of mass and half-life.** For an EMA with smoothing $\alpha$:

$$\text{CoM} = \frac{1-\alpha}{\alpha}, \qquad \text{half-life} = \frac{\ln 2}{-\ln(1-\alpha)}$$

The half-life is the number of bars after which an observation's weight decays to 50%. A 10-period EMA ($\alpha = 2/11 \approx 0.182$) has a half-life of about 3.8 bars.

## Code

```python
import numpy as np, pandas as pd
np.random.seed(7)
close = pd.Series(100 * np.exp(np.cumsum(np.random.normal(0.0005, 0.01, 60))))

n = 10
sma = close.rolling(n).mean()
ema = close.ewm(span=n, adjust=False).mean()  # alpha = 2/(n+1)
w = np.arange(1, n + 1)
wma = close.rolling(n).apply(lambda x: np.dot(x, w) / w.sum(), raw=True)

print(f"close={close.iloc[-1]:.4f}  SMA={sma.iloc[-1]:.4f}  "
      f"EMA={ema.iloc[-1]:.4f}  WMA={wma.iloc[-1]:.4f}")
# close=100.5585  SMA=99.9334  EMA=99.5693  WMA=99.8585
```

There is no universal lag ranking across price paths. On a steady linear trend after warmup, this SMA and EMA both lag by $(n-1)/2$ bars; the linearly weighted WMA lags by $(n-1)/3$. For $n=10$, those lags are 4.5, 4.5, and 3 bars. The synthetic path above is not a steady trend.

## Resources

- John Murphy — *Technical Analysis of the Financial Markets* (Chs. 9-11)
- Hyndman & Athanasopoulos — *Forecasting: Principles and Practice* (exponential smoothing chapter)

## Connections

- [[bollinger-bands|Bollinger Bands]] — mid band is an SMA; the entire indicator is MA ± $k\sigma$
- [[macd|MACD]] — built from three EMAs
- [[atr|ATR]] — Wilder-smoothed EMA of true range
- [[rsi|RSI]] — gains/losses are smoothed with a Wilder EMA ($\alpha = 1/n$)
- [[momentum|Momentum]] — MA crossovers are the canonical trend-following trigger
- [[mean-reversion|Mean Reversion]] — single-asset MR uses deviation from an MA as the signal
