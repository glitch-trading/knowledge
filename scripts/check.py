"""Read-only structural checks for the Markdown vault; never execute note code."""

from __future__ import annotations

import argparse
import os
import re
import stat
from pathlib import Path


def check_vault(root: Path) -> list[str]:
    """Return path-qualified errors without exposing note contents."""
    if root.is_symlink() or not root.is_dir():
        return ["vault root must be an existing directory, not a symlink"]
    files = sorted(
        path
        for path in root.rglob("*.md")
        if not any(part.startswith(".") for part in path.relative_to(root).parts)
    )
    if not files:
        return ["vault contains no Markdown notes"]
    relative_paths = {path.relative_to(root).as_posix() for path in files}
    basenames: dict[str, int] = {}
    for path in files:
        basenames[path.name] = basenames.get(path.name, 0) + 1
    errors: list[str] = []
    for path in files:
        label = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f"{label}: symlink notes are not allowed")
            continue
        try:
            descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
            with os.fdopen(descriptor, "rb") as stream:
                if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                    errors.append(f"{label}: note must be a regular file")
                    continue
                contents = stream.read(1_048_577)
            if len(contents) > 1_048_576:
                errors.append(f"{label}: note exceeds 1 MiB")
                continue
            lines = contents.decode("utf-8").splitlines()
        except (OSError, UnicodeError):
            errors.append(f"{label}: cannot read UTF-8 note")
            continue
        if not lines or lines[0] != "---":
            errors.append(f"{label}: missing frontmatter opening delimiter")
            continue
        try:
            closing = lines.index("---", 1)
        except ValueError:
            errors.append(f"{label}: unclosed frontmatter")
            continue
        keys: set[str] = set()
        for line in lines[1:closing]:
            if not line.strip() or line.startswith((" ", "#")):
                continue
            match = re.fullmatch(r"([A-Za-z][A-Za-z0-9_-]*):(?:\s.*)?", line)
            if match is None:
                errors.append(f"{label}: malformed frontmatter top-level field")
                continue
            key = match[1]
            if key in keys:
                errors.append(f"{label}: duplicate frontmatter key")
            keys.add(key)
        if not {"title", "type"} <= keys:
            errors.append(f"{label}: frontmatter requires title and type fields")
        fence = ""
        for line_number, line in enumerate(lines, start=1):
            marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if marker:
                if not fence:
                    fence = marker[1]
                elif (
                    marker[1][0] == fence[0]
                    and len(marker[1]) >= len(fence)
                    and not marker[2].strip()
                ):
                    fence = ""
                continue
            if fence:
                continue
            for raw in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", line):
                target = raw.split("#", 1)[0]
                if not target or target.startswith("{{"):
                    continue
                target = target if target.endswith(".md") else target + ".md"
                if "/" in target:
                    count = int(target in relative_paths)
                else:
                    count = basenames.get(target, 0)
                if count != 1:
                    kind = "unresolved" if count == 0 else "ambiguous"
                    errors.append(f"{label}:{line_number}: {kind} wikilink")
        if fence:
            errors.append(f"{label}: unclosed code fence")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "content",
    )
    args = parser.parse_args()
    errors = check_vault(args.root)
    for error in errors:
        print(error)
    print(f"Vault check: {len(errors)} errors")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
