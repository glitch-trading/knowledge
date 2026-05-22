---
title: "AI in Trading — Map of Content"
type: MOC
tags:
  - MOC
  - ai
---

How LLMs and agentic systems are entering quant research and trading workflows. This MOC indexes concepts, not the underlying math — for foundations see [[Karpathy — Neural Networks Zero to Hero]] and [[The Elements of Statistical Learning — Hastie, Tibshirani & Friedman]].

## Core Concepts

- [[Large Language Models in Quant Research]] — Where LLMs fit (and where they fail) in research workflows
- [[Retrieval-Augmented Generation]] — Grounding LLMs on private financial data via vector search
- [[Multi-Agent Systems for Trading]] — Decomposing research into specialized LLM agents (AlphaGPT-style)

## Foundations

- [[Karpathy — Neural Networks Zero to Hero]] — Build a GPT from scratch
- [[The Elements of Statistical Learning — Hastie, Tibshirani & Friedman]] — Classical-ML primer

## Why It's a Separate Section

Pre-2023 quant research relied on traditional ML (gradient-boosted trees, factor regressions) and statistical models. Post-2023, every major fund has integrated LLMs into some part of the research stack — research co-pilot, document search, code generation, multi-agent strategy generation. The skill set is now part of baseline expectation for new hires at top firms.

The concepts in this MOC are the minimum vocabulary for that conversation: what an LLM can and can't do on financial data, how to ground a model on internal documents, and how to compose agents into a research workflow.

## How AI Fails on Financial Data

Recurring failure modes that appear across all three concepts above:

- [[Look-Ahead Bias]] — LLM-generated backtest code routinely uses future information
- [[Survivorship Bias]] — Asking an LLM for "the universe as of 2010" returns today's constituents
- [[Overfitting]] — Multi-agent systems multiply the throughput of hypothesis testing, multiplying false discoveries

## Connections

- [[Level 6 — Advanced Topics]] — Machine learning section
- [[Math MOC]] — Foundational math
- [[Trading Strategies MOC]] — Where agentic systems propose strategies into
