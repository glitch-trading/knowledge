---
type: concept
title: "Trading Bot Operations"
tags:
  - concept
  - operations
  - infrastructure
level: 3
prerequisites:
  - "[[Paper Trading]]"
  - "[[Kill Switch]]"
---

## What It Is

The operational layer that makes the difference between a strategy that *works in theory* and one that *runs reliably in production*. The math, the signal, and the sizing rules are necessary; this note is the rest of the production checklist — the parts that get traders into trouble more often than the strategy does.

Most live-trading failures are operational, not analytical. The bot didn't have edge it just gave away during the few minutes the websocket was disconnected. Or it had edge but a leaked API key emptied the wallet. Or the kill switch existed but the alert went to a Slack channel no one was monitoring.

## Why It Matters

### 1. Data ingestion that survives reality

- **Websocket as primary, REST as fallback.** Streaming feeds avoid poll-induced staleness. Hold a REST poller in reserve for reconnect gaps.
- **Auto-reconnect with exponential backoff.** Disconnects are routine. Reconnect with backoff (e.g. 1s → 2s → 4s, capped at ~30s, max retries before alerting). Reset the backoff on a successful reconnect, not on the first message after — some venues replay stale frames first.
- **Stale-data guard.** Stamp every received tick with arrival time; refuse to trade on data older than a strategy-specific $\tau$. Trip a [[Kill Switch]] pause if $\tau$ is breached. Cross-check by comparing exchange-side timestamps when the venue supplies them.
- **Clock discipline.** Run NTP / chrony with monitoring. Compute latency as `received_at - exchange_timestamp` and alert on regressions.
- **Sequence-number / heartbeat checks.** Many venues' streams include sequence numbers or heartbeats; drops or gaps must trigger a resubscribe, not be silently bridged.
- **Cross-feed sanity.** When two feeds for the same instrument diverge beyond tolerance, halt — one of them is wrong and you don't know which.

### 2. Execution path

- **Async / non-blocking.** Single-threaded blocking I/O in an order-submission loop is the most common avoidable source of latency. Use the platform-native async runtime (asyncio in Python, tokio in Rust, etc.) end-to-end.
- **Dedicated execution RPC / endpoint.** On-chain venues: a private RPC (Alchemy, Quicknode, self-hosted) for execution traffic, separated from public read endpoints. Off-chain venues: a co-located or direct API session for orders, kept distinct from any backtest / research connections sharing the same key.
- **Latency budget.** Allocate it explicitly — e.g. "edge detect ≤ X ms, sign ≤ Y ms, submit ≤ Z ms". Measure each stage. Alert on regressions, not just absolute breaches.
- **Atomicity awareness.** If the strategy depends on multi-leg execution, every leg's atomicity model is a load-bearing assumption. See [[Leg Risk]].
- **Idempotency on submit.** Network retries must not double-submit. Use a client-side order id and rely on the venue's deduplication, or maintain an outbox that records every submit before it goes over the wire.
- **Nonce / sequence management.** On-chain: a single source of truth for the next nonce, persisted across restarts. Off-chain CLOBs with monotonically increasing client order ids: same idea.

### 3. Key management & OpSec

- **Secrets in environment / vault, never in source.** Loaded at startup from `.env` (development) or a managed secret store (production). `.env` must be in `.gitignore` before the first commit. No exceptions; one accidental push is a drained wallet.
- **Least-privilege API keys.** Generate a separate key per process; restrict to the minimum permissions needed (e.g. trade-only, no withdraw). IP-allowlist where the venue supports it.
- **Withdrawal disabled by default.** API keys with withdrawal rights should not be the keys the bot holds.
- **Key rotation cadence and revocation drill.** You should know how to revoke and rotate in under 10 minutes. Time it once before you need it.
- **Signing key segregation (on-chain).** A hot wallet for execution holds only working capital; a cold address holds the rest and is the destination for periodic sweeps. The hot wallet's blast radius is bounded by the working balance.

