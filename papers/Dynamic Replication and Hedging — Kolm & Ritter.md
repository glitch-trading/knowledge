---
type: paper
title: "Dynamic Replication and Hedging: A Practitioner's Approach"
authors: "Petter N. Kolm & Gordon Ritter"
year: 2015
status: unread
tags:
  - paper
  - kalman-filter
  - hedging
level: 6
topics:
  - "[[Statistical Arbitrage]]"
---

# Dynamic Replication and Hedging — Kolm & Ritter

**Authors:** Petter N. Kolm & Gordon Ritter
**Year:** 2015

## Summary

Applies Kalman filters to dynamic hedging and replication problems in finance. The Kalman filter tracks hidden state variables (true price, hedge ratio, spread mean) from noisy observations, adapting in real time as market conditions change.

## Key Results

- Kalman filters provide optimal estimates of hidden states given noisy observations — natural fit for estimating fair value from multiple venue prices
- Dynamic hedge ratios estimated via Kalman filter outperform static OLS estimates for pairs trading
- State-space formulation handles regime changes gracefully through time-varying parameters
- Practical framework connecting signal processing to trading strategy implementation

## Connections

- [[Level 6 — Advanced Topics]] — Kalman filters in advanced statistical methods
- [[Statistical Arbitrage]] — dynamic hedge ratio estimation for pairs trading
- [[Quantitative Risk Management — McNeil, Frey & Embrechts]] — EVT pairs with Kalman for tail-aware filtering
