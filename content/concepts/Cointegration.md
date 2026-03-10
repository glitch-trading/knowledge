---
type: concept
title: "Cointegration"
tags:
  - concept
  - statistics
  - time-series
  - stat-arb
level: 3
prerequisites:
  - "[[Stationarity]]"
  - "[[Regression]]"
---

## What It Is

Two (or more) non-stationary time series are cointegrated if there exists a linear combination of them that is stationary. In plain terms: each series individually wanders randomly (like a random walk), but they are "tethered" together — when they drift apart, they tend to revert back.

**The classic analogy**: A drunk person walking a dog. The person (price A) and the dog (price B) each wander randomly. But the leash (the cointegrating relationship) keeps them from drifting too far apart.

**Formal definition**: If $X_t \sim I(1)$ and $Y_t \sim I(1)$ (both integrated of order 1, i.e., non-stationary but their first differences are stationary), and there exists $\beta$ such that:

$$Z_t = Y_t - \beta X_t \sim I(0) \text{ (stationary)}$$

then $X_t$ and $Y_t$ are cointegrated with cointegrating vector $(1, -\beta)$.

**Key distinction from correlation**: High correlation means two series move together *at each point in time*. Cointegration means two series maintain a long-run equilibrium. You can have high correlation without cointegration, and cointegration without high correlation.

## Why It Matters

- **THE concept for pairs/stat-arb trading**: Cointegration is the theoretical foundation for [[Statistical Arbitrage]]. If two assets are cointegrated, their spread $Z_t$ is mean-reverting — buy when the spread is wide, sell when it narrows.
- **More robust than correlation**: Correlation can be spurious between trending series. Cointegration is a rigorous test for a genuine long-run relationship.
- **Trading signal**: The spread $Z_t$ itself is the trading signal. When $Z_t$ deviates from its mean by more than a threshold (e.g., 2 standard deviations), enter a mean-reversion trade.
- **Hedge ratio**: The cointegrating coefficient $\beta$ is the hedge ratio — how much of one asset to trade against the other.
- **Regime changes**: Cointegration relationships can break down. A pair that was cointegrated may decouple permanently (structural break). This is the primary risk in pairs trading.

## Key Equations

**Cointegrating relationship:**
$$Z_t = Y_t - \beta X_t$$

Where $Z_t$ is stationary (the "spread").

**Engle-Granger two-step procedure:**
1. Regress $Y_t$ on $X_t$: $\hat{\beta} = \frac{\text{Cov}(Y, X)}{\text{Var}(X)}$
2. Test residuals $\hat{Z}_t = Y_t - \hat{\beta} X_t$ for stationarity using ADF test
3. If residuals are stationary → cointegrated

**Error correction model (ECM):**
$$\Delta Y_t = \alpha(Y_{t-1} - \beta X_{t-1}) + \gamma \Delta X_t + \epsilon_t$$

- $\alpha < 0$: speed of adjustment (how fast $Y$ reverts when spread deviates)
- $\beta$: long-run equilibrium ratio
- Combines short-run dynamics ($\Delta X_t$) with long-run equilibrium correction

**Johansen test** (multivariate cointegration):
- Tests for the number of cointegrating relationships among $n$ variables
- Uses VAR framework
- More powerful than Engle-Granger for multiple series

**Half-life of mean reversion:**
$$t_{1/2} = \frac{-\ln 2}{\ln(1 + \alpha)}$$

Where $\alpha$ is the speed of adjustment. Shorter half-life → faster reversion → more trading opportunities.

## Resources

- Engle & Granger (1987) — "Co-integration and Error Correction" (Nobel Prize)
- Johansen (1991) — "Estimation and Hypothesis Testing of Cointegration Vectors"
- Vidyamurthy — *Pairs Trading: Quantitative Methods and Analysis*
- Ernie Chan — *Algorithmic Trading* (practical cointegration for pairs trading)

## Connections

- [[Statistical Arbitrage]] — Cointegration is the theoretical backbone of stat arb
- [[Stationarity]] — The spread must be stationary for the relationship to be tradeable
- [[Time Series Analysis]] — Cointegration is a fundamental concept in multivariate time series
- [[Regression]] — Engle-Granger uses regression as its first step (but with non-standard inference)
- [[ARIMA]] — The spread can be modeled as an ARMA process for forecasting
