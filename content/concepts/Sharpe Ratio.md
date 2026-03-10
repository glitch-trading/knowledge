---
type: concept
title: "Sharpe Ratio"
tags:
  - concept
  - risk
  - metrics
level: 3
prerequisites: []
---

## What It Is

The Sharpe Ratio measures risk-adjusted return: how much excess return you earn per unit of volatility.

$$SR = \frac{R_p - R_f}{\sigma_p}$$

Where:
- $R_p$ = portfolio return
- $R_f$ = risk-free rate
- $\sigma_p$ = standard deviation of portfolio returns

Higher is better. A Sharpe of 1.0 means you earn 1% excess return per 1% of volatility. In traditional finance, Sharpe > 1.0 is good, > 2.0 is excellent, > 3.0 is suspicious (likely overfit or fraudulent).

## Why It Matters

The Sharpe Ratio is the most widely used performance metric in quantitative finance. It enables comparison across strategies with different return levels and risk profiles.

**Strengths:**
- Universal comparability — normalizes for leverage and risk
- Simple to compute and communicate
- Foundation of [[Portfolio Optimization]] (mean-variance framework)

**Critical weaknesses:**
- **Symmetric penalty**: [[Variance]] penalizes upside and downside equally. A strategy with occasional large gains gets punished. Use [[Sortino Ratio]] if returns are asymmetric.
- **Assumes normality**: Sharpe is a complete description of risk-adjusted return only if returns are normally distributed. For [[Fat Tails|fat-tailed]] distributions (crypto), it misses tail risk entirely.
- **Vulnerable to manipulation**: Selling OTM options, smoothing returns, and illiquid asset valuations all inflate Sharpe artificially.
- **Multiple testing**: If you test 100 strategies and pick the best Sharpe, you haven't found a good strategy — you've found noise. See [[The Deflated Sharpe Ratio — Bailey & López de Prado]].

**Annualization:**
$$SR_{\text{annual}} = SR_{\text{daily}} \times \sqrt{252}$$

This assumes i.i.d. returns (they aren't), but it's standard practice.

## Key Equations

**Information Ratio (relative Sharpe):**
$$IR = \frac{R_p - R_b}{\sigma_{p-b}}$$

Excess return relative to a benchmark, divided by tracking error.

**Ex-ante Sharpe (from Kelly):**
$$SR = \frac{\mu}{\sigma}$$

Directly connects to [[Kelly Criterion]]: $f^* = \mu / \sigma^2 = SR / \sigma$.

## Resources

- Sharpe, W.F. (1966) — "Mutual Fund Performance"
- [[The Deflated Sharpe Ratio — Bailey & López de Prado]] — Multiple testing correction
- [[Advances in Financial Machine Learning — López de Prado]]

## Connections

- [[Sortino Ratio]] — Downside-only version, better for asymmetric returns
- [[Variance]] — Sharpe uses total variance; this penalizes upside
- [[The Deflated Sharpe Ratio — Bailey & López de Prado]] — Corrects Sharpe for multiple testing and [[Overfitting]]
