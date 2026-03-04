---
type: concept
title: "Taylor Series"
tags:
  - concept
  - math
  - calculus
level: 1
prerequisites: []
---

# Taylor Series

## What It Is

A **Taylor series** approximates a smooth function $f(x)$ as an infinite polynomial around a point $a$:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots$$

When $a = 0$, it is called a **Maclaurin series**. In practice, we often truncate after a few terms to get a polynomial approximation that is accurate for $x$ near $a$.

Common Taylor expansions:
- $e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots$
- $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ for $|x| < 1$
- $\frac{1}{1-x} = 1 + x + x^2 + x^3 + \cdots$ for $|x| < 1$

## Why It Matters

Taylor series appear throughout quantitative finance:

- **Itô's Lemma derivation**: Itô's Lemma is essentially a Taylor expansion of $f(S, t)$ to second order, where the $(dS)^2$ term survives because Brownian motion has $dW^2 = dt$. This is the key insight of stochastic calculus.
- **Avellaneda-Stoikov asymptotic expansions**: The optimal bid/ask quotes in the Avellaneda-Stoikov model are derived via Taylor expansion of the value function around the terminal time. The famous formula $\delta^* \approx \gamma\sigma^2(T-t) + \frac{2}{\gamma}\ln(1 + \gamma/k)$ comes from such an expansion.
- **Delta-gamma approximation**: Truncating at second order gives $\Delta P \approx \Delta \cdot \delta S + \frac{1}{2}\Gamma \cdot (\delta S)^2$, the standard risk approximation for option portfolios.
- **Log return approximation**: $\ln(1 + r) \approx r - \frac{r^2}{2}$ for small $r$, connecting simple and log returns.

## Key Equations

$$f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2}(x-a)^2 + \mathcal{O}((x-a)^3)$$

**Multivariate Taylor expansion** (needed for Itô's Lemma):

$$f(x+\Delta x, y+\Delta y) \approx f(x,y) + f_x \Delta x + f_y \Delta y + \frac{1}{2}f_{xx}(\Delta x)^2 + f_{xy}\Delta x \Delta y + \frac{1}{2}f_{yy}(\Delta y)^2$$

## Resources

- *Calculus* by James Stewart — Chapter on sequences and series
- *Stochastic Calculus for Finance II* by Shreve — Taylor expansion in the context of Itô's Lemma
- Avellaneda & Stoikov (2008) — asymptotic expansion techniques

## Connections

- [[Derivatives]] — Taylor coefficients are built from successive derivatives
- [[Avellaneda-Stoikov]] — asymptotic expansion of the value function uses Taylor series
- [[Itô's Lemma]] — is a second-order Taylor expansion adapted for stochastic processes
