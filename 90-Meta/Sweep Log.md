---
type: meta
tags: [meta, ingestion, log]
created: 2026-11-12
---

# Sweep Log

One entry per sweep run (manual or scheduled), newest last. The daily sweep reads the last entry to set its lookback window.

## 2026-11-03
- Lookback: ~2026-08-05 → 2026-11-03 (manual dry run, strict filter per `pipeline/sweep_prompt.md`)
- Staged: 9
- Sites: arXiv — search fallback (direct access blocked by network policy)
- Overflow / notes: 5 borderline papers skipped; see commit 8ffc52a.
