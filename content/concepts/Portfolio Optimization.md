---
type: concept
title: "Portfolio Optimization"
tags:
  - concept
  - portfolio
level: 5
prerequisites: []
---

## What It Is

Portfolio optimization is the process of selecting asset weights to maximize some objective (usually risk-adjusted return) subject to constraints. The foundational framework is Markowitz's mean-variance optimization (MVO), which traces out the **efficient frontier** — the set of portfolios offering maximum expected return for each level of risk.

**The Markowitz problem:**
$$\min_w \; w^T \Sigma w \quad \text{s.t.} \quad w^T \mu = \mu_{\text{target}}, \quad w^T \mathbf{1} = 1$$

Where $w$ = weight vector, $\Sigma$ = covariance matrix, $\mu$ = expected return vector.

**Diversification is the only free lunch in finance.** By combining assets with imperfect [[Correlation]], portfolio variance can be reduced below the variance of any individual asset. This is the core insight.

## Why It Matters

Portfolio optimization moves you from "picking good trades" to "constructing good portfolios." The distinction matters because:

- **Correlation dominates.** Two great strategies that are perfectly correlated give you no diversification. One great and one mediocre strategy with negative correlation can outperform both.
- **Risk budgeting.** Optimization lets you allocate risk where you have the most edge, not just capital.
- **Constraint management.** Real portfolios have constraints: max position sizes, sector limits, liquidity limits, margin requirements. Optimization handles these systematically.

**Problems with naive MVO:**
- **Estimation error.** Expected returns are notoriously hard to estimate. Small errors in $\mu$ produce wildly different optimal portfolios. Garbage in, garbage out.
- **Instability.** Optimal weights flip dramatically with small input changes. This is impractical.
- **Concentration.** Unconstrained MVO often produces extreme allocations (200% long, -100% short one asset).

**Practical improvements:**
- **Black-Litterman model**: Combines market equilibrium with investor views
- **Risk parity**: Equalize risk contribution rather than optimizing return
- **Shrinkage estimators**: Regularize the covariance matrix to reduce estimation error
- **Robust optimization**: Optimize for the worst case within an uncertainty set

## Key Equations

**Portfolio variance:**
$$\sigma_p^2 = w^T \Sigma w = \sum_i \sum_j w_i w_j \sigma_i \sigma_j \rho_{ij}$$

**Tangency portfolio (max [[Sharpe Ratio]]):**
$$w^* = \frac{\Sigma^{-1}(\mu - R_f \mathbf{1})}{\mathbf{1}^T \Sigma^{-1}(\mu - R_f \mathbf{1})}$$

**Two-asset diversification benefit:**
$$\sigma_p = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \sigma_1 \sigma_2 \rho_{12}}$$

When $\rho_{12} < 1$, $\sigma_p < w_1 \sigma_1 + w_2 \sigma_2$. Free lunch.

## Resources

- Markowitz, H. (1952) — "Portfolio Selection"
- Meucci, A. — *Risk and Asset Allocation*
- [[Quantitative Risk Management — McNeil, Frey & Embrechts]]

## Connections

- [[Sharpe Ratio]] — The tangency portfolio maximizes Sharpe
- [[Correlation]] — The key input that makes diversification work
- [[Variance]] — Portfolio variance depends on covariance structure, not just individual variances
