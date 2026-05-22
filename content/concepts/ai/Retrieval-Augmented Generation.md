---
type: concept
title: "Retrieval-Augmented Generation"
tags:
  - concept
  - ai
  - research-workflow
level: 6
prerequisites:
  - "[[Large Language Models in Quant Research]]"
---

## What It Is

**Retrieval-Augmented Generation (RAG)** is the pattern of grounding an LLM's response on a corpus of external documents at inference time. Rather than relying on the model's training data, the system retrieves relevant document chunks for each query and includes them in the prompt as context.

The standard pipeline:

1. **Chunk** source documents into ~200-1000 token segments (paragraphs, sections, fixed windows with overlap).
2. **Embed** each chunk with an embedding model — a fixed-dimensional vector that places semantically similar chunks near each other.
3. **Index** embeddings in a vector database (FAISS, Pinecone, Weaviate, Qdrant, pgvector).
4. At query time, **embed the query**, retrieve the top-$k$ nearest chunks by cosine similarity.
5. **Synthesize** the answer by passing the retrieved chunks plus the query to an LLM.

Modern variants add:
- **Hybrid search** combining semantic similarity with BM25 / keyword for exact-match recall.
- **Re-ranking** retrieved chunks with a cross-encoder for precision.
- **Citation grounding** — the LLM cites which chunk supported each claim, allowing audit.

## Why It Matters

RAG is how funds put their *own* data behind an LLM without retraining. It is the architecture behind D.E. Shaw's DocLab, Balyasny's internal gateway, and most institutional "ask our docs" systems. Three reasons it is the dominant pattern in quant research right now:

- **No training, no leakage.** The LLM never sees the data during training; it is supplied per query. Sensitive internal notes never leave the perimeter if the embedding model and vector store are on-prem.
- **Auditability.** Each answer carries citations back to source chunks. A compliance team can verify what the model used to produce a claim — a hard requirement in regulated finance.
- **Fresh data.** Indexing happens nightly or in real time. The system can answer questions about today's filings without retraining.

Common quant applications:

- **Internal research memory.** "What did we conclude about energy markets in the last 2 years?" Returns synthesis with citations to specific notes and authors.
- **Regulatory and filings search.** Embed all 10-Ks, 10-Qs, 8-Ks, and earnings transcripts for a coverage universe. Query by theme, by company, by event.
- **Trade-rationale archive.** Search all post-trade write-ups for similar setups historically.
- **News alpha.** Real-time embedding of newswires; retrieve historically similar events to forecast price impact.

## Embedding Models

The retrieval quality is dominated by the embedding model. As of 2026:

- **OpenAI `text-embedding-3-large`** — strong general-purpose default.
- **Voyage, Cohere, BGE** — competitive open-weights options.
- **Domain-specific embeddings** (FinBERT, FinE5) — better recall on financial vocabulary but smaller ecosystem.

Embedding dimension typically 768-3072. Trade-off: larger embeddings improve recall but cost more to store and search.

## Chunking Strategies (the part that breaks)

Most RAG failures are bad chunking. Patterns:

- **Fixed-size with overlap** (e.g. 512 tokens, 50-token overlap) — simple, works adequately.
- **Semantic chunking** — split on section boundaries, paragraphs, or topical shifts (using a small model to detect breaks).
- **Hierarchical chunking** — index both coarse summaries and fine-grained passages; retrieve coarse first, drill down.
- **Document-type-aware** — 10-Ks split by SEC item, research notes split by section header, earnings calls split by speaker turn.

Financial-document specific gotchas:

- **Tables.** Naive chunking shreds tables. Either extract tables to a separate searchable store or include the full table in any chunk that references it.
- **Footnotes.** Often material; chunking that drops footnotes loses the precise definition of a metric.
- **Numeric precision.** Embedding "revenue grew 12.3% YoY" and "revenue grew 12% YoY" produces nearly identical vectors — preserving exact numbers requires keyword fallback.

## Evaluation

RAG is hard to evaluate well. Standard metrics:

- **Retrieval:** recall@k, MRR — does the right chunk appear in the top-$k$?
- **Generation:** faithfulness (does the answer match the retrieved context?), answer relevancy (does it actually address the question?).
- **End-to-end:** human-rated correctness on a held-out QA set built by domain experts.

The realistic workflow: build a small (50-200 item) QA evaluation set with known answers, sweep chunk size / embedding model / retrieval $k$ / re-ranker against it, ship the configuration that wins.

## Resources

- [[Large Language Models in Quant Research]] — Parent concept; RAG is the standard pattern for grounding LLMs on private data
- [[Karpathy — Neural Networks Zero to Hero]] — Tokenizer and embedding episodes provide the foundations

## Connections

- [[AI in Trading MOC]] — Index of AI-in-quant concepts
- [[Large Language Models in Quant Research]] — Parent concept
- [[Multi-Agent Systems for Trading]] — Agents commonly use RAG as their "memory" tool
