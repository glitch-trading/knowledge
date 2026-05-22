---
type: concept
title: "Maximum Entropy Principle"
tags:
  - concept
  - information-theory
  - probability
level: 4
prerequisites:
  - "[[Shannon Entropy]]"
  - "[[KL Divergence]]"
---

## What It Is

The Maximum Entropy Principle (Jaynes, 1957) states: given partial information about a distribution — typically in the form of moment constraints — the least biased estimate is the distribution with the highest [[Shannon Entropy]] consistent with those constraints. Equivalently, it is the distribution that adds no information beyond what is given.

**Constrained optimization form** — maximize $H(p)$ subject to:

- Normalization: $\sum_i p_i = 1$
- Constraints: $\sum_i f_k(x_i)\,p_i = \mu_k$ for $k = 1, \dots, K$ (known moments / expectations)

The Lagrangian solution is the **exponential family**:

$$p^*(x_i) = \frac{1}{Z}\exp\!\left(\sum_k \lambda_k f_k(x_i)\right)$$

where $Z = \sum_i \exp(\cdot)$ is the partition function and $\lambda_k$ are Lagrange multipliers fixed by the constraint equations.

**Recovery of familiar distributions** as max-ent solutions:

- No constraints (finite support): uniform.
- Fixed mean on $[0, \infty)$: exponential.
- Fixed mean and variance on $\mathbb{R}$: Gaussian.
- Fixed mean and variance on $[0, \infty)$: gamma (in the limit).
- Fixed binary mean: Bernoulli.

Maximum entropy is also the distribution that **minimizes $D_{\mathrm{KL}}$ from a chosen prior** subject to the constraints (the prior is uniform when not specified).

## Why It Matters

**Honest prior construction under partial information.** Two practical regimes where this is the right tool:

- **Signal fusion without overfitting.** Given several probability estimates for the same event (model output, base rate, order-book skew, sentiment), and a confidence weight per signal, the max-ent fused distribution under the constraint that the weighted mean matches the consensus is the unique Bernoulli that injects no further information. You cannot overfit because there is no free parameter to fit — only the constraints you already specified. Compare to averaging (silently assumes equal weights and independence), ad-hoc weighted blends (subjective), or ML ensembles (need data, drift, overfit on backtests).
- **Tail-modeling under moment constraints.** When all you reliably know about a return distribution is the mean and variance, the Gaussian is the max-ent answer. If you also constrain a higher moment or a tail probability, the max-ent solution deforms toward fatter tails by construction, giving a principled fat-tail model without invoking a specific parametric form. See [[Fat Tails]].

**What it does not do:**

- Generate information you didn't supply. The output is only as good as the constraints. Garbage moments in, garbage distribution out.
- Replace causal modeling. Max-ent is a *prior* under stated constraints, not a forecast.
- Eliminate the need to validate the constraints themselves. If the constraint is a model output that is biased, the max-ent distribution inherits the bias.

**Connection to ML.** Conditional maximum entropy classifiers are exactly logistic / softmax regression. The cross-entropy loss minimized in training is the gap between empirical labels and the model's max-ent fit under the feature-expectation constraints. See [[Logistic Regression]].

## Key Equations

**Max-ent distribution under moment constraints:**
$$p^*(x_i) = \frac{1}{Z(\boldsymbol{\lambda})}\exp\!\left(\sum_k \lambda_k f_k(x_i)\right)$$

**Lagrange multipliers solve:**
$$\frac{\partial \log Z}{\partial \lambda_k} = \mu_k$$

**Equivalence to minimum KL from a prior $q$:**
$$p^* = \arg\min_{p} D_{\mathrm{KL}}(p \,\|\, q) \quad \text{s.t. constraints}$$

(Uniform $q$ recovers pure max-entropy.)

## Resources

- Jaynes, E.T. (1957) — "Information Theory and Statistical Mechanics" (two-part paper)
- Jaynes, E.T. — *Probability Theory: The Logic of Science*
- Cover & Thomas — *Elements of Information Theory*, Ch. 12

## Connections

- [[Shannon Entropy]] — the quantity being maximized
- [[KL Divergence]] — max-ent equals min-KL from the prior; the dual view
- [[Logistic Regression]] — conditional max-ent under feature-expectation constraints
- [[Normal Distribution]] — max-ent under fixed mean and variance on $\mathbb{R}$
- [[Exponential Distribution]] — max-ent under fixed positive mean
- [[Fat Tails]] — adding higher-moment constraints produces principled heavy-tailed priors
- [[Prediction Markets]] — natural setting for fusing heterogeneous signals into a single tradable probability
