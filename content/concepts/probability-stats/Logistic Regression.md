---
type: concept
title: "Logistic Regression"
tags:
  - concept
  - statistics
  - ML
level: 3
prerequisites:
  - "[[Regression]]"
---

## What It Is

Logistic regression models the probability of a binary outcome (yes/no, up/down, fill/no-fill) as a function of input variables. Unlike linear regression which outputs unbounded values, logistic regression maps inputs through the sigmoid (logistic) function to produce a probability in $[0, 1]$.

**The model:**
$$P(Y = 1 \mid X) = \sigma(\beta_0 + \beta_1 X_1 + \cdots + \beta_n X_n) = \frac{1}{1 + e^{-(\beta_0 + \beta^T X)}}$$

The sigmoid function $\sigma(z) = 1/(1+e^{-z})$ squashes any real number into $(0, 1)$, giving a natural probability interpretation.

**Key properties:**
- Coefficients are estimated via maximum likelihood (not OLS).
- $\beta_i$ represents the change in **log-odds** for a unit change in $X_i$.
- Decision boundary: classify as 1 if $P > 0.5$ (or any chosen threshold).
- Can be extended to multiple categories: multinomial logistic regression.

## Why It Matters

- **Binary prediction in trading**: "Will this trade be profitable?" "Will this order fill?" "Will this position get liquidated?" These are all binary outcomes naturally suited to logistic regression.
- **Prediction markets**: Prediction market contracts settle at 0 or 1. Logistic regression is a natural model for estimating the probability of the event, helping you price and trade these contracts.
- **Classification with probability**: Unlike many ML classifiers, logistic regression gives calibrated probabilities, not just yes/no predictions. This is crucial for trading where you need to size positions based on confidence.
- **Interpretability**: Coefficients have clear interpretations (odds ratios). In a field where understanding *why* a model makes a prediction matters for risk management, interpretability is valuable.
- **Baseline model**: Before trying complex ML, try logistic regression. If it can't find a signal, fancier models probably won't either (or they'll overfit).

## Key Equations

**Logistic (sigmoid) function:**
$$\sigma(z) = \frac{1}{1 + e^{-z}} = \frac{e^z}{1 + e^z}$$

**Log-odds (logit):**
$$\ln\left(\frac{P}{1-P}\right) = \beta_0 + \beta^T X$$

**Odds ratio for coefficient $\beta_j$:**
$$OR_j = e^{\beta_j}$$

A one-unit increase in $X_j$ multiplies the odds by $e^{\beta_j}$.

**Maximum likelihood estimation:**
$$\ell(\beta) = \sum_{i=1}^n \left[ y_i \ln(\hat{p}_i) + (1-y_i) \ln(1-\hat{p}_i) \right]$$

This is the log-likelihood (equivalently, negative cross-entropy loss) that is maximized to find $\hat{\beta}$.

**Classification metrics:**
- Accuracy, precision, recall, F1
- AUC-ROC: Area under the receiver operating characteristic curve
- Brier score: $\frac{1}{n}\sum(p_i - y_i)^2$ — measures probability calibration

## Resources

- James, Witten, Hastie, Tibshirani — *An Introduction to Statistical Learning* (ISL), Chapter 4
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning* (ESL)
- Andrew Ng — Stanford CS229 lecture notes on logistic regression

## Connections

- [[Regression]] — Logistic regression extends linear regression to binary outcomes
- [[Probability Distributions]] — The Bernoulli distribution underlies logistic regression
- [[Time Series Analysis]] — Logistic regression can incorporate lagged features for sequential prediction
