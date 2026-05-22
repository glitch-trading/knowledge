---
type: concept
title: "Look-Ahead Bias"
tags:
  - concept
  - backtesting
  - data-quality
  - risk
level: 3
prerequisites: []
---

## What It Is

**Look-ahead bias** is the use, at simulated time $t$, of information that was not actually available until some later time $t + \delta$. The backtest "looks ahead" at the future and earns a return that the live strategy could never replicate. Unlike [[survivorship-bias|Survivorship Bias]] (a data-sourcing problem), look-ahead bias is a *logic* bug in the simulation pipeline.

It is the single most common reason a profitable backtest collapses in production.

## Why It Matters

Look-ahead bias produces backtests that are not merely optimistic — they are *physically impossible*. Examples that appear constantly in real code:

- **Using close-of-day data to trade at the open.** A signal computed from today's close cannot drive today's open.
- **Using as-reported earnings data without restatement timestamps.** Compustat fields are often retroactively revised. Using today's "as-cleaned" earnings value at the date of the original announcement embeds future revisions.
- **Standardizing or scaling features over the full sample.** A z-score that uses the full-period mean and stdev leaks the future mean into every historical observation. Use a rolling or expanding window with only past data.
- **Index reconstitutions on the announcement date instead of effective date.** Rebalances scheduled "on the day Apple was added to the index" cannot be executed before the addition is announced and effective.
- **Filling forward then computing.** Forward-filling missing prices, then computing returns or signals on the filled series, can encode future information into past timestamps depending on how the fill propagates.
- **Hyperparameter selection using full-sample CV.** Cross-validating on the entire panel before splitting train/test leaks test-period information into training (see [[the-elements-of-statistical-learning-hastie-tibshirani-and-friedman|The Elements of Statistical Learning — Hastie, Tibshirani & Friedman]] on time-series CV).

## How To Avoid It

- **Walk-forward simulation.** At each simulated time $t$, only ever access data with timestamps strictly less than $t$. Make this an architectural invariant of the backtester, not a discipline the user maintains by inspection.
- **Point-in-time data sources.** When a feed offers as-reported vs. revised values, use as-reported. Vendors that flag this: Compustat (point-in-time), CRSP, several institutional bond feeds.
- **Lag every fundamental signal explicitly.** Earnings announced on day $t$ should be usable from day $t+1$ at earliest, accounting for announcement time and execution latency.
- **Time-aware cross-validation.** Use expanding-window or rolling-window splits. Never random k-fold on time-series data — that is the most common ML look-ahead.
- **Sanity check: does the in-sample Sharpe drop sharply when you shift signals by one period?** If yes, your signal is using same-period information. A genuine signal should degrade only modestly with a 1-period lag.

## Numerical Smell Tests

- **Implausibly high Sharpe.** Any backtest > 3.0 Sharpe at daily frequency should be assumed look-ahead-biased until proven otherwise.
- **Out-of-sample collapse.** Strategy Sharpe falls from 4 in-sample to 0.2 out-of-sample → almost certainly look-ahead in the in-sample portion.
- **Predicting through events.** Strategy is suspiciously well-positioned heading into a known announcement (FOMC, earnings, CPI). Check timestamps on every input.

## Related Distortions

- **[[survivorship-bias|Survivorship Bias]]** — Sister problem in data sourcing.
- **[[overfitting|Overfitting]]** — Look-ahead amplifies overfitting because the future-leaked signal almost always wins parameter searches.
- **Selection bias in feature pipelines** — Standardization, winsorization, and feature selection done over the full sample all leak future statistics into past observations.

## Resources

- [[advances-in-financial-machine-learning-lopez-de-prado|Advances in Financial Machine Learning — López de Prado]] — Chapter on backtest pitfalls, embargo, and purged k-fold CV
- [[the-elements-of-statistical-learning-hastie-tibshirani-and-friedman|The Elements of Statistical Learning — Hastie, Tibshirani & Friedman]] — Section 7.10 on cross-validation done wrong

## Connections

- [[survivorship-bias|Survivorship Bias]] — The other canonical backtest-killer
- [[overfitting|Overfitting]] — Look-ahead-biased features almost always win in-sample
- [[hypothesis-testing|Hypothesis Testing]] — Look-ahead invalidates the assumed distribution of test statistics
- [[statistical-arbitrage|Statistical Arbitrage]] — Especially exposed because signals are weak and small leaks dominate
