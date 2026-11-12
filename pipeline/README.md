# Pipeline

Ingestion tooling. Not yet implemented — see `PLAN.md` at the repo root for the phased roadmap.

Contents:

- `sweep_prompt.md` — standing instructions for the agentic paper-discovery pass (Phase 1).
- `daily_sweep_prompt.md` — loose-filter variant run by the daily scheduled sweep (~8 am IST); stages stubs to `00-Inbox/`, logs to `90-Meta/Sweep Log.md`, pushes to the `inbox-sweeps` branch.
- `refine_prompt.md` — Claude Code instructions: literature note → atoms + links (Phase 3).
- `recombine_prompt.md` — Claude Code instructions: atom graph → signal candidates (Phase 4).
- `check_vault.py` — integrity checker: broken wikilinks, orphan/under-linked atoms, atoms missing from MOCs, missing frontmatter. Run `python3 pipeline/check_vault.py` from the vault root after every refine/recombine pass.

Planned:

- `extract.py` + `requirements.txt` — python extractor: hand-picked inbox PDF → draft literature note (Phase 2). Blocked on arxiv.org network access (or locally supplied PDFs).
