import os
import subprocess
import sys
from pathlib import Path

from check import check_vault


def note(root: Path, name: str, body: str = "") -> Path:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\ntitle: Example\ntype: concept\n---\n{body}", encoding="utf-8"
    )
    return path


def test_rejects_missing_wikilink(tmp_path: Path) -> None:
    note(tmp_path, "first.md", "[[missing|Missing]]")
    assert any("unresolved wikilink" in error for error in check_vault(tmp_path))


def test_rejects_ambiguous_basename(tmp_path: Path) -> None:
    note(tmp_path, "first.md", "[[target]]")
    note(tmp_path, "one/target.md")
    note(tmp_path, "two/target.md")
    assert any("ambiguous wikilink" in error for error in check_vault(tmp_path))


def test_accepts_qualified_links_and_ignores_fenced_code(tmp_path: Path) -> None:
    note(
        tmp_path,
        "first.md",
        "[[one/target#Section|Label]]\n```python\n[[not_a_link]]\n```\n",
    )
    note(tmp_path, "one/target.md")
    note(tmp_path, "two/target.md")
    assert check_vault(tmp_path) == []


def test_rejects_missing_frontmatter(tmp_path: Path) -> None:
    (tmp_path / "first.md").write_text("# Example\n", encoding="utf-8")
    assert any("frontmatter" in error for error in check_vault(tmp_path))


def test_rejects_duplicate_metadata_key(tmp_path: Path) -> None:
    (tmp_path / "first.md").write_text(
        "---\ntitle: One\ntitle: Two\ntype: concept\n---\n", encoding="utf-8"
    )
    assert any("duplicate frontmatter key" in error for error in check_vault(tmp_path))


def test_rejects_unclosed_fence(tmp_path: Path) -> None:
    note(tmp_path, "first.md", "```python\nprint(1)\n")
    assert any("unclosed code fence" in error for error in check_vault(tmp_path))


def test_rejects_unclosed_frontmatter(tmp_path: Path) -> None:
    (tmp_path / "first.md").write_text(
        "---\ntitle: One\ntype: concept\n", encoding="utf-8"
    )
    assert any("unclosed frontmatter" in error for error in check_vault(tmp_path))


def test_rejects_empty_vault(tmp_path: Path) -> None:
    assert any("no Markdown notes" in error for error in check_vault(tmp_path))


def test_rejects_symlink_notes(tmp_path: Path) -> None:
    target = note(tmp_path, "first.md")
    (tmp_path / "linked.md").symlink_to(target)
    assert any("symlink" in error for error in check_vault(tmp_path))


def test_rejects_nonexistent_root(tmp_path: Path) -> None:
    assert any(
        "existing directory" in error for error in check_vault(tmp_path / "missing")
    )


def test_rejects_oversized_note(tmp_path: Path) -> None:
    note(tmp_path, "first.md", "x" * 1_048_576)
    assert any("exceeds 1 MiB" in error for error in check_vault(tmp_path))


def test_rejects_non_utf8_note(tmp_path: Path) -> None:
    (tmp_path / "first.md").write_bytes(b"\xff")
    assert any("UTF-8" in error for error in check_vault(tmp_path))


def test_rejects_missing_type(tmp_path: Path) -> None:
    (tmp_path / "first.md").write_text("---\ntitle: One\n---\n", encoding="utf-8")
    assert any("requires title and type" in error for error in check_vault(tmp_path))


def test_rejects_malformed_metadata_field(tmp_path: Path) -> None:
    (tmp_path / "first.md").write_text(
        "---\ntitle: One\ntype: concept\nbroken\n---\n", encoding="utf-8"
    )
    assert any("malformed frontmatter" in error for error in check_vault(tmp_path))


def test_checks_frontmatter_links(tmp_path: Path) -> None:
    (tmp_path / "first.md").write_text(
        '---\ntitle: One\ntype: concept\nprerequisites:\n  - "[[missing]]"\n---\n',
        encoding="utf-8",
    )
    assert any("unresolved wikilink" in error for error in check_vault(tmp_path))


def test_ignores_hidden_notes(tmp_path: Path) -> None:
    note(tmp_path, "first.md")
    note(tmp_path, ".obsidian/ignored.md", "[[missing]]")
    assert check_vault(tmp_path) == []


def test_short_fence_does_not_close_long_fence(tmp_path: Path) -> None:
    note(tmp_path, "first.md", "````python\n```\n")
    assert any("unclosed code fence" in error for error in check_vault(tmp_path))


def test_accepts_tilde_fences_and_local_anchors(tmp_path: Path) -> None:
    note(tmp_path, "first.md", "[[#Heading]]\n~~~text\n[[missing]]\n~~~\n")
    assert check_vault(tmp_path) == []


def test_rejects_fifo_without_blocking(tmp_path: Path) -> None:
    os.mkfifo(tmp_path / "pipe.md")
    completed = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check.py")), str(tmp_path)],
        capture_output=True,
        text=True,
        timeout=2,
        check=False,
    )
    assert completed.returncode == 1 and "regular file" in completed.stdout
