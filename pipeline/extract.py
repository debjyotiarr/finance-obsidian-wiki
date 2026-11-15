#!/usr/bin/env python3
"""Turn picked inbox papers into draft literature notes (Phase 2).

    python3 pipeline/extract.py --picked            # every stub with `status: picked`
    python3 pipeline/extract.py 00-Inbox/<stub>.md  # or name stubs explicitly
    options: --keep (leave stub and PDF in the inbox), --out DIR (write notes elsewhere),
             --force (overwrite a note that already exists)

For each paper it reads the PDF text and pulls out, with page numbers, the
sentences a trading project needs: how the idea is implemented, what data it
uses, what it says about costs, what it says about latency, and the headline
results. Maths is deliberately not extracted; the note only records how
maths-heavy the paper is. If a paper never mentions costs or latency the note
says so explicitly, because that silence matters.

This is mechanical extraction (keyword scoring, no model). The note is a draft
with `status: skimmed`; the refine pass (pipeline/refine_prompt.md) turns it
into ideas in the vault.

Needs `pip install pypdf` (or the `pdftotext` command on PATH).
PDFs are treated as untrusted data: text is only read, never executed.
"""
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "00-Inbox"
LIT = ROOT / "10-Literature"
PER_SECTION = 7

CATEGORIES = {
    "implementation": (
        r"algorithm|we implement|implementation|procedure|step \d|pseudo|features?\b|inputs?\b|"
        r"parameters?|hyperparameter|calibrat|estimat|train(ed|ing)|architecture|window|threshold|"
        r"signal is|is defined as|we compute|we construct|we use|we define|rebalanc|"
        r"enters?|exit|buys?|sells?|long|short|position|order is|quotes? (are|is)|strategy"
    ),
    "data": (
        r"data ?set|\bdata\b|sample period|lobster|nasdaq|nyse|\bcme\b|euronext|tick|message|snapshot|"
        r"from (19|20)\d\d|between (19|20)\d\d|(19|20)\d\d\s*(-|–|to)\s*(19|20)\d\d|"
        r"stocks|futures|contracts?|options?|symbols?|trading days|frequency|level[- ]?[123]|order book data"
    ),
    "costs": (
        r"bid[- ]ask|half[- ]spread|\bspread\b|gross|liquidity cost|frictions?"
    ),
    "latency": (
        r"speed|delay|real[- ]time|queue position|throughput"
    ),
    "results": (
        r"sharpe|p&l|\bpnl\b|profit|returns? of|outperform|drawdown|accuracy|out[- ]of[- ]sample|"
        r"annuali[sz]ed|statistically significant|r-squared|r\^?2|we find|results show|improv|"
        r"hit rate|information ratio|per (trade|day|year)"
    ),
}
COMPILED = {k: re.compile(v, re.I) for k, v in CATEGORIES.items()}
# Terms that on their own prove the paper really discusses the topic.
STRONG = {
    "costs": re.compile(
        r"transaction costs?|trading costs?|execution costs?|fees?\b|rebates?|commission|slippage|"
        r"basis points?|\bbps\b|\bnet of|after costs|turnover|capacity|break[- ]even|"
        r"market impact|price impact|implementation shortfall", re.I),
    "latency": re.compile(
        r"latenc|microsecond|millisecond|nanosecond|co-?locat|tick[- ]to[- ]trade|fpga|round[- ]trip|"
        r"inference time|run ?time|computation(al)? (cost|time)|reaction time", re.I),
}
MATHS = re.compile(r"\b(theorem|lemma|proposition|corollary|proof)\b", re.I)
HEADING = re.compile(r"^\s*(\d{1,2}(?:\.\d{1,2})*)\.?\s+([A-Z][A-Za-z][A-Za-z ,:&\-/]{2,70})\s*$")


def pdf_pages(pdf: Path) -> list[str]:
    try:
        from pypdf import PdfReader  # type: ignore
        return [(p.extract_text() or "") for p in PdfReader(str(pdf)).pages]
    except ImportError:
        pass
    if shutil.which("pdftotext"):
        out = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True, check=True)
        return out.stdout.split("\f")
    raise SystemExit("Need a PDF reader: run `pip install pypdf` (or install pdftotext).")


