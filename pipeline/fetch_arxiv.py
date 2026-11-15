#!/usr/bin/env python3
"""Fetch verbatim abstracts and PDFs for arXiv papers staged in 00-Inbox/.

Usage (from the vault root):
    python3 -I pipeline/fetch_arxiv.py [--limit N] [--dry-run] [--no-pdf] [--redo-abstracts]

For every inbox stub (recursively) whose `url:` is an arxiv.org link, this
  1. downloads the abstract page and replaces the stub's "## Abstract" section
     with the verbatim abstract (heading marked as verbatim, so stubs that were
     built from search snippets are corrected), and
  2. downloads the PDF to 00-Inbox/papers/<stub-name>.pdf (checked for the
     %PDF magic bytes) and sets `pdf:` in the stub's frontmatter.

Stubs that already have both are skipped, so it is safe to re-run. Requests are
spaced 3 s apart per arXiv's access guidelines. Only arxiv.org is contacted; no
paywalled or login-protected sources are touched. Fetched content is treated as
data: only regex extraction, never executed.
"""
import html
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "00-Inbox"
PDFS = INBOX / "papers"
DELAY = 3.0
UA = "finance-obsidian-wiki-sweeper/1.0 (personal research vault; polite 1 req/3s)"
MAX_PDF = 40 * 1024 * 1024

_last = 0.0


def get(url: str, limit: int) -> bytes:
    global _last
    wait = DELAY - (time.time() - _last)
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read(limit + 1)
    finally:
        _last = time.time()
    if len(data) > limit:
        raise ValueError("response too large")
    return data


def arxiv_id(url: str) -> str | None:
    m = re.search(r"arxiv\.org/(?:abs|pdf)/([a-z\-]+/\d{7}|\d{4}\.\d{4,5})", url)
    return m.group(1) if m else None


def parse_abstract(page: str) -> str | None:
    m = re.search(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>', page, re.S)
    if not m:
        return None
    t = re.sub(r"<span class=\"descriptor\">.*?</span>", "", m.group(1), flags=re.S)
    t = re.sub(r"<[^>]+>", "", t)
    return " ".join(html.unescape(t).split()) or None


def main() -> int:
    dry = "--dry-run" in sys.argv
    want_pdf = "--no-pdf" not in sys.argv
    redo = "--redo-abstracts" in sys.argv
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    if not dry:
        PDFS.mkdir(parents=True, exist_ok=True)

    done = failed = skipped = 0
    for stub in sorted(INBOX.rglob("*.md")):
        text = stub.read_text(encoding="utf-8")
        m = re.search(r"^url:\s*(\S+)", text, re.M)
        aid = arxiv_id(m.group(1)) if m else None
        if not aid or not re.search(r"^status:\s*inbox", text, re.M):
            continue
        pdf_path = PDFS / (stub.stem + ".pdf")
        has_pdf = bool(re.search(r"^pdf:\s*\S", text, re.M)) and pdf_path.exists()
        has_abs = "(verbatim from arXiv)" in text and not redo
        if has_abs and (has_pdf or not want_pdf):
            skipped += 1
            continue
        if limit is not None and done + failed >= limit:
            break
        print(f"{aid}  {stub.name}", flush=True)
        if dry:
            done += 1
            continue
        try:
            if not has_abs:
                page = get(f"https://arxiv.org/abs/{aid}", 2_000_000).decode("utf-8", "replace")
                abstract = parse_abstract(page)
                if not abstract:
                    raise ValueError("abstract not found on page")
                section = f"## Abstract (verbatim from arXiv)\n{abstract}\n\n"
                repl = section.rstrip("\n") + "\n"
                new, n = re.subn(r"## Abstract.*?(?=\n## |\Z)", lambda _m: repl, text, count=1, flags=re.S)
                if n == 0:
                    raise ValueError("no Abstract section in stub")
                text = new
            if want_pdf and not has_pdf:
                pdf = get(f"https://arxiv.org/pdf/{aid}", MAX_PDF)
                if not pdf.startswith(b"%PDF"):
                    raise ValueError("response is not a PDF")
                pdf_path.write_bytes(pdf)
                rel = pdf_path.relative_to(ROOT).as_posix()
                text = re.sub(r"^pdf:.*$", f"pdf: {rel}", text, count=1, flags=re.M)
            stub.write_text(text, encoding="utf-8")
            done += 1
        except Exception as e:  # keep going; report at the end
            failed += 1
            print(f"  FAILED: {e}", flush=True)

    print(f"{'DRY RUN: ' if dry else ''}processed {done}, failed {failed}, already complete {skipped}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
