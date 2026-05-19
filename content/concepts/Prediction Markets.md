---
type: concept
title: "Prediction Markets"
tags:
  - concept
  - prediction-markets
  - market-structure
level: 3
prerequisites:
  - "[[Conditional Probability]]"
  - "[[Expected Value]]"
---

## What It Is

Prediction markets trade contracts that pay out a fixed amount (typically $1) if a specified real-world event resolves YES, and $0 otherwise. The traded price therefore sits in $[0, 1]$ and is interpretable — with caveats — as the market's implied probability of the event.

**Venue landscape:**

- **Polymarket** — on-chain CLOB on Polygon, USDC-settled, broadest event coverage (politics, sports, macro, crypto-specific).
- **Kalshi** — CFTC-regulated US exchange, CLOB, fiat-settled, regulated event categories.
- **Augur, Manifold, Limitless, Azuro** — earlier on-chain or AMM-based designs.
- **PredictIt** (legacy) — US academic exchange, position-capped.

**Microstructure flavors:**

- **CLOB-based** (Polymarket, Kalshi): standard limit order books per outcome; spreads, depth, and queue priority work as in any limit-order venue.
- **AMM-based** (Azuro, original Augur): liquidity from a market-maker contract using cost functions like the [[Logarithmic Market Scoring Rule]] (LMSR); always-on quotes, parameterized maximum loss.

**Resolution.** Each market specifies an oracle (UMA, exchange-designated resolver, regulated reporter). Resolution risk — ambiguity, oracle dispute, delay — is a first-class risk and is not present in spot/derivatives markets.

## Why It Matters

**Prices are probabilities (almost).** This is the structural feature that makes prediction markets uniquely tractable for information-theoretic analysis:

- Edge over the market is exactly $D_{\mathrm{KL}}(p \,\|\, q)$ — see [[KL Divergence]] and [[Kelly Criterion]] for the expected-log-growth identity.
- Implied uncertainty is just $H_2(q)$ — see [[Shannon Entropy]].
- Anomalous moves can be flagged as entropy collapses on a price-implied $H(t)$ time series; threshold $|dH/dt|$ against rolling $\sigma_H$.

**Caveats on the probability interpretation.** Prices equal mean beliefs only under restrictive conditions (risk-neutral traders, identical wealth). With risk aversion, capital constraints, or thin participation, prices systematically deviate from consensus probabilities — well-calibrated in the 0.10–0.90 range, much less so at the extremes. See [[Interpreting Prediction Market Prices — Manski]].

**Why quants trade here:**

- **Clean payoff structure** — binary, capped at $[0, 1]$, no funding/borrow mechanics to model.
- **Direct cross-venue signal flow** — Polymarket vs. Kalshi vs. offshore sportsbooks on the same event create [[Spatial Arbitrage]] and [[Statistical Arbitrage]] opportunities driven by jurisdictional fragmentation.
- **Cross-asset signal** — political and macro markets lead and lag spot/options prices; mineable as features for traditional strategies.
- **Capacity is small but edges can be large** — the same inefficiencies that make capacity small (thin participation, lack of pro market-makers in long-tail markets) make $D_{\mathrm{KL}}$ edges much larger than in equities or perps.

**Recurring risk surface specific to prediction markets:**

- **Resolution / oracle risk** — the dominant non-market risk. Closely read the resolution criteria *before* trading.
- **Insider flow** — political, sports, and person-specific markets attract participants with non-public information. Detectable via entropy-collapse / order-flow anomalies but cannot be eliminated.
- **Liquidity / thinness** — many markets are decoration; tradable size is often $\ll$ posted depth.
- **Long time to resolution** — capital lock-up and discount-rate considerations matter; an annualized return on a 6-month binary differs from the raw payoff.
- **Regulatory** — US access has historically shifted (Polymarket geofencing, Kalshi regulatory wins/losses); jurisdictional risk is part of the trade.

## Resources

- [[Interpreting Prediction Market Prices — Manski]] — when prices ≠ probabilities
- [[Logarithmic Market Scoring Rule]] — the standard AMM design

## Connections

- [[Logarithmic Market Scoring Rule]] — AMM cost function used in prediction-market making
- [[Shannon Entropy]] — implied uncertainty of any binary market price
- [[KL Divergence]] — trading edge in bits between your estimate and the market price
- [[Maximum Entropy Principle]] — fusing heterogeneous signals into a single tradable $p$
- [[Kelly Criterion]] — sizing rule whose expected log-growth equals $D_{\mathrm{KL}}$
- [[Statistical Arbitrage]] — prediction market ↔ spot/derivatives signal flow as a stat-arb source
- [[Interpreting Prediction Market Prices — Manski]] — calibration caveats
