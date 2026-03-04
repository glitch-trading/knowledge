---
type: concept
title: "Log-Normal Distribution"
tags:
  - concept
  - probability
  - distributions
level: 1
prerequisites: []
---

# Log-Normal Distribution

## What It Is

A random variable $X$ has a **log-normal distribution** if $\ln(X)$ is normally distributed. If $\ln(X) \sim \mathcal{N}(\mu, \sigma^2)$, then:

$$f(x) = \frac{1}{x\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right), \quad x > 0$$

Key properties:
- $X > 0$ always — the support is strictly positive
- Right-skewed: the distribution has a long right tail
- $E[X] = e^{\mu + \sigma^2/2}$
- $\text{Var}(X) = (e^{\sigma^2} - 1) \cdot e^{2\mu + \sigma^2}$
- The product of independent log-normals is log-normal (because the sum of their logs is normal)
- The median is $e^\mu$, which is less than the mean

## Why It Matters

The log-normal distribution is the standard model for asset prices (as opposed to returns):

- **Price positivity**: Prices cannot go negative (ignoring rare cases like oil futures). The log-normal distribution enforces this constraint naturally, while the normal distribution does not.
- **Geometric Brownian Motion**: The Black-Scholes model assumes $dS = \mu S\,dt + \sigma S\,dW$. The solution is $S_T = S_0 \exp\!\left((\mu - \sigma^2/2)T + \sigma W_T\right)$, which means $S_T$ is log-normally distributed.
- **Multiplicative returns**: Price changes are multiplicative (a 10% gain followed by a 10% loss is not zero). The log-normal model captures this multiplicative nature.
- **Log returns are normal**: If prices are log-normal, then log returns $\ln(S_t/S_{t-1})$ are normally distributed. This is why quants work with log returns — they transform the multiplicative problem into an additive one.
- **Drift correction**: Note the $-\sigma^2/2$ term in the exponent. This is the Itô correction — the expected log return is $\mu - \sigma^2/2$, not $\mu$. This distinction matters for volatility drag in portfolio management.

## Key Equations

If $\ln(S_T) \sim \mathcal{N}(\mu, \sigma^2)$:

$$S_T = S_0 \exp\!\left(\left(\mu - \frac{\sigma^2}{2}\right)T + \sigma W_T\right)$$

$$E[S_T] = S_0 e^{\mu T}$$

$$\ln\!\left(\frac{S_T}{S_0}\right) \sim \mathcal{N}\!\left(\left(\mu - \frac{\sigma^2}{2}\right)T,\; \sigma^2 T\right)$$

## Resources

- *Options, Futures, and Other Derivatives* by John Hull — Chapter on Black-Scholes
- *Stochastic Calculus for Finance II* by Shreve — rigorous derivation
- *Paul Wilmott Introduces Quantitative Finance* — intuitive treatment

## Connections

- [[Normal Distribution]] — the logarithm of a log-normal variable is normal
- [[Geometric Brownian Motion]] — the process whose solution is log-normally distributed
