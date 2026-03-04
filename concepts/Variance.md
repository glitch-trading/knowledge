---
type: concept
title: "Variance"
tags:
  - concept
  - probability
level: 1
prerequisites: []
---

# Variance

## What It Is

**Variance** measures how spread out a random variable's values are around its mean:

$$\text{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$

The **standard deviation** $\sigma = \sqrt{\text{Var}(X)}$ has the same units as $X$, making it more interpretable.

Key properties:
- $\text{Var}(aX + b) = a^2 \text{Var}(X)$ — scaling squares, shifts vanish
- $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)$
- If $X$ and $Y$ are independent: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$
- **Covariance**: $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$
- **Correlation**: $\rho_{XY} = \text{Cov}(X,Y) / (\sigma_X \sigma_Y)$, bounded in $[-1, 1]$

## Why It Matters

Variance is the default measure of risk in quantitative finance:

- **Volatility**: The standard deviation of returns ($\sigma$) is called **volatility** and is the single most important risk parameter. Annualized volatility is $\sigma_{\text{annual}} = \sigma_{\text{daily}} \sqrt{252}$.
- **Portfolio theory**: Markowitz portfolio optimization minimizes portfolio variance for a given expected return. Portfolio variance depends on all pairwise covariances.
- **Sharpe ratio**: $\text{SR} = \frac{E[R] - R_f}{\sigma}$ — risk-adjusted return divides excess return by volatility.
- **Avellaneda-Stoikov**: The parameter $\sigma^2$ directly determines how wide optimal quotes should be. Higher variance means wider spreads to compensate for adverse selection risk.
- **Position sizing**: Variance determines how much capital to allocate. Kelly sizing is inversely proportional to variance.
- **Limitations**: Variance treats upside and downside deviations equally and may understate risk when returns have [[Fat Tails]]. Alternatives include semi-variance, VaR, and Expected Shortfall.

## Key Equations

$$\text{Var}(X) = E[X^2] - (E[X])^2$$

$$\sigma = \sqrt{\text{Var}(X)}$$

$$\sigma_{\text{portfolio}}^2 = \sum_i \sum_j w_i w_j \text{Cov}(R_i, R_j)$$

$$\sigma_{\text{annual}} = \sigma_{\text{daily}} \sqrt{252}$$

## Resources

- *All of Statistics* by Larry Wasserman — Chapters 3-4
- *Quantitative Risk Management* by McNeil, Frey & Embrechts
- *Active Portfolio Management* by Grinold & Kahn — Chapter 2 on risk

## Connections

- [[Expected Value]] — variance is the expected squared deviation from the mean
- [[Normal Distribution]] — fully characterized by mean and variance
- [[Sharpe Ratio]] — risk-adjusted returns use standard deviation as the risk measure
- [[Fat Tails]] — when variance alone understates true risk
