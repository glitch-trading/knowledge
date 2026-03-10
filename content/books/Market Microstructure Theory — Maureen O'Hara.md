---
type: book
title: "Market Microstructure Theory"
author: Maureen O'Hara
status: unread
tags:
  - book
  - microstructure
level: 6
topics:
  - "[[Adverse Selection]]"
  - "[[Market Impact]]"
  - "[[Order Book]]"
---

**The academic foundation of market microstructure. Information models, inventory models, and the theory behind how markets actually work.**

## Why Read This

This is the canonical academic textbook on market microstructure — the study of how trading actually happens. While most finance theory assumes frictionless markets, microstructure theory studies the mechanisms: order books, dealers, information asymmetry, and price formation.

It's dense and academic, but it provides the theoretical foundations that applied market making (Avellaneda-Stoikov, Cartea et al.) builds on. If you want to understand *why* spreads exist, *why* market impact follows certain patterns, and *why* informed trading affects prices the way it does, this is the source.

## Key Takeaways

- **Information models (Glosten-Milgrom, Kyle).** These models formalize how informed trading moves prices. In Glosten-Milgrom, the market maker updates beliefs after each trade using Bayesian inference. In Kyle, a single informed trader strategically hides behind noise traders. Both explain why the spread exists: it compensates the market maker for [[Adverse Selection]].
- **Inventory models (Stoll, Ho-Stoll, Amihud-Mendelson).** Market makers accumulate unwanted inventory and must be compensated for holding it. Inventory risk leads to quote shading — adjusting prices to attract offsetting flow. This is the theoretical basis for the inventory penalty in [[Avellaneda-Stoikov]].
- **Price discovery.** How information gets incorporated into prices. The permanent component of [[Market Impact]] reflects information; the transient component reflects liquidity. Hasbrouck's information share measures which venue contributes most to price discovery.
- **Market design.** How the rules of the market (continuous vs. call auction, maker-taker fees, tick sizes, priority rules) affect outcomes for different participants. Relevant for understanding differences between CEX order books and DEX AMMs.
- **Transparency and anonymity.** How much information should be public? Pre-trade transparency (visible order book) vs. post-trade transparency (published trades). Anonymity protects informed traders but hurts price discovery.


## Connections

- [[Adverse Selection]] — The core concept in information-based microstructure models
- [[Market Impact]] — How and why trading moves prices
- [[Order Book]] — The central mechanism studied in microstructure theory
