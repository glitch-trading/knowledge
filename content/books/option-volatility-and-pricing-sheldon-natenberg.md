---
type: book
title: "Option Volatility and Pricing"
author: Sheldon Natenberg
status: unread
tags:
  - book
  - options
  - volatility
level: 2, 4
topics:
  - "[[geometric-brownian-motion|Geometric Brownian Motion]]"
  - "[[greeks|Greeks]]"
  - "[[implied-volatility|Implied Volatility]]"
---

**The practical companion to Hull. How traders actually think about options and volatility.**

## Why Read This

Where Hull gives you the theory, Natenberg gives you the trader's perspective. This book explains how options market makers think about volatility, how they manage risk in practice, and why certain trades make sense. The treatment of volatility — historical vs implied, the vol surface, vol trading strategies — is particularly strong.

For crypto/DeFi, understanding vol is critical: LP positions are short vol, funding rates reflect vol expectations, and options markets on Deribit increasingly drive price discovery.

## Key Takeaways

- **Volatility is the key variable.** Everything in options comes back to vol. Historical vol tells you what happened, [[implied-volatility|implied vol]] tells you what the market expects. The gap between them is where vol traders find edge.
- **Trader's [[greeks|Greeks]].** Practical understanding of how to use Delta, Gamma, Theta, Vega to manage a book — not just formulas but intuition for what each means for P&L.
- **Spreads and strategies.** Vertical, horizontal, diagonal spreads, straddles, strangles — each expresses a different view on direction and vol.
- **Vol surface.** The smile, skew, and term structure of [[implied-volatility|Implied Volatility]] — why it exists and what it tells you about market expectations.


## Connections

- [[options-futures-and-other-derivatives-john-hull|Options, Futures, and Other Derivatives — John Hull]] — Theory complement
- [[greeks|Greeks]] — Trader-facing exposition of the Greeks
- [[implied-volatility|Implied Volatility]] — The book's central object
- [[put-call-parity|Put-Call Parity]] — Used for cleaning surface inputs
- [[impermanent-loss|Impermanent Loss]] — Understanding LP as short vol
- [[level-4-mev-and-algorithmic-trading|Level 4 — MEV & Algorithmic Trading]] — Greeks and derivatives section
