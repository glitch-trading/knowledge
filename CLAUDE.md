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
