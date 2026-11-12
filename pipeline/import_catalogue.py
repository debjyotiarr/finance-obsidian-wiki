#!/usr/bin/env python3
"""Import a papers.csv catalogue (baobach/hft_papers format) as inbox stubs.

Usage (run from the vault root):
    python3 -I pipeline/import_catalogue.py <path/to/papers.csv> [--dry-run]

The catalogue is a scraped list of titles/authors/links (no abstracts, no
paper text), so stubs are keyword-triaged and labelled as unreviewed. Only
rows matching core trading/microstructure terms (and not obviously off-scope
topics) become stubs, written to 00-Inbox/baobach-catalogue/. Rows already
staged (same arXiv id/DOI/normalised title in 00-Inbox/ or 10-Literature/)
are skipped. Re-runnable: existing stub files are never overwritten.
"""
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "00-Inbox" / "baobach-catalogue"

STRONG = re.compile(
    r"limit order|order book|order flow|market making|market maker|microstructure|"
    r"market impact|price impact|optimal execution|high[- ]frequency|bid[- ]ask|queue|"
    r"latency|adverse selection|hawkes|statistical arbitrage|pairs trading|lead[- ]lag|"
    r"dealer|gamma|implied vol|tick size|auction|slippage|transaction cost|intraday",
    re.I,
)
NOISE = re.compile(
    r"blockchain|cryptocurr|bitcoin|crypto|sentiment|twitter|behavio|herding|survey|"
    r"bibliometric|literacy|retail investor|india|karnataka|forex|esg|bank|fintech|"
    r"chatgpt|llm|large language|kenya|nigeria|pakistan|indonesia",
    re.I,
)
HIGH_TITLE = re.compile(
    r"limit order|order book|order flow|market making|market maker|microstructure|"
    r"market impact|price impact|optimal execution|hawkes|queue|adverse selection|"
    r"latency|bid[- ]ask|tick size|lead[- ]lag",
    re.I,
)

# keyword -> (atom wikilink, tag)
ATOMS = [
    (r"order flow|flow imbalance", "[[Order Flow Imbalance]]", "orderflow"),
    (r"limit order|order book", "[[Limit Order Book Shape as Signal]]", "orderbook"),
    (r"market making|market maker", "[[Market Maker Inventory Control]]", "market-making"),
    (r"adverse selection", "[[Adverse Selection]]", "market-making"),
    (r"queue", "[[Queue Position Value]]", "orderbook"),
    (r"hawkes", "[[Hawkes Processes for Order Flow]]", "point-process"),
    (r"market impact|price impact|slippage", "[[Square-Root Law of Market Impact]]", "impact"),
    (r"optimal execution|execution", "[[Optimal Execution (Almgren-Chriss)]]", "execution"),
    (r"transaction cost", "[[Implementation Shortfall]]", "execution"),
    (r"latency", "[[Latency Arbitrage]]", "hft"),
    (r"lead[- ]lag", "[[Futures-ETF Lead-Lag]]", "lead-lag"),
    (r"pairs trading|statistical arbitrage", "[[Pairs Trading and Statistical Arbitrage]]", "stat-arb"),
    (r"intraday", "[[Intraday Momentum]]", "intraday"),
    (r"gamma|dealer", "[[Gamma Exposure and Dealer Hedging]]", "options"),
    (r"implied vol", "[[Implied Volatility Surface Dynamics]]", "options"),
    (r"auction", "[[Opening and Closing Auctions]]", "auctions"),
    (r"tick size", "[[Tick Size Constraints]]", "market-structure"),
    (r"bid[- ]ask", "[[Bid-Ask Spread Decomposition]]", "microstructure"),
    (r"microstructure", "[[Microstructure Noise and Price Discovery]]", "microstructure"),
]


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def slug(s: str, n: int = 6) -> str:
    return "-".join(re.findall(r"[A-Za-z0-9]+", s)[:n]) or "paper"


def q(s: str) -> str:
    return json.dumps(" ".join(s.split()), ensure_ascii=False)


def venue_of(source_label: str, link: str) -> str:
    m = re.search(r"\[([a-z]+)[-_]", source_label)
    kind = m.group(1) if m else ""
    if kind == "arxiv":
        return "arXiv " + link.rsplit("/", 1)[-1]
    if kind == "doi":
        return "DOI " + link.replace("https://doi.org/", "")
    return (kind or "unknown").upper() + (" (conference)" if kind not in ("pubmed",) else "")


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not args:
        print(__doc__)
        return 2
    rows = list(csv.DictReader(open(args[0], encoding="utf-8")))

    seen_ids, seen_titles = set(), set()
    for d in (ROOT / "00-Inbox", ROOT / "10-Literature"):
        for p in d.rglob("*.md"):
            t = p.read_text(encoding="utf-8")
            seen_ids |= set(re.findall(r"\d{4}\.\d{4,5}|10\.\d{4,9}/\S+", t))
            m = re.search(r'^title: "?(.+?)"?$', t, re.M)
            if m:
                seen_titles.add(norm(m.group(1)))
            seen_titles.add(norm(p.stem))

    counts = {"high": 0, "medium": 0, "low": 0}
    skipped_dup = 0
    if not dry:
        OUT.mkdir(parents=True, exist_ok=True)

    for r in rows:
        title = r["Paper"].strip()
        desc = (r.get("Description") or "").strip()
        text = title + " " + desc
        if not STRONG.search(text) or NOISE.search(title):
            continue
        link = r["Source Link"].strip()
        ident = link.rsplit("arxiv.org/abs/", 1)[-1] if "arxiv.org" in link else link.replace("https://doi.org/", "")
        if ident in seen_ids or norm(title) in seen_titles:
            skipped_dup += 1
            continue

        is_arxiv = "arxiv.org" in link
        rel = "high" if HIGH_TITLE.search(title) else ("medium" if is_arxiv or STRONG.search(title) else "low")
        counts[rel] += 1

        authors = [a.strip() for a in r["Author(s)"].split(";") if a.strip()]
        first = (authors[0].split()[-1] if authors else "Unknown")
        year = r["Date"][:4]
        h = hashlib.sha1(link.encode()).hexdigest()[:6]
        fname = f"{slug(first,1)}{year}-{slug(title)}-{h}.md"

        matched = [(wl, tag) for pat, wl, tag in ATOMS if re.search(pat, text, re.I)]
        links = ", ".join(dict.fromkeys(wl for wl, _ in matched)) or "no obvious atom match"
        tags = sorted({t for _, t in matched} | ({"arxiv"} if is_arxiv else set()))

        body = f"""---
type: literature
status: inbox
title: {q(title)}
authors: [{", ".join(q(a) for a in authors)}]
year: {year}
venue: {q(venue_of(r["Source"], link))}
url: {link}
pdf_url:
pdf:
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: {rel}
tags: [{", ".join(tags)}]
---

# {" ".join(title.split())}

## Abstract
*Not available — the source catalogue has no abstracts. Fetch from the URL above before extracting.*
{("Catalogue description: " + " ".join(desc.split())) if desc else ""}

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: {links}.
"""
        if not dry:
            path = OUT / fname
            if not path.exists():
                path.write_text(body, encoding="utf-8")

    total = sum(counts.values())
    print(f"{'DRY RUN: ' if dry else ''}staged {total} (high {counts['high']}, medium {counts['medium']}, "
          f"low {counts['low']}); skipped {skipped_dup} duplicates; {len(rows)} catalogue rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
