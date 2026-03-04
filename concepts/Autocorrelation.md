---
type: concept
title: "Autocorrelation"
tags:
  - concept
  - statistics
  - time-series
level: 3
prerequisites: []
---

# Autocorrelation

## What It Is

Autocorrelation (serial correlation) measures how a time series is correlated with lagged versions of itself. It answers: "Does knowing today's value help predict tomorrow's?"

The autocorrelation at lag $k$ is the correlation between $X_t$ and $X_{t-k}$. Plot the autocorrelation for lags $k = 1, 2, 3, \ldots$ and you get the **autocorrelation function (ACF)** — a fundamental diagnostic tool for time series analysis.

**What ACF patterns tell you:**
- **Slowly decaying ACF**: Series is non-stationary or has a strong trend. Needs differencing.
- **Significant positive lag-1 autocorrelation**: Momentum / trending behavior. Today's direction predicts tomorrow's.
- **Significant negative lag-1 autocorrelation**: Mean reversion. Today's move predicts an opposite move tomorrow.
- **Sharp cutoff after lag $q$**: Suggests an MA($q$) process.
- **Exponential decay**: Suggests an AR process.
- **No significant lags**: White noise — no predictable structure. (But check squared returns for volatility clustering.)

**Partial autocorrelation function (PACF):** The correlation between $X_t$ and $X_{t-k}$ after removing the effects of intermediate lags. PACF helps identify the order of AR models — it cuts off sharply after the AR order.

## Why It Matters

- **Strategy selection**: Positive autocorrelation → momentum strategies. Negative autocorrelation → mean reversion strategies. This is the most basic quantitative strategy classification.
- **Market efficiency test**: The efficient market hypothesis implies returns should have zero autocorrelation. Significant autocorrelation = predictability = potential alpha.
- **In practice**: Return autocorrelation at daily frequency in liquid markets is very small (often <0.05) and unstable. At higher frequencies, microstructure effects (bid-ask bounce) create negative autocorrelation. At lower frequencies, momentum effects create positive autocorrelation.
- **Model identification**: ACF and PACF plots are used to determine the appropriate [[ARIMA]] model order — a critical step in time series modeling.
- **Residual diagnostics**: After fitting any model, check that residuals have no remaining autocorrelation (Ljung-Box test). Autocorrelated residuals mean your model is missing structure.

## Key Equations

**Autocorrelation at lag $k$:**
$$\rho_k = \frac{\text{Cov}(X_t, X_{t-k})}{\text{Var}(X_t)} = \frac{E[(X_t - \mu)(X_{t-k} - \mu)]}{\sigma^2}$$

**Sample autocorrelation:**
$$\hat{\rho}_k = \frac{\sum_{t=k+1}^{T}(X_t - \bar{X})(X_{t-k} - \bar{X})}{\sum_{t=1}^{T}(X_t - \bar{X})^2}$$

**Ljung-Box test for joint significance of autocorrelations:**
$$Q = T(T+2) \sum_{k=1}^{m} \frac{\hat{\rho}_k^2}{T-k}$$

Under $H_0$ (no autocorrelation), $Q \sim \chi^2_m$.

**Significance bounds for ACF (approximate):**
$$\pm \frac{1.96}{\sqrt{T}}$$

Values outside these bounds are statistically significant at the 5% level.

## Resources

- Box, Jenkins & Reinsel — *Time Series Analysis: Forecasting and Control*
- Tsay — *Analysis of Financial Time Series*, Chapter 2
- Hyndman & Athanasopoulos — *Forecasting: Principles and Practice*

## Connections

- [[Time Series Analysis]] — Autocorrelation is the primary diagnostic tool for time series
- [[Stationarity]] — Autocorrelation is only meaningful for stationary series
- [[ARIMA]] — ACF/PACF patterns determine ARIMA model order
- [[Variance]] — Autocorrelation affects variance estimation (Newey-West standard errors)
