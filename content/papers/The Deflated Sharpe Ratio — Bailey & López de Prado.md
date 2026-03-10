---
type: paper
title: "The Deflated Sharpe Ratio"
authors:
  - David H. Bailey
  - Marcos López de Prado
year: 2014
status: unread
tags:
  - paper
  - statistics
  - risk
topics:
  - "[[Sharpe Ratio]]"
  - "[[Overfitting]]"
---

**Multiple testing correction for strategy evaluation. When you test 100 strategies, ~5 look significant by chance.**

## Summary

The paper addresses a critical problem in quantitative finance: when you evaluate many strategies and select the one with the highest [[Sharpe Ratio]], you're almost certainly selecting noise. The Deflated Sharpe Ratio (DSR) corrects the observed Sharpe for the number of trials conducted, the skewness and kurtosis of returns, and the length of the track record.

The core argument: a Sharpe Ratio is not a single number — it is a random variable with a sampling distribution. When you pick the maximum Sharpe from $N$ trials, the expected maximum increases with $N$ even if all strategies have zero true Sharpe. The DSR asks: "What is the probability that the best observed Sharpe is above zero, given how many strategies we tested?"

## Key Results

**The Deflated Sharpe Ratio:**
$$DSR = PSR[\widehat{SR^*}] = \Phi\left(\frac{(\widehat{SR} - SR^*)\sqrt{n-1}}{\sqrt{1 - \hat{\gamma}_3 \cdot \widehat{SR} + \frac{\hat{\gamma}_4 - 1}{4}\widehat{SR}^2}}\right)$$

Where:
- $\widehat{SR}$ = observed Sharpe ratio of the selected strategy
- $SR^*$ = expected maximum Sharpe under the null (all strategies have SR = 0)
- $n$ = number of return observations
- $\hat{\gamma}_3$ = skewness of returns
- $\hat{\gamma}_4$ = kurtosis of returns
- $\Phi$ = standard normal CDF

**Expected maximum Sharpe under the null:**
$$SR^* \approx \sqrt{V[\widehat{SR}]} \left( (1 - \gamma) \Phi^{-1}\left(1 - \frac{1}{N}\right) + \gamma \Phi^{-1}\left(1 - \frac{1}{N} e^{-1}\right) \right)$$

Where $N$ = number of independent trials and $\gamma \approx 0.5772$ (Euler-Mascheroni constant).

**Practical implications:**
- A Sharpe of 2.0 from testing 10 strategies is far more meaningful than a Sharpe of 2.0 from testing 1,000 strategies.
- Non-normal returns (high kurtosis, negative skew) inflate the variance of the Sharpe estimator, making it even easier to find spuriously high Sharpes.
- Short track records produce unreliable Sharpe estimates regardless of how few strategies you tested.

**The paper's punchline:** Most published backtests are overfit. The authors estimate that the majority of strategies reported in academic finance papers would fail the DSR test.

## Connections

- [[Sharpe Ratio]] — The metric being corrected
- [[Overfitting]] — The problem DSR detects and quantifies
