---
type: concept
title: "Value at Risk"
tags:
  - concept
  - risk
level: 3
prerequisites: []
---

# Value at Risk

## What It Is

Value at Risk (VaR) answers: "What is the maximum loss at X% confidence over Y days?" For example, a 1-day 95% VaR of $1M means: "On 95% of days, we expect to lose no more than $1M."

**Common VaR methods:**
- **Parametric (variance-covariance)**: Assumes returns are [[Normal Distribution|normally distributed]]. VaR = $\mu - z_\alpha \cdot \sigma$. Fast, but the normality assumption is badly wrong for most financial assets.
- **Historical simulation**: Use the empirical distribution of past returns. No distributional assumptions, but limited by sample size and assumes the past represents the future.
- **Monte Carlo**: Simulate many scenarios from a fitted model. Flexible, but only as good as your model.

## Why It Matters

VaR became the standard risk metric in banking regulation (Basel accords) and institutional risk management. It's simple, intuitive, and easy to communicate to management.

**But VaR has critical flaws:**

1. **It says nothing about tail losses.** A 95% VaR tells you the threshold, not what happens beyond it. Your worst 5% of outcomes could be catastrophic, and VaR doesn't care.
2. **It is not subadditive.** Combining two portfolios can produce a VaR worse than the sum of individual VaRs. This violates basic diversification logic.
3. **Nearly useless for crypto.** Crypto returns exhibit extreme [[Fat Tails]] — the 1% worst outcomes are far worse than any Gaussian model predicts. A VaR model calibrated to normal conditions fails spectacularly during crashes.
4. **Encourages tail risk.** Traders can game VaR by selling deep out-of-the-money options: most days look fine, but blow-up days are catastrophic.

Use [[Expected Shortfall]] instead — it addresses most of these problems.

## Key Equations

**Parametric VaR (normal):**
$$VaR_\alpha = \mu + z_\alpha \cdot \sigma$$

Where $z_\alpha$ = z-score at confidence level $\alpha$ (e.g., $z_{0.05} = -1.645$).

**Portfolio VaR:**
$$VaR_p = z_\alpha \cdot \sqrt{w^T \Sigma w}$$

Where $w$ = weight vector, $\Sigma$ = covariance matrix.

## Resources

- [[Quantitative Risk Management — McNeil, Frey & Embrechts]] — Rigorous treatment
- Jorion, P. — *Value at Risk* (the standard reference)

## Connections

- [[Expected Shortfall]] — The superior alternative that measures average tail loss
- [[Normal Distribution]] — The assumption behind parametric VaR (and why it fails)
- [[Fat Tails]] — Why VaR breaks down for crypto and most real financial data
