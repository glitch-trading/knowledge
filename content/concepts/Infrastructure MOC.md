---
title: "Infrastructure — Map of Content"
type: MOC
tags:
  - MOC
  - infrastructure
---

## Operations & Reliability
- [[Trading Bot Operations]] — end-to-end production checklist (ingestion, execution, OpSec, deployment, monitoring)
- [[Paper Trading]] — pre-live validation discipline and ongoing canary
- [[Kill Switch]] — automated halts on drawdown, loss streaks, stale data, behavioral divergence

## Data Pipeline
- WebSocket connections (CEX APIs)
- DEX event listeners / subgraph queries
- Prediction market data feeds
- TimescaleDB for time-series storage
- Redis for real-time state
- Stale-data guard (refuse trades on data older than $\tau$)
- Auto-reconnect with exponential backoff; sequence-number / heartbeat checks
- Cross-feed sanity cross-checks

## Execution Systems
- Order management
- Atomic on-chain execution (smart contracts)
- Gas optimization
- Nonce management
- [[Kill Switch|Kill switches]]
- Idempotent submit (client order id, persisted outbox)
- Async / non-blocking I/O end-to-end
- Dedicated execution endpoint separated from research traffic

## Monitoring & Alerting
- Real-time P&L dashboards
- Strategy health metrics
- Anomaly detection
- Automated [[Kill Switch|kill switches]]
- Heartbeat (absence-is-the-alert)
- Tiered alerts to avoid alert fatigue
- Structured logs with correlation ids; rotating files or centralized store

## Libraries & Tools

### Python
- `numpy`, `scipy`, `statsmodels` — numerics and statistics
- `pandas` — DataFrames and time series; `polars` for 10-50x speed on large datasets
- `xgboost`, `lightgbm`, `catboost` — gradient boosting for tabular data
- `pytorch` — deep learning
- `cvxpy` — convex optimization
- QuantLib — industry-grade derivatives pricing (C++ backend)
- NautilusTrader — high-performance backtesting and live trading (Rust core + Python API)
- `vectorbt` / Backtrader — lighter backtesting alternatives
- Microsoft Qlib — end-to-end quant research platform
- FinRL — RL framework for trading

### Rust / C++
- RustQuant — Rust quant finance library
- NautilusTrader — Rust core for latency-critical paths
- QuantLib (C++), Eigen, Boost

### Data & APIs
- `ccxt` — unified crypto exchange API
- `web3.py` / `ethers.js` / `alloy` (Rust) — on-chain interaction
- yfinance, Finnhub, Alpha Vantage — free market data
- Polygon.io — mid-range ($199/mo, <20ms latency)
- Alchemy — free blockchain archive tier
- The Graph — DEX subgraphs
- Nansen, Arkham — wallet labeling

### Solvers
- Gurobi — fastest commercial MIP solver (free academic license)
- Google OR-Tools — strongest free solver
- PuLP / Pyomo — Python modeling interfaces

## Architecture Patterns
- Event-driven vs polling
- Python for research, Rust/C++ for execution
- Data flow: ingestion → normalization → storage → features → signal → execution
