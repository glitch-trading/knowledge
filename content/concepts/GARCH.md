---
type: concept
title: "GARCH"
tags:
  - concept
  - statistics
  - time-series
  - volatility
level: 3
prerequisites:
  - "[[Time Series Analysis]]"
---

## What It Is

GARCH models capture one of the most prominent features of financial returns: **volatility clustering** — periods of high volatility tend to be followed by high volatility, and calm periods tend to be followed by calm periods. Returns themselves may be uncorrelated, but their magnitudes (squared returns) are highly autocorrelated.

"Conditional heteroskedasticity" means the variance of returns changes over time and depends on past information. GARCH models this time-varying variance explicitly.

**GARCH(1,1)** — the workhorse model:
$$r_t = \mu + \epsilon_t, \quad \epsilon_t = \sigma_t z_t, \quad z_t \sim N(0,1)$$
$$\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$

- $\omega$: baseline variance (long-run)
- $\alpha$: reaction to recent shocks (how much yesterday's surprise matters)
- $\beta$: persistence (how much yesterday's volatility carries forward)
- $\alpha + \beta < 1$: stationarity condition. Closer to 1 = more persistent volatility.

The model says: tomorrow's variance is a weighted average of the long-run variance ($\omega/(1-\alpha-\beta)$), yesterday's squared shock ($\epsilon_{t-1}^2$), and yesterday's variance ($\sigma_{t-1}^2$).

## Why It Matters

- **Volatility forecasting**: GARCH provides a principled way to forecast next-period volatility. This is critical for options pricing, risk management, and position sizing.
- **Risk management**: VaR and Expected Shortfall estimates are much better when using GARCH volatility instead of historical volatility, because GARCH adapts to current market conditions.
- **Position sizing**: Kelly criterion and risk parity both depend on volatility estimates. GARCH gives you a responsive, forward-looking estimate.
- **Options trading**: Implied volatility should relate to expected realized volatility. GARCH forecasts of realized vol help identify mispriced options.
- **Stylized facts it captures**:
  - Volatility clustering
  - Fat tails in returns (even with normal innovations, time-varying variance produces unconditional fat tails)
  - Mean reversion in volatility (variance reverts to $\omega/(1-\alpha-\beta)$)

**Extensions:**
- **EGARCH**: Allows asymmetric response (negative returns increase vol more than positive — the leverage effect)
- **GJR-GARCH**: Another asymmetric specification
- **GARCH-M**: Includes volatility in the mean equation (risk premium)

## Key Equations

**GARCH(1,1):**
$$\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$

**Long-run (unconditional) variance:**
$$\bar{\sigma}^2 = \frac{\omega}{1 - \alpha - \beta}$$

**Volatility half-life (how fast vol reverts to long-run level):**
$$t_{1/2} = \frac{\ln 2}{-\ln(\alpha + \beta)}$$

**General GARCH(p,q):**
$$\sigma_t^2 = \omega + \sum_{i=1}^{q} \alpha_i \epsilon_{t-i}^2 + \sum_{j=1}^{p} \beta_j \sigma_{t-j}^2$$

**EGARCH (asymmetric effects):**
$$\ln(\sigma_t^2) = \omega + \alpha \left(\frac{|\epsilon_{t-1}|}{\sigma_{t-1}} - \sqrt{2/\pi}\right) + \gamma \frac{\epsilon_{t-1}}{\sigma_{t-1}} + \beta \ln(\sigma_{t-1}^2)$$

The $\gamma$ term captures asymmetry: negative $\gamma$ means negative shocks increase volatility more.

**Typical parameter estimates (daily equity returns):**
- $\alpha \approx 0.05-0.10$ (shock reaction)
- $\beta \approx 0.85-0.95$ (persistence)
- $\alpha + \beta \approx 0.95-0.99$ (high persistence)

## Resources

- Engle (1982) — "Autoregressive Conditional Heteroskedasticity" (ARCH, Nobel Prize)
- Bollerslev (1986) — "Generalized Autoregressive Conditional Heteroskedasticity" (GARCH)
- Tsay — *Analysis of Financial Time Series*, Chapter 3
- `arch` package (Python) — GARCH implementation

## Connections

- [[Time Series Analysis]] — GARCH is the standard model for the variance equation in financial time series
- [[Variance]] — GARCH models the conditional variance as a time-varying process
- [[ARIMA]] — Often paired: ARIMA for the conditional mean, GARCH for the conditional variance
- [[Stationarity]] — GARCH requires $\alpha + \beta < 1$ for variance stationarity
