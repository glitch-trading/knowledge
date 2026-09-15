---
type: concept
title: "RSI"
tags:
  - concept
  - indicators
level: 1
prerequisites:
  - "[[moving-average|Moving Average]]"
---

## What It Is

The Relative Strength Index is a bounded oscillator that compares smoothed average gains to smoothed average losses over a lookback window (default 14). Output sits in $[0, 100]$.

Let $\Delta_t = P_t - P_{t-1}$ and split into positive and negative parts:

$$U_t = \max(\Delta_t, 0), \qquad D_t = -\min(\Delta_t, 0)$$

Smooth both with Wilder's method (an EMA with $\alpha = 1/n$):

$$\overline{U}_t = (1-\alpha)\,\overline{U}_{t-1} + \alpha U_t, \qquad \overline{D}_t = (1-\alpha)\,\overline{D}_{t-1} + \alpha D_t$$

Then:

$$\text{RS}_t = \frac{\overline{U}_t}{\overline{D}_t}, \qquad \text{RSI}_t = 100 - \frac{100}{1 + \text{RS}_t}$$

Equivalently, $\text{RSI}_t = 100 \cdot \overline{U}_t / (\overline{U}_t + \overline{D}_t)$ — the smoothed share of total absolute movement that was up.

## Why It Matters

- **Bounded means comparable across regimes.** Unlike raw return momentum, RSI has the same scale on every asset and every timeframe. Useful for cross-sectional ranking and as a feature in a regression.
- **The "70/30" trade is largely folklore.** Unconditional "buy at RSI < 30, sell at RSI > 70" loses in trending markets — RSI sits below 30 for weeks during a strong downtrend. The setup only works when conditioned on a [[mean-reversion|mean-reverting]] regime (range, contracted [[bollinger-bands|Bollinger]] BW, low [[atr|ATR]] percentile).
- **Divergence is the standard discretionary read.** Price makes a new high, RSI doesn't → bearish divergence. Treat as a *feature* whose forward edge you must measure, not a deterministic signal.
- **Lookback matters more than thresholds.** RSI(2) (Larry Connors' setup) is essentially a one-bar gain/loss filter — sharp, noisy, used for short-horizon MR. RSI(14) is the default. RSI(50) approaches a slow trend feature. Don't reuse the same 70/30 thresholds across these lookbacks — they have completely different distributions.
- **Stochastic, Williams %R, CCI are close cousins.** All are bounded momentum oscillators with near-identical conditional information. Pick one; don't stack them.

## Key Equations

**Wilder smoothing in EMA form** — equivalent to the original "running average":

$$\overline{X}_t = \overline{X}_{t-1} + \frac{X_t - \overline{X}_{t-1}}{n}$$

This corresponds to $\alpha = 1/n$, not the $\alpha = 2/(n+1)$ used in standard EMAs. A Wilder-14 ≈ a span-27 EMA in [[moving-average|standard EMA convention]] — a common silent bug when porting code between libraries.

**RSI as smoothed share of up-movement:**

$$\text{RSI}_t = 100 \cdot \frac{\overline{U}_t}{\overline{U}_t + \overline{D}_t}$$

## Code

```python
import numpy as np, pandas as pd
np.random.seed(7)
close = pd.Series(100 * np.exp(np.cumsum(np.random.normal(0.0005, 0.01, 60))))

def rsi(s, n=14):
    d = s.diff()
    up = d.clip(lower=0)
    dn = -d.clip(upper=0)
    # Wilder smoothing == EMA with alpha = 1/n
    au = up.ewm(alpha=1/n, adjust=False).mean()
    ad = dn.ewm(alpha=1/n, adjust=False).mean()
    return 100 - 100 / (1 + au / ad)

print(f"RSI(14) = {rsi(close, 14).iloc[-1]:.4f}")
# RSI(14) = 56.6954
```

A reading of 56.7 is mid-range — neither overbought nor oversold under the 70/30 convention.

## Resources

- J. Welles Wilder Jr. — *New Concepts in Technical Trading Systems* (1978, the originating text)
- Larry Connors & Cesar Alvarez — *Short Term Trading Strategies That Work* (RSI(2) variant and conditional-edge framing)

## Connections

- [[moving-average|Moving Average]] — Wilder smoothing is an EMA with $\alpha=1/n$ (not the $2/(n+1)$ default)
- [[macd|MACD]] — both are momentum indicators; MACD is unbounded, RSI is bounded
- [[bollinger-bands|Bollinger Bands]] — RSI is to momentum what %B is to price location; pair for confirmation
- [[mean-reversion|Mean Reversion]] — RSI extremes are a textbook MR feature, valid only in range regimes
- [[stationarity|Stationarity]] — RSI is bounded, hence stationary by construction; raw price is not
