---
type: roadmap
level: 2
status: not-started
tags:
  - level-2
  - roadmap
prerequisites:
  - "[[Level 1 — Fundamentals]]"
---

# Level 2 — Basic Probabilistic Arbitrage

**Goal:** Understand arbitrage theory, learn to identify and model price discrepancies, build your first data pipelines and simulators. No real money yet.

## Sections

### 2.1 Stochastic Calculus

This is the hardest single section of the entire roadmap, but you've built the prerequisites.

#### From Random Walks to Continuous Processes
How a [[Random Walk]] with smaller steps converges to [[Brownian Motion]]. What `dW` means — an infinitesimal random increment. What `dS = σdW` means — price moves randomly with volatility σ. [[Geometric Brownian Motion]] `dS/S = μdt + σdW` — the standard stock price model.

#### [[Itô Calculus]]
Normal calculus chain rule fails because [[Brownian Motion]] is "rough." The single most important fact in quantitative finance: `(dW_t)² = dt`. This is why [[Itô's Lemma]] has an extra second-order term that doesn't appear in ordinary calculus. Given `f(S,t)` where S follows an SDE, compute `df`. Practice this mechanically — it's a tool you'll use constantly.

- **Exercise:** Apply Itô's lemma to `ln(S)` where S follows GBM. You should get the `−σ²/2` drift correction — this is why GBM's expected log return isn't just μ.

#### [[Stochastic Differential Equations]]
How to read and interpret an SDE. What it means for a process to "solve" an SDE. The paper's `dS = σdW` is the simplest. The appendix uses `dS/S = σdW`. Understand drift vs diffusion terms.

#### Expectations and the PDE Connection
[[Feynman-Kac Theorem]]: expected values of functions of stochastic processes satisfy PDEs. This is why the paper's optimization problem (maximize expected utility) becomes a PDE (the [[HJB Equation]]). You don't need to prove it — understand the connection.

- **Resource:** [[Stochastic Calculus for Finance II — Steven Shreve]], chapters 1-4. Standard textbook, written for finance people. Alternative: [[A First Course in Stochastic Calculus — Louis-Pierre Arguin]] for a gentler path. Supplement with [[MIT 18.S096 — Topics in Mathematics with Applications in Finance|MIT 18.S096 lectures 17-21]].
- **Exercise:** Derive the full Black-Scholes PDE from delta hedging. Then implement Black-Scholes pricing from scratch and compare against Monte Carlo simulation — they should converge.

### 2.2 Optimization & Control Theory

#### [[Utility Theory]] and [[Risk Aversion]]
- Why maximize utility instead of raw profit (a dollar lost hurts more than a dollar gained helps)
- [[Exponential Utility]] `U(x) = -exp(-γx)` — the paper's choice. γ = risk aversion parameter. High γ = hate risk. Low γ ≈ risk-neutral.
- [[Reservation Price]] (indifference prices) — the price at which you're equally happy buying or not. This is Definition 1 in [[Avellaneda-Stoikov]] and the key concept.

#### [[Dynamic Programming]]
- Bellman's principle: an optimal policy from any point onward remains optimal.
- Value functions: `v(state, time) = best expected outcome from here forward`
- Discrete time → [[Bellman Equation]] (recursion). Continuous time → [[HJB Equation]] (PDE).

#### [[HJB Equation]]s
- Read the HJB equation in the paper (after equation 13) term by term: time decay, price diffusion, optimal bid/ask contributions.
- The ansatz trick (equation 14): guess the solution form, substitute back, get a simpler equation.
- First-order conditions: set derivatives to zero for optimal δa and δb → equations 18-19.

- **Resource:** [[Convex Optimization — Boyd & Vandenberghe]], chapters 1-5 (free Stanford PDF) for the optimization foundations. [[Algorithmic and High-Frequency Trading — Cartea et al.]], chapters on optimal control. Or [[Continuous-time Stochastic Control and Optimization — Pham]], chapters 1-3.
- **Exercise:** Implement gradient descent from scratch and minimize the Rosenbrock function. Then do portfolio optimization with `cvxpy` including transaction cost constraints.

### 2.3 Reading the [[Avellaneda-Stoikov]] Paper

With all prerequisites in place, work through it with pen and paper.

**Part 1: Sections 1-2**
- Derive value function (equation 3) yourself
- Derive [[Reservation Price]]s (equations 6, 7, 8) — algebra once you understand definitions
- Understand limit order model (section 2.4): how δa, δb control execution probability
- Work through trading intensity (section 2.5): [[Poisson Process]] rates + [[Power Law Distribution]] order sizes + price impact → equation 12

**Part 2: Section 3**
- Follow the HJB derivation
- Understand and reproduce the ansatz substitution
- Work through asymptotic expansion in q (equations 22-28) line by line
- Arrive at equations 29 and 30 — the practical punchline:
  - Reservation price: `r = s - qγσ²(T-t)`
  - Optimal spread: `δa + δb = γσ²(T-t) + (2/γ)ln(1 + γ/k)`
- Study simulation results: why [[Inventory Risk]] management reduces variance at cost of slightly lower returns

### 2.4 Arbitrage Theory & Taxonomy

#### Types of Crypto Arbitrage
Understand what each demands and where the competition lives:

- **[[Spatial Arbitrage]]** — same asset, different venue (Binance vs Coinbase, Uniswap vs SushiSwap). Latency-sensitive, highly competitive.
- **[[Triangular Arbitrage]]** — A→B→C→A within one exchange. Math-heavy, competitive.
- **[[Cross-Chain Arbitrage]]** — same asset across L1s/L2s. Bridge risk and finality delays are the challenge.
- **[[CEX-DEX Arbitrage]]** — price discrepancy between on-chain and off-chain. MEV territory.
- **[[Funding Rate Arbitrage]]** — perps vs spot, or perps across venues. More carry trade than pure arb.
- **[[Statistical Arbitrage]]** — not a riskless spread but a probabilistic edge from cross-venue signal extraction. This is where prediction markets come in.

#### The No-Arbitrage Principle and Why Arbs Exist Anyway
In theory, arbitrage opportunities are instantly eliminated. In practice, they persist because of: transaction costs, latency, capital requirements, information asymmetry, risk, and structural market segmentation. Your job is to find where these frictions create persistent (not fleeting) mispricings.

### 2.5 Data Pipeline & Observation

**Build before you trade. Observe before you build.**

#### What to Build
- WebSocket connections to 2-3 CEX APIs (Binance, Bybit — well-documented)
- DEX event listeners or subgraph queries (Uniswap, Curve)
- Prediction market data feed (Polymarket API)
- Store everything timestamped in PostgreSQL or TimescaleDB
- Build a simple dashboard to visualize cross-venue spreads in real time

#### What to Observe
- How fast CEX-CEX spreads close
- How DEX prices lag CEX prices (and by how much)
- How prediction market probability movements correlate with spot price changes
- Realistic latency from your infrastructure to each venue
- Gas costs, withdrawal fees, bridge times — the friction layer that kills paper profits

This is where your web dev and Docker skills directly apply.

- **Resource:** `ccxt` library (unified crypto exchange API), The Graph (DEX subgraphs), Polymarket API docs.

## Prerequisites
- [[Level 1 — Fundamentals]]

## Unlocks
- [[Level 3 — Hands-On Niche Markets]]
