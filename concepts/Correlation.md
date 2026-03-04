---
type: concept
title: "Correlation"
tags:
  - concept
  - statistics
level: 3
prerequisites: []
---

# Correlation

## What It Is

Correlation measures the strength and direction of the linear relationship between two variables. The Pearson correlation coefficient $\rho$ (population) or $r$ (sample) ranges from -1 to +1:

- $\rho = +1$: Perfect positive linear relationship
- $\rho = 0$: No linear relationship (but could still be nonlinearly related!)
- $\rho = -1$: Perfect negative linear relationship

**Critical distinction**: Correlation measures *linear* association only. Two variables can have strong nonlinear dependence with zero correlation (e.g., $Y = X^2$ with symmetric $X$).

**Variants:**
- **Pearson**: Linear correlation. Assumes normality for inference.
- **Spearman**: Rank correlation. Captures monotonic (not just linear) relationships. More robust to outliers.
- **Kendall**: Another rank correlation. Better for small samples.

## Why It Matters

- **Portfolio construction**: Correlation drives portfolio risk. Low correlation between assets → diversification benefits. The portfolio variance formula depends critically on pairwise correlations.
- **Correlation is NOT causation**: The single most dangerous statistical trap. Spurious correlations in financial data are everywhere — data-mined "relationships" that are meaningless. Always ask: is there a causal mechanism?
- **Correlation is unstable**: Financial correlations are time-varying and spike during crises (correlation breakdown). The diversification you counted on disappears exactly when you need it most.
- **Pairs trading signal**: High correlation between two assets may suggest a statistical relationship worth trading, but [[Cointegration]] is the proper test for mean-reverting spreads.

## Key Equations

**Pearson correlation coefficient:**
$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{E[(X - \mu_X)(Y - \mu_Y)]}{\sigma_X \sigma_Y}$$

**Sample correlation:**
$$r = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2} \sqrt{\sum(y_i - \bar{y})^2}}$$

**Portfolio variance (two assets):**
$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2$$

Lower $\rho_{12}$ → lower portfolio variance → diversification benefit.

**Correlation matrix (n assets):**
$$\Sigma_{ij} = \rho_{ij} \sigma_i \sigma_j$$

**Relationship to regression:**
$$R^2 = r^2 \text{ (simple linear regression)}$$

$$\beta_1 = r \cdot \frac{\sigma_Y}{\sigma_X}$$

## Resources

- Embrechts, McNeil & Straumann — "Correlation and Dependence in Risk Management: Properties and Pitfalls"
- Taleb — *Fooled by Randomness* (on spurious correlations)
- Tyler Vigen — *Spurious Correlations* (humorous but instructive)

## Connections

- [[Regression]] — Regression quantifies the relationship that correlation identifies
- [[Cointegration]] — A more robust concept than correlation for pairs trading
- [[Portfolio Optimization]] — Correlation matrix is a key input to mean-variance optimization
- [[Variance]] — Correlation interacts with variance to determine portfolio risk
