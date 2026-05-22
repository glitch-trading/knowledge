---
type: concept
title: "Fama-French Factor Model"
tags:
  - concept
  - factor-models
  - asset-pricing
level: 3
prerequisites:
  - "[[Regression]]"
  - "[[Correlation]]"
---

## What It Is

A linear factor model that decomposes an asset's excess return into systematic exposures to a small set of *factor* returns plus an idiosyncratic residual. The original three-factor model (Fama & French, 1993):

$$R_i - R_f = \alpha_i + \beta_i^{\mathrm{MKT}}(R_M - R_f) + \beta_i^{\mathrm{SMB}}\,\mathrm{SMB} + \beta_i^{\mathrm{HML}}\,\mathrm{HML} + \varepsilon_i$$

- $\mathrm{MKT}$ — market excess return
- $\mathrm{SMB}$ — small-minus-big (long small caps, short large caps)
- $\mathrm{HML}$ — high-minus-low (long high book-to-market / "value", short low / "growth")
- $\alpha_i$ — the part of returns not explained by the factors (the residual "alpha")
- $\varepsilon_i$ — idiosyncratic residual

Extensions in common use:

- **Carhart four-factor** (1997) — adds momentum (UMD / WML).
- **Fama-French five-factor** (2015) — adds profitability (RMW) and investment (CMA), partially subsuming HML.
- **Q-factor model** (Hou, Xue & Zhang, 2015) — alternative parametrization built around the investment-CAPM.

## Why It Matters

**Two distinct uses:**

1. **Performance attribution.** Regressing a strategy's return on the factors decomposes performance into systematic factor exposure and residual $\alpha_i$. A manager who looks like they have skill but loads heavily on SMB and HML may simply be harvesting documented factor premia — cheap to replicate with a passive multi-factor fund. The intercept $\alpha$ after factor adjustment is the honest measure of skill.
2. **Signal construction.** Each factor is itself a tradeable signal with its own (typically low) [[Information Coefficient]]. Factor returns are largely independent of each other by construction (or at least less correlated than naive style cuts), which makes them natural inputs to an [[Alpha Combination]] stack.

**Why the factors persist:**

- **Value (HML), profitability (RMW), investment (CMA)** are typically rationalized as compensation for risk or as behavioral mispricing — debate is unresolved.
- **Size (SMB)** has weakened materially in post-publication out-of-sample periods, illustrating that documented premia can decay.
- **Momentum (UMD/WML)** remains the most robust premium across asset classes but is the most behaviorally controversial.

**Limitations to keep in mind:**

- **Factor zoo problem.** Hundreds of factors have been "discovered" in the literature. Multiple-testing correction (Harvey, Liu & Zhu, 2016) cuts the credible list dramatically. Most reported factors are noise.
- **Time-varying loadings.** $\beta$s drift across regimes; a single full-sample regression hides regime-dependent exposures.
- **Crypto specifics.** Crypto factor models (size, momentum, value-via-network-metrics) exist but are far less mature; the three-factor model is not directly transferable.
- **Long-only constraints** kill access to the short legs of SMB / HML; transfer coefficient drops, see [[Fundamental Law of Active Management]].

## Key Equations

**Three-factor model:**
$$R_i - R_f = \alpha_i + \beta_i^{\mathrm{MKT}}(R_M - R_f) + \beta_i^{\mathrm{SMB}}\,\mathrm{SMB} + \beta_i^{\mathrm{HML}}\,\mathrm{HML} + \varepsilon_i$$

**Factor-adjusted alpha (regression intercept) is the testable claim of skill:**
$$H_0:\ \alpha_i = 0$$

**Carhart extension:**
$$+\ \beta_i^{\mathrm{UMD}}\,\mathrm{UMD}$$

**Five-factor extension:**
$$+\ \beta_i^{\mathrm{RMW}}\,\mathrm{RMW} + \beta_i^{\mathrm{CMA}}\,\mathrm{CMA}$$

## Resources

- Fama & French (1993) — "Common Risk Factors in the Returns on Stocks and Bonds"
- Carhart (1997) — "On Persistence in Mutual Fund Performance"
- Fama & French (2015) — "A Five-Factor Asset Pricing Model"
- Harvey, Liu & Zhu (2016) — "...and the Cross-Section of Expected Returns" (factor-zoo critique)
- Kenneth French data library — public factor return series

## Connections

- [[Regression]] — the tool factor models are implemented with
- [[Information Coefficient]] — each factor return series is a low-IC signal
- [[Alpha Combination]] — factors as inputs to a combined signal stack
- [[Statistical Arbitrage]] — residual returns $\varepsilon_i$ after factor regression are the canonical stat-arb target
- [[Portfolio Optimization]] — factor models provide the covariance structure
- [[Sharpe Ratio]] / [[Information Ratio]] — factor-adjusted alpha is what gets credited as skill
