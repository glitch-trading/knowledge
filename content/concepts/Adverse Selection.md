---
type: concept
title: "Adverse Selection"
tags:
  - concept
  - market-making
  - microstructure
level: 1-2
prerequisites: []
---

## What It Is

Adverse selection in trading occurs when the counterparties who choose to trade against you are disproportionately informed. When you post a bid and an ask, you hope to earn the spread from noise traders. But informed traders — those who possess superior information about the asset's true value — will selectively hit your quotes precisely when your prices are wrong.

If the true value just moved up, informed traders buy from your stale ask. If it moved down, they sell into your stale bid. You fill orders on the wrong side systematically, turning what should be a profitable spread into a losing position.

The key insight: **the very act of someone trading against you is informative**. A filled order is not neutral — it signals that your price was attractive to someone who may know more than you.

## Why It Matters

Adverse selection is the fundamental risk in market making. It explains:

- **Why spreads exist**: The spread is compensation for adverse selection risk. Higher adverse selection → wider spreads.
- **Why market makers cancel quotes**: Stale quotes are free options for informed traders. Speed matters because it reduces your adverse selection window.
- **Why some markets are harder to make**: Assets with more informed trading (e.g., individual stocks around earnings) have higher adverse selection costs.
- **Queue position tradeoffs**: Being first in the queue means you get filled more — but more fills can mean more adverse selection if informed traders are sweeping the book.

In crypto/DeFi, adverse selection is acute for [[AMM]] liquidity providers: arbitrageurs are the informed traders who systematically extract value from LPs whenever prices move.

## Key Equations

**Glosten-Milgrom spread decomposition:**

The bid-ask spread compensates for:
$$\text{Spread} = \text{Adverse Selection Cost} + \text{Inventory Cost} + \text{Order Processing Cost}$$

**Probability of informed trading (PIN):**
$$PIN = \frac{\alpha \cdot \mu}{\alpha \cdot \mu + 2\epsilon}$$

Where:
- $\alpha$ = probability of an information event
- $\mu$ = arrival rate of informed traders
- $\epsilon$ = arrival rate of uninformed traders

Higher PIN → wider spread required to break even.

**Expected loss per trade to informed flow:**
$$E[\text{loss}] = P(\text{informed}) \times E[\text{price move} \mid \text{informed}]$$

## Resources

- Glosten & Milgrom (1985) — "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders"
- Kyle (1985) — "Continuous Auctions and Insider Trading"
- Larry Harris — *Trading and Exchanges*, Chapter 13
- Easley, Kiefer, O'Hara & Paperman (1996) — PIN model

## Connections

- [[Market Making]] — Adverse selection is the primary risk a market maker faces
- [[Spread]] — Spread width is largely determined by adverse selection intensity
- [[Inventory Risk]] — The other major market making risk, but adverse selection is often dominant
- [[Impermanent Loss]] — IL in AMMs is a form of adverse selection loss to arbitrageurs
