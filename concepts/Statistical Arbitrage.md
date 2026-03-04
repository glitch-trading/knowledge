---
type: concept
title: "Statistical Arbitrage"
tags:
  - concept
  - strategies
  - stat-arb
level: 2-5
prerequisites: []
---

# Statistical Arbitrage

## What It Is

Statistical arbitrage (stat arb) is not riskless arbitrage — it is a **probabilistic edge** derived from statistical relationships between assets or markets. You identify a pattern that has historically been profitable, model its expected behavior, and trade deviations from that model. The "arbitrage" is in the expected value, not in guaranteed profit.

**Core approaches:**
- **Mean reversion / pairs trading**: Two correlated assets diverge. Bet on convergence. Requires [[Cointegration]] (not just correlation) to be robust.
- **Cross-venue signal extraction**: Use price information from one venue to predict moves on another. CEX price leads DEX price — trade the DEX using CEX signals.
- **Prediction markets**: Market prices embed probabilities. When your model disagrees with the market price, you trade the edge.
- **Factor models**: Decompose returns into systematic factors. Trade residuals (alpha) after hedging out factor exposure.

**Key distinction:** Deterministic arbitrage (spatial arb, triangular arb) guarantees profit per trade. Stat arb guarantees nothing per trade — the edge only materializes over many trades through the law of large numbers.

## Why It Matters

Stat arb is where most of the money in quantitative trading is made. Pure arbitrage opportunities are competed away to near-zero. Stat arb opportunities persist because:

- **They require models.** Not everyone has the same model or the same data.
- **They require infrastructure.** Fast execution, reliable data pipelines, risk management systems.
- **They involve risk.** Most participants won't take the risk, even if the expected value is positive.
- **They are dynamic.** Relationships change. You need to continuously adapt.

**What makes stat arb hard:**
- **[[Overfitting]]**: The biggest enemy. Historical patterns that aren't real.
- **Regime changes**: Correlations break during crises. Mean-reverting pairs can diverge permanently.
- **Crowding**: If too many people trade the same signal, the edge disappears (or inverts).
- **Transaction costs**: Many stat arb signals are small. After fees and slippage, net edge can be zero.

## Key Equations

**Cointegration test (Engle-Granger):**

For assets $X_t$ and $Y_t$, test if $Z_t = Y_t - \beta X_t$ is stationary (i.e., mean-reverting).

$$Y_t = \alpha + \beta X_t + Z_t$$

If $Z_t$ is stationary (ADF test rejects unit root), the pair is cointegrated. Trade when $Z_t$ deviates from its mean.

**Z-score entry signal:**
$$z = \frac{Z_t - \mu_Z}{\sigma_Z}$$

Enter when $|z| > 2$, exit when $|z| < 0.5$ (typical thresholds, but beware overfitting these).

## Resources

- [[Algorithmic Trading — Ernie Chan]] — Practical stat arb implementation
- Avellaneda & Lee (2010) — "Statistical Arbitrage in the U.S. Equities Market"
- [[Advances in Financial Machine Learning — López de Prado]]

## Connections

- [[Cointegration]] — The statistical foundation for pairs trading / mean reversion
- [[Funding Rate Arbitrage]] — A specific stat arb strategy in crypto
- [[Regression]] — Core tool for modeling statistical relationships
