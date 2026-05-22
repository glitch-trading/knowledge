---
type: concept
title: "Hypothesis Testing"
tags:
  - concept
  - statistics
  - backtesting
level: 1
prerequisites:
  - "[[probability-distributions|Probability Distributions]]"
  - "[[normal-distribution|Normal Distribution]]"
  - "[[expected-value|Expected Value]]"
---

## What It Is

**Hypothesis testing** is the formal procedure for deciding whether observed data is consistent with a baseline ("null") explanation, or whether the data is unlikely enough under that baseline to justify rejecting it in favor of an alternative.

The structure is fixed:

1. Specify a **null hypothesis** $H_0$ (typically "no effect," "no edge," "random").
2. Specify an **alternative** $H_1$ (the claim you want evidence for).
3. Choose a **test statistic** $T$ whose distribution under $H_0$ is known.
4. Compute $T_{\text{obs}}$ from the data and its **p-value**: $P(T \geq T_{\text{obs}} \mid H_0)$ (one-sided) or two-sided equivalent.
5. Reject $H_0$ if $p < \alpha$ for a chosen significance level $\alpha$ (commonly 0.05).

**Two error types matter and they trade off:**

- **Type I (false positive):** rejecting $H_0$ when it is true. Controlled at level $\alpha$.
- **Type II (false negative):** failing to reject $H_0$ when $H_1$ is true. Probability $\beta$; statistical **power** = $1 - \beta$.

## Why It Matters

In quant trading, almost every claim that matters is a hypothesis test in disguise:

- "Does this strategy have positive expected return?" → t-test on backtested returns.
- "Is this Sharpe statistically distinguishable from zero?" → its own test, see [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]].
- "Is the spread between these two assets cointegrated?" → ADF test (see [[cointegration|Cointegration]]).
- "Is yesterday's return predictive of today's?" → test on the [[autocorrelation|Autocorrelation]] coefficient.

**The trap is multiple testing.** Run 100 independent strategy backtests at $\alpha = 0.05$ and you expect ~5 false positives even if none of the strategies have any edge. This is the central reason why naively reported backtest Sharpe ratios overstate live performance — see [[overfitting|Overfitting]].

Corrections:

- **Bonferroni:** use $\alpha / N$ where $N$ is the number of tests. Crude but safe.
- **Benjamini-Hochberg:** controls false discovery rate (expected proportion of false positives among rejections), less conservative.
- **Deflated Sharpe ratio:** the principled version for backtest counts — see [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]].

## Key Tests Used in Quant Work

| Test | Asks | Used For |
|---|---|---|
| One-sample $t$-test | Is the mean of these returns ≠ 0? | Backtest alpha |
| Two-sample $t$-test | Do two strategies have different mean returns? | A/B testing strategy variants |
| Augmented Dickey-Fuller (ADF) | Is this series stationary? | [[cointegration|Cointegration]], spread mean-reversion |
| Ljung-Box | Are residuals serially correlated? | Diagnosing regression / ARIMA fits |
| Jarque-Bera | Are returns normal? | Almost always rejects on financial data (see [[fat-tails|Fat Tails]]) |
| White's / Hansen's SPA | Out-of-sample superior predictive ability | Strategy selection with multiple comparisons |

## Equations

**One-sample $t$-statistic** for mean return $\bar r$ over $n$ observations:

$$t = \frac{\bar r - 0}{s / \sqrt n}, \qquad t \sim t_{n-1} \text{ under } H_0$$

**Sharpe-based test** (annualized Sharpe $\widehat{SR}$ from $n$ monthly observations):

$$t = \widehat{SR} \cdot \sqrt{n / 12}$$

A Sharpe of 1.0 over 3 years of monthly data gives $t \approx 1.73$ — *not significant at 5%* by a naive one-sided test. Most retail backtest claims fail this sanity check.

**Bonferroni-adjusted significance** for $N$ trials:

$$\alpha_{\text{adj}} = \alpha / N$$

A Sharpe that clears $p < 0.05$ in isolation needs to clear $p < 0.0005$ to mean the same thing after testing 100 strategies.

## Resources

- [[all-of-statistics-larry-wasserman|All of Statistics — Larry Wasserman]] — Chapters 10-11 cover hypothesis testing rigorously
- [[introduction-to-statistical-learning-islr|Introduction to Statistical Learning (ISLR)]] — Applied perspective
- [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]] — Multiple-testing correction for strategies

## Connections

- [[overfitting|Overfitting]] — Multiple testing without correction is the most common path to overfit conclusions
- [[regression|Regression]] — t-tests on coefficients underpin most factor model claims
- [[cointegration|Cointegration]] — ADF is the test that makes pairs trading rigorous
- [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]] — Strategy-specific multiple-testing correction
- [[look-ahead-bias|Look-Ahead Bias]] — Even a correctly designed test gives wrong answers if inputs use future information
