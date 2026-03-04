---
type: concept
title: "Normal Distribution"
tags:
  - concept
  - probability
  - distributions
level: 1
prerequisites: []
---

# Normal Distribution

## What It Is

The **normal (Gaussian) distribution** is the most important continuous distribution in statistics and finance. A random variable $X \sim \mathcal{N}(\mu, \sigma^2)$ has PDF:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$

Key properties:
- Symmetric bell curve centered at $\mu$
- $\sigma$ controls the width: 68% of values within $\pm 1\sigma$, 95% within $\pm 2\sigma$, 99.7% within $\pm 3\sigma$
- **Standard normal**: $Z = (X - \mu)/\sigma \sim \mathcal{N}(0, 1)$ — any normal can be standardized
- Sum of independent normals is normal: $X + Y \sim \mathcal{N}(\mu_X + \mu_Y, \sigma_X^2 + \sigma_Y^2)$
- **Central Limit Theorem (CLT)**: The sum (or average) of many independent, identically distributed random variables converges to a normal distribution, regardless of the original distribution. This is why the normal distribution appears so often.
- Fully characterized by two parameters: $\mu$ (mean) and $\sigma^2$ (variance)

## Why It Matters

The normal distribution is the default model in classical finance, and understanding its strengths and limitations is essential:

- **Return modeling**: Short-horizon log returns are often modeled as $r_t \sim \mathcal{N}(\mu, \sigma^2)$. This is the assumption behind Black-Scholes, Markowitz portfolio theory, and most risk models.
- **Brownian motion**: $W_t \sim \mathcal{N}(0, t)$ — Brownian increments are normally distributed. This drives all of stochastic calculus.
- **Risk metrics**: VaR under normality is simply $\mu - z_\alpha \sigma$. Easy to compute, but dangerously wrong in the tails.
- **Z-scores**: Standardizing returns as $z = (r - \mu)/\sigma$ allows comparison across assets and time periods.
- **Where it breaks down**: Real market returns exhibit [[Fat Tails]] — extreme events (crashes, squeezes) happen far more often than the normal distribution predicts. A "6-sigma" event under normality should happen once every 1.5 million years; in markets, they happen every few years. This is the central limitation of normal-based models.

## Key Equations

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

$$Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1)$$

$$P(|X - \mu| > k\sigma) \approx \begin{cases} 31.7\% & k=1 \\ 4.6\% & k=2 \\ 0.27\% & k=3 \\ 0.006\% & k=4 \end{cases}$$

$$\text{CLT: } \bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{d} \mathcal{N}\!\left(\mu, \frac{\sigma^2}{n}\right)$$

## Resources

- *All of Statistics* by Larry Wasserman — Chapter 3
- *Options, Futures, and Other Derivatives* by John Hull — normal assumption in Black-Scholes
- *The Black Swan* by Nassim Taleb — why the normal distribution is dangerous in finance

## Connections

- [[Log-Normal Distribution]] — if $\ln(X)$ is normal, then $X$ is log-normal; prices vs. returns
- [[Brownian Motion]] — increments are normally distributed
- [[Fat Tails]] — the most important limitation of the normal model in finance
- [[Variance]] — the normal distribution is fully defined by mean and variance
