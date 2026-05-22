---
type: concept
title: "Itô's Lemma"
tags:
  - concept
  - stochastic-calculus
level: 2
prerequisites:
  - "[[ito-calculus|Itô Calculus]]"
  - "[[chain-rule|Chain Rule]]"
---

## What It Is
Itô's Lemma is the chain rule for stochastic calculus. Given a smooth function $f(t, X)$ where $X$ follows a stochastic process, Itô's Lemma tells you how $f$ evolves. The critical difference from the ordinary chain rule is an extra second-order term that arises because $(dW)^2 = dt$.

In ordinary calculus, the chain rule for $f(t, x)$ gives $df = f_t \, dt + f_x \, dx$. In stochastic calculus, you must keep the second-order term: $\frac{1}{2} f_{xx} (dX)^2$. This term survives because the quadratic variation of Brownian Motion is non-zero.

## Why It Matters
Itô's Lemma is used constantly in quantitative finance:
- Deriving the [[black-scholes-equation|Black-Scholes Equation]] from GBM
- Solving the GBM SDE to get the explicit stock price formula (and the $\sigma^2/2$ correction)
- Transforming value functions in the HJB equation (as done in Avellaneda-Stoikov Section 3)
- Converting between different representations of stochastic processes

## Key Equations

If $dX = \mu \, dt + \sigma \, dW$ and $f = f(t, X)$, then:

$$df = \frac{\partial f}{\partial t} dt + \frac{\partial f}{\partial X} dX + \frac{1}{2} \frac{\partial^2 f}{\partial X^2} (dX)^2$$

Expanding $(dX)^2 = \sigma^2 \, dt$:

$$df = \left(\frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial X} + \frac{1}{2} \sigma^2 \frac{\partial^2 f}{\partial X^2}\right) dt + \sigma \frac{\partial f}{\partial X} dW$$

The $\frac{1}{2} \sigma^2 f_{XX}$ term is the Itô correction — absent in ordinary calculus.

## Applied: GBM → log-price drift

Take $S$ following GBM, $dS = \mu S \, dt + \sigma S \, dW$, and let $f(S) = \log S$. Then $f' = 1/S$ and $f'' = -1/S^2$:

$$d(\log S) = \frac{1}{S} \cdot dS + \tfrac{1}{2}\left(-\frac{1}{S^2}\right)(\sigma S)^2 dt = \left(\mu - \tfrac{1}{2}\sigma^2\right) dt + \sigma\, dW$$

That $-\sigma^2/2$ is the entire reason geometric returns differ from arithmetic returns. Verifying it numerically also verifies that Itô's lemma is the right calculus:

```python
import numpy as np

mu, sigma, T, n_steps, n_paths = 0.10, 0.30, 1.0, 252, 100_000
dt = T / n_steps
rng = np.random.default_rng(0)
dW = rng.normal(0.0, np.sqrt(dt), size=(n_paths, n_steps))

# Exact GBM step (Itô-aware): log-additive with the -σ²/2 correction.
log_S = np.cumsum((mu - 0.5 * sigma**2) * dt + sigma * dW, axis=1)

drift_per_unit_time = log_S[:, -1].mean() / T
print(f"empirical drift of log S: {drift_per_unit_time:.4f}")  # ≈ μ − σ²/2 = 0.055
print(f"Itô-predicted drift:      {mu - 0.5 * sigma**2:.4f}")  # 0.055
```

Drop the $-\tfrac{1}{2}\sigma^2$ term and the simulated drift will systematically overshoot — that bias is exactly the Itô correction made visible.

## Resources
- Shreve, *Stochastic Calculus for Finance II*, Chapter 4.4
- Oksendal, *Stochastic Differential Equations*, Theorem 4.1.2

## Connections
- [[ito-calculus|Itô Calculus]] — the framework from which Itô's Lemma is derived
- [[chain-rule|Chain Rule]] — the ordinary calculus analog that Itô's Lemma generalizes
- [[stochastic-differential-equations|Stochastic Differential Equations]] — Itô's Lemma is the primary tool for manipulating SDEs
- [[black-scholes-equation|Black-Scholes Equation]] — the canonical application; derivation hinges on Itô applied to $V(S, t)$
- [[greeks|Greeks]] — partial derivatives of $V$; their P&L expansion is Itô applied to the option's value
