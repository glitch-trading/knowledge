---
type: concept
title: "Fama-French Factor Model"
tags:
  - concept
  - factor-models
  - asset-pricing
level: 3
prerequisites:
  - "[[CAPM]]"
  - "[[Regression]]"
  - "[[Correlation]]"
---

## What It Is

A linear factor model that decomposes an asset's excess return into systematic exposures to a small set of *factor* returns plus an idiosyncratic residual. The original three-factor model (Fama & French, 1993) extends [[CAPM]] by adding two empirically motivated factors:

$$R_i - R_f = \alpha_i + \beta_i^{\mathrm{MKT}}(R_M - R_f) + \beta_i^{\mathrm{SMB}}\,\mathrm{SMB} + \beta_i^{\mathrm{HML}}\,\mathrm{HML} + \varepsilon_i$$

- $\mathrm{MKT}$ — market excess return (same as CAPM)
- $\mathrm{SMB}$ ("Small Minus Big") — long small-caps, short large-caps. Captures the **size premium**.
- $\mathrm{HML}$ ("High Minus Low") — long high book-to-market (value), short low (growth). Captures the **value premium**.
- $\alpha_i$ — the part of returns not explained by the factors (the residual "alpha")
- $\varepsilon_i$ — idiosyncratic residual

Each factor is constructed as a long-short, dollar-neutral portfolio rebalanced annually using NYSE breakpoints. Fama & French publish the daily and monthly return series free at the [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html).

Extensions in common use:

- **Carhart four-factor** (1997) — adds momentum (UMD / WML).
- **Fama-French five-factor** (2015) — adds profitability (RMW) and investment (CMA), partially subsuming HML.
- **Q-factor model** (Hou, Xue & Zhang, 2015) — alternative parametrization built around the investment-CAPM.

## Why It Matters

The Fama-French model is the empirical refutation of CAPM and the conceptual ancestor of every multi-factor model in modern asset management. Two distinct uses for quants:

1. **Performance attribution.** Regressing a strategy's return on the factors decomposes performance into systematic factor exposure and residual $\alpha_i$. A manager who looks like they have skill but loads heavily on SMB and HML may simply be harvesting documented factor premia — cheap to replicate with a passive multi-factor fund. The intercept $\alpha$ after factor adjustment is the honest measure of skill.
2. **Signal construction.** Each factor is itself a tradeable signal with its own (typically low) [[Information Coefficient]]. Factor returns are largely independent of each other by construction (or at least less correlated than naive style cuts), which makes them natural inputs to an [[Alpha Combination]] stack.

It is also the **template for factor research**: construct a long-short portfolio sorted on a candidate signal, control for known factors, test the residual alpha. This is the workflow Jegadeesh-Titman used to establish [[Momentum]] and that every subsequent factor paper has followed.

**Why the factors persist:**

- **Value (HML), profitability (RMW), investment (CMA)** are typically rationalized as compensation for risk or as behavioral mispricing — debate is unresolved.
- **Size (SMB)** has weakened materially in post-publication out-of-sample periods, illustrating that documented premia can decay.
- **Momentum (UMD/WML)** remains the most robust premium across asset classes but is the most behaviorally controversial.

**Limitations to keep in mind:**

- **Factor zoo problem.** Hundreds of factors have been "discovered" in the literature. Multiple-testing correction (Harvey, Liu & Zhu, 2016) cuts the credible list dramatically. Most reported factors are noise.
- **Time-varying loadings.** $\beta$s drift across regimes; a single full-sample regression hides regime-dependent exposures.
- **Factor returns are sample-period dependent.** SMB and HML have had multi-decade stretches of near-zero or negative returns. Treat factor premia as long-run averages, not guaranteed payoffs.
- **Crowdedness.** Every major asset manager runs some form of size/value tilt. Crowdedness compresses expected returns and increases drawdown correlation.
- **Crypto specifics.** Crypto factor models (size, momentum, value-via-network-metrics) exist but are far less mature; the three-factor model is not directly transferable. The *methodology* (long-short construction, factor regression for alpha) does transfer cleanly.
- **Long-only constraints** kill access to the short legs of SMB / HML; transfer coefficient drops, see [[Fundamental Law of Active Management]].

## Key Equations

**Three-factor model:**
$$R_i - R_f = \alpha_i + \beta_i^{\mathrm{MKT}}(R_M - R_f) + \beta_i^{\mathrm{SMB}}\,\mathrm{SMB} + \beta_i^{\mathrm{HML}}\,\mathrm{HML} + \varepsilon_i$$

**Factor regression** to compute alpha and exposures:
$$R_{i,t} - R_{f,t} = \alpha_i + \sum_{k} \beta_i^{(k)} F_{k,t} + \varepsilon_{i,t}$$

OLS estimates of $\beta_i^{(k)}$ are the strategy's factor loadings; $\hat\alpha_i$ is the alpha; significance is tested via [[Hypothesis Testing|t-tests]] (Newey-West standard errors if there is autocorrelation).

**Factor-adjusted alpha (regression intercept) is the testable claim of skill:**
$$H_0:\ \alpha_i = 0$$

**Factor construction** (SMB at month $t$):
$$\text{SMB}_t = \frac{1}{3}\left( R^{S/L}_t + R^{S/M}_t + R^{S/H}_t \right) - \frac{1}{3}\left( R^{B/L}_t + R^{B/M}_t + R^{B/H}_t \right)$$

where $S/L$ = small-cap low-B/M portfolio, etc. — the $2 \times 3$ Fama-French sort.

**Carhart extension:**
$$+\ \beta_i^{\mathrm{UMD}}\,\mathrm{UMD}$$

**Five-factor extension:**
$$+\ \beta_i^{\mathrm{RMW}}\,\mathrm{RMW} + \beta_i^{\mathrm{CMA}}\,\mathrm{CMA}$$

## Resources

- Fama & French (1993) — "Common Risk Factors in the Returns on Stocks and Bonds"
- Carhart (1997) — "On Persistence in Mutual Fund Performance"
- Fama & French (2015) — "A Five-Factor Asset Pricing Model"
- Harvey, Liu & Zhu (2016) — "...and the Cross-Section of Expected Returns" (factor-zoo critique)
- [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) — Free daily/monthly factor returns
- [[Returns to Buying Winners and Selling Losers — Jegadeesh & Titman]] — the momentum anomaly that FF3 could not explain, leading to Carhart's fourth factor

## Connections

- [[CAPM]] — direct predecessor; FF3 is the empirically-motivated extension
- [[Regression]] — the tool factor models are implemented with
- [[Hypothesis Testing]] — significance of $\hat\alpha$ is the standard test of strategy edge
- [[Information Coefficient]] — each factor return series is a low-IC signal
- [[Alpha Combination]] — factors as inputs to a combined signal stack
- [[Statistical Arbitrage]] — residual returns $\varepsilon_i$ after factor regression are the canonical stat-arb target
- [[Portfolio Optimization]] — factor models provide the covariance structure
- [[Sharpe Ratio]] / [[Information Ratio]] — factor-adjusted alpha is what gets credited as skill
- [[Momentum]] — the Carhart fourth factor added to FF3
- [[Principal Component Analysis]] — top PCs of stock returns roughly correspond to market, size, and value