def sentences(page: str) -> list[str]:
    text = re.sub(r"-\n(?=[a-z])", "", page)
    text = " ".join(text.split())
    out = []
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\[(])", text):
        s = s.strip()
        if not 60 <= len(s) <= 420:
            continue
        letters = sum(c.isalpha() or c.isspace() for c in s)
        if letters / len(s) < 0.78:   # equations, tables, garbage
            continue
        out.append(s)
    return out


def field(text: str, key: str) -> str:
    m = re.search(rf"^{key}:[ \t]*(.*)$", text, re.M)
    return m.group(1).strip() if m else ""


def fm_list(text: str, key: str) -> list[str]:
    """A frontmatter list, whether inline (`key: [a, b]`) or in the block style
    Obsidian rewrites it to (`key:` followed by `  - a` lines)."""
    inline = field(text, key)
    if inline:
        quoted = re.findall(r'"([^"]+)"', inline)
        return quoted or [p.strip() for p in inline.strip("[]").split(",") if p.strip()]
    m = re.search(rf"^{key}:[ \t]*\n((?:[ \t]+-[ \t]*.*\n?)+)", text, re.M)
    if not m:
        return []
    return [i.strip().strip('"\'') for i in re.findall(r"^[ \t]+-[ \t]*(.*)$", m.group(1), re.M) if i.strip()]


def inline_list(items: list[str]) -> str:
    return "[" + ", ".join(json.dumps(i, ensure_ascii=False) for i in items) + "]"


def last_names(authors: list[str]) -> list[str]:
    if len(authors) > 1 and len(authors) % 2 == 0 and all(" " not in a for a in authors):
        return authors[0::2]                      # legacy stubs: Last, First, Last, First
    return [a.split()[-1] for a in authors]


def note_name(text: str) -> str:
    names = last_names(fm_list(text, "authors")) or ["Unknown"]
    who = " ".join(names) if len(names) <= 3 else f"{names[0]} et al"
    title = field(text, "title").strip('"')
    short = " ".join(re.sub(r"[^\w\s\-]", "", title).split()[:9])
    return f"{who} {field(text, 'year')} - {short}"


