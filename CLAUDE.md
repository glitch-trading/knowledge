# Knowledge Base

Obsidian vault for the Glitch quant trading learning roadmap.

## Structure

- `roadmap/` — Learning levels 1-6, the main progression path
- `concepts/` — Individual concept notes (MOCs and leaf notes)
- `books/` — One page per book with key takeaways and connections
- `papers/` — One page per paper with summary, key results, and connections
- `courses/` — One page per course/video series with key takeaways and connections
- `templates/` — Obsidian templates for new notes (book, paper, concept, course)

## Conventions

- Notes use `[[wikilinks]]` for internal links and YAML frontmatter
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
- New concepts go in `concepts/`, books in `books/`, papers in `papers/`, courses in `courses/`
- Check for orphan wikilinks after adding new references

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
5. **MOC linkage is required.** Every new concept must be linked from at least one relevant MOC (`Trading Strategies MOC`, `Risk Management MOC`, `Market Structure MOC`, `Math MOC`, `Probability & Statistics MOC`, `Infrastructure MOC`).
6. **Report what was skipped.** When done, briefly note what was intentionally left out and why, so the user can flag anything misjudged.
