---
type: concept
title: "Large Language Models in Quant Research"
tags:
  - concept
  - ai
  - research-workflow
level: 6
prerequisites: []
---

## What It Is

A **large language model (LLM)** is a transformer-based model trained on large text corpora to predict the next token. In quant research the model is rarely the alpha — it is a **research co-pilot** that compresses text-heavy work: summarizing filings, generating code from natural-language descriptions, structuring unstructured data, and acting as a tireless interlocutor for derivations.

The 2025-2026 wave of agentic and tool-using LLMs has moved their role from chat assistant to active component in research workflows. Examples publicly disclosed by funds:

- **D.E. Shaw — DocLab.** Vector database over internal research notes; queries return structured answers with confidence scores and audit trails.
- **Point72.** GPT-class models running in a locked Azure V-Net so internal data does not leave the perimeter.
- **Bridgewater — AIA Labs.** Multi-agent workflow that replicates parts of the human macro-research process.
- **Man Group — AlphaGPT.** Multi-agent system that generates strategy hypotheses, codes backtests, and critiques results — see [[Multi-Agent Systems for Trading]].

## Why It Matters

LLMs change the cost structure of three quant activities:

- **Reading.** A 200-page 10-K can be summarized, compared to prior filings for wording shifts, and tagged with sentiment in seconds. Year-over-year wording changes in MD&A are a documented alpha source.
- **Writing code.** "Backtest a 12-1 momentum strategy on this universe with realistic transaction costs" produces runnable code in seconds. The bottleneck shifts from typing to specifying and validating.
- **Deriving / debugging.** A stuck point on a [[Stochastic Calculus for Finance II — Steven Shreve|Shreve]] proof, an obscure Pandas error, or a confusing paper section — all become 30-second resolutions with the right prompt.

The effect compounds. A researcher who saves two hours per day on dead time (reading, boilerplate, debugging) reinvests that time in compounding research output.

## Where LLMs Fail on Financial Data

Failure modes that recur in production:

- **Hallucinated numbers.** LLMs will confidently invent statistics, dates, and price figures. Any numeric claim from an LLM must be traced to a source.
- **Look-ahead in generated code.** LLMs frequently produce backtest code that uses future information without flagging it — close-of-day features computed and traded at the same close, full-sample standardization, leaky cross-validation. See [[Look-Ahead Bias]].
- **Survivorship in universe selection.** Asking an LLM to "give me the S&P 500 in 2010" produces today's constituents, not the actual point-in-time membership. See [[Survivorship Bias]].
- **Confident wrong derivations.** LLMs will produce step-by-step math that looks right but has a sign error or a dropped term. Treat every derivation as needing manual verification.
- **Tokenization quirks on numeric text.** "$1,234.56" can tokenize unpredictably; numbers in scanned PDFs especially.
- **Stale training data.** Public models cut off at a fixed date. They do not know about recent earnings, recent regulatory changes, recent papers.

The working pattern is **LLM proposes, human disposes.** Use the model to generate candidates fast; verify every load-bearing claim before acting on it.

## Concrete Use Patterns

- **Paper-to-code reproduction.** Feed a paper PDF; ask for a step-by-step plan (math, data, pseudocode, pitfalls); implement and verify against any reported numbers in the paper.
- **Earnings-call sentiment.** Feed call transcripts; extract tone, forward-looking statements, and changes vs. prior calls. Test the resulting signal as an alpha factor.
- **10-K diff.** Feed this year's and last year's filings; surface wording changes in risk factors and MD&A.
- **Code review of backtesters.** Ask for "5 hypotheses about why this backtest looks too good" — the model usually catches at least one [[Look-Ahead Bias|look-ahead]] or [[Survivorship Bias|survivorship]] issue.
- **Math co-pilot.** "Stuck on this Itô step — explain three ways: formal, geometric, numerical example."

## Cost / Capability Tradeoffs

| Model class | Use for |
|---|---|
| Frontier (Claude Opus, GPT-5, Gemini Ultra) | Complex derivations, long-context analysis, agent reasoning |
| Mid-tier (Claude Sonnet, GPT-5 mini) | Most code generation, summarization, day-to-day research chat |
| Small / open-weights | Bulk text processing (millions of filings, embeddings), on-prem deployment |
| Domain-specific (BloombergGPT-class) | When training data leakage to a public API is unacceptable |

For research workflows, the dominant cost is not API spend but the engineer's time. Pay for the best model unless you are doing high-volume batch.

## Resources

- [[Karpathy — Neural Networks Zero to Hero]] — Build a GPT from scratch; the right primer to know what's under the hood
- [[Retrieval-Augmented Generation]] — How to give an LLM access to your own data
- [[Multi-Agent Systems for Trading]] — How research-co-pilot use scales into AlphaGPT-style workflows

## Connections

- [[AI in Trading MOC]] — Index of AI-in-quant concepts
- [[Retrieval-Augmented Generation]] — Standard pattern for grounding LLMs on private/financial data
- [[Multi-Agent Systems for Trading]] — Multi-LLM workflows that mimic research pods
- [[Look-Ahead Bias]] / [[Survivorship Bias]] — The two failure modes LLM-generated backtest code most often introduces
