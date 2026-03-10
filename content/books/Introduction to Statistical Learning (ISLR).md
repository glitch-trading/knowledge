---
type: book
title: "An Introduction to Statistical Learning"
author: "Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani"
status: unread
tags:
  - book
  - machine-learning
  - statistics
level: 3, 6
topics:
  - "[[Regression]]"
  - "[[Overfitting]]"
---

**ML fundamentals. Free PDF. Excellent writing.**

## Why Read This
Accessible introduction to statistical learning / ML. Covers regression, classification, resampling, tree-based methods, SVMs. Free PDF available.

## Reading Plan
- **Chapters 2-4:** Regression, classification (Level 3)
- **Chapters 5-8:** Resampling, tree methods, SVMs, boosting (Level 6)

## Key Takeaways

- **Bias-variance trade-off governs everything.** Simple models underfit (high bias), complex models overfit (high variance). The sweet spot depends on the signal-to-noise ratio — which is terrible in finance, so lean towards simpler models.
- **Regularization is mandatory.** Lasso (L1) and Ridge (L2) penalize model complexity. Lasso performs feature selection (drives coefficients to zero); Ridge shrinks them. In finance, where features outnumber useful signals, regularization prevents overfitting noise.
- **Tree-based methods dominate tabular data.** Random forests and gradient boosting (XGBoost, LightGBM) consistently outperform linear models and neural networks on structured/tabular financial data. They handle non-linearities and interactions automatically.
- **Resampling methods estimate generalization.** Cross-validation and bootstrap tell you how well your model will perform on unseen data. In finance, standard CV is invalid — use walk-forward or time-series-aware splits.
- **Classification vs regression.** Predicting direction (up/down) is classification; predicting magnitude is regression. For trading, classification with meta-labeling (predict whether to trade, then size separately) often works better than predicting exact returns.

