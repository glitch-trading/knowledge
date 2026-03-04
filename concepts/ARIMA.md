---
type: concept
title: "ARIMA"
tags:
  - concept
  - statistics
  - time-series
level: 3
prerequisites:
  - "[[Stationarity]]"
  - "[[Autocorrelation]]"
---

# ARIMA (AutoRegressive Integrated Moving Average)

## What It Is

ARIMA is a general-purpose time series model that combines three components:

- **AR (AutoRegressive, order $p$)**: The current value depends linearly on its own past values. "The past predicts the future."
- **I (Integrated, order $d$)**: The series is differenced $d$ times to achieve [[Stationarity]]. Prices → returns is $d=1$.
- **MA (Moving Average, order $q$)**: The current value depends linearly on past forecast errors. "Past surprises persist."

An ARIMA($p, d, q$) model first differences the series $d$ times, then fits an ARMA($p, q$) model:

$$\Phi(B)(1-B)^d X_t = \Theta(B) \epsilon_t$$

Where $B$ is the backshift operator ($BX_t = X_{t-1}$), $\Phi(B)$ is the AR polynomial, and $\Theta(B)$ is the MA polynomial.

**Box-Jenkins methodology:**
1. **Identify**: Plot ACF/PACF of the (differenced) series. ACF cutoff → MA order. PACF cutoff → AR order.
2. **Estimate**: Fit the model via maximum likelihood.
3. **Diagnose**: Check residuals for remaining autocorrelation (Ljung-Box test), normality, heteroskedasticity.
4. **Forecast**: Use the fitted model for out-of-sample prediction.

## Why It Matters

- **Workhorse for mean-reverting processes**: If a spread or return series is mean-reverting, ARIMA (specifically ARMA on the stationary series) can model and forecast it. This is directly useful for mean-reversion trading strategies.
- **Baseline forecasting model**: Before trying complex ML, fit an ARIMA. It often performs surprisingly well and provides an interpretable benchmark.
- **Understanding AR and MA intuition**:
  - AR captures momentum/mean-reversion in levels
  - MA captures how the effect of shocks persists or dies out
  - The combination captures rich temporal dynamics
- **Pairs trading**: The spread in a cointegrated pair is stationary and can be modeled with ARMA. Forecasting the spread → trading signals.
- **Limitations in finance**: Financial returns often have very weak autocorrelation, making ARIMA forecasts nearly equivalent to "predict zero" (the random walk). ARIMA is more useful for spreads, volatility (via GARCH), and macro variables than raw returns.

## Key Equations

**AR(1):**
$$X_t = c + \phi X_{t-1} + \epsilon_t$$

Stationary if $|\phi| < 1$. Mean-reverting: $E[X] = c/(1-\phi)$.

**MA(1):**
$$X_t = \mu + \epsilon_t + \theta \epsilon_{t-1}$$

Always stationary. Shock at time $t$ affects $X_t$ and $X_{t+1}$, then dies.

**ARMA(1,1):**
$$X_t = c + \phi X_{t-1} + \epsilon_t + \theta \epsilon_{t-1}$$

**ARIMA(p,d,q) in backshift notation:**
$$(1 - \phi_1 B - \cdots - \phi_p B^p)(1-B)^d X_t = (1 + \theta_1 B + \cdots + \theta_q B^q) \epsilon_t$$

**Model selection criteria:**
- AIC: $-2\ln(L) + 2k$ (penalizes complexity)
- BIC: $-2\ln(L) + k\ln(n)$ (heavier penalty, favors simpler models)

Choose the model with lowest AIC/BIC.

**Half-life of mean reversion (AR(1)):**
$$t_{1/2} = \frac{-\ln 2}{\ln |\phi|}$$

Useful for pairs trading: how quickly does the spread revert?

## Resources

- Box, Jenkins & Reinsel — *Time Series Analysis: Forecasting and Control* (the original)
- Tsay — *Analysis of Financial Time Series*
- Hyndman & Athanasopoulos — *Forecasting: Principles and Practice*
- `statsmodels` (Python) — ARIMA implementation

## Connections

- [[Time Series Analysis]] — ARIMA is the core model in the Box-Jenkins time series framework
- [[Stationarity]] — The "I" component handles non-stationarity via differencing
- [[Autocorrelation]] — ACF/PACF determine the AR and MA orders
- [[Cointegration]] — Cointegrated spreads can be modeled with ARMA
- [[GARCH]] — Often combined with ARIMA: ARIMA for the mean equation, GARCH for the variance equation
