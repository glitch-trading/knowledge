---
type: concept
title: "Regression"
tags:
  - concept
  - statistics
  - econometrics
level: 3
prerequisites: []
---

# Regression

## What It Is

Regression is a statistical method for modeling the relationship between a dependent variable (what you're trying to predict) and one or more independent variables (what you're using to predict it). At its core, regression answers: "When X moves, how much does Y move?"

**Simple linear regression:**
$$Y = \beta_0 + \beta_1 X + \epsilon$$

One predictor. The slope $\beta_1$ tells you the marginal effect of X on Y.

**Multiple linear regression:**
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_n X_n + \epsilon$$

Multiple predictors. Each $\beta_i$ tells you the effect of $X_i$ on $Y$, holding all other variables constant.

**Key diagnostic concepts:**
- **$R^2$** (coefficient of determination): Fraction of variance in $Y$ explained by the model. $R^2 = 0.05$ is actually quite good in finance.
- **Residuals** ($\epsilon$): The unexplained part. Should be random — if they show patterns, your model is misspecified.
- **p-values**: Probability that the observed relationship is due to chance. In finance, be skeptical — multiple testing and overfitting inflate significance.
- **Heteroskedasticity**: Non-constant variance of residuals. Very common in financial data. Use robust standard errors (White, Newey-West).

## Why It Matters

- **Alpha modeling**: Most quantitative trading signals are discovered and validated through regression. "Does this factor predict future returns?"
- **Hedging**: Regression tells you the hedge ratio. If stock Y has $\beta = 0.8$ against the market, you need to short 0.8 units of market exposure to hedge.
- **Risk decomposition**: Factor regressions (Fama-French, Barra) decompose returns into systematic factors and idiosyncratic alpha.
- **Danger of overfitting**: With enough variables, you can fit any historical data perfectly. Out-of-sample, it will fail catastrophically. Regularization (Ridge, Lasso) and cross-validation are essential.

## Key Equations

**OLS estimator (matrix form):**
$$\hat{\beta} = (X^T X)^{-1} X^T Y$$

**$R^2$:**
$$R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

**Adjusted $R^2$ (penalizes additional variables):**
$$\bar{R}^2 = 1 - \frac{(1-R^2)(n-1)}{n-k-1}$$

**t-statistic for coefficient significance:**
$$t = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}$$

**Standard error of $\hat{\beta}$ (homoskedastic):**
$$SE(\hat{\beta}) = \sqrt{\hat{\sigma}^2 (X^T X)^{-1}}$$

## Resources

- Wooldridge — *Introductory Econometrics* (gold standard textbook)
- James, Witten, Hastie, Tibshirani — *An Introduction to Statistical Learning* (ISL)
- Angrist & Pischke — *Mostly Harmless Econometrics* (causal inference focus)

## Connections

- [[Correlation]] — Regression quantifies the linear relationship that correlation measures
- [[Logistic Regression]] — Extension for binary outcomes
- [[Cointegration]] — Regression of non-stationary series on each other (Engle-Granger method)
- [[Time Series Analysis]] — Regression with lagged variables and autocorrelated errors
