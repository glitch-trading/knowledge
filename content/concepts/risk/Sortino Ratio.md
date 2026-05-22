---
type: concept
title: "Sortino Ratio"
tags:
  - concept
  - risk
  - metrics
level: 3
prerequisites: []
---

## What It Is

The Sortino Ratio is a modification of the [[Sharpe Ratio]] that only penalizes downside volatility. Instead of dividing by total standard deviation, it divides by the standard deviation of negative returns (downside deviation).

$$\text{Sortino} = \frac{R_p - R_f}{\sigma_d}$$

Where:
- $R_p$ = portfolio return
- $R_f$ = risk-free rate (or minimum acceptable return)
- $\sigma_d$ = downside deviation

**Downside deviation:**
$$\sigma_d = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \min(R_i - R_f, \; 0)^2}$$

Only returns below the target/risk-free rate contribute to the denominator.

## Why It Matters

The Sortino Ratio is more appropriate than Sharpe for strategies with asymmetric return distributions — which is most real-world strategies.

**Why Sortino > Sharpe in many contexts:**
- **Upside volatility is good.** Sharpe penalizes a strategy that occasionally makes 10x. Sortino doesn't — it only cares about the downside.
- **Crypto returns are heavily skewed.** Long crypto positions have right-skewed returns (small frequent losses, occasional large gains). Sharpe undervalues these strategies; Sortino evaluates them more fairly.
- **Options-like payoffs.** Any strategy with convex payoffs (long gamma, trend-following) looks worse on Sharpe than on Sortino.
- **Better alignment with investor preferences.** Investors care about losing money, not about "too much" upside.

**Interpretation:** Like Sharpe, higher is better. A Sortino of 2.0+ is strong. If Sortino >> Sharpe, the strategy has positive skew (good). If Sortino << Sharpe, the strategy has negative skew (hidden tail risk).

## Resources

- Sortino, F. & van der Meer, R. (1991) — "Downside Risk"
- Sortino, F. & Forsey, H. (1996) — "On the Use and Misuse of Downside Risk"

## Connections

- [[Sharpe Ratio]] — The symmetric version; Sortino improves on it for skewed distributions
- [[Maximum Drawdown]] — Both focus on the downside experience of a strategy
