---
type: concept
title: "MEV"
tags:
  - concept
  - MEV
  - DeFi
level: 4
prerequisites:
  - "[[AMM]]"
---

# MEV (Maximal Extractable Value)

## What It Is

Maximal Extractable Value (originally "Miner Extractable Value") is the profit that can be captured by manipulating the ordering, inclusion, or censorship of transactions within a block. Whoever controls transaction ordering can extract value by strategically placing their own transactions relative to others.

**The MEV supply chain (post-merge Ethereum):**
1. **Searchers**: Find MEV opportunities (arbitrage, liquidations, sandwich attacks). They construct profitable transaction bundles.
2. **Builders**: Aggregate bundles from searchers, construct the most profitable block. Compete in a block-building auction.
3. **Validators** (proposers): Select the highest-paying block from builders via MEV-Boost/PBS (proposer-builder separation).

**Major MEV categories:**
- **[[CEX-DEX Arbitrage]]**: Most of MEV by dollar value. AMM prices lag CEX; arbitrageurs correct them.
- **[[Sandwich Attack]]**: Frontrun + backrun around a victim's swap.
- **[[Liquidation Botting]]**: Triggering undercollateralized DeFi positions.
- **[[Backrunning]]**: Placing a transaction right after a large trade to capture reversion.
- **JIT Liquidity**: Providing concentrated liquidity just-in-time for a large swap, then removing it.

## Why It Matters

- **It's a massive market**: Billions in cumulative MEV extracted on Ethereum alone.
- **It shapes DeFi design**: Protocols must be designed with MEV awareness. Ignorance of MEV = leaving money for searchers.
- **It's adversarial**: If you're swapping on-chain without protection (private mempools, MEV protection services), you are the victim.
- **Career opportunity**: MEV searching is one of the most technically demanding and profitable niches in crypto trading. Competitive edge comes from latency, strategy sophistication, and builder relationships.
- **It drives centralization**: The MEV supply chain has centralization pressures — dominant builders, exclusive order flow arrangements, vertical integration.

## Key Equations

**Simple arbitrage profit (two-venue):**
$$\pi = |P_{AMM} - P_{CEX}| \times Q - \text{gas cost} - \text{builder tip}$$

**Sandwich profit:**
$$\pi = \text{backrun revenue} - \text{frontrun cost} - \text{gas} - \text{tip}$$

The profit comes from the price impact the victim's trade creates between the frontrun and backrun.

**Expected MEV per block:**
$$E[MEV] = \sum_i P(\text{opportunity}_i) \times E[\text{profit}_i]$$

## Resources

- Flashbots — research, MEV-Explore, MEV-Boost
- Phil Daian et al. — "Flash Boys 2.0" (seminal MEV paper)
- Flashbots Docs — MEV supply chain, PBS
- MEV Blocker, MEV Share — OFA (order flow auction) designs
- EigenPhi, Zeromev — MEV dashboards and analytics

## Connections

- [[Frontrunning]] — Classic MEV extraction via priority ordering
- [[Backrunning]] — Less adversarial MEV, capturing post-trade reversion
- [[Sandwich Attack]] — The combination of frontrunning and backrunning
- [[CEX-DEX Arbitrage]] — The largest category of MEV by volume
- [[AMM]] — Primary venue where MEV is extracted
- [[Liquidation Botting]] — MEV from triggering undercollateralized positions
