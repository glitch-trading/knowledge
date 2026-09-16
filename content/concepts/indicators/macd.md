---
type: concept
title: "MACD"
tags:
  - concept
  - indicators
level: 1
prerequisites:
  - "[[moving-average|Moving Average]]"
---

## What It Is

Moving Average Convergence Divergence is the difference between a fast and slow EMA, with a third EMA on top as a signal line. The default parameters are $(12, 26, 9)$.

$$\text{MACD}_t = \text{EMA}_t^{(12)} - \text{EMA}_t^{(26)}$$
$$\text{signal}_t = \text{EMA}^{(9)}(\text{MACD})_t$$
$$\text{hist}_t = \text{MACD}_t - \text{signal}_t$$

The MACD line filters price through the difference of two EMAs. The signal line smooths MACD once more. The histogram is their residual: its zero crossing is the MACD/signal crossing, not an earlier event. Changes in histogram slope may precede a crossing, but do not guarantee one.

## Why It Matters

- **It's both a trend and momentum indicator.** The sign of MACD tells you the medium-term trend (fast EMA above or below slow). The slope of MACD tells you momentum (fast EMA pulling away or converging back). One feature, two readings — which is why it shows up so often.
- **The signal-line cross is the most-traded technical event in TradFi.** Like all crossover systems, it loses in chop and pays in trends. Unconditional edge is small; conditional edge (cross from below zero in expanding [[atr|ATR]], for example) can be material.
- **Zero-line cross matters more than signal cross for trend confirmation.** MACD crossing zero means the fast EMA crossed the slow EMA — the textbook "golden / death cross" but on a shorter horizon.
- **Histogram divergence is leading.** When MACD is still making new highs but the histogram is shrinking, momentum is decelerating. A histogram peak typically precedes a MACD-signal cross by several bars.
- **Parameter sensitivity is real.** (12, 26, 9) are not magic — they're Gerald Appel's defaults from the 1970s for daily stock data. On intraday crypto, retest the parameter grid; the optimum drifts with bar size and asset volatility.
- **It's correlated with price-MA crosses.** $\text{MACD} > 0 \iff \text{EMA}_{12} > \text{EMA}_{26}$. If you already have a 12/26 EMA cross in your feature set, MACD adds smoothing but not new information.

## Key Equations

**Histogram as a derivative approximation.** With $f = \text{EMA}^{(12)} - \text{EMA}^{(26)}$, $\text{hist} = f - \text{EMA}^{(9)}(f)$ removes a smoothed component of $f$. At low frequencies this behaves approximately like a scaled second derivative of price. It is a discrete filter, not an exact derivative or a forecast.

**Percent MACD** (normalized for cross-asset comparability):

$$\text{MACD\%}_t = \frac{\text{EMA}_t^{(12)} - \text{EMA}_t^{(26)}}{\text{EMA}_t^{(26)}}$$

Use this when comparing MACD readings across assets at different price levels.

## Code

```python
import numpy as np, pandas as pd
np.random.seed(7)
close = pd.Series(100 * np.exp(np.cumsum(np.random.normal(0.0005, 0.01, 60))))

ema12 = close.ewm(span=12, adjust=False).mean()
ema26 = close.ewm(span=26, adjust=False).mean()
macd = ema12 - ema26
signal = macd.ewm(span=9, adjust=False).mean()
hist = macd - signal

print(f"MACD={macd.iloc[-1]:.6f}  signal={signal.iloc[-1]:.6f}  "
      f"hist={hist.iloc[-1]:.6f}")
# MACD=0.315832  signal=0.115484  hist=0.200348
```

MACD above signal with a positive histogram is the canonical "fast EMA pulling away from slow" reading — momentum aligned with trend.

## Resources

- Gerald Appel — *Technical Analysis: Power Tools for Active Investors* (the originator's text)
- John Murphy — *Technical Analysis of the Financial Markets* (Ch. 9)

## Connections

- [[moving-average|Moving Average]] — MACD is constructed entirely from three EMAs
- [[rsi|RSI]] — RSI is bounded, MACD is unbounded; pair for trend (MACD) + extremity (RSI)
- [[bollinger-bands|Bollinger Bands]] — MACD signals are stronger when triggered out of a BW squeeze
- [[momentum|Momentum]] — MACD is the discretionary trader's momentum proxy; cross-sectional quant momentum uses raw returns
- [[overfitting|Overfitting]] — sweeping (12, 26, 9) over many assets without an out-of-sample test is a classic overfit
