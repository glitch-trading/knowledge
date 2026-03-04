---
type: concept
title: "Integrals"
tags:
  - concept
  - math
  - calculus
level: 1
prerequisites: []
---

# Integrals

## What It Is

**Integration** is the inverse operation of differentiation. There are two main types:

- **Indefinite integral**: $\int f(x)\,dx = F(x) + C$, where $F'(x) = f(x)$. This gives a family of antiderivatives.
- **Definite integral**: $\int_a^b f(x)\,dx$ computes the signed area under the curve $f(x)$ from $a$ to $b$.

The **Fundamental Theorem of Calculus** connects them:

$$\int_a^b f(x)\,dx = F(b) - F(a)$$

Key techniques include substitution, integration by parts, and partial fractions.

## Why It Matters

Integrals are essential in quant finance for:

- **Expected values**: $E[X] = \int_{-\infty}^{\infty} x \, f(x)\,dx$ — computing means, variances, and any function of a random variable requires integration over the probability density.
- **Option pricing**: The Black-Scholes price is an integral over the risk-neutral distribution of terminal payoffs: $C = e^{-rT} \int_K^{\infty} (S_T - K) f(S_T)\,dS_T$.
- **Cumulative distribution functions**: $F(x) = \int_{-\infty}^{x} f(t)\,dt$ — probabilities are areas under density curves.
- **P&L computation**: Total profit over a period is the integral of instantaneous P&L.
- **Numerical methods**: When closed-form integrals don't exist (which is most of the time in practice), Monte Carlo simulation and numerical quadrature approximate them.

## Key Equations

$$\int_a^b f(x)\,dx = F(b) - F(a) \quad \text{where } F'(x) = f(x)$$

$$E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x)\,dx$$

Integration by parts:

$$\int u\,dv = uv - \int v\,du$$

## Resources

- *Calculus* by James Stewart — Chapters on integration
- 3Blue1Brown: *Essence of Calculus* — integration episodes
- MIT OpenCourseWare: 18.01 Single Variable Calculus

## Connections

- [[Derivatives]] — integration is the inverse of differentiation
- [[Expected Value]] — expected values are computed via integration over densities
- [[Probability Distributions]] — CDFs are integrals of PDFs
