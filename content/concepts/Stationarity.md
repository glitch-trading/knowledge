---
type: concept
title: "Stationarity"
tags:
  - concept
  - statistics
  - time-series
level: 3
prerequisites: []
---

## What It Is

A time series is stationary if its statistical properties — mean, variance, and autocorrelation structure — do not change over time. A stationary process looks roughly the same no matter when you observe it. It fluctuates around a constant mean with constant variance.

**Strict stationarity**: The joint distribution of $(X_t, X_{t+1}, \ldots, X_{t+k})$ is the same for all $t$. Very strong condition, rarely tested.

**Weak (covariance) stationarity**: The practical definition:
1. $E[X_t] = \mu$ (constant mean for all $t$)
2. $\text{Var}(X_t) = \sigma^2$ (constant variance for all $t$)
3. $\text{Cov}(X_t, X_{t-k})$ depends only on lag $k$, not on $t$

**Why prices are non-stationary**: Prices have a unit root — they follow a random walk (or random walk with drift). The mean and variance of a random walk grow over time. You cannot meaningfully compute a "mean price" because it keeps changing.

**Why returns are (often) stationary**: Taking log returns $r_t = \ln(P_t/P_{t-1})$ removes the unit root. Returns fluctuate around a roughly constant mean with roughly constant variance (though volatility clustering violates strict stationarity).

**Why spreads can be stationary**: Even though two price series are each non-stationary, their difference (or a linear combination) may be stationary. This is [[Cointegration]] — the foundation of pairs trading.

## Why It Matters

- **Required for most models**: ARMA, regression on time series, autocorrelation analysis — all assume stationarity. Applying these to non-stationary data produces **spurious results** (high $R^2$, significant coefficients that are meaningless).
- **Spurious regression**: Regressing one random walk on another can yield $R^2 > 0.9$ even when the series are completely unrelated. This is the #1 statistical trap in quantitative finance.
- **Transformation is key**: The first step in any time series analysis is checking stationarity and transforming if necessary:
  - Prices → returns (first differences of log prices)
  - Trends → detrend or difference
  - Seasonality → seasonal differencing or decomposition
- **Cointegration testing**: The Engle-Granger procedure for [[Cointegration]] tests whether the residuals of a regression between non-stationary series are stationary. If yes → cointegrated → tradeable spread.

## Key Equations

**Random walk (non-stationary):**
$$P_t = P_{t-1} + \epsilon_t$$

Variance grows with time: $\text{Var}(P_t) = t \sigma^2$

**Differencing to achieve stationarity:**
$$\Delta P_t = P_t - P_{t-1} = \epsilon_t$$

First differences of a random walk are stationary (white noise).

**Augmented Dickey-Fuller (ADF) test:**
$$\Delta X_t = \alpha + \beta t + \gamma X_{t-1} + \sum_{i=1}^{p} \delta_i \Delta X_{t-i} + \epsilon_t$$

- $H_0$: $\gamma = 0$ (unit root present, non-stationary)
- $H_1$: $\gamma < 0$ (stationary)
- Reject $H_0$ → series is stationary

**KPSS test (reversed hypotheses):**
- $H_0$: Series is stationary
- $H_1$: Series has a unit root

Use ADF and KPSS together for robustness. If ADF rejects and KPSS does not → confidently stationary.

## Resources

- Hamilton — *Time Series Analysis*, Chapters 15-17
- Enders — *Applied Econometric Time Series*
- Phillips & Perron (1988) — alternative unit root test
- Kwiatkowski et al. (1992) — KPSS test

## Connections

- [[Time Series Analysis]] — Stationarity is the foundational assumption for time series methods
- [[Cointegration]] — Non-stationary series whose linear combination is stationary
- [[ARIMA]] — The "I" in ARIMA handles non-stationarity through differencing
- [[Autocorrelation]] — Autocorrelation analysis is only valid for stationary series
