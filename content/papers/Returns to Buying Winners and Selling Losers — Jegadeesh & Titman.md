---
type: paper
title: "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency"
authors: "Narasimhan Jegadeesh & Sheridan Titman"
year: 1993
status: not-started
tags:
  - paper
  - factor-investing
  - momentum
  - market-anomalies
level: 5
topics:
  - "[[Momentum]]"
  - "[[Statistical Arbitrage]]"
---

## Summary

Jegadeesh and Titman document that, in U.S. equities from 1965-1989, a long-short portfolio that buys the past 3-12 month winners and sells the past 3-12 month losers earns ~1% per month for the following 3-12 months. The effect is statistically and economically significant, robust across formation/holding-window combinations, and not explained by [[CAPM]] beta or known size effects. This is the founding empirical paper of [[Momentum]] as a tradeable factor.

## Key Results

- A 6-month-formation / 6-month-holding momentum strategy returns ~12% per year before transaction costs, with the long leg and short leg both contributing.
- The effect is strongest in months 3-12 after formation and partially reverses at longer horizons (2-3 years), foreshadowing the De Bondt-Thaler long-term reversal.
- Returns are not eaten up by exposure to market beta or firm size — there is residual alpha after controlling for [[CAPM]]-style factors.
- Transaction costs are real but do not eliminate the strategy at institutional scale.

## Equations & Derivations

For each month $t$, sort stocks by return over the prior $J$ months (formation period). Form an equal-weighted long portfolio of the top decile (winners) and short portfolio of the bottom decile (losers). Hold for $K$ months. The strategy return is

$$R_t^{\text{mom}} = \frac{1}{K} \sum_{k=1}^{K} \left( R_{t,k}^{\text{winners}} - R_{t,k}^{\text{losers}} \right)$$

The overlapping-portfolios construction means at any time $t$ you hold $K$ stacked formations — averaging away formation-month idiosyncratic noise.

The reported alpha is from regressing $R_t^{\text{mom}}$ on the market excess return:

$$R_t^{\text{mom}} = \alpha + \beta \, R_t^{m,e} + \varepsilon_t$$

with $\hat\alpha$ significantly positive across $(J, K)$ combinations.

## Connections

- [[Momentum]] — The factor concept this paper established
- [[Fama-French Three-Factor Model]] — Momentum is the canonical "fourth factor" later added (Carhart 1997)
- [[Statistical Arbitrage]] — Momentum is one of the canonical [[Statistical Arbitrage|stat arb]] signals
- [[Overfitting]] — Momentum is one of the few academic anomalies that has survived out-of-sample across decades and markets
- [[The Deflated Sharpe Ratio — Bailey & López de Prado]] — Useful counterweight: most "discovered" anomalies don't survive multiple-testing correction; momentum does
