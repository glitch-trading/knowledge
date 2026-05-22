---
type: concept
title: "Market Profile"
tags:
  - concept
  - market-structure
  - technical-analysis
level: 3
prerequisites: []
---

## What It Is

Market Profile is a charting framework developed by J. Peter Steidlmayer at the CBOT that organizes price action by **time spent at each price level** rather than by candle. The output is the **TPO chart** (Time-Price Opportunity): a histogram-like distribution where each price level is stacked with letters representing the time periods (typically 30-minute brackets) in which that price traded.

**Core constructs:**

- **TPO (Time-Price Opportunity)**: one letter per time period at each price the market touched in that period.
- **Value Area (VA)**: the price range containing ~70% of the session's TPOs (one standard deviation). VAH = Value Area High, VAL = Value Area Low.
- **Point of Control (POC)**: the price with the most TPOs — the session's "fair price" by volume of time.
- **Single Prints**: prices touched in only one time period — gaps in the profile that mark fast, one-sided rejection moves. Often act as future magnets or pivots.
- **Initial Balance (IB)**: the range of the first hour, a reference for whether later action extends or stays inside.
- **Composite profile**: multiple sessions merged to find HTF value, POCs, and single prints.

A normal-distribution-shaped profile means balanced two-way trade (range day). A skewed or thin profile means one-sided initiative trade (trend day).

## Why It Matters

Market Profile is not a strategy on its own — it is a **trade location and confluence tool**. It answers questions that pure candle charts answer poorly:

- *Where is the market's accepted value vs. rejected price?* (VA vs. single prints)
- *Where is unfinished business the market is likely to revisit?* (single prints, naked POCs on composite profiles)
- *Is today a trend day or a balance day?* (profile shape)
- *Is a move into a level participation-backed or thin?*

For discretionary traders it is a secondary confluence layered on a primary playbook (e.g., mean reversion fades at composite VAH/VAL with single-print magnets behind them). For quants it overlaps with volume-profile features used in microstructure models, and the VA / POC are useful prior distributions for where a session will mean-revert.

**Caveats:**

- Built originally for futures pit data with clear session boundaries; in 24/7 crypto markets you must choose meaningful session windows.
- Like all derived chart constructs, it can be overfit. The level "worked" because price often visits the POC tautologically — measure actual edge before assuming significance.

## Resources

- J. Peter Steidlmayer — *Steidlmayer on Markets*
- James Dalton — *Mind Over Markets*, *Markets in Profile*

## Connections

- [[Order Book]] — Market Profile is the time-domain analogue of an L2 snapshot's volume distribution
- [[VWAP]] / [[TWAP]] — related "fair price" anchors used by execution algos
- [[Mean Reversion]] — POC and VA edges are common mean-reversion anchors
- [[Liquidity]] — single prints mark thin, low-liquidity regions
