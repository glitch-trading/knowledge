---
type: concept
title: "Sandwich Attack"
tags:
  - concept
  - MEV
level: 4
prerequisites:
  - "[[Frontrunning]]"
  - "[[Backrunning]]"
  - "[[MEV]]"
---

## What It Is

A sandwich attack combines [[Frontrunning]] and [[Backrunning]] around a victim's swap transaction. The attacker places two transactions — one before and one after the victim — to extract profit from the price impact of the victim's trade.

**Step by step:**
1. **Victim** submits a swap: buy token Y with token X on an AMM.
2. **Attacker frontrun**: Buy token Y before the victim, pushing the price up.
3. **Victim's trade executes**: Victim buys token Y at the now-higher price, pushing it up further.
4. **Attacker backrun**: Sell token Y at the elevated price.

The attacker profits from the difference between their buy price (step 2) and sell price (step 4). The victim receives fewer tokens than they would have without the attack — they pay a worse price, effectively a hidden tax.

**Why it works**: The victim's slippage tolerance defines the attack's profit ceiling. If the victim allows 1% slippage, the attacker can extract up to ~1% of the trade value (minus gas and builder tips).

## Why It Matters

- **Most visible form of MEV**: Sandwich attacks are the most intuitive and commonly discussed MEV extraction method.
- **Direct cost to retail**: Unlike CEX-DEX arb (which arguably improves price accuracy), sandwiching purely extracts value from the victim. It is adversarial.
- **Slippage settings matter**: Your slippage tolerance is your maximum loss to sandwich attacks. Setting it too high invites extraction; setting it too low causes trade failures.
- **Defense mechanisms**: Private transaction submission (Flashbots Protect, MEV Blocker), MEV-aware DEX aggregators, and batch auction designs (CowSwap) exist specifically to counter sandwiching.

## Key Equations

**Sandwich profit (simplified, constant product AMM):**

$$\pi = \Delta y_{\text{backrun}} - \Delta x_{\text{frontrun}} \cdot P_0 - \text{gas} - \text{tip}$$

**Maximum extractable from victim (given slippage tolerance $s$):**

$$\pi_{\max} \approx s \times V_{\text{victim}} - 2 \times \text{gas cost}$$

Where $V_{\text{victim}}$ is the notional value of the victim's swap.

**Optimal frontrun size**: The attacker optimizes the frontrun size to maximize profit. Too small = not enough price impact to extract. Too large = the attacker's own slippage eats into profits. The optimal size depends on:
- Pool liquidity (reserves $x, y$)
- Victim's trade size
- Victim's slippage tolerance
- Gas costs and builder tips

## Resources

- "Flash Boys 2.0" — Daian et al.
- "High-Frequency Trading on Decentralized On-Chain Exchanges" — Zhou et al.
- EigenPhi — real-time sandwich attack tracking
- Flashbots Protect / MEV Blocker — sandwich defense tools

## Connections

- [[MEV]] — Sandwiching is a major category of MEV extraction
- [[Frontrunning]] — The first leg of a sandwich attack
- [[Backrunning]] — The second leg of a sandwich attack
- [[Slippage]] — The victim's slippage tolerance determines the attack's profit ceiling
- [[AMM]] — Sandwich attacks exploit AMM price impact mechanics
