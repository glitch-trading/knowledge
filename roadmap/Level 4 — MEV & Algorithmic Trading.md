---
type: roadmap
level: 4
status: not-started
tags:
  - level-4
  - roadmap
prerequisites:
  - "[[Level 3 — Hands-On Niche Markets]]"
---

# Level 4 — MEV & Algorithmic Trading

**Goal:** Understand the adversarial on-chain environment and build more sophisticated execution. This level is about surviving and profiting in the MEV ecosystem rather than being eaten by it.

## Sections

### 4.1 MEV Fundamentals

#### What [[MEV]] Is
Maximal Extractable Value — the profit that can be extracted by manipulating transaction ordering within a block. Anyone transacting on-chain is exposed to MEV whether they know it or not.

#### The MEV Supply Chain
- **Searchers** — find profitable opportunities (arb, liquidations, sandwich attacks)
- **Builders** — construct blocks by ordering transactions for maximum value
- **Validators/proposers** — select the highest-value block to propose
- **Relays** — connect builders to proposers (Flashbots relay, bloXroute, etc.)

Understand each role and where value accrues. Most independent operators compete as searchers, but the other roles have different risk/reward profiles.

#### Common MEV Strategies
- **[[Frontrunning]]** — seeing a pending transaction and placing yours first to profit from the price impact
- **[[Backrunning]]** — placing your transaction immediately after a large trade to capture the reversion
- **[[Sandwich Attack]]** — frontrun + backrun around a victim's swap. Buy before them (raising price), let them buy at higher price, sell after them
- **[[Liquidation Botting]]** — triggering undercollateralized positions on lending protocols for a bonus
- **[[CEX-DEX Arbitrage]]** — cross-DEX price alignment via atomic transactions in a single block

- **Resource:** Flashbots documentation and research. [[Flash Boys 2.0 — Daian et al.]]. Phil Daian's YouTube talks.

### 4.2 On-Chain Execution

#### Smart Contract Interaction
- web3.py or ethers.js for transaction construction
- ABI encoding, function selectors, calldata construction
- Gas estimation and optimization (EIP-1559 mechanics, priority fees)
- Nonce management, pending transaction handling, replacement transactions

#### Protecting Yourself from MEV
- **Flashbots Protect** — submit transactions to a private mempool, invisible to sandwich bots
- **Private RPCs** — MEV Blocker, Flashbots RPC
- **Atomic execution** — if your arb requires multiple steps, do them in one transaction via a custom smart contract. If any step fails, the whole thing reverts.
- **[[Slippage]] tolerance** — set tight slippage on DEX swaps. Better to have the transaction fail than to be sandwiched.

#### Building an Arb Bot (On-Chain)
- Monitor DEX pool states for price discrepancies
- Calculate profitability net of gas
- Submit atomic arb transactions
- Handle failures gracefully (reverts still cost gas on some chains)
- Start on L2s (Arbitrum, Base, Optimism) where competition is thinner than mainnet

### 4.3 Derivatives & the Greeks

Understanding options is essential even for non-options strategies — LPing is selling options, many DeFi positions have embedded optionality, and the Greeks framework applies broadly.

- **Delta (Δ):** option price change per $1 underlying move — your hedge ratio
- **Gamma (Γ):** delta's sensitivity to price — convexity, the reason market makers care about large moves
- **Theta (Θ):** time decay — options lose value daily, this is the cost of holding
- **Vega (V):** sensitivity to implied volatility — the profit center for vol trading
- **Rho (ρ):** interest rate sensitivity — less relevant for crypto, critical in TradFi

Taylor expansion connects to hedging: delta hedging is 1st order, gamma hedging is 2nd order. Understand why delta-hedged portfolios still have gamma risk.

- **Resource:** [[Options, Futures, and Other Derivatives — John Hull]], chapters on Black-Scholes and Greeks. [[Option Volatility and Pricing — Sheldon Natenberg]] for practical intuition.

### 4.4 AMM Mathematics — Deep Dive

#### Uniswap v3 Concentrated Liquidity
- Virtual reserves, tick math, fee tiers
- How concentrated positions amplify both fees and [[Impermanent Loss]]
- LP returns decomposition: fees earned - IL - gas

#### [[Curve Stableswap]]
- Hybrid constant sum / constant product invariant
- The amplification parameter A and how it affects the bonding curve
- Why Curve dominates stablecoin swaps

#### [[Impermanent Loss]] — Mathematical Derivation
Derive it from first principles. Understand when IL is real loss vs opportunity cost. Understand that LPing is equivalent to selling options (short gamma).

- **Resource:** [[Uniswap v3 Whitepaper]] + Dan Robinson's concentrated liquidity deep dive. [[Curve Whitepaper — Michael Egorov]]. [[Uniswap v3 — The Universal AMM — Adams et al.]].

### 4.5 Oracle Mechanics

- Chainlink, Pyth, UMA — update frequencies, deviation thresholds, heartbeat intervals
- The gap between oracle price and true market price creates both risk and opportunity
- Oracle Extractable Value (OEV) — trading against stale oracle prices in lending protocols and perps
- How [[Liquidation Botting]] exploits oracle latency

- **Resource:** Chainlink docs, Pyth docs, research on OEV.

### 4.6 Algorithmic Order Execution

#### Execution Algorithms
Moving beyond "just send a market order":
- **[[TWAP]]** (Time-Weighted Average Price) — split order over time to reduce impact
- **[[VWAP]]** (Volume-Weighted Average Price) — weight execution by volume profile
- **Implementation shortfall** — minimize the gap between decision price and execution price
- **Iceberg orders** — show only a fraction of your order on the book

#### [[Market Impact]] Modeling
Your order moves the price. Model how much:
- Temporary impact (price moves during execution, then partially reverts)
- Permanent impact (information content of your trade shifts the equilibrium)
- Square-root law of market impact: impact ∝ √(order_size / daily_volume)

Understanding [[Market Impact]] is critical for sizing strategies — a strategy that backtests profitably on 1 BTC might be unprofitable at 10 BTC because impact eats the edge.

- **Resource:** [[Algorithmic and High-Frequency Trading — Cartea et al.]], chapters on optimal execution.

## Prerequisites
- [[Level 3 — Hands-On Niche Markets]]

## Unlocks
- [[Level 5 — Profitable Strategies]]
