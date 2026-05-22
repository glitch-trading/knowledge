---
type: concept
title: "Fama-French Three-Factor Model"
tags:
  - concept
  - factor-models
  - asset-pricing
level: 5
prerequisites:
  - "[[CAPM]]"
  - "[[Regression]]"
---

## What It Is

The **Fama-French three-factor model** (Fama & French, 1993) extends [[CAPM]] by adding two empirically motivated factors to explain the cross-section of stock returns:

$$R_i - R_f = \alpha_i + \beta_i^{\text{MKT}} (R_m - R_f) + \beta_i^{\text{SMB}} \cdot \text{SMB} + \beta_i^{\text{HML}} \cdot \text{HML} + \varepsilon_i$$

The three factors:

- **MKT** — the market excess return $R_m - R_f$, same as CAPM.
- **SMB** ("Small Minus Big") — long small-cap stocks, short large-cap stocks. Captures the **size premium**: small-cap stocks have historically earned higher returns than large-cap, beyond what CAPM beta predicts.
- **HML** ("High Minus Low") — long high book-to-market (value) stocks, short low book-to-market (growth) stocks. Captures the **value premium**: cheap stocks have historically outperformed expensive ones.

Each factor is constructed as a long-short, dollar-neutral portfolio rebalanced annually using NYSE breakpoints. Fama & French publish the daily and monthly return series free at the [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html).

## Why It Matters

The Fama-French model is the empirical refutation of CAPM and the conceptual ancestor of every multi-factor model in modern asset management. Three reasons it matters for quants:

- **It defines the benchmark for alpha.** Any "alpha" claim should be regressed on at least these three factors. Many strategies that look like alpha against CAPM collapse to zero once size and value are added.
- **It is the template for factor research.** Construct a long-short portfolio sorted on a candidate signal, control for known factors, test the residual alpha. This is the workflow Jegadeesh-Titman used to establish [[Momentum]] and that every subsequent factor paper has followed.
- **It is widely used in attribution.** When a strategy returns 12%, factor regression tells you how much came from being long the market, long small-caps, long value — versus residual skill.

Carhart (1997) added a fourth factor, [[Momentum]] (UMD, "up minus down"). The five-factor extension (Fama-French, 2015) adds profitability (RMW) and investment (CMA) factors. The pattern is the same: each generation finds anomalies the prior model could not explain and incorporates them.

## Key Equations

**Factor regression** to compute alpha and exposures:

$$R_{i,t} - R_{f,t} = \alpha_i + \sum_{k} \beta_i^{(k)} F_{k,t} + \varepsilon_{i,t}$$

where $F_{k,t}$ is the $k$-th factor's return at time $t$. OLS estimates of $\beta_i^{(k)}$ are the strategy's factor loadings; $\hat\alpha_i$ is the alpha; significance of $\hat\alpha$ is tested via [[Hypothesis Testing|t-tests]] (Newey-West standard errors if there is autocorrelation).

**Factor construction** (SMB at month $t$):

$$\text{SMB}_t = \frac{1}{3}\left( R^{S/L}_t + R^{S/M}_t + R^{S/H}_t \right) - \frac{1}{3}\left( R^{B/L}_t + R^{B/M}_t + R^{B/H}_t \right)$$

where $S/L$ = small-cap low-B/M portfolio, etc. — the $2 \times 3$ Fama-French sort.

## Practical Notes

- **Factor returns are sample-period dependent.** SMB and HML have had multi-decade stretches of near-zero or negative returns. Treat factor premia as long-run averages, not guaranteed payoffs.
- **Factors are crowded.** Every major asset manager runs some form of size/value tilt. Crowdedness compresses expected returns and increases drawdown correlation.
- **The size premium is the most contested.** Once microcaps and post-publication data are excluded, the SMB premium is small. The value premium is more robust historically.
- **For crypto and non-equity asset classes** Fama-French in its original form does not apply — but the *methodology* (long-short construction, factor regression for alpha) transfers cleanly.

## Resources

- Fama & French (1993), "Common Risk Factors in the Returns on Stocks and Bonds" — The original three-factor paper
- Fama & French (2015), "A Five-Factor Asset Pricing Model" — Adds profitability and investment
- [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) — Free daily/monthly factor returns
- [[Returns to Buying Winners and Selling Losers — Jegadeesh & Titman]] — The momentum anomaly that Fama-French could not explain, leading to Carhart's fourth factor

## Connections

- [[CAPM]] — Direct predecessor; FF3 is the empirically-motivated extension
- [[Momentum]] — The Carhart fourth factor added to FF3
- [[Returns to Buying Winners and Selling Losers — Jegadeesh & Titman]] — Established momentum as the anomaly FF3 missed
- [[Statistical Arbitrage]] — Factor regression is the standard alpha-attribution tool
- [[Regression]] — Multivariate OLS underpins factor estimation
- [[Hypothesis Testing]] — Significance of $\hat\alpha$ is the standard test of strategy edge
- [[Principal Component Analysis]] — Top PCs of stock returns roughly correspond to market, size, and value
