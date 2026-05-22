---
type: concept
title: "Regime Switching"
tags:
  - concept
  - statistics
  - time-series
  - regimes
level: 5
prerequisites:
  - "[[markov-chain|Markov Chain]]"
  - "[[time-series-analysis|Time Series Analysis]]"
---

## What It Is

**Regime switching** models treat the market as moving between a small number of qualitatively distinct *regimes* — bull / bear / sideways, low-vol / high-vol, risk-on / risk-off — with regime transitions governed by a [[markov-chain|Markov Chain]]. The full model is then *piecewise stationary*: within each regime the data-generating process is approximately stable, but the regime itself jumps over time.

The framework has two flavors:

- **Observable regimes** — the modeler labels each historical period using some rule (e.g., 20-day rolling return above threshold → bull) and estimates the transition matrix directly. Simple, transparent, and easy to backtest, but the regime labels are reverse-engineered from price and can lag the true underlying state.
- **Hidden regimes** — the regime is latent and inferred jointly with the model parameters from returns and other observables. See [[hidden-markov-models|Hidden Markov Models]].

Common state definitions:

- **Trend regimes**: bull / bear / sideways from rolling return sign and magnitude, or position of price vs. moving averages.
- **Volatility regimes**: low / medium / high from rolling realized vol thresholds. Often the most economically meaningful split.
- **Liquidity regimes**: high / low from bid-ask spread or order-book depth percentiles.
- **Cross-asset regimes**: risk-on / risk-off from credit spreads, term structure, or cross-asset correlations.

The state space must be **mutually exclusive and collectively exhaustive** — every observation belongs to exactly one regime, no gaps and no overlaps. This is a hard constraint on how thresholds are defined.

## Why It Matters

Strategies have regime-dependent edge. Mean reversion makes money in ranges and loses in trends. Momentum is the inverse. A market-making book that is well-sized in calm vol becomes catastrophically over-sized in a volatility spike. Regime switching gives you a quantitative handle on which world you are in *and* the probability of transitioning into a different one in the next $k$ steps.

Concrete uses:

- **Position sizing.** Scale up in regimes where the strategy historically has positive expectancy; scale down or flatten in regimes where it does not.
- **Hedging.** A bull → bear transition probability above some threshold is a quantitative trigger to add downside hedges, not a feeling.
- **Strategy allocation.** Multi-strategy books can rotate capital toward regime-appropriate sleeves (momentum in trending vol regimes, market making in calm regimes).
- **Tail-risk awareness.** The stationary distribution tells you the long-run proportion of time spent in each regime. A strategy that depends on a regime the stationary distribution says occurs 5% of the time is taking implicit tail risk.

## From States to a Trading Signal

The pipeline:

1. Define states (thresholds + window length).
2. Label every historical bar with its state.
3. Estimate the transition matrix $\mathbf{P}$ from labeled history (see [[markov-chain|Markov Chain]]).
4. At each new bar, compute the one-step forecast $\mathbf{P}[s_t]$ where $s_t$ is the current state.
5. Map the forecast distribution to a position.

Two simple mappings:

- **Direct allocation**: long in bull, short / flat in bear, reduced size in sideways.
- **Difference signal**: $\text{signal}_t = P(\text{bull next}) - P(\text{bear next})$, scaled to a position $\in [-1, 1]$. Threshold the signal to avoid noise around zero.

```python
def regime_signal(P: np.ndarray, current_state: int,
                  bull: int = 0, bear: int = 1) -> float:
    next_dist = P[current_state]
    return next_dist[bull] - next_dist[bear]
```

## Walk-Forward Estimation

The transition matrix must be re-estimated using only data available at the time of the decision. Standard k-fold cross-validation leaks the future into the training set and inflates backtest Sharpe by 2–3x in our experience. See `Cross-Validation in Finance` in [[level-6-advanced-topics|Level 6 — Advanced Topics]] for the proper protocol (walk-forward, purging, embargo).

```python
def walkforward_signals(returns, states, lookback=252):
    sigs = []
    for i in range(lookback, len(states)):
        P = estimate_transition_matrix(states.iloc[i-lookback:i].values, n_states=3)
        sigs.append(regime_signal(P, int(states.iloc[i])))
    return pd.Series(sigs, index=states.index[lookback:])
```

Shorter lookbacks adapt faster to regime changes but produce noisier $\hat{\mathbf{P}}$ estimates. Longer lookbacks are stable but lag. There is no universally right window — calibrate to the strategy's holding period.

## Assumptions and Where They Break

Three assumptions to scrutinize before any live capital touches a regime-switching model:

1. **Markov property is an approximation.** In reality, a trend that has been running six months has different transition probabilities than one that just started. Partial fix: expand the state space to include duration or trend age. The cost is exponentially more transitions to estimate.
2. **Time-homogeneity is violated.** The probability of bull → bear in 2008 was very different from 2021. Rolling-window re-estimation (above) is the standard mitigation; richer alternatives include hierarchical priors or letting $\mathbf{P}$ itself follow a meta-process.
3. **Estimation noise on rare transitions.** Each cell of $\mathbf{P}$ should be backed by at least 20–30 observed transitions. Bull → bear in a 10-year sample on monthly bars may have only a handful of observations; that cell is essentially noise. Mitigate by merging states, extending the sample, or applying a Dirichlet prior.

## Anti-Patterns

- Defining states with overlapping or non-exhaustive thresholds (some bars belong to no regime or two regimes).
- Re-using a fixed $\mathbf{P}$ estimated on the full history across the backtest (lookahead bias — model "knew" about regime shifts before they happened).
- Treating regime labels as ground truth when they were reverse-engineered from price. The label is a *projection* of the underlying regime, not the regime itself.
- Over-fine state spaces (8+ states) on limited data. Most cells will be sparse and the off-diagonals will be sampling noise.
- Trading the *current state* rather than the *transition probabilities*. The signal lives in $\mathbf{P}[s_t]$, not in $s_t$.

## Resources

- Hamilton (1989) — "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle" (the canonical regime-switching paper)
- Ang & Bekaert (2002) — "Regime Switches in Interest Rates"
- *Regime-Switching Models* in Hamilton, *Time Series Analysis*, Ch. 22

## Connections

- [[markov-chain|Markov Chain]] — the underlying mathematical object
- [[hidden-markov-models|Hidden Markov Models]] — the latent-regime extension when states are not directly observable
- [[time-series-analysis|Time Series Analysis]] — the broader methodological context
- [[garch|GARCH]] — volatility regimes are often modeled with regime-switching GARCH variants
- [[position-sizing|Position Sizing]] — regime forecasts feed sizing decisions
- [[maximum-drawdown|Maximum Drawdown]] — regime-aware drawdown limits are tighter than static ones
- [[trading-strategies-moc|Trading Strategies MOC]] — where regime-aware strategies live
