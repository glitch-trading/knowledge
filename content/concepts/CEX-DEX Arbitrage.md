---
type: concept
title: "CEX-DEX Arbitrage"
tags:
  - concept
  - strategies
  - arbitrage
  - MEV
level: 2-4
prerequisites: []
---

## What It Is

CEX-DEX arbitrage exploits price discrepancies between centralized exchanges (Binance, Coinbase) and decentralized exchanges ([[AMM]]s like Uniswap, Curve). CEX prices update continuously via order books; DEX prices only update when someone transacts on-chain. This structural lag creates persistent arbitrage opportunities.

**How it works:**
1. CEX price moves (e.g., ETH goes from $3,000 to $3,050 on Binance)
2. DEX price is stale at $3,000 (no one has traded yet)
3. Arbitrageur buys cheap ETH on the DEX, sells on CEX (or vice versa)
4. DEX price adjusts to match CEX price

**This is the dominant source of [[MEV]] on Ethereum.** Most MEV extraction is simply informed CEX-DEX arbers trading against stale AMM prices.

## Why It Matters

- **Largest MEV category**: CEX-DEX arb is estimated to account for the majority of MEV on Ethereum. It's the primary revenue source for sophisticated searchers.
- **MEV territory**: On-chain execution means your transactions are visible in the mempool. You compete with other searchers for block inclusion, and must deal with [[Frontrunning]], [[Sandwich Attack]]s, and priority gas auctions.
- **Atomic execution helps**: Using flashbots or private transaction submission, you can atomically execute the DEX leg without risk of the CEX leg failing (or vice versa, hedge the CEX side).
- **Latency game**: The edge is in seeing CEX price moves and executing on-chain before other arbers. Milliseconds matter.
- **LP adverse selection**: From the LP's perspective, CEX-DEX arb is pure [[Adverse Selection]] — informed flow that systematically extracts value from liquidity providers.

**Execution approaches:**
- **Atomic on-chain**: Use smart contracts to execute DEX trades atomically via flashbots bundles
- **Statistical**: Don't try to arb every move — identify persistent mispricings with high probability of profit
- **Hybrid**: Hedge on CEX, execute on DEX with private transaction submission

## Resources

- [[Flash Boys 2.0 — Daian et al.]] — Foundational MEV paper documenting these dynamics
- Flashbots — MEV research and infrastructure
- EigenPhi, MEV Boost dashboard — Real-time MEV analytics

## Connections

- [[Spatial Arbitrage]] — CEX-DEX arb is spatial arb across on-chain/off-chain venues
- [[MEV]] — CEX-DEX arb is the primary MEV extraction strategy
- [[AMM]] — The on-chain venue being arbitraged
