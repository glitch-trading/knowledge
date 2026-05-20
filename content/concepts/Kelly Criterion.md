---
type: concept
title: "Kelly Criterion"
tags:
  - concept
  - risk
  - position-sizing
level: 3
prerequisites: []
---

## What It Is

The Kelly Criterion determines the optimal fraction of your bankroll to bet on a favorable wager. It maximizes the expected logarithmic growth rate of wealth — i.e., the geometric compounding rate over time.

For a simple binary bet with probability $p$ of winning and odds of $b$ to 1:

$$f^* = \frac{bp - q}{b}$$

Where:
- $f^*$ = optimal fraction of bankroll to wager
- $b$ = net odds (win $b$ for every $1$ wagered)
- $p$ = probability of winning
- $q = 1 - p$ = probability of losing

**For even-money bets** ($b = 1$): $f^* = 2p - 1$. You need $p > 0.5$ (an edge) for a positive Kelly fraction.

**For continuous distributions** (e.g., trading): Kelly generalizes to maximizing $E[\ln(1 + f \cdot R)]$ where $R$ is the return distribution of the bet.

## Why It Matters

Kelly is the bridge between "having an edge" and "sizing your bets to exploit it." Without Kelly thinking:

- **Bet too large**: You risk ruin. Even with a positive edge, overbetting eventually blows up your account through variance. Betting 2x Kelly cuts your long-run growth rate to zero.
- **Bet too small**: You leave money on the table. Growth is suboptimal.
- **Full Kelly is aggressive**: In practice, full Kelly is rarely used because it produces large drawdowns (~50% drawdowns are common). Parameter estimation errors also mean your perceived edge may be wrong.

**Fractional Kelly** is the standard practice:
- **Half Kelly** ($f^*/2$): ~75% of the growth rate, dramatically lower drawdowns
- **Quarter Kelly** ($f^*/4$): Even more conservative, suitable when edge estimates are uncertain

The key insight: **the optimal bet size depends on both your edge AND your uncertainty about that edge.** When you're unsure of your edge (you always are), size down.

## Key Equations

**Binary Kelly:**
$$f^* = \frac{bp - q}{b}$$

**Continuous Kelly (Gaussian returns):**
$$f^* = \frac{\mu}{\sigma^2}$$

Where $\mu$ = expected excess return, $\sigma^2$ = variance of returns. This says: bet more when edge is high, less when variance is high.

**Growth rate at Kelly fraction $f$:**
$$g(f) = p \ln(1 + bf) + q \ln(1 - f)$$

Maximum at $f = f^*$.

## Why Overbetting Kills

The growth rate $g(f)$ is concave, symmetric around $f^*$, and crosses zero at $f = 0$ and $f = 2f^*$. Bet *anywhere* above $2f^*$ and your long-run log-wealth is negative — you compound toward zero with probability one, despite a positive-expectation bet.

```python
import numpy as np

def simulate_growth(p: float, b: float, fraction: float,
                    n_bets: int, n_paths: int, seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    wins = rng.random((n_paths, n_bets)) < p
    log_returns = np.where(wins, np.log(1 + b * fraction), np.log(1 - fraction))
    return np.exp(log_returns.cumsum(axis=1))         # wealth, shape: (n_paths, n_bets)

def max_drawdown(W: np.ndarray) -> np.ndarray:
    peaks = np.maximum.accumulate(W, axis=1)
    return (1 - W / peaks).max(axis=1)

p, b = 0.55, 1.0                                      # 55% edge on even money
f_star = (b * p - (1 - p)) / b                        # = 0.10 (full Kelly)

for label, f in [("full",  f_star),
                 ("half",  f_star / 2),
                 ("2×",    2 * f_star),
                 ("3×",    3 * f_star)]:
    W = simulate_growth(p, b, f, n_bets=1_000, n_paths=5_000)
    print(f"{label:5s} (f={f:.3f})  median wealth = {np.median(W[:, -1]):8.2f}x  "
          f"median max DD = {np.median(max_drawdown(W)):.1%}")
```

Typical output (1,000 sequential bets, 5,000 paths):

```
full  (f=0.100)  median wealth =   149.66x  median max DD = 89.5%
half  (f=0.050)  median wealth =    42.63x  median max DD = 61.3%
2×    (f=0.200)  median wealth =     0.87x  median max DD = 99.9%
3×    (f=0.300)  median wealth =     0.00x  median max DD = 100.0%
```

Full Kelly compounds spectacularly *and* spends most of its life near a path-worst drawdown of ~90%. Half Kelly forfeits a third of the growth and cuts drawdowns roughly in half — a deal that becomes obviously correct once your edge estimate has any uncertainty. At $2f^*$ the long-run log growth is zero by construction; the median wealth hovering near $1$ confirms it.

## Resources

- [[A Man for All Markets — Ed Thorp]] — Thorp popularized Kelly for gambling and investing
- Kelly, J.L. (1956) — "A New Interpretation of Information Rate"
- Thorp, E.O. — "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market"

## Connections

- [[Position Sizing]] — Kelly is the foundational framework for position sizing
- [[Risk Aversion]] — Fractional Kelly maps to different levels of risk aversion
- [[A Man for All Markets — Ed Thorp]] — Thorp applied Kelly from blackjack to Wall Street
- [[Maximum Drawdown]] — Full Kelly produces ~50% expected max drawdown; fractional Kelly reduces this
