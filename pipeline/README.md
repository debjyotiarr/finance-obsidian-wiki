# Pipeline

Ingestion tooling. Not yet implemented — see `PLAN.md` at the repo root for the phased roadmap.

Planned contents:

- `sweep_prompt.md` — standing instructions for the agentic paper-discovery pass (Phase 1).
- `extract.py` + `requirements.txt` — python extractor: hand-picked inbox PDF → draft literature note (Phase 2).
- `refine_prompt.md` — Claude Code instructions: literature note → atoms + links (Phase 3).
- `recombine_prompt.md` — Claude Code instructions: atom graph → signal candidates (Phase 4).
