---
type: concept
title: "Overfitting"
tags:
  - concept
  - statistics
  - risk
level: 3
prerequisites: []
---

## What It Is

Overfitting occurs when a model or strategy is tuned so tightly to historical data that it captures noise rather than signal. The result: perfect in-sample performance, zero out-of-sample predictive power. The strategy has memorized the past instead of learning from it.

In quantitative trading, overfitting is the single most common failure mode. You backtest 200 parameter combinations, find one with a [[sharpe-ratio|Sharpe Ratio]] of 3.0, deploy it, and watch it bleed money. The strategy was never real — it was an artifact of data mining.

**Key mechanisms:**
- **Multiple testing**: Test enough hypotheses and some will appear significant by chance. 100 strategies at 5% significance → ~5 false positives. See [[hypothesis-testing|Hypothesis Testing]].
- **Data snooping**: Repeatedly looking at the same dataset to "discover" patterns. Each peek contaminates your statistical tests.
- **Excessive parameters**: More free parameters = more ways to fit noise. A 50-parameter model can fit almost any historical dataset perfectly.
- **[[survivorship-bias|Survivorship Bias]]**: Only seeing strategies/funds that survived, not the graveyard of failures.
- **[[look-ahead-bias|Look-Ahead Bias]]**: Using information that wasn't actually available at simulated decision time. The most common backtest-killer.

## Why It Matters

Overfitting is the graveyard of quant strategies. Most backtested strategies that look profitable are overfit. The problem is especially severe in crypto markets where:

- Historical datasets are short (a few years)
- Regime changes are frequent and dramatic
- The temptation to optimize on recent data is strong
- Transaction cost assumptions can hide overfitting

**Red flags that a strategy is overfit:**
- Sharp degradation out-of-sample
- Highly specific parameters (e.g., "rebalance every 3.7 days using a 14.2-period lookback")
- Only works on one asset or one time period
- Performance collapses with small parameter perturbations

## Key Equations

**Deflated Sharpe Ratio** (see [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]]):

The DSR adjusts the observed Sharpe Ratio for the number of trials, skewness, and kurtosis:
$$DSR = PSR[\widehat{SR^*}] = \Phi\left(\frac{(\widehat{SR} - SR^*)\sqrt{n-1}}{\sqrt{1 - \hat{\gamma}_3 \cdot \widehat{SR} + \frac{\hat{\gamma}_4 - 1}{4}\widehat{SR}^2}}\right)$$

**Bonferroni correction** (crude but useful):
$$\alpha_{\text{adjusted}} = \frac{\alpha}{N}$$

Where $N$ = number of strategies tested. If you tested 100 strategies, your significance threshold drops from 5% to 0.05%.

## Resources

- [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]] — Multiple testing correction for Sharpe ratios
- [[advances-in-financial-machine-learning-lopez-de-prado|Advances in Financial Machine Learning — López de Prado]] — Extensive treatment of backtest overfitting
- Bailey et al. — "The Probability of Backtest Overfitting"

## Connections

- [[sharpe-ratio|Sharpe Ratio]] — The metric most vulnerable to overfitting via multiple testing
- [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]] — Statistical correction for overfitting in strategy evaluation
- [[hypothesis-testing|Hypothesis Testing]] — Multiple testing without correction is the most common path to overfit conclusions
- [[survivorship-bias|Survivorship Bias]] — A data-sourcing failure that masquerades as edge
- [[look-ahead-bias|Look-Ahead Bias]] — A logic failure that masquerades as edge
- [[probability-distributions|Probability Distributions]] — Understanding why random variation produces spurious results
