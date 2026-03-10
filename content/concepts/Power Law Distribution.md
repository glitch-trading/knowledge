---
type: concept
title: "Power Law Distribution"
tags:
  - concept
  - probability
  - distributions
level: 1
prerequisites: []
---

## What It Is

A **power law distribution** has a probability tail that decays polynomially rather than exponentially:

$$P(X > x) \sim x^{-\alpha}, \quad x \to \infty$$

The PDF (for a Pareto distribution, the canonical power law) is:

$$f(x) = \frac{\alpha x_m^\alpha}{x^{\alpha+1}}, \quad x \ge x_m$$

Key properties:
- **Heavy tails**: Probability decays much slower than for the normal or exponential distributions. Extreme values are far more likely.
- **Scale invariance**: Power laws look the same at any scale — zooming in on the tail gives the same shape. This is self-similarity.
- **Moments may not exist**: If $\alpha \le 2$, the variance is infinite. If $\alpha \le 1$, even the mean is infinite. This has profound implications for estimation.
- **80/20 rule**: Power laws generate Pareto-like phenomena — a small fraction of events accounts for the bulk of the effect.
- **Log-log linearity**: On a log-log plot, power law data appears as a straight line with slope $-\alpha$.

## Why It Matters

Power laws capture features of financial markets that normal distributions cannot:

- **Market order sizes**: The distribution of trade sizes in most markets follows a power law with $\alpha \approx 1.5$. A few very large orders dominate total volume.
- **Price impact**: Large orders have disproportionate price impact. The square-root impact model $\Delta P \propto \sqrt{V}$ is closely related to power law order size distributions.
- **Extreme events**: Market crashes, flash crashes, and liquidity crises are power-law-distributed. A "100-year flood" in normal distribution terms might actually occur every decade.
- **Avellaneda-Stoikov context**: While the basic model uses exponential fill probabilities, real-world order book dynamics exhibit power law features in queue sizes and order flow clustering.
- **Crypto markets**: Cryptocurrency markets exhibit particularly strong power law behavior — extreme moves, highly skewed returns, and heavy-tailed volume distributions.
- **Wealth and returns**: Cross-sectional returns often exhibit power law tails. The best-performing assets vastly outperform the median.
- **Tail exponent estimation**: Estimating $\alpha$ from data is tricky. The Hill estimator and maximum likelihood methods are preferred over naive log-log regression.

## Key Equations

$$P(X > x) \sim C x^{-\alpha} \quad \text{(tail probability)}$$

$$f(x) = \frac{\alpha x_m^\alpha}{x^{\alpha+1}}, \quad x \ge x_m \quad \text{(Pareto PDF)}$$

$$E[X^k] < \infty \iff k < \alpha \quad \text{(moment existence)}$$

Hill estimator for $\alpha$:

$$\hat{\alpha} = \left(\frac{1}{n}\sum_{i=1}^{n} \ln\frac{X_{(i)}}{X_{(n)}}\right)^{-1}$$

## Resources

- *The Black Swan* by Nassim Taleb — power laws and fat tails in practice
- *Critical Phenomena in Natural Sciences* by Sornette — power laws in financial crashes
- Gabaix et al. (2003), "A Theory of Power-Law Distributions in Financial Market Fluctuations"
- Clauset, Shalizi & Newman (2009), "Power-Law Distributions in Empirical Data"

## Connections

- [[Fat Tails]] — power laws are the primary mechanism producing fat tails in financial data
- [[Avellaneda-Stoikov]] — real order flow deviates from exponential assumptions toward power laws
