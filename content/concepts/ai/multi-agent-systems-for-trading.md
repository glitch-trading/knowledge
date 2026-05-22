---
type: concept
title: "Multi-Agent Systems for Trading"
tags:
  - concept
  - ai
  - research-workflow
level: 6
prerequisites:
  - "[[large-language-models-in-quant-research|Large Language Models in Quant Research]]"
---

## What It Is

A **multi-agent system** decomposes a complex task into a graph of specialized LLM-driven agents, each with a narrow role and access to specific tools. For trading research the canonical decomposition mirrors a human research pod:

| Agent | Role |
|---|---|
| **Idea generator** | Produces strategy hypotheses in free form: "mean reversion in small-cap energy stocks intraday" |
| **Implementer** | Converts a hypothesis to runnable backtest code with data loading, signal construction, performance metrics |
| **Risk critic** | Inspects backtest results for overfitting, look-ahead, survivorship, factor exposures, regime sensitivity |
| **Portfolio manager** | (optional) Sizes the strategy in the broader book, allocates capital |

The agents communicate via structured messages, share access to data and tools (Python interpreter, SQL, vector store, market data APIs), and can loop until a quality threshold or a human checkpoint.

The publicly documented example is **Man Group's AlphaGPT** — an agentic system that generates ~50-100 strategy ideas per day, converts them to code, evaluates them, and surfaces the survivors for human researchers to review. Bridgewater's AIA Labs is a more ambitious instance, applying the same pattern to macro investing.

## Why It Matters

Multi-agent systems collapse the idea-to-evaluation cycle from weeks to hours.

- **Throughput.** A human research pod evaluates 3-10 hypotheses per week. An agentic system runs 50-100 per day. Most are duds — but the survivors hit the human team's queue already vetted for the common failure modes.
- **Standardization.** Every hypothesis goes through the same gauntlet — same backtest harness, same risk checks, same factor regressions. Variance from "researcher A is sloppy about transaction costs" disappears.
- **Documentation.** The system produces a written rationale, code, and critique for every run. The audit trail is automatic.
- **Specialization.** Each agent has a tight scope and can be tuned, evaluated, and replaced independently. The idea generator can be a frontier model; the implementer can be a smaller code-tuned model; the risk critic can be a rule-based ensemble.

## Architecture Patterns

**Linear pipeline:** Idea → Implement → Evaluate → Critique → Output. Simplest, easiest to debug.

**Adversarial loop:** Implementer proposes, critic finds flaws, implementer revises, repeat until critic passes or hits an iteration cap. Mimics peer review. Catches more issues than a linear pipeline but is more expensive.

**Tree-of-thought:** Idea agent branches into multiple variants; each is evaluated in parallel; only the top-$k$ proceed to deeper evaluation. Mimics research breadth-first search.

**Human-in-the-loop checkpoints:** At least one human approval before code touches real data, one before any strategy is sized in a real book. Non-negotiable for production deployment.

## Tools the Agents Use

- **Code interpreter / sandbox.** Run generated Python with restricted file system and network access.
- **Vector store / [[retrieval-augmented-generation|RAG]] over research history.** Avoid re-deriving things the team has already concluded.
- **Market data APIs and historical databases.** With strict point-in-time access to prevent [[look-ahead-bias|Look-Ahead Bias]].
- **Factor regression services.** Pre-built [[fama-french-factor-model|factor regressions]] callable as a tool.
- **Backtest harness.** A standardized library the implementer must use; rejects code that does not respect timing invariants.

## Failure Modes

- **Cascading errors.** A subtle bug in the idea generator (vague hypotheses) propagates into bad code and useless critiques. Each agent's output quality is bounded by its input.
- **Reward hacking.** If the critic agent is too lenient or the optimizer too greedy, the implementer learns to produce code that *looks* clean to the critic but is broken in subtler ways.
- **Cost explosions.** Adversarial loops can spin indefinitely; always cap iterations and total tokens per run.
- **Hidden over-fitting.** The system can run thousands of "independent" hypotheses that share the same underlying [[look-ahead-bias|look-ahead]] flaw in the harness. Multiple-testing correction must account for the agent throughput.
- **Loss of explanation.** Decisions become harder to trace as agents chain. Mitigate with structured logging at every hop.

## Minimal Implementation Sketch

A three-agent loop in Python pseudocode:

```python
hypothesis = idea_agent.generate(market_state, prior_results)
code = implementer.write_backtest(hypothesis)
result = sandbox.run(code, data_provider=point_in_time)
critique = risk_critic.evaluate(code, result, hypothesis)

if critique.passes:
    queue_for_human_review(hypothesis, code, result, critique)
else:
    if iterations < MAX_ITERATIONS:
        code = implementer.revise(code, critique)
        result = sandbox.run(code, data_provider=point_in_time)
        # continue loop
    else:
        log_failure(hypothesis, critique)
```

A weekend's work with a frontier model API gets you a working prototype. The hard parts — point-in-time data, a robust backtest harness, the critic's specification — are also the parts where institutional firms have a moat.

## Resources

- [[large-language-models-in-quant-research|Large Language Models in Quant Research]] — Foundational context for what each agent can do
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]] — The standard memory layer for these systems
- Man Group blog posts on AlphaGPT and Alpha Assistant (publicly available)

## Connections

- [[ai-in-trading-moc|AI in Trading MOC]] — Index of AI-in-quant concepts
- [[large-language-models-in-quant-research|Large Language Models in Quant Research]] — Each agent is an LLM application
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]] — Memory and research-history tool
- [[overfitting|Overfitting]] — The throughput of agentic systems multiplies the multiple-testing problem
- [[look-ahead-bias|Look-Ahead Bias]] — The agent harness must enforce point-in-time data access architecturally
