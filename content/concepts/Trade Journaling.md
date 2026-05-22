---
type: concept
title: "Trade Journaling"
tags:
  - concept
  - process
  - psychology
level: 3
prerequisites: []
---

## What It Is

Systematically logging every trade and the surrounding decision process so that performance can be analyzed instead of guessed at. A useful journal captures the **inputs to the decision** and the **state of the trader**, not just the P&L.

**Typical fields to capture per trade:**

- **Setup**: which playbook / pattern (e.g., mean reversion, range extreme, breakout)
- **Entry rationale ("Why?")**: explicitly written — why this price, why now
- **Stop placement rationale**: why this invalidation level
- **Confluences**: which secondary signals supported the trade (divergences, EMAs, levels, etc.)
- **Setup grade**: A* / B / C tier, with risk sized accordingly
- **Execution pattern**: how the position was entered (single clip, scale-in, etc.)
- **Macro / data events on the day**
- **Thoughts during the trade lifecycle**: emotions, hesitations, deviations from plan
- **Post-trade review**: what worked, what didn't, at which stage of the lifecycle mistakes happened (entry / management / exit)

The point of the "Why?" field is to force articulated reasoning. If you can't explain why your entry or stop is at a given level, you're trading noise.

## Why It Matters

Without a journal, you have no data on your own behavior — only on the market. You can't tell whether your edge is in the entry, the management, or the exit, and you can't tell which mistakes are recurring vs. one-offs.

**What journaling enables:**

- **Setup expectancy estimation**: tag setups and measure realized win rate, payoff, and expectancy per tag. This is what makes setup tiering (A* / B / C) anything more than a feeling.
- **Execution pattern attribution**: discover which entry mechanics (e.g., scale-in vs. market entry) actually produce better outcomes.
- **Lifecycle mistake attribution**: separate entry mistakes from management mistakes from exit mistakes. If your entry and management are clean but you round-trip winners, the fix is at the exit stage — not the strategy.
- **Process-based goals**: replace P&L goals with weakness-targeted goals (e.g., "always use TP limit orders", "don't move TP after fill"). Process goals are controllable; P&L isn't.
- **Devil's advocate review**: before taking a trade, list reasons *not* to take it. This often demotes a perceived A* setup to a B and forces smaller size.

For systematic strategies the journal is the strategy log + monitoring; for discretionary trading it is the only honest record of what actually happened.

## Resources

- [[Fooled by Randomness]] — why your unrecorded memory of trades is unreliable

## Connections

- [[Position Sizing]] — sizing by setup grade requires per-setup expectancy data
- [[Trading Psychology]] — emotional logging is the input to fixing process leaks
- [[Overfitting]] — small per-setup samples invite the same overfitting risks as backtests
- [[Sharpe Ratio]] / [[Sortino Ratio]] — journaled returns feed the metrics
