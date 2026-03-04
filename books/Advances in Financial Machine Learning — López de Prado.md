---
type: book
title: "Advances in Financial Machine Learning"
author: "Marcos López de Prado"
status: unread
tags:
  - book
  - machine-learning
level: 6
topics:
  - "[[Overfitting]]"
  - "[[Time Series Analysis]]"
---

# Advances in Financial Machine Learning — López de Prado

**Making ML work in finance. The gap between ML theory and financial practice.**

## Why Read This
Most ML approaches fail in finance because of non-stationarity, low signal-to-noise, and improper cross-validation. This book addresses each of these problems head-on.

## Key Chapters
- **Chapters 2-5:** Feature engineering for financial data
- **Chapters 7-8:** Cross-validation for financial data (walk-forward, purging, embargo)

## Key Takeaways

- **Standard cross-validation destroys financial ML.** K-fold CV leaks future data into training via autocorrelation. Use walk-forward validation with purging (remove overlapping samples) and embargo (gap between train and test) to get honest out-of-sample estimates.
- **Features, not models.** The bottleneck in financial ML is feature engineering, not model selection. Raw prices are useless — transform them into returns, rolling statistics, order book imbalances, cross-asset ratios. Triple barrier labeling replaces naive fixed-horizon returns.
- **Meta-labeling.** Train a first model for side (buy/sell), then a second model for size (confidence). This separation dramatically improves practical performance by letting you filter low-confidence signals.
- **The Deflated Sharpe Ratio.** When you test many strategies, some will look good by chance. Correct for multiple testing using the DSR — it adjusts the Sharpe ratio for the number of trials, skewness, and kurtosis.
- **Fractional differentiation preserves memory.** Fully differencing a price series makes it stationary but destroys long-range dependence. Fractionally differenced series are stationary *and* retain memory — better features for ML models.


## Connections
- See also [[The Deflated Sharpe Ratio — Bailey & López de Prado]]
- Prerequisite understanding: [[Introduction to Statistical Learning (ISLR)]]
