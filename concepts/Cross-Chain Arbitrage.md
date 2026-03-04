---
type: concept
title: "Cross-Chain Arbitrage"
tags:
  - concept
  - strategies
  - arbitrage
level: 2
prerequisites: []
---

# Cross-Chain Arbitrage

## What It Is

Cross-chain arbitrage exploits price discrepancies for the same asset across different blockchains (L1s, L2s, sidechains). Buy USDC cheaper on Arbitrum, sell it at par on Ethereum mainnet. Or exploit a stablecoin depeg on one L2 relative to another.

This is [[Spatial Arbitrage]] extended to the on-chain world, with blockchain-specific complications.

**Key differences from CEX spatial arb:**
- **Bridge risk**: Moving assets cross-chain requires bridges, which introduce smart contract risk, exploits, and potential loss of funds. Bridges are the weakest link.
- **Finality delays**: Different chains have different finality guarantees. Optimistic rollups have 7-day challenge periods. Even "fast bridges" involve trust assumptions.
- **Gas costs**: Each chain has its own gas market. Arb profitability depends on gas costs on both source and destination chains.
- **Fragmented liquidity**: DEX liquidity varies dramatically across chains. Thin liquidity on one side means slippage eats the edge.

## Why It Matters

- **Structural inefficiency**: Cross-chain markets are more fragmented than CEX markets. Bridges are slow and expensive, creating persistent (but small) price discrepancies.
- **Growing opportunity set**: As more L2s and appchains launch, the number of cross-chain pairs grows combinatorially.
- **High complexity barrier**: The operational complexity (bridge integrations, multi-chain node infra, gas management) creates a moat for those who build it.
- **Risk-adjusted returns may be poor**: Bridge risk is non-trivial. A single bridge exploit can wipe out months of arb profits. Size positions accordingly.

**Practical considerations:**
- Monitor native bridges vs. third-party bridges (Across, Stargate, etc.) — different trust assumptions and speeds
- Maintain inventory on multiple chains to avoid bridge delays
- Account for gas on both chains plus bridge fees in profitability calculations

## Resources

- L2Beat — Bridge risk analysis and TVL tracking
- Chain-specific block explorers for monitoring finality

## Connections

- [[Spatial Arbitrage]] — The general principle; cross-chain is a specific venue type
- [[CEX-DEX Arbitrage]] — Often combined: arb between a CEX and a DEX on a specific L2
