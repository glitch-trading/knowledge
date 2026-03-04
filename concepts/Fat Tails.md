---
type: concept
title: "Fat Tails"
tags:
  - concept
  - probability
  - risk
level: 1
prerequisites: []
---

# Fat Tails

## What It Is

A distribution has **fat tails** (or **heavy tails**) when extreme events occur much more frequently than a normal distribution predicts. Formally, a distribution is fat-tailed if its tails decay slower than exponentially — typically following a power law $P(X > x) \sim x^{-\alpha}$.

Ways to measure fat tails:
- **Kurtosis**: $\kappa = E[(X-\mu)^4]/\sigma^4$. The normal distribution has $\kappa = 3$. Fat-tailed distributions have **excess kurtosis** $\kappa - 3 > 0$. Financial returns typically show $\kappa$ between 5 and 50.
- **QQ-plot**: Plot quantiles of your data against quantiles of a normal distribution. Fat tails show up as deviations at both extremes — the observed extremes are much larger than predicted.
- **Tail index**: The power law exponent $\alpha$ — smaller values mean fatter tails. Many financial time series have $\alpha$ between 2 and 5.

Related concepts:
- **Leptokurtic**: More peaked center and fatter tails than normal (most financial returns)
- **Sub-exponential tails**: The sum of sub-exponential random variables is dominated by the maximum — one extreme event drives the total

## Why It Matters

Fat tails are not an academic curiosity — they are the central risk management challenge in quantitative trading:

- **Risk underestimation**: A normal model says a 5-sigma daily move in the S&P 500 should happen roughly once every 14,000 years. In reality, it happens every few years. Models built on normality systematically understate the probability and magnitude of extreme losses.
- **Crypto is extremely fat-tailed**: Cryptocurrency returns have some of the fattest tails of any asset class. 10-20% daily moves in BTC are not rare; 50%+ moves have occurred. Any risk model or market-making strategy that assumes normality will be catastrophically wrong.
- **VaR failures**: [[Value at Risk]] under normality told banks they were safe before 2008. Fat tails meant the actual losses were multiples of what VaR predicted. [[Expected Shortfall]] partially addresses this but still depends on the tail model.
- **Practical implications for market making**:
  - Wider spreads are needed to compensate for extreme adverse moves
  - Inventory limits must be tighter than normal-based models suggest
  - Stop-losses may gap through — you can't always exit at your intended price
  - The Avellaneda-Stoikov model assumes Brownian (normal) price dynamics; real implementation must account for fat tails
- **Diversification breaks down**: In fat-tailed markets, correlations spike during crises. The diversification benefit you counted on evaporates exactly when you need it most.
- **Positive fat tails exist too**: Extreme positive returns (squeezes, breakouts) are also more common than normal. This matters for position sizing and opportunity capture.

## Key Equations

Excess kurtosis:

$$\kappa_{\text{excess}} = \frac{E[(X - \mu)^4]}{\sigma^4} - 3$$

For a power law tail with exponent $\alpha$:

$$P(|X| > x) \sim x^{-\alpha}$$

- $\alpha > 4$: finite kurtosis (mild fat tails)
- $2 < \alpha \le 4$: infinite kurtosis (moderate fat tails)
- $\alpha \le 2$: infinite variance (extreme fat tails)

Rule of thumb — ratio of actual extreme events to normal-predicted:

| Event size | Normal predicts | Actual (typical) |
|---|---|---|
| 3-sigma | 1 in 370 | 1 in 50-100 |
| 5-sigma | 1 in 3.5M | 1 in 1,000-5,000 |
| 10-sigma | ~impossible | Has happened |

## Resources

- *The Black Swan* by Nassim Taleb — the definitive popular treatment
- *Statistical Consequences of Fat Tails* by Nassim Taleb — technical treatment
- *Quantitative Risk Management* by McNeil, Frey & Embrechts — EVT and tail modeling
- Cont (2001), "Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues"

## Connections

- [[Power Law Distribution]] — the mathematical model behind most fat-tailed phenomena
- [[Normal Distribution]] — the baseline that fat tails deviate from
- [[Value at Risk]] — risk metric that fails under fat tails
- [[Expected Shortfall]] — a tail-sensitive alternative to VaR