### 4. Deployment topology

- **Always-on host.** A laptop is not deployment. A small cloud VM (DO / Linode / Vultr / AWS) or co-located instance gives you uptime independent of your physical presence.
- **Region selection.** Pick a region close to the venue's matching engine or RPC endpoint. Latency-sensitive strategies live or die on this choice.
- **Process supervision.** Use `systemd`, `supervisord`, `pm2`, or a container runtime that restarts on crash. Crash-loop guards (back off after N rapid restarts to avoid noisy-neighbor problems) are mandatory.
- **One process per concern.** Data ingestion, signal computation, execution, monitoring, and journaling are easier to reason about as separate processes communicating via queues than as one monolith. Failure domains don't bleed.
- **Reproducible environment.** Pinned dependency versions (lockfile committed), pinned base image, infrastructure as code. "Works on my machine" is not an excuse twice.
- **Backups.** Journal, configuration, and any persisted state (positions, fills, parameters) backed up off-host. Lost journal = lost ability to reconstruct what happened.

### 5. Monitoring, alerting, journaling

- **Heartbeat.** Periodic "I am alive and these are my positions / P&L" messages on a known cadence. Absence of heartbeat *is* the alert.
- **Tiered alerts.** Informational events to a log; significant events (kill-switch trigger, exception, fill anomaly) to a pager-style channel; routine fills to a low-priority feed. Alert fatigue is the failure mode here.
- **Structured logs.** JSON or equivalent, with timestamps, strategy id, event type, and correlation ids. Grep-friendly, machine-parseable, suitable for retroactive analytics.
- **Rotating files / centralized log store.** Disk fills, hosts get replaced. Logs should survive both.
- **Trade journal as a first-class artifact.** Every fill, cancel, and kill-switch event written to a durable store with the inputs that drove the decision. See [[Trade Journaling]].
- **Dashboards over inboxes.** A single page showing strategy state, P&L, recent trades, and feed health is consulted more reliably than an email digest.

### 6. Pre-live discipline

- **Default to [[Paper Trading|paper mode]].** Live execution should require explicit, intentional opt-in (multiple flags, environment toggle, configuration switch — pick the construction that makes accidental live trading impossible).
- **Live graduation criteria.** Articulated before paper trading starts: minimum N completed paper trades, win-rate / Sharpe within band of backtest, N consecutive days without unhandled exception.
- **Stage live exposure.** First-week sizes well below model. Compare live vs. paper P&L daily; investigate divergence beyond tolerance.
- **Postmortems on every incident.** Kill-switch trigger, unexpected loss, missed fill — written up briefly with cause, fix, and preventative change. Cheap to do; compounds.

### 7. Anti-patterns

- Hardcoded credentials anywhere in source.
- Single key with full account permissions.
- Logging that drops the structured context (just `print()` statements) and can't be reconstructed weeks later.
- A kill switch that depends on the strategy code itself to fire (instead of an out-of-band watchdog).
- Live-mode-by-default with paper as opt-in. Always the reverse.
- "It works on my laptop" as a deployment plan.
- Adding a feature directly to live without re-running paper validation.
- Alerting channels no one is actually subscribed to.

## Resources

- Harris, *Trading and Exchanges*, Ch. 14 (execution mechanics)
- López de Prado — *Advances in Financial Machine Learning* (incident-discipline framing for systematic strategies)

## Connections

- [[Paper Trading]] — validation layer before live; also runs as ongoing canary
- [[Kill Switch]] — the structural safeguard automating "stop trading when conditions degrade"
- [[Trade Journaling]] — the durable record of decisions and outcomes the operations layer produces
- [[Leg Risk]] — execution atomicity is one of the operational concerns the bot must handle
- [[Trading Psychology]] — operator-discipline issues that operational structure removes from the loop
- [[Infrastructure MOC]] — broader inventory of tools and patterns
- [[Maximum Drawdown]] / [[Position Sizing]] — risk-side inputs the kill switch is calibrated against
