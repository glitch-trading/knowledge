---
type: concept
title: "Kill Switch"
tags:
  - concept
  - operations
  - risk
level: 3
prerequisites:
  - "[[Maximum Drawdown]]"
  - "[[Position Sizing]]"
---

## What It Is

An automated halt that takes a running strategy out of the market when a pre-defined risk threshold is breached. The kill switch is the structural safeguard that prevents the bot from converting a temporary failure (bug, data outage, regime break) into an account-ending loss. Distinct from a *circuit breaker* in exchange parlance (which halts the venue); the kill switch halts *you*.

**Common trigger families:**

- **P&L-based.** Daily loss exceeding $X$% of day-start balance; trailing drawdown from all-time-high portfolio value; per-strategy loss caps.
- **Streak-based.** $N$ consecutive losing trades; rolling win-rate dropping below threshold; rolling Sharpe collapsing.
- **Data-integrity.** Price feed stale beyond $\tau$ seconds; reference venue disconnected; ticker timestamps out of order; cross-feed price divergence beyond tolerance.
- **Execution-integrity.** Order reject rate spike; fill latency exceeding budget; partial-fill rate above expected.
- **Behavioral.** Realized vs. backtest/paper divergence beyond tolerance (see [[Paper Trading]]); position size drifting from sizing model; cumulative exposure beyond stated risk budget.
- **External.** Macro / data-event windows (e.g. flat through CPI release); manual override flag; venue-side maintenance windows.

**Recovery semantics matter.** Three useful classes:

| Class | Trigger | Recovery |
| --- | --- | --- |
| **Pause** | Soft (e.g. loss streak, transient stale feed) | Auto-resume after timeout or condition clears |
| **Daily halt** | Intraday loss cap; loss-streak after pause | Auto-resume next session; alert sent |
| **Hard halt** | Trailing drawdown; data corruption; unhandled exception | Stop, page operator, require manual restart with reviewed cause |

The strictest tier should be **non-bypassable from inside the strategy code itself** — flat positions, cancel open orders, refuse new ones, and require an explicit operator action to re-enable. Soft auto-resumes are easy to reason about; hard halts are easy to *trust*.

## Why It Matters

**The asymmetry kill switches exist to handle.** Most failure modes you will encounter — feed glitches, reconnects, transient API errors, brief mispriced ticks — are recoverable. A small minority — a stuck stale feed during a regime break, a serialization bug that flips a sign, an unmodeled cost regime that turns the strategy negative-EV overnight — are account-ending. You cannot reliably distinguish *which* class you are in *during* the event. The kill switch settles the question by defaulting to "halt and ask later."

**Why automated, not discretionary.** Discretionary halts depend on the operator being awake, alert, and unbiased about their own strategy. None of these are reliably true. Automated halts execute at machine speed and don't suffer from loss aversion. The relationship is the same one [[Trading Psychology]] describes between system and operator: the kill switch is process discipline encoded into infrastructure.

**Designing trigger thresholds:**

- **Anchor to recoverable loss, not headline number.** "20% of day-start" sounds aggressive but on a strategy with daily volatility of 5% it triggers ~once a year and means something. Same threshold on a strategy with daily vol of 0.5% triggers monthly on noise.
- **Calibrate to backtest tail percentiles.** If a 4σ daily loss is the kill-switch threshold, the backtest should give you a credible 4σ estimate. Otherwise the threshold is decoration.
- **Cap unique vs. correlated triggers.** Multiple per-strategy halts triggering simultaneously usually means one underlying cause — make sure the portfolio-level halt fires first to avoid uncoordinated unwind.
- **Test the recovery path.** A halt you cannot cleanly resume from is a halt that turns into days of downtime. Practice the resume in paper mode.

**Practical implementation checklist:**

- Sized in *current* portfolio value, not entry-time value.
- Triggers checked **before** every new order, not just on a timer (a fast-moving event can blow through a periodic check).
- Trigger evaluation and order-submission code paths use the same clock and same position cache to avoid race conditions.
- Triggering writes a structured log entry (cause, state, positions, last $N$ events) for postmortem.
- Hard halts cancel all open orders before flatting; flatting before cancel can create unintended new positions.
- Alerts on trigger go to a channel the operator actually monitors, with enough context to act without opening the console.
- Paper-mode trigger logic is identical to live, so paper P&L curves show the same halts and you can tune thresholds before they cost money. See [[Paper Trading]].
- A regularly tested "kill all" out-of-band action (a script, an exchange-account-level cancel-all, a withdrawal of API permissions) exists as the last line of defense when the bot itself is the problem.

**Specific failure modes the kill switch closes:**

- **Stale-data trading.** Without a staleness halt, a frozen feed lets the bot trade phantom prices. See [[Trading Bot Operations]].
- **Self-reinforcing loss spiral.** Loss-streak pauses give a strategy time to be diagnosed before averaging-down logic compounds the error.
- **Operator-asleep failure.** Hard halts plus paging convert a 3 AM incident into a contained loss instead of a wakeup-too-late one.
- **Silent edge decay.** Trailing-drawdown halts catch strategies whose edge has decayed but whose operator hasn't yet noticed.

## Key Equations

**Trailing drawdown trigger:**
$$\text{halt} \iff \frac{V_{\text{HWM}} - V_t}{V_{\text{HWM}}} > d_{\max}$$

where $V_{\text{HWM}}$ is the all-time-high portfolio value and $d_{\max}$ is the drawdown budget.

**Daily P&L trigger:**
$$\text{halt} \iff \frac{V_t - V_{\text{day-open}}}{V_{\text{day-open}}} < -\ell_{\text{day}}$$

**Staleness trigger:**
$$\text{halt} \iff (t_{\text{now}} - t_{\text{feed}}) > \tau$$

## Resources

- López de Prado — *Advances in Financial Machine Learning*, on backtest-derived stop rules

## Connections

- [[Maximum Drawdown]] — the metric most kill switches are sized against
- [[Position Sizing]] — kill-switch budget should be consistent with per-trade sizing
- [[Trading Bot Operations]] — kill switch is one component of the production checklist
- [[Paper Trading]] — where trigger thresholds and recovery paths are tuned and tested
- [[Trade Journaling]] — every kill-switch trigger is journaled as a process event
- [[Trading Psychology]] — kill switches are operator-emotion-proof process discipline
- [[Risk Management MOC]] — sits alongside [[Value at Risk]] / [[Expected Shortfall]] as a structural risk control
