---
type: book
title: "Analysis of Financial Time Series"
author: "Ruey S. Tsay"
status: not-started
tags:
  - book
  - time-series
  - econometrics
level: 3
topics:
  - "[[time-series-analysis|Time Series Analysis]]"
  - "[[arima|ARIMA]]"
  - "[[garch|GARCH]]"
  - "[[autocorrelation|Autocorrelation]]"
  - "[[stationarity|Stationarity]]"
  - "[[cointegration|Cointegration]]"
---

## Key Takeaways

- Financial returns exhibit volatility clustering, fat tails, and leverage effects — standard ARMA models are insufficient without GARCH-type extensions
- Autocorrelation analysis distinguishes predictable structure from noise in return series
- Cointegration is the mathematical foundation of pairs trading and cross-venue arbitrage — two non-stationary series whose spread is mean-reverting
- Multivariate volatility models (DCC, BEKK) capture time-varying correlations critical for portfolio risk

## What It Covers

Chapters 1-3: linear time series models (AR, MA, ARMA, ARIMA), unit root tests, stationarity. Chapter 3: conditional heteroskedastic models (ARCH, GARCH, EGARCH). Chapter 8: multivariate time series, cointegration, vector autoregression. The standard academic reference for financial time series econometrics.

## Resources

- [[algorithmic-trading-ernie-chan|Algorithmic Trading — Ernie Chan]] — Code-first approach to cointegration strategies
- [[level-3-hands-on-niche-markets|Level 3 — Hands-On Niche Markets]] — Where this fits in the roadmap
