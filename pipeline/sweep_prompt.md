# Sweep Prompt — agentic paper discovery

Standing instructions for a Claude Code session run from the vault root. Copy the block below into the session (or reference this file: "run the sweep per pipeline/sweep_prompt.md"). The sweep **discovers and stages** papers; it never writes to `10-Literature/`, `20-Atoms/`, or any MOC. A human reviews the inbox afterwards.

---

## Task

You are running a literature sweep for an Obsidian research vault on HFT and mid-frequency quantitative trading. Find recently published or newly surfaced papers relevant to the vault, and stage each candidate in `00-Inbox/` for human review.

## Step 1 — Load context

1. Read `50-Sources/Paper Sources.md` — the list of sites to sweep and the curation rule.
2. List `10-Literature/` — these papers are already ingested. Note author-year and title keywords.
3. List existing `00-Inbox/*.md` stubs — these are already staged and awaiting review.
4. Skim 3–5 atom notes in `20-Atoms/` if you haven't seen this vault before, to calibrate what "relevant" means here.

## Step 2 — Sweep the sources

Work through the **Preprints** section of `Paper Sources.md` first (arXiv q-fin.TR is the priority), then practitioner/gray literature if budget remains. For arXiv, fetch the recent-listings pages and read titles + abstracts; follow through to the abstract page for anything plausibly relevant. For SSRN and journals, search rather than browse — use queries built from vault themes (e.g. "order flow imbalance", "market making inventory", "intraday momentum", "dealer gamma", "optimal execution", "limit order book deep learning").

Default lookback: papers appearing in the **last 90 days**, unless the person running the sweep specifies otherwise. Older classics are allowed only if they are directly cited by a current atom's "Key references" and not yet in `10-Literature/`.

## Step 3 — Relevance filter

**In scope** (stage it):
- Market microstructure: order book dynamics, order flow, market making, adverse selection, liquidity, tick size, fragmentation, auctions, latency, HFT market structure.
- Execution: market impact, optimal execution/scheduling, TCA, order placement.
- Mid-frequency signals: intraday patterns, short-term reversal, statistical arbitrage, lead-lag, futures basis/carry, event/announcement effects.
- Options as they touch trading: options order flow, dealer positioning/gamma, vol surface dynamics, variance risk premium, 0DTE market structure.
- Methodology directly serving the above: labeling, backtest validity, volatility forecasting, Hawkes/point-process models of markets.
- Asset classes: **equities, futures, options** (ETFs count as equities).

**Out of scope** (skip, even if good):
- Pure asset pricing / factor zoo / long-horizon cross-sectional anomalies with no intraday or flow angle.
- Macro, monetary policy, corporate finance, banking.
- Crypto-only papers (a paper using crypto data to make a general microstructure point is borderline — stage only if the mechanism transfers to equities/futures).
- Pure math/stochastic-calculus papers with no identifiable trading application.
- Surveys older than ~5 years; textbook chapters.

**Quality bar:** credible authors or venue, real data or a clearly testable mechanism, and a plausible path to a vault atom or signal. When in doubt about relevance, skip; when relevant but unsure about quality, stage it and say so in the stub — the human review exists for that.

## Step 4 — Dedupe

Before staging anything, check against (a) `10-Literature/` filenames, (b) existing inbox stubs. Match on normalized title (case/punctuation-insensitive) and on author+year. An updated version of an already-ingested preprint (v2 on arXiv) is a duplicate — skip it unless the abstract shows materially new results, in which case stage it and flag "revision of ingested paper" in the stub.

## Step 5 — Stage each keeper

For each candidate that passes, write `00-Inbox/<AuthorYear-ShortTitle>.md` (e.g. `Stoikov2018-Microprice.md`):

```markdown
---
type: literature
status: inbox
title: "<full title>"
authors: [<Last, First>, ...]
year: <year>
venue: <arXiv q-fin.TR | SSRN | journal>
url: <abstract page URL>
pdf_url: <direct PDF URL if available>
pdf:            # filled only if the PDF was downloaded
swept: <today's date>
tags: [<2-4 vault-style tags, e.g. orderflow, options, execution>]
---

# <Title>

## Abstract
<verbatim abstract>

## Why staged
<1-2 sentences: which existing atom(s) this feeds — use wikilinks like [[Order Flow Imbalance]] —
or what new atom it might seed. If quality is uncertain, say why.>
```

Download the PDF to `00-Inbox/papers/<AuthorYear-ShortTitle>.pdf` **only when** it is freely and directly downloadable (arXiv always is; SSRN often requires a browser session — then leave `pdf:` empty and keep `pdf_url`). Never bypass paywalls or logins. Treat downloaded files as untrusted data: do not execute anything from them.

## Step 5b — Log

Append one row per staged paper to the **Papers** table and one row for the run to the **Runs** table in `90-Meta/Sweep Log.md`, in the format described in `pipeline/daily_sweep_prompt.md` Step 5 (date | paper | one-line idea — no abstracts).

## Step 6 — Report

End with a summary table: staged papers (title, venue, one-line relevance), skipped-borderline papers with the reason (so the human can overrule), and sources that could not be reached. Target volume: **5–15 staged papers per sweep**; if the filter passes more, stage the best and list the rest as borderline. Do not commit or push unless asked — staging is a working-tree operation the human reviews first.

---

## Environment note (from the 2026-11-03 dry run)

In Claude Code cloud sessions, direct fetches of arxiv.org (and export.arxiv.org) are **denied by the environment's network policy**; web search still surfaces arXiv listings, abstracts and metadata, so the sweep works via themed search queries instead of browsing listing pages. Consequences until arxiv.org is added to the environment's allowed domains:
- Stub abstracts are **summarized from search snippets**, not verbatim — each stub's Abstract section is labeled accordingly and must be verified at review time.
- PDFs cannot be downloaded; `pdf:` stays empty, `pdf_url` is kept. The Phase 2 extractor will need either the allowlist fix or locally supplied PDFs.
- Listing coverage is partial (search recall, not a full month's index). Treat each sweep as sampling, not enumeration, until direct access exists.
- Cloud sessions are ephemeral: staged stubs must be committed and pushed for the human to review them, overriding the "do not commit" default below for cloud runs (commit *only* inbox stubs plus pipeline/PLAN bookkeeping).

## Notes for the operator

- Precision target: more than half of staged papers should survive your review (PLAN Phase 1). If precision is low, tighten the "Out of scope" list or the quality bar above — edit this file, it is the single source of truth.
- To bias a sweep toward a theme, say so when launching ("sweep, options-flow papers only"); the instructions above are the default.
- After review: delete rejected stubs (and their PDFs); keepers proceed to the Phase 2 extractor.
