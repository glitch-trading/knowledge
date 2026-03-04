---
type: paper
title: "Uniswap v3: The Universal AMM"
authors: "Hayden Adams, Noah Zinsmeister, Dan Robinson"
year: 2021
status: unread
tags:
  - paper
  - AMM
  - DeFi
level: 4
topics:
  - "[[AMM]]"
  - "[[Impermanent Loss]]"
  - "[[Market Making]]"
---

# Uniswap v3 — The Universal AMM — Adams et al.

**Authors:** Hayden Adams, Noah Zinsmeister, Dan Robinson
**Year:** 2021

## Summary

Deep dive into concentrated liquidity mechanics beyond the [[Uniswap v3 Whitepaper]]. Shows that Uniswap v3's design can replicate any AMM curve by appropriate distribution of liquidity across ticks — hence "universal." Analyzes capital efficiency gains and LP return decomposition.

## Key Results

- Concentrated liquidity positions are equivalent to a combination of a constant-product position and a leveraged position
- LP returns decompose into: fees earned minus impermanent loss minus gas costs
- Any monotonically increasing price curve can be approximated by distributing liquidity across Uniswap v3 ticks
- LPing is economically equivalent to selling options (short gamma)

## Connections

- Extends [[Uniswap v3 Whitepaper]] with deeper analysis
- [[Impermanent Loss]] — mathematical derivation of LP risk
- [[Curve Whitepaper — Michael Egorov]] — alternative AMM design for correlated assets