def extract(stub: Path, out_dir: Path, keep: bool, force: bool = False) -> str:
    text = stub.read_text(encoding="utf-8")
    existing = out_dir / (note_name(text) + ".md")
    if existing.exists() and not force:
        return f"SKIP {stub.name}: note already exists ({existing.name}); pass --force to overwrite it"
    pdf = INBOX / "papers" / (stub.stem + ".pdf")
    if not pdf.exists():
        return f"SKIP {stub.name}: no PDF in 00-Inbox/papers/ (run pipeline/fetch_arxiv.py, or drop the PDF in under the stub's name)"
    pages = pdf_pages(pdf)

    # cut the reference list
    full = "\n".join(pages)
    cut = max(full.rfind("\nReferences"), full.rfind("\nREFERENCES"), full.rfind("\nBibliography"))
    n_body_pages = len(pages)
    if cut > len(full) * 0.5:
        acc = 0
        for i, p in enumerate(pages):
            acc += len(p) + 1
            if acc > cut:
                n_body_pages = i + 1
                pages[i] = p[: len(p) - (acc - cut)]
                break

    picked = {k: [] for k in COMPILED}
    seen = set()
    for i, page in enumerate(pages[:n_body_pages], start=1):
        for s in sentences(page):
            key = s[:80]
            if key in seen:
                continue
            if sum(ord(c) > 127 for c in s) > 4:      # leftover equation fragments
                continue
            has_digit = bool(re.search(r"\d", s))
            scores, strong = {}, {}
            for k, rx in COMPILED.items():
                weak = len(set(m.group(0).lower() for m in rx.finditer(s)))
                strong[k] = len(set(m.group(0).lower() for m in STRONG[k].finditer(s))) if k in STRONG else 0
                scores[k] = weak + 2 * strong[k]
            # costs and latency are the scarce ones: a strong term always wins
            best = max(scores, key=lambda k: (strong[k] > 0, scores[k]))
            if best in STRONG:
                if not strong[best]:
                    continue
            elif scores[best] < 2 and not (best == "results" and scores[best] == 1 and has_digit):
                continue
            seen.add(key)
            bonus = 1 if has_digit else 0
            picked[best].append((scores[best] + bonus, i, s))

    def block(k: str) -> str:
        top = sorted(picked[k], key=lambda t: -t[0])[:PER_SECTION]
        top.sort(key=lambda t: t[1])
        return "\n".join(f"- (p.{pg}) {s}" for _, pg, s in top)

    headings, last = [], ""
    for page in pages[:n_body_pages]:
        for line in page.splitlines():
            m = HEADING.match(line)
            if m and m.group(2) != last and len(headings) < 40:
                headings.append(f"{m.group(1)} {m.group(2).strip()}")
                last = m.group(2)

    maths_hits = len(MATHS.findall(full))
    per_page = maths_hits / max(1, n_body_pages)
    maths = "heavy" if per_page > 1.5 else "moderate" if per_page > 0.3 else "light"
    has_costs, has_latency = bool(picked["costs"]), bool(picked["latency"])

    abstract = re.search(r"## Abstract[^\n]*\n(.*?)(?=\n## |\Z)", text, re.S)
    why = re.search(r"## Why staged\n(.*?)(?=\n## |\Z)", text, re.S)
    name = note_name(text)
    pdf_field = field(text, "pdf")
    if not keep and out_dir == LIT:
        (LIT / "pdfs").mkdir(exist_ok=True)
        shutil.move(str(pdf), LIT / "pdfs" / (name + ".pdf"))
        pdf_field = f"10-Literature/pdfs/{name}.pdf"

    note = f"""---
type: literature
status: skimmed
title: {field(text, "title")}
authors: {inline_list(fm_list(text, "authors"))}
year: {field(text, "year")}
venue: {field(text, "venue")}
url: {field(text, "url")}
pdf: {pdf_field}
pages: {len(pages)}
maths: {maths}
costs_discussed: {"yes" if has_costs else "no"}
latency_discussed: {"yes" if has_latency else "no"}
tags: {inline_list(fm_list(text, "tags"))}
created: {dt.date.today().isoformat()}
---

# {field(text, "title").strip('"')}

> Draft produced by `pipeline/extract.py` (keyword extraction, not read by anyone yet). Quotes are verbatim from the PDF with page numbers. Maths is not extracted; this paper's maths load is **{maths}**.

## One-line summary
*To be written in the refine pass.*

## Abstract
{abstract.group(1).strip() if abstract else "*Not available.*"}

## Implementation: how it is built
{block("implementation") or "*Nothing matched. Read the method section by hand.*"}

## Data used
{block("data") or "*No data description found. Possibly a theoretical or simulation-only paper.*"}

## Costs and frictions
{block("costs") or "**No discussion of transaction costs, fees, slippage or market impact found. Treat any reported performance as gross.**"}

## Latency and infrastructure
{block("latency") or "**No discussion of latency or infrastructure found. Whether the idea survives realistic delays is untested.**"}

## Reported results
{block("results") or "*No headline results matched.*"}

## Section outline
{chr(10).join("- " + h for h in headings) or "*Headings not detected.*"}

## Implementation checklist (fill in during refine)
- Signal / decision rule in one line:
- Inputs and data granularity needed:
- Key parameters and how they are set:
- Horizon and turnover:
- Cost assumption vs. what we would actually pay:
- Latency needed for the edge to exist:
- What would break it:

## Atoms extracted
{why.group(1).strip() if why else ""}

## Critique / open questions
"""
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / (name + ".md")).write_text(note, encoding="utf-8")
    if not keep and out_dir == LIT:
        stub.unlink()
    return (f"OK   {name}.md  [{len(pages)} pp, maths {maths}, "
            f"costs {'yes' if has_costs else 'NO'}, latency {'yes' if has_latency else 'NO'}]")


def main() -> int:
    args = sys.argv[1:]
    keep = "--keep" in args
    force = "--force" in args
    out_dir = LIT
    if "--out" in args:
        out_dir = Path(args[args.index("--out") + 1]).resolve()
        args.remove(args[args.index("--out") + 1])
    stubs = [Path(a).resolve() for a in args if not a.startswith("--")]
    if "--picked" in args:
        stubs += [p for p in sorted(INBOX.rglob("*.md"))
                  if re.search(r"^status:\s*picked", p.read_text(encoding="utf-8"), re.M)]
    if not stubs:
        print(__doc__)
        return 2
    for s in stubs:
        print(extract(s, out_dir, keep, force))
    return 0


if __name__ == "__main__":
    sys.exit(main())
