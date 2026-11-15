---
type: source
tags: [sources, catalogue]
created: 2026-11-12
---

# baobach/hft_papers catalogue

**What it is.** A public GitHub list, [baobach/hft_papers](https://github.com/baobach/hft_papers) (Apache-2.0), that scrapes Paper Digest's "algorithmic trading / HFT" feed monthly: 2,302 papers dated 2019–2026 with title, authors, source link and date (1,494 have a short description). **It contains no abstracts or paper text**, so on its own it supplies candidates, not ideas.

**Quality.** Very mixed. Roughly 85% of rows are DOI links to assorted journals and many are off-topic (behavioural finance, regional studies, crypto, bibliometrics). Only 234 are arXiv papers.

**What was imported (2026-11-12).**
- Full copy: `catalogues/baobach-hft-papers.csv` (snapshot of upstream commit `c0ae9a0`; licence copied alongside). Use it to re-triage or to search older papers.
- 352 keyword-matched rows staged as inbox stubs in `00-Inbox/baobach-catalogue/` (58 high, 261 medium, 33 low relevance). Triage was by keyword, not by reading, so treat `relevance:` as a rough sort key. The other ~1,950 rows were left in the CSV on purpose.
- Importer: `pipeline/import_catalogue.py` (re-runnable; skips papers already staged or ingested). Re-run it on a fresh copy of the upstream CSV when the repo updates monthly.

**Next steps for these stubs.** Review by relevance (high first); fetch abstracts (arXiv works directly now) before the extractor runs; delete rejects.

**Abstracts and PDFs (2026-11-15).** The 54 arXiv stubs now carry verbatim abstracts; their PDFs go in `00-Inbox/papers/`, which is not committed (run `python3 -I pipeline/fetch_arxiv.py` locally to download them). The other 298 stubs (288 DOI journal links, 6 PubMed, 4 conference pages) have neither: those hosts are not reachable from the cloud environment and many are paywalled, so their PDFs must be added by hand.
