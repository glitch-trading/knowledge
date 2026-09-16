# Knowledge vault

Read `CLAUDE.md` before editing notes. This repository is an independent Markdown vault; do not restore website tooling or add a submodule link.

- Preserve existing user edits and `.obsidian` settings. Do not read or modify workspace state.
- Open a GitHub issue before fixes or additions. Use a feature branch; never commit directly to `main`.
- Do not commit, push, or open a pull request without an explicit instruction for that action.
- Run `python3 scripts/check.py`, `python3 -m pytest scripts/check_test.py -q`, and `git diff --check` before handing off a change. The checker uses only the standard library; its tests require pytest.
- Manually inspect runnable snippets before executing them. Record actual outputs and dependency versions. Structural checks do not establish correctness or profitability.
- Keep examples causal. State approximations, initialization choices, and missing data rather than treating them as measured evidence.
