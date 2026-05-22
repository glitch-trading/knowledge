---
type: concept
title: "Sandwich Attack"
tags:
  - concept
  - MEV
level: 4
prerequisites:
  - "[[frontrunning|Frontrunning]]"
  - "[[backrunning|Backrunning]]"
  - "[[mev|MEV]]"
---

## What It Is

A sandwich attack combines [[frontrunning|Frontrunning]] and [[backrunning|Backrunning]] around a victim's swap transaction. The attacker places two transactions — one before and one after the victim — to extract profit from the price impact of the victim's trade.

**Step by step:**
1. **Victim** submits a swap: buy token Y with token X on an AMM.
2. **Attacker frontrun**: Buy token Y before the victim, pushing the price up.
3. **Victim's trade executes**: Victim buys token Y at the now-higher price, pushing it up further.
4. **Attacker backrun**: Sell token Y at the elevated price.

```mermaid
sequenceDiagram
  participant V as Victim
  participant M as Mempool / Builder
  participant A as Attacker (searcher)
  participant P as AMM Pool
  V->>M: tx: buy Y with X (slippage tol = s)
  A->>M: tx_front: buy Y (small)
  A->>M: tx_back:  sell Y (small)
  Note over M: builder orders: front → victim → back
  M->>P: tx_front executes; price up
  M->>P: victim executes at worse price
  M->>P: tx_back executes; attacker exits
  P-->>A: profit = exit − entry − gas − builder tip
  P-->>V: receives Δy below quoted mid (≤ s slippage)
```

The builder enforces the ordering atomically: if any leg reverts, the whole bundle is dropped, so the attacker never gets caught holding inventory.

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

**Frontrun-size search (CPMM, no fee):**

```python
def sandwich_profit(x: float, y: float, victim_dx: float, attacker_dx: float) -> float:
    # 1. Attacker buys Y with attacker_dx of X.
    dy_front = (y * attacker_dx) / (x + attacker_dx)
    x1, y1 = x + attacker_dx, y - dy_front
    # 2. Victim buys Y.
    dy_victim = (y1 * victim_dx) / (x1 + victim_dx)
    x2, y2 = x1 + victim_dx, y1 - dy_victim
    # 3. Attacker sells back the dy_front they bought.
    dx_back = (x2 * dy_front) / (y2 + dy_front)
    return dx_back - attacker_dx                      # profit in X (gas/tip ignored)

# Scan attacker sizes against a fixed victim trade.
import numpy as np
sizes = np.linspace(0.1, 200, 200)
profits = [sandwich_profit(x=1_000, y=3_000_000, victim_dx=50, attacker_dx=s) for s in sizes]
best = sizes[int(np.argmax(profits))]                 # optimal attacker_dx
```

The profit curve is concave: small frontrun = little impact captured; large frontrun = attacker's own slippage eats the gain. Builders auction the right to land the bundle, so the optimum is also a function of how much tip the searcher must pay to win the slot.

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

- [[mev|MEV]] — Sandwiching is a major category of MEV extraction
- [[frontrunning|Frontrunning]] — The first leg of a sandwich attack
- [[backrunning|Backrunning]] — The second leg of a sandwich attack
- [[slippage|Slippage]] — The victim's slippage tolerance determines the attack's profit ceiling
- [[amm|AMM]] — Sandwich attacks exploit AMM price impact mechanics
