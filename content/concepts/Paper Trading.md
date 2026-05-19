---
type: concept
title: "Paper Trading"
tags:
  - concept
  - operations
  - validation
level: 3
prerequisites:
  - "[[Overfitting]]"
---

## What It Is

Running a strategy end-to-end against live market data with simulated rather than real fills. Distinct from **backtesting** (replay over historical data) in that paper trading exercises the full production pipeline — data feeds, signal computation, sizing, order construction, monitoring, alerting — minus the actual transaction. It is the last validation layer before live capital.

Two variants:

- **Simulated-fill paper trading.** The bot computes the trade it would place and writes it to a local log (e.g. SQLite); fills are assumed at the prevailing top-of-book or a model price. Cheap; misses any execution-side reality (queue position, partial fills, slippage, taker-vs-maker classification).
- **Shadow trading.** The bot submits real orders but at sizes too small to influence the market, or to a sandbox / staging venue if one exists. Catches more execution reality (latency, rejects, throttling, market impact at small size) at the cost of real fees.

Treat paper trading as a *graduation criterion*, not a permanent home. The point is to prove the pipeline works in live conditions and then move on; running indefinitely in paper mode is procrastination.

## Why It Matters

**What paper trading catches that backtesting doesn't:**

- **Data-pipeline bugs in live conditions.** Out-of-order ticks, replayed messages, missing fields, exchange feed quirks, timezone drift, daylight-savings edges — most of these never appear cleanly in a backtest dataset.
- **Connection / reconnection logic.** Websocket disconnects, exponential-backoff behavior, stale-data detection, failover to secondary feeds. See [[Trading Bot Operations]].
- **Stale-data trading.** A bot will happily trade on a price feed that froze 30 seconds ago unless you explicitly check. Paper mode is where you find that out.
- **Alert / monitoring plumbing.** Telegram/Slack/PagerDuty integrations, heartbeat cadence, log rotation, dashboard refresh — paper mode is when these are exercised under realistic event frequency.
- **Operator workflow.** Whether you actually know how to start, stop, restart, and inspect the bot at 3 AM.

**What paper trading does *not* catch:**

- **Realized slippage and market impact** beyond what fits in the fill model. Live fills against your own order will differ from "assumed top-of-book" — the gap is your unmodeled execution cost.
- **Adverse selection.** Your simulated fills are filled by no one and selected by nothing; live limit-order fills disproportionately occur when the price is about to move against you. See [[Adverse Selection]].
- **Queue priority and time-priority effects.** Maker fills require being at the front of the queue at the right moment; paper mode assumes a fill that real-life queueing might never deliver.
- **Cost asymmetries** — taker vs. maker fees, rebates, gas tips, MEV-related ordering costs.
- **Feedback effects** — at any size, your orders move the book; this matters even before classical [[Market Impact]] kicks in.

**Graduation criteria (template, calibrate to strategy).**

- Minimum N completed paper trades (high-frequency: hundreds in a week; lower-frequency: weeks-to-months of data).
- Win rate / Sharpe within an a-priori band of the backtest. If paper is materially better than backtest, the backtest is using cleaner data than reality. If paper is materially worse, something in live conditions is off.
- N consecutive days without a crash, watchdog restart, or unhandled exception. Choose N relative to the strategy horizon.

**Paper trading as ongoing canary.** After going live, keep a parallel paper instance running. Real-vs-paper divergence beyond a calibrated threshold is the cleanest early signal of an unmodeled cost (slippage drift, adverse selection ramping), an [[Adverse Selection]] regime change, or a silent live-pipeline bug. Treat divergence the same as any kill-switch trigger — halt, diagnose, restart only with a documented fix. See [[Kill Switch]].

**Anti-patterns:**

- **Paper-only forever.** No live exposure means no live learning. Set explicit graduation criteria up front.
- **Paper mode that quietly drifts from production code.** Running paper through a separate codepath ("simulator") that has different bugs than the live path defeats the purpose. The same execution module should service both, with a `paper=True` flag toggling the fill source.
- **Paper mode without alerting on simulated kill-switch triggers.** If a simulated daily-drawdown halt wouldn't have woken you up at 3 AM, neither will the real one.
- **Reading paper P&L as forecast.** It is a *pipeline* test, not an edge test. Paper edge that doesn't survive live trading is the rule, not the exception.

## Resources

- [[Advances in Financial Machine Learning — López de Prado]] — backtest-vs-live methodology and overfitting controls

## Connections

- [[Trading Bot Operations]] — paper trading is the validation layer in the production checklist
- [[Kill Switch]] — paper mode is also where kill-switch logic is exercised and tuned
- [[Overfitting]] — paper mode catches some out-of-sample drift the backtest didn't
- [[Trade Journaling]] — paper trades feed the same journal pipeline as live trades
- [[Adverse Selection]] — the dominant unmodeled cost paper trading misses
- [[Market Impact]] / [[Slippage]] — the second category of unmodeled cost
- [[Leg Risk]] — non-atomic multi-leg fills are paper-mode-invisible unless explicitly simulated
