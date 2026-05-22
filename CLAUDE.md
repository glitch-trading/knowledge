# Knowledge Base

Obsidian vault for the Glitch quant trading learning roadmap.

## Structure

- `roadmap/` — Learning levels 1-6, the main progression path
- `concepts/` — Individual concept notes (MOCs and leaf notes), organized into topic subfolders:
  - `concepts/math/` — calculus, optimization, stochastic calculus, PDEs, dynamic programming
  - `concepts/probability-stats/` — distributions, regression, time series, Markov / HMM, information theory
  - `concepts/strategies/` — arbitrage, MEV, mean reversion, market making, momentum, combinatorial
  - `concepts/market-microstructure/` — order book, AMMs, liquidity, prediction-market venues, LMSR
  - `concepts/execution/` — TWAP, VWAP
  - `concepts/derivatives-options/` — Black-Scholes, Greeks, implied vol, put-call parity
  - `concepts/risk/` — VaR, Sharpe, Kelly, factor models, alpha attribution, operational risk
  - `concepts/ai/` — LLMs, RAG, multi-agent systems in quant
  - `concepts/infrastructure/` — bot ops, infrastructure MOC
  - `concepts/trader-meta/` — psychology, journaling, mental math, reflective reads
- `books/` — One page per book with key takeaways and connections
- `papers/` — One page per paper with summary, key results, and connections
- `courses/` — One page per course/video series with key takeaways and connections
- `templates/` — Obsidian templates for new notes (book, paper, concept, course)

## Conventions

- Notes use `[[wikilinks]]` for internal links and YAML frontmatter
- Filenames are kebab-case (lowercase, hyphens, no apostrophes or diacritics). Wikilinks target the kebab basename with an alias for the display title: `[[bayes-theorem|Bayes' Theorem]]`. Frontmatter `title:` carries the human-readable name.
- Every book, paper, and course referenced in the roadmap must have its own page
- Plain-text resource mentions should be converted to wikilinks
- Concept notes follow: What It Is, Why It Matters, Key Equations, Resources, Connections
- Book notes follow: Key Takeaways, What It Covers, Resources
- Paper notes follow: Summary, Key Results, Equations & Derivations, Connections
- Course notes follow: What It Covers, Key Takeaways, Connections
- `level:` in frontmatter indicates which roadmap level the resource belongs to
- `status:` tracks reading progress (not-started, in-progress, completed)

## Rules

- Do not modify `.obsidian/workspace.json`
- Do not add time estimates or durations to any content
- Do not use "tier" — use "level" for the roadmap progression
- Keep notes concise — no `## Notes`, `## Progress`, or `## Chapter Notes` sections
- New concepts go in the appropriate `concepts/<topic>/` subfolder, books in `books/`, papers in `papers/`, courses in `courses/`. If a new concept does not fit any existing topic folder, add a new folder rather than dropping the file at `concepts/` root.
- Check for orphan wikilinks after adding new references
- Always add a short, runnable code snippet (fenced, language-tagged) when the concept has a computable side — pricing, estimation, simulation, sizing, signal construction. The snippet should illustrate the equations directly above it, not duplicate them. Skip code only when the idea is purely conceptual or the snippet would be longer than the surrounding prose.
- Always add a mermaid diagram when the concept involves a flow, sequence, state machine, dependency graph, or visual structure (e.g., sandwich attacks, MEV pipelines, regime transitions, derivation chains). Skip diagrams when the relationship is already obvious from prose or a single equation.
- When you add code, run it locally and reflect the actual output in inline comments — never invent numbers.

## Contribution workflow

- **Never commit additions directly to `main`.** Every new note, edit, or ingest goes on a feature branch and lands via a pull request — even small, single-file changes.
- Branch naming: `add/<short-slug>` for new notes (e.g. `add/trade-journaling`), `edit/<short-slug>` for edits to existing notes, `ingest/<source-slug>` for batched ingests of an article/post/transcript.
- One coherent change per PR. If an ingest produces several unrelated new notes, prefer one PR for the batch (titled after the source) over splintering — reviewers want to see the same filtering decisions together.
- PR title: Conventional Commits (`feat(concepts): add Mean Reversion and Trade Journaling`, `docs(claude): codify ingest workflow`).
- PR body must include: (1) what was added/changed, (2) which MOCs were updated, (3) for ingests, what was intentionally skipped from the source and why.
- Do not self-merge unless the user says so.

## Ingesting external posts / articles

When asked to ingest an article, blog post, thread, or video transcript:

1. **Filter ruthlessly.** Extract only ideas that are durable, non-obvious, and relevant to the quant-trading focus of this KB. Skip marketing fluff, motivational platitudes, personal-brand framing ("my exact 5-step process"), generic "AI will change everything" claims, proprietary-spreadsheet specifics, and "1% better every day" content. If a paragraph would not survive being summarized in one sentence to a senior quant, drop it.
2. **Translate, don't transcribe.** Rewrite extracted ideas in the KB's voice — concise, technical, framed against existing concepts. Never paste author phrasing verbatim. Do not name the author or post in the note (the KB is concept-centric, not source-centric). If a Resources link is warranted, add the source there.
3. **Prefer updating existing notes** over creating new ones. Only create a new concept note if the idea is substantial enough to stand alone and is genuinely missing — search `concepts/` first.
4. **Cross-disciplinary content** (e.g., a discretionary-TA post) should be folded in only where it generalizes. A "weekly bias" concept from a discretionary trader maps to HTF regime conditioning for a quant; write the general form, not the TA-specific form.
5. **MOC linkage is required.** Every new concept must be linked from at least one relevant MOC (`trading-strategies-moc`, `risk-management-moc`, `market-structure-moc`, `math-moc`, `probability-and-statistics-moc`, `infrastructure-moc`).
6. **Report what was skipped.** When done, briefly note what was intentionally left out and why, so the user can flag anything misjudged.
