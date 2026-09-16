# Knowledge

An independent Obsidian research vault. Open `content/` in Obsidian, or read the Markdown directly. There is no website build or deployment.

## Verify notes

Run the structural check with Python 3.12 or newer on macOS or Linux:

```sh
python3 scripts/check.py
```

It rejects missing or ambiguous note links, missing frontmatter delimiters, duplicate top-level metadata fields, missing `title` or `type`, and unclosed fenced code. Qualified wikilinks are relative to `content/`; unqualified names must identify one note. Heading anchors are not checked. Hidden directories are skipped. Notes must be regular files, not symlinks or pipes, and each read is bounded to 1 MiB plus one byte to detect overflow.

This is a basic frontmatter shape check, not a YAML parser. It does not verify equations, external URLs, financial claims, or code outputs. Fenced code is never executed automatically.

Run the checker's regression tests in an environment with pytest installed:

```sh
python3 -m pytest scripts/check_test.py -q
git diff --check
```

## Indicator examples

The six indicator snippets were manually inspected and executed with Python 3.13, NumPy 2.3.3, and pandas 2.3.2 on 2026-09-16. Every printed value matched the adjacent comment. Their synthetic outputs demonstrate calculations, not profitable trading. Review a snippet before running it; its dependencies are separate from the structural checker.

## Contributions

Read [CLAUDE.md](CLAUDE.md) for note conventions. New work belongs on a feature branch. Open an issue before fixes or additions. Commit, push, and pull-request actions each require an explicit instruction.
