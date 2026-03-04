---
type: roadmap
level: 5
status: not-started
tags:
  - level-5
  - roadmap
prerequisites:
  - "[[Level 4 — MEV & Algorithmic Trading]]"
---

# Level 5 — Hands-On With Some Profit

**Goal:** Deploy capital strategically across multiple strategies with proper risk management. You should be consistently identifying real (not backtested-only) edges and sizing them appropriately.

## Sections

### 5.1 Portfolio Theory & Multi-Strategy Management

#### Modern Portfolio Theory
- Mean-variance optimization, efficient frontier, [[Sharpe Ratio]]
- Diversification as the only free lunch — even across arb strategies
- Correlation between strategies matters: if all your strategies fail simultaneously, diversification is illusory

#### Multi-Strategy Allocation
- How to allocate capital across different strategies based on Sharpe, capacity, and correlation
- When to scale up vs when to shut down a strategy
- Strategy lifecycle: discovery → backtest → paper trade → small live → scale → decay → retire

#### Regime Detection
- Strategies that work in high-vol fail in low-vol. Mean reversion works in ranges, momentum in trends.
- Simple regime indicators: realized vol regimes, funding rate regime, correlation regime
- Build systems that detect regime changes and adapt allocation or shut down

### 5.2 On-Chain Information Alpha

#### Whale Wallet Tracking with Context
Not just "big wallet moved tokens." The edge is interpreting *intent*:
- VC unlock wallets moving to exchanges → likely selling
- DeFi team multisigs deploying new contracts → something launching
- Known market maker wallets repositioning → informed flow
- Map wallet identities to behavioral patterns using Nansen, Arkham, Etherscan labels

#### Governance Flow Trading
DAOs vote on things that move prices: emissions changes, treasury diversification, fee switches, incentive programs. Most proposals are public days before execution, voting trajectory visible on-chain. Markets often don't price these in until execution or after.

Model: governance outcome → expected token impact → [[Position Sizing]].

#### Smart Contract Deployment Monitoring
New contracts deployed on-chain signal upcoming launches, upgrades, new pools. Watch factory contracts for major DEXs, lending protocols, launchpads. Early signal before public announcements.

### 5.3 Statistical Arbitrage: Prediction Markets ↔ Spot/Derivatives

#### Signal Extraction
- Connect to prediction market data feeds. Detect statistically significant probability movements.
- Filter noise: what magnitude of probability change constitutes a signal?
- Categorize by event type and map to affected assets.

#### Historical Modeling
- For each signal type: what was the average subsequent move in the correlated asset?
- What's the Sharpe? Win rate? [[Maximum Drawdown]]?
- Use walk-forward validation, not in-sample fitting.

#### Live Execution
- When a signal fires, place trades on the appropriate venue.
- This strategy is latency-tolerant (information processing speed, not execution speed) — your edge is research quality, not colocation.
- Position size based on signal confidence using [[Kelly Criterion]] or fractional Kelly.

#### Edge Maintenance
- Monitor whether your edge is decaying (more participants modeling the same relationship)
- Track signal Sharpe over time, not just P&L
- Be willing to retire a signal that stops working

### 5.4 Funding Rate & Basis Strategies

#### [[Funding Rate Arbitrage]] Harvesting Across Perp DEXs
- Long a perp on a venue with negative funding (you get paid), short same asset on a venue with positive funding (also get paid). Delta neutral.
- Capital efficiency challenge: margin required on both sides.
- Works best on newer perp DEXs where rates are more volatile and less efficiently arbitraged.

#### Basis Trading
- Perp price vs spot price divergence. When basis is wide, go long spot + short perp (or vice versa).
- Carry trade: earn the basis convergence + funding.
- Risk: basis can widen before converging. Size accordingly.

### 5.5 Structural DeFi Opportunities

#### [[Liquidation Botting]]
- Monitor health factors across lending protocols (Aave, Compound, Morpho, smaller ones)
- When positions become undercollateralized, trigger liquidation and collect bonus
- Competitive on mainnet, thinner on L2s and alt-L1s
- Requires understanding oracle update cycles and gas optimization

#### New Protocol Launch Dynamics
- When a new DEX, lending protocol, or perp platform launches, early liquidity dynamics are inefficient
- Pools are imbalanced, prices diverge from fair value, incentive programs create yield distortions
- Being systematic about exploiting launch-phase inefficiencies is repeatable

#### Token Unlock & Vesting Schedule Trading
- Every VC-backed token has a public vesting schedule. Large unlocks create predictable sell pressure.
- But not always: sometimes priced in, sometimes OTC'd beforehand.
- Model which unlocks actually create selling pressure vs which are already hedged.
- Data: Token Unlocks, on-chain vesting contract monitoring.

### 5.6 Behavioral Edge Identification (Ongoing)

#### "Why Does This Edge Exist?"
For every strategy, answer this clearly. Edges exist due to:
- Structural reasons: regulatory constraints, capital requirements, information asymmetry
- Behavioral reasons: biased probability estimates, loss aversion, herding
- Transient reasons: new market, broken infrastructure, temporary dislocation

If you can't explain why the counterparty is willing to lose money to you, you probably don't have an edge.

#### Market Participant Analysis
Who's on the other side?
- Prediction markets: politically motivated bettors with biased estimates
- CEX retail: momentum chasers, overlevered positions getting liquidated
- DeFi LPs: passive liquidity providers not adjusting for [[Adverse Selection]]
- Understanding counterparty motivation tells you if your edge is sustainable

- **Resource:** Soros, [[The Alchemy of Finance]]. Taleb, [[Fooled by Randomness]]. Follow quant finance blogs/Twitter (Quantocracy aggregates).

## Prerequisites
- [[Level 4 — MEV & Algorithmic Trading]]

## Unlocks
- [[Level 6 — Advanced Topics]]
