#!/usr/bin/env python3
"""Daily paper sweep, no agent needed. Run from the vault root:

    python3 -I pipeline/daily_sweep.py [--dry-run] [--days N]

1. Asks the arXiv API for recent submissions in the quantitative-finance
   categories below.
2. Keeps papers posted since the last logged run (min 3, max 14 days back)
   that pass a loose filter: everything in q-fin.TR, plus anything elsewhere
   whose title/abstract mentions trading-related terms.
3. Writes one stub per paper in 00-Inbox/ with the verbatim abstract, and
   appends rows to 90-Meta/Sweep Log.md (the idea column is left as "—" for a
   later review pass to fill in).

It does not download PDFs (use pipeline/fetch_arxiv.py locally) and does not
commit or push: the GitHub Action, or you, do that.
"""
import datetime as dt
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from import_catalogue import ATOMS, HIGH_TITLE, STRONG  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "00-Inbox"
LOG = ROOT / "90-Meta" / "Sweep Log.md"
CATEGORIES = ["q-fin.TR", "q-fin.ST", "q-fin.CP", "q-fin.MF", "q-fin.PM", "q-fin.PR", "q-fin.RM"]
CAP = 25
UA = "finance-obsidian-wiki-sweeper/1.0 (personal research vault)"
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}

LOOSE = re.compile(
    r"trading|trader|liquidity|volatil|option|futures|execution|momentum|mean[- ]reversion|"
    r"arbitrage|backtest|order|market maker|market making|hedg|intraday|high[- ]frequency|"
    r"price formation|return predict|alpha|signal",
    re.I,
)


def fetch(max_results: int = 300) -> list[dict]:
    query = " OR ".join(f"cat:{c}" for c in CATEGORIES)
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": query, "sortBy": "submittedDate", "sortOrder": "descending",
         "start": 0, "max_results": max_results}
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        root = ET.fromstring(r.read())
    out = []
    for e in root.findall("a:entry", NS):
        aid = re.sub(r"v\d+$", "", e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1])
        out.append({
            "id": aid,
            "title": " ".join(e.findtext("a:title", "", NS).split()),
            "abstract": " ".join(e.findtext("a:summary", "", NS).split()),
            "authors": [a.findtext("a:name", "", NS) for a in e.findall("a:author", NS)],
            "published": e.findtext("a:published", "", NS)[:10],
            "primary": (e.find("x:primary_category", NS).get("term")
                        if e.find("x:primary_category", NS) is not None else ""),
        })
    return out


def last_run_date() -> dt.date | None:
    runs = LOG.read_text(encoding="utf-8").split("## Runs", 1)[-1]
    dates = re.findall(r"^\| (\d{4}-\d{2}-\d{2}) \|", runs, re.M)
    return dt.date.fromisoformat(max(dates)) if dates else None


def known_ids() -> set[str]:
    ids: set[str] = set()
    for d in (INBOX, ROOT / "10-Literature", ROOT / "90-Meta"):
        for p in d.rglob("*.md"):
            ids |= set(re.findall(r"\d{4}\.\d{4,5}", p.read_text(encoding="utf-8")))
    return ids


def q(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def main() -> int:
    dry = "--dry-run" in sys.argv
    today = dt.date.today()
    if "--days" in sys.argv:
        days = int(sys.argv[sys.argv.index("--days") + 1])
    else:
        last = last_run_date()
        days = min(14, max(3, (today - last).days)) if last else 14
    since = today - dt.timedelta(days=days)

    papers = fetch()
    seen = known_ids()
    picked = []
    for p in papers:
        if p["published"] < since.isoformat() or p["id"] in seen:
            continue
        text = p["title"] + " " + p["abstract"]
        if p["primary"] != "q-fin.TR" and not LOOSE.search(text):
            continue
        if HIGH_TITLE.search(p["title"]) or (p["primary"] == "q-fin.TR" and STRONG.search(text)):
            p["rel"] = "high"
        elif p["primary"] == "q-fin.TR" or STRONG.search(text):
            p["rel"] = "medium"
        else:
            p["rel"] = "low"
        picked.append(p)

    order = {"high": 0, "medium": 1, "low": 2}
    picked.sort(key=lambda p: (order[p["rel"]], p["published"]), reverse=False)
    overflow, picked = picked[CAP:], picked[:CAP]

    rows = []
    for p in picked:
        text = p["title"] + " " + p["abstract"]
        matched = [(wl, tag) for pat, wl, tag in ATOMS if re.search(pat, text, re.I)]
        links = ", ".join(dict.fromkeys(wl for wl, _ in matched)) or "no obvious match"
        tags = sorted({t for _, t in matched})
        last_names = [a.split()[-1] for a in p["authors"]] or ["Unknown"]
        who = (last_names[0] if len(last_names) == 1 else
               " & ".join(last_names) if len(last_names) == 2 else last_names[0] + " et al.")
        slug = "-".join(re.findall(r"[A-Za-z0-9]+", p["title"])[:6])
        first = re.sub(r"[^A-Za-z]", "", last_names[0]) or "Unknown"
        name = f"{first}{p['published'][:4]}-{slug}-{p['id'].replace('.', '')}.md"
        stub = f"""---
type: literature
status: inbox
title: {q(p["title"])}
authors: [{", ".join(q(a) for a in p["authors"])}]
year: {p["published"][:4]}
venue: {q("arXiv " + p["primary"] + " (" + p["id"] + ")")}
url: https://arxiv.org/abs/{p["id"]}
pdf_url: https://arxiv.org/pdf/{p["id"]}
pdf: 00-Inbox/papers/{name[:-3]}.pdf
swept: {today.isoformat()}
posted: {p["published"]}
origin: daily sweep script
relevance: {p["rel"]}
tags: [{", ".join(tags)}]
---

# {p["title"]}

## Abstract (verbatim from arXiv)
{p["abstract"]}

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: {links}.
"""
        if not dry:
            (INBOX / name).write_text(stub, encoding="utf-8")
        title = p["title"].replace("|", "/")
        rows.append(f"| {today.isoformat()} | {who} — [{title}](https://arxiv.org/abs/{p['id']}) | — |\n")
        print(f"{p['rel']:6} {p['id']}  {p['title'][:90]}")

    n = {k: sum(1 for p in picked if p["rel"] == k) for k in order}
    note = f"Script sweep, {len(papers)} listed. Ideas not yet written."
    if overflow:
        note += " Over cap, not staged: " + ", ".join(p["id"] for p in overflow) + "."
    run_row = (f"| {today.isoformat()} | {since.isoformat()} → {today.isoformat()} | "
               f"{len(picked)} (h/m/l: {n['high']}/{n['medium']}/{n['low']}) | arXiv: direct (API) | {note} |\n")
    if not dry:
        log = LOG.read_text(encoding="utf-8")
        head, runs = log.split("\n## Runs", 1)
        LOG.write_text(head.rstrip("\n") + "\n" + "".join(rows) + "\n## Runs" + runs.rstrip("\n") + "\n" + run_row,
                       encoding="utf-8")
    print(f"{'DRY RUN: ' if dry else ''}staged {len(picked)} since {since} "
          f"(high {n['high']}, medium {n['medium']}, low {n['low']}); overflow {len(overflow)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
