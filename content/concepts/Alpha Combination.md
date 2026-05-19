---
type: concept
title: "Alpha Combination"
tags:
  - concept
  - signals
  - portfolio-construction
level: 4
prerequisites:
  - "[[Information Coefficient]]"
  - "[[Information Ratio]]"
  - "[[Fundamental Law of Active Management]]"
  - "[[Regression]]"
---

## What It Is

Alpha combination (also "alpha blending" or "signal combination") is the procedure that takes $N$ raw forecasts of the same target — expected returns, residual returns, probabilities — and produces a single weighted composite. The weights are chosen so that each signal's contribution reflects its **independent** predictive content, not its raw strength.

This is what the [[Fundamental Law of Active Management]] promises and what most live alpha programs spend the majority of their engineering effort on. Without an honest combination step, breadth is double-counted and the realized [[Information Ratio]] falls well below the Fundamental Law's $\mathrm{IC} \cdot \sqrt{N}$ estimate.

## Why It Matters

**The hidden-redundancy problem.** Two signals with $\mathrm{IC} = 0.05$ each look like two independent edges. If they are 0.9-correlated to each other, they are effectively one signal expressed twice. Naive equal weighting both *underuses* the genuine information and *oversizes* exposure to the shared underlying cause. The standard institutional failure mode — being directionally correct and losing money on the trade — is almost always a sizing error rooted in unmeasured signal correlation.

**Core principle.** A defensible combination weight for signal $i$ scales with the **residual edge** that survives after removing what other signals already capture, divided by the signal's noise:

$$w_i \propto \frac{\text{independent expected edge of signal } i}{\text{noise of signal } i}$$

This is mean-variance optimization on signal forecasts, with the critical detail being how "independent expected edge" is constructed.

**A standard procedural recipe** (one common formulation; many variants exist):

1. Collect each signal's realized-return time series $R_{i,s}$ over $M$ historical periods.
2. Demean each signal in time: $X_{i,s} = R_{i,s} - \overline{R_i}$.
3. Standardize: $Y_{i,s} = X_{i,s} / \sigma_i$, where $\sigma_i^2 = \mathrm{Var}(X_{i,\cdot})$. Signals are now on the same scale.
4. Drop the most recent period to keep the weight estimation out-of-sample.
5. Cross-sectionally demean at each $s$: $\Lambda_{i,s} = Y_{i,s} - \overline{Y_{\cdot,s}}$. This strips out the market-wide common factor — what all signals were doing together at that moment.
6. Estimate each signal's forward expected return, e.g. a rolling $d$-period mean $E_i$, normalized by $\sigma_i$.
7. Regress the normalized $E_i$ on the standardized cross-sectionally-demeaned series $\Lambda_{i,s}$; take the residual $\varepsilon_i$. This isolates the component of signal $i$'s forecast that is *not* explained by patterns shared across the stack.
8. Set $w_i \propto \varepsilon_i / \sigma_i$.
9. Normalize $\sum_i |w_i| = 1$ to bound leverage.

The combined forecast on any instrument is then $\sum_i w_i \cdot s_i$, where $s_i$ is signal $i$'s current output.

**This is one recipe, not the recipe.** Production systems often replace steps with: shrinkage estimators for the covariance, Bayesian or hierarchical priors on weights, regime-conditional combination, online learning with decay, or full mean-variance optimization with a covariance matrix and constraint set. All of them share the same two-part structure: estimate independent edge, then weight inversely by noise.

**Practical pitfalls:**

- **Sample-period dependence.** Combination weights estimated on a single regime become wrong in the next regime. Rolling re-estimation with shrinkage toward equal weights is the typical defense.
- **Look-ahead in $E_i$.** Anything that uses the same period for both expected-return estimation and weight selection inflates the apparent IR. Strict out-of-sample windowing matters more than the specific functional form.
- **Cost integration.** Weights chosen purely on pre-cost edge oversize signals that turn over fast. Combination should be jointly optimized with the cost model, not bolted on after.
- **Capacity stacking.** Multiple signals trading the same names at the same time multiply market impact non-linearly. Effective $N$ for sizing purposes is smaller than effective $N$ for IR forecasting.

**Application to [[Prediction Markets]].** The same machinery applies with the substitution: signals output implied probabilities rather than expected returns. Cross-venue pricing, calibration to historical resolution rates, Bayesian updates on new evidence, order-flow imbalance ([[VPIN]]), and momentum can each produce an independent probability estimate. Combine via the same procedure; compare the composite to the current market price to get edge in probability space; size via [[Kelly Criterion]], typically with a downward adjustment for the uncertainty in the edge estimate (e.g. shrink by the coefficient of variation of the edge across bootstrap or Monte Carlo paths).

## Key Equations

**Generic optimal weight (mean-variance form):**
$$\mathbf{w}^* \propto \Sigma^{-1} \boldsymbol{\mu}$$

where $\boldsymbol{\mu}$ is the vector of expected signal returns and $\Sigma$ is the signal-return covariance matrix. The procedural recipe above is a structured estimator for $\Sigma^{-1}\boldsymbol{\mu}$ that handles a dominant common factor explicitly.

**Combined forecast on an instrument:**
$$\hat{s}_{\text{combined}} = \sum_{i=1}^N w_i \cdot s_i$$

## Resources

- Grinold & Kahn — *Active Portfolio Management*, Ch. 7 (information analysis, combining signals)
- Kakushadze & Serur — *151 Trading Strategies* (catalog including specific alpha-combination formulae)
- [[Advances in Financial Machine Learning — López de Prado]] — covariance shrinkage and combination under multiple testing

## Connections

- [[Information Coefficient]] — per-signal input the combination is built from
- [[Information Ratio]] — system-level output the combination is trying to maximize
- [[Fundamental Law of Active Management]] — combination is the mechanism that makes breadth $\sqrt{N}$ real instead of nominal
- [[Portfolio Optimization]] — alpha combination is portfolio optimization on signals rather than assets
- [[Regression]] — the residual-edge step is a regression of expected returns on shared variance
- [[Kelly Criterion]] — sizes the combined forecast once edge is estimated
- [[Prediction Markets]] — same machinery applied in probability space
