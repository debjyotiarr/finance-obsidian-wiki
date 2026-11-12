#!/usr/bin/env python3
"""Vault integrity checker. Run from the vault root: python3 pipeline/check_vault.py

Checks:
  1. Broken wikilinks (target note does not exist)
  2. Orphan atoms (no inbound links from any other note)
  3. Atoms missing from every MOC
  4. Atoms with fewer than 2 outgoing atom links (Conventions: >=2)
  5. Notes missing a `type:` frontmatter key

Exit code 0 if clean, 1 if any check fails. Templates and inbox are exempt
from link rules; template placeholders ([[...]], [[Atom Name]]) are ignored.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDERS = {"...", "Atom Name"}
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")

EXEMPT_DIRS = {"90-Meta", "00-Inbox"}  # templates/placeholders; unreviewed stubs


def main() -> int:
    notes = {p.stem: p for p in ROOT.rglob("*.md") if ".obsidian" not in p.parts}
    atoms = {p.stem: p for p in (ROOT / "20-Atoms").glob("*.md")}
    mocs = list((ROOT / "40-MOCs").glob("*.md"))

    outlinks: dict[str, set[str]] = {}
    inbound: dict[str, set[str]] = {stem: set() for stem in notes}
    problems: list[str] = []

    for stem, path in notes.items():
        text = path.read_text(encoding="utf-8")
        targets = {t.strip() for t in WIKILINK.findall(text)} - PLACEHOLDERS
        outlinks[stem] = targets
        rel = path.relative_to(ROOT)
        exempt = rel.parts[0] in EXEMPT_DIRS
        for t in targets:
            if t in notes:
                inbound[t].add(stem)
            elif not exempt:
                problems.append(f"broken link: [[{t}]] in {rel}")

    moc_targets: set[str] = set()
    for m in mocs:
        moc_targets |= outlinks.get(m.stem, set())

    for stem, path in sorted(atoms.items()):
        rel = path.relative_to(ROOT)
        if not inbound[stem]:
            problems.append(f"orphan atom (no inbound links): {rel}")
        if stem not in moc_targets:
            problems.append(f"atom in no MOC: {rel}")
        atom_links = {t for t in outlinks[stem] if t in atoms}
        if len(atom_links) < 2:
            problems.append(
                f"under-linked atom ({len(atom_links)} atom links, need >=2): {rel}"
            )

    for stem, path in sorted(notes.items()):
        rel = path.relative_to(ROOT)
        if rel.name == "README.md" or rel.parts[0] in {"pipeline"} or rel.name in {"PLAN.md"}:
            continue
        head = path.read_text(encoding="utf-8").split("\n", 12)[:12]
        if head and head[0].strip() == "---" and not any(
            line.startswith("type:") for line in head
        ):
            problems.append(f"frontmatter missing `type:`: {rel}")

    if problems:
        print(f"FAIL — {len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"OK — {len(notes)} notes, {len(atoms)} atoms, {len(mocs)} MOCs; all checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
