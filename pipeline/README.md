# Pipeline

Ingestion tooling. Not yet implemented — see `PLAN.md` at the repo root for the phased roadmap.

Contents:

- `sweep_prompt.md` — standing instructions for the agentic paper-discovery pass (Phase 1).
- `daily_sweep.py` — the daily sweep as a plain script: arXiv API → loose keyword filter → stubs with verbatim abstracts in `00-Inbox/` → rows in the sweep log (idea column left as — for a later review). Run every morning by `.github/workflows/daily-sweep.yml` on the `inbox-sweeps` branch.
- `build_inbox_index.py` — rebuilds `00-Inbox/Inbox Index.md`, one sortable table of every stub awaiting review.
- `daily_sweep_prompt.md` (agent version, now a fallback for sites the script cannot reach) — loose-filter variant run by the daily scheduled sweep (~8 am IST); stages stubs to `00-Inbox/`, logs to `90-Meta/Sweep Log.md`, pushes to the `inbox-sweeps` branch.
- `import_catalogue.py` — imports a papers.csv catalogue (baobach/hft_papers format) as keyword-triaged inbox stubs in `00-Inbox/baobach-catalogue/`; re-runnable, skips already-staged papers.
- `fetch_arxiv.py` — for every arXiv stub in `00-Inbox/` (recursively): writes the verbatim abstract into the stub and downloads the PDF to `00-Inbox/papers/`. Re-runnable; 3 s between requests.
- `install_hooks.sh` — one-time local setup (`sh pipeline/install_hooks.sh`): after every `git pull`, PDFs for new arXiv stubs download in the background.
- `refine_prompt.md` — Claude Code instructions: literature note → atoms + links (Phase 3).
- `recombine_prompt.md` — Claude Code instructions: atom graph → signal candidates (Phase 4).
- `check_vault.py` — integrity checker: broken wikilinks, orphan/under-linked atoms, atoms missing from MOCs, missing frontmatter. Run `python3 pipeline/check_vault.py` from the vault root after every refine/recombine pass.

Planned:

- `extract.py` + `requirements.txt` — python extractor: hand-picked inbox PDF → draft literature note (Phase 2). Blocked on arxiv.org network access (or locally supplied PDFs).
