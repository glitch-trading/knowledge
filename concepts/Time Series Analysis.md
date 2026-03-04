---
type: concept
title: "Time Series Analysis"
tags:
  - concept
  - statistics
  - econometrics
level: 3
prerequisites: []
---

# Time Series Analysis

## What It Is

Time series analysis is the study of data points collected sequentially over time. Financial data is inherently time series data — prices, returns, volume, spreads, and order flow are all indexed by time and exhibit temporal dependencies.

Unlike cross-sectional data (comparing different entities at one point in time), time series data has a natural ordering that creates structure: what happened yesterday affects what happens today. Exploiting this temporal structure is the foundation of many quantitative trading strategies.

**Core concepts:**
- **[[Stationarity]]**: Are the statistical properties (mean, variance) constant over time? Most time series methods require stationarity.
- **[[Autocorrelation]]**: Is the series correlated with its own past values? This is the basis of AR models and mean-reversion strategies.
- **Trend and seasonality**: Long-term drift and periodic patterns. Must be removed or modeled before applying stationary methods.
- **Volatility clustering**: Big moves follow big moves ([[GARCH]]). Returns may be uncorrelated, but squared returns are highly autocorrelated.

**Major model families:**
- **[[ARIMA]]**: Models for level/return prediction. AR (past values predict future), I (differencing for stationarity), MA (past errors predict future).
- **[[GARCH]]**: Models for volatility prediction. Captures the conditional heteroskedasticity in financial returns.
- **[[Cointegration]]**: Models for spread prediction. Two non-stationary series whose linear combination is stationary.
- **VAR (Vector Autoregression)**: Multivariate extension — multiple time series predicting each other.

## Why It Matters

- **Financial data IS time series**: You cannot do quantitative finance without time series analysis. Every price chart, every backtest, every signal is a time series problem.
- **Mean reversion detection**: Autocorrelation analysis tells you if a series is mean-reverting (negative autocorrelation) or trending (positive autocorrelation) — directly informing strategy choice.
- **Forecasting**: ARIMA, GARCH, and their extensions are workhorses for forecasting returns, volatility, and spreads.
- **Pitfalls are severe**: Applying standard regression to non-stationary time series produces spurious results (meaningless high $R^2$). Understanding stationarity and cointegration prevents this.
- **Feature engineering for ML**: Even when using ML models, the features you construct (lagged returns, rolling statistics, volatility estimates) are fundamentally time series transformations.

## Key Equations

**Autoregressive model AR(p):**
$$X_t = c + \sum_{i=1}^{p} \phi_i X_{t-i} + \epsilon_t$$

**Moving Average model MA(q):**
$$X_t = \mu + \sum_{j=1}^{q} \theta_j \epsilon_{t-j} + \epsilon_t$$

**ARMA(p,q):**
$$X_t = c + \sum_{i=1}^{p} \phi_i X_{t-i} + \sum_{j=1}^{q} \theta_j \epsilon_{t-j} + \epsilon_t$$

**Autocorrelation function (ACF):**
$$\rho_k = \frac{\text{Cov}(X_t, X_{t-k})}{\text{Var}(X_t)}$$

**Augmented Dickey-Fuller test statistic (for stationarity):**
$$\Delta X_t = \alpha + \beta t + \gamma X_{t-1} + \sum \delta_i \Delta X_{t-i} + \epsilon_t$$

Test $H_0: \gamma = 0$ (unit root, non-stationary).

## Resources

- Hamilton — *Time Series Analysis* (comprehensive reference)
- Tsay — *Analysis of Financial Time Series*
- Enders — *Applied Econometric Time Series*
- Hyndman & Athanasopoulos — *Forecasting: Principles and Practice* (free online)

## Connections

- [[Autocorrelation]] — The fundamental diagnostic tool for time series dependence
- [[Stationarity]] — The critical assumption underlying most time series models
- [[ARIMA]] — The workhorse model for stationary/differenced time series
- [[Cointegration]] — Time series relationship between non-stationary series
- [[GARCH]] — Time series model for volatility dynamics
