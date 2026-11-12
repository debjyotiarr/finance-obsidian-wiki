---
type: source
tags: [sources, ingestion]
created: 2026-11-03
---

# Paper Sources

Where the agentic sweep looks. Add/remove sources here: **the daily scheduled sweep reads this file fresh every run**, so editing this list (on the `inbox-sweeps` branch, or merged into it) is how you change which sites are checked.

## Preprints (primary sweep targets)
- **arXiv q-fin.TR** (Trading and Market Microstructure) — https://arxiv.org/list/q-fin.TR/recent — highest signal-to-noise for this vault.
- **arXiv q-fin.ST / q-fin.CP** — statistical finance, computational finance.
- **SSRN FEN** — Financial Economics Network; microstructure and derivatives eJournals. Search, don't browse.

## Journals to track (via new-issue alerts)
- Journal of Financial Economics, Journal of Finance, Review of Financial Studies (big results surface here late — preprints first).
- Journal of Financial Markets, Market Microstructure and Liquidity (specialist).
- Quantitative Finance, Journal of Financial Econometrics (methods).

## Practitioner / gray literature
- BIS, FCA, SEC/CFTC working papers (market-structure data access nobody else has — e.g., Aquilina-Budish-O'Neill races paper).
- CFM, AQR, Man Group research portals (practitioner-grade, cost-aware).
- Lopez de Prado's SSRN page; Bouchaud/CFM arXiv output.

## Curation rule
The sweep collects candidates into `00-Inbox/`; a human (you) hand-picks what proceeds to extraction. Do not auto-extract unreviewed papers.
