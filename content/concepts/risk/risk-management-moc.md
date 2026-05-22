---
title: "Risk Management — Map of Content"
type: MOC
tags:
  - MOC
  - risk
---

## Position Sizing
- [[kelly-criterion|Kelly Criterion]]
- [[position-sizing|Position Sizing]]
- Fractional Kelly (practical application)

## Risk Metrics
- [[value-at-risk|Value at Risk]]
- [[expected-shortfall|Expected Shortfall]]
- [[maximum-drawdown|Maximum Drawdown]]
- [[sharpe-ratio|Sharpe Ratio]]
- [[sortino-ratio|Sortino Ratio]]
- [[information-ratio|Information Ratio]] — benchmark-relative, the standard active-management metric
- [[information-coefficient|Information Coefficient]] — signal-level skill, feeds the [[fundamental-law-of-active-management|Fundamental Law of Active Management]]

## Fat Tails & Extreme Events
- [[fat-tails|Fat Tails]]
- [[power-law-distribution|Power Law Distribution]]
- Extreme value theory (Level 6)
- Correlation ≠ 1 until a crash (contagion)

## Crypto-Specific Risks
- Exchange counterparty risk
- Smart contract risk
- [[liquidity|Liquidity]] risk
- Oracle manipulation
- Bridge risk (cross-chain)
- Regulatory risk

## Execution Risk
- [[leg-risk|Leg Risk]] — non-atomic multi-leg fills convert "guaranteed" arbs into directional positions
- "Becoming exit liquidity" — copy-trading a faster arber means filling the *corrected* price

## Risk Aversion & Utility
- [[risk-aversion|Risk Aversion]]
- [[utility-theory|Utility Theory]]
- [[exponential-utility|Exponential Utility]]

## Stress Testing
- Historical crash scenarios (March 2020, May 2021, FTX Nov 2022)
- Correlation breakdown under stress

## Operational Risk Controls
- [[kill-switch|Kill Switch]] — automated halt on drawdown / loss streaks / stale data / behavioral divergence
- [[paper-trading|Paper Trading]] — validation layer that catches operational bugs before live capital sees them
- [[trading-bot-operations|Trading Bot Operations]] — the production checklist that prevents most "the strategy was fine but…" losses

## Execution & Process Discipline
- [[trade-journaling|Trade Journaling]]
- [[trading-psychology|Trading Psychology]]
- Macro / high-impact data event awareness (avoid open trades into known releases)
- Pre-trade devil's advocate (list reasons *not* to take the trade)

## Backtest Pitfalls
- [[overfitting|Overfitting]]
- [[survivorship-bias|Survivorship Bias]]
- [[look-ahead-bias|Look-Ahead Bias]]
- [[hypothesis-testing|Hypothesis Testing]] — multiple-testing correction
- [[the-deflated-sharpe-ratio-bailey-and-lopez-de-prado|The Deflated Sharpe Ratio — Bailey & López de Prado]]
