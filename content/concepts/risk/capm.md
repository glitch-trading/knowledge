---
type: concept
title: "Capital Asset Pricing Model (CAPM)"
tags:
  - concept
  - factor-models
  - asset-pricing
level: 5
prerequisites:
  - "[[portfolio-optimization|Portfolio Optimization]]"
  - "[[variance|Variance]]"
  - "[[regression|Regression]]"
---

## What It Is

The **Capital Asset Pricing Model** is the foundational equilibrium asset-pricing theory. It states that, in equilibrium, the expected excess return of any asset is proportional to its covariance with the market portfolio:

$$\mathbb{E}[R_i] - R_f = \beta_i \left( \mathbb{E}[R_m] - R_f \right), \qquad \beta_i = \frac{\operatorname{Cov}(R_i, R_m)}{\operatorname{Var}(R_m)}$$

Two ideas combine to produce this:

- **The tangency portfolio is the market.** Every investor holding the same beliefs and using mean-variance optimization arrives at the same risk-asset portfolio — the [[portfolio-optimization|tangency portfolio]]. In equilibrium that portfolio must be the market itself.
- **Only systematic risk is priced.** Idiosyncratic risk can be diversified away for free. The market only compensates investors for the part of risk they cannot diversify — exposure to the market factor — quantified by $\beta$.

## Why It Matters

CAPM is empirically a weak forecasting model — beta alone does not explain the cross-section of stock returns. But the model is the single most important *language* in finance:

- **Beta** is the universal vocabulary for systematic risk. "High-beta name," "beta-neutral book," "market beta" — all are CAPM concepts that survived the empirical refutation.
- **Alpha** is defined relative to CAPM (and its successors). When a quant fund advertises alpha, it means the intercept $\alpha$ in the regression $R_i - R_f = \alpha + \beta(R_m - R_f) + \varepsilon$ — return that beta cannot explain.
- **Hedging by beta** is the simplest [[statistical-arbitrage|market-neutral]] construction: long $\$X$ of a stock, short $\$\beta X$ of an index futures contract.

The empirical failures of CAPM motivated factor extensions: the [[fama-french-factor-model|Fama-French Factor Model]] adds size and value, Carhart adds [[momentum|Momentum]], and modern multi-factor models add quality, low-volatility, and investment factors.

## Key Equations

**Security Market Line** (equilibrium relation):

$$\mathbb{E}[R_i] = R_f + \beta_i \left( \mathbb{E}[R_m] - R_f \right)$$

**Beta estimation** by OLS regression of excess returns:

$$R_{i,t} - R_{f,t} = \alpha_i + \beta_i (R_{m,t} - R_{f,t}) + \varepsilon_{i,t}$$

Statistical significance of $\hat\alpha$ is the canonical test of "does this asset / portfolio have an edge after controlling for the market?" — see [[hypothesis-testing|Hypothesis Testing]].

**Treynor ratio** (return per unit of beta, the CAPM-natural analogue to [[sharpe-ratio|Sharpe Ratio]]):

$$\text{Treynor}_i = \frac{\mathbb{E}[R_i] - R_f}{\beta_i}$$

## Estimation Caveats

- $\hat\beta$ is noisy and time-varying. Rolling-window estimates over 60-252 trading days are standard; shrinkage toward 1.0 (Vasicek adjustment) reduces noise.
- Beta is a *linear* projection. A name with non-linear exposure (e.g. a long-vol position) can have $\beta \approx 0$ while carrying massive market risk.
- The "market" in practice is a proxy (S&P 500, MSCI World). In crypto, "the market" might be BTC, ETH, or a basket — choice matters and is part of the strategy.

## Resources

- [[options-futures-and-other-derivatives-john-hull|Options, Futures, and Other Derivatives — John Hull]] — CAPM and APT chapters as standard reference
- Sharpe (1964), "Capital Asset Prices" — The original paper
- Fama & French (2004), "The Capital Asset Pricing Model: Theory and Evidence" — Honest retrospective on what CAPM does and doesn't predict

## Connections

- [[portfolio-optimization|Portfolio Optimization]] — CAPM is the equilibrium consequence of universal mean-variance optimization
- [[fama-french-factor-model|Fama-French Factor Model]] — Direct successor that adds size and value
- [[momentum|Momentum]] — Added by Carhart (1997) as a fourth factor
- [[statistical-arbitrage|Statistical Arbitrage]] — Beta-neutrality is the simplest factor-neutral construction
- [[sharpe-ratio|Sharpe Ratio]] — Sharpe and Treynor differ on which "risk" they normalize by
- [[principal-component-analysis|Principal Component Analysis]] — PC1 of stock returns is the empirical analogue of the market factor
