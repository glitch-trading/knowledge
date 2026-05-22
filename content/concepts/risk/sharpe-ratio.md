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
- Foundation of [[portfolio-optimization|Portfolio Optimization]] (mean-variance framework)

**Critical weaknesses:**
- **Symmetric penalty**: [[variance|Variance]] penalizes upside and downside equally. A strategy with occasional large gains gets punished. Use [[sortino-ratio|Sortino Ratio]] if returns are asymmetric.
- **Assumes normality**: Sharpe is a complete description of risk-adjusted return only if returns are normally distributed. For [[fat-tails|fat-tailed]] distributions (crypto), it misses tail risk entirely.
- **Vulnerable to manipulation**: Selling OTM options, smoothing returns, and illiquid asset valuations all inflate Sharpe artificially.
- **Multiple testing**: If you test 100 strategies and pick the best Sharpe, you haven't found a good strategy — you've found noise. See [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]].

**Annualization:**
$$SR_{\text{annual}} = SR_{\text{daily}} \times \sqrt{252}$$

This assumes i.i.d. returns (they aren't), but it's standard practice.

## Key Equations

**Information Ratio (relative Sharpe):**
$$IR = \frac{R_p - R_b}{\sigma_{p-b}}$$

Excess return relative to a benchmark, divided by tracking error. See [[information-ratio|Information Ratio]] for the full treatment and its decomposition via the [[fundamental-law-of-active-management|Fundamental Law of Active Management]].

**Ex-ante Sharpe (from Kelly):**
$$SR = \frac{\mu}{\sigma}$$

Directly connects to [[kelly-criterion|Kelly Criterion]]: $f^* = \mu / \sigma^2 = SR / \sigma$.

## Computing Sharpe in Code

From a series of arithmetic daily returns:

```python
import numpy as np
import pandas as pd

def annualized_sharpe(returns: pd.Series, rf_annual: float = 0.0,
                      periods_per_year: int = 252) -> float:
    rf_per_period = rf_annual / periods_per_year
    excess = returns - rf_per_period
    return np.sqrt(periods_per_year) * excess.mean() / excess.std(ddof=1)

# Toy strategy: 10% expected annual return, 15% annual vol, 2 years of data.
rng = np.random.default_rng(0)
daily = pd.Series(rng.normal(0.10 / 252, 0.15 / np.sqrt(252), size=2 * 252))
print(f"SR = {annualized_sharpe(daily):.2f}")         # 0.22 with seed=0 (true SR is 0.67)
```

That gap — a 0.22 *sample* Sharpe drawn from a 0.67 *true* Sharpe — is the headline reason ex-post Sharpe over a few hundred days is a weak estimator. The standard error of an annual Sharpe over $T$ years is roughly $\sqrt{(1 + SR^2/2)/T}$; with 2 years, it's around 0.75. **You cannot tell a 0 strategy from a 1 strategy from 2 years of data.**

Two things to watch for in real data:

```python
# 1. Use sample stdev (ddof=1) — population stdev biases SR upward on small samples.
# 2. The √252 scaling only holds if returns are i.i.d. — autocorrelated returns inflate SR.
rolling_sr = daily.rolling(63).apply(annualized_sharpe, raw=False)    # 3-month rolling
```

The rolling Sharpe is what most LPs actually look at — a strategy with strong overall Sharpe but a brutal rolling 3-month window is harder to hold than the headline number suggests.

## Resources

- Sharpe, W.F. (1966) — "Mutual Fund Performance"
- [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]] — Multiple testing correction
- [[advances-in-financial-machine-learning-lopez-de-prado|Advances in Financial Machine Learning — López de Prado]]

## Connections

- [[sortino-ratio|Sortino Ratio]] — Downside-only version, better for asymmetric returns
- [[variance|Variance]] — Sharpe uses total variance; this penalizes upside
- [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]] — Corrects Sharpe for multiple testing and [[overfitting|Overfitting]]
- [[information-ratio|Information Ratio]] — benchmark-relative cousin; the standard metric for active management
- [[information-coefficient|Information Coefficient]] — signal-level analogue (per-forecast skill)
