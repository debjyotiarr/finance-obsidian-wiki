# PLAN

Implementation roadmap for the ingestion pipeline and vault growth. The vault structure and seed content (31 atoms, 3 example literature notes, 5 MOCs, templates, conventions) exist as of 2026-11-03; what follows is the remaining work, in order.

## Phase 1 — Agentic sweep (papers → `00-Inbox/`)

Goal: a repeatable agentic pass that discovers candidate papers from known sites and stages them for human review.

- [x] Write `pipeline/sweep_prompt.md`: the standing instruction for a Claude Code session. Inputs: `50-Sources/Paper Sources.md` (the site list) and the existing `10-Literature/` index (to skip already-ingested papers). Output per candidate: a stub markdown in `00-Inbox/` with frontmatter (`status: inbox`, title, authors, year, venue, url, abstract, a one-line "why this is relevant") and the PDF in `00-Inbox/papers/` when downloadable.
- [x] Define relevance criteria in the prompt: microstructure/HFT/mid-freq for equities, futures, options; skip pure asset-pricing, macro, and crypto-only papers.
- [x] Add a dedupe rule: check title similarity against `10-Literature/` and existing inbox stubs before writing.
- [x] Decide cadence: on-demand first; later a scheduled session (weekly arXiv q-fin.TR sweep). *Decided 2026-11-12: daily scheduled sweep at ~8 am IST with a loose filter (`pipeline/daily_sweep_prompt.md`), pushing stubs to the `inbox-sweeps` branch; runs logged in `90-Meta/Sweep Log.md`.*
- [x] Dry-run on arXiv q-fin.TR recent listings; tune the relevance filter until precision is acceptable (target: >half of staged papers survive human review). *Done 2026-11-03: 9 papers staged in `00-Inbox/` via themed web searches. Finding: cloud environment's network policy blocks arxiv.org directly, so abstracts are search-snippet summaries and PDFs could not be downloaded — see the environment note in `pipeline/sweep_prompt.md`. Precision to be measured at first human review.*
- [ ] Add `arxiv.org` (and `export.arxiv.org`) to the cloud environment's allowed network domains so future sweeps get verbatim abstracts and PDFs.

## Phase 2 — Python extractor (hand-picked PDFs → draft literature notes)

Goal: deterministic script that converts a reviewed inbox paper into a draft literature note. Papers are **hand-chosen**; the script does mechanical extraction only.

- [ ] `pipeline/extract.py`: input = inbox stub + PDF; output = `10-Literature/Author Year - Short Title.md` prefilled from the Literature Note Template (metadata from the stub, abstract, section headings, and extracted key sentences; `status: skimmed`).
- [ ] PDF text layer: pypdf/pdfplumber first; add OCR fallback later only if needed.
- [ ] Carry a `pdf:` frontmatter link to the archived PDF; move the PDF from inbox to a `10-Literature/pdfs/` folder (or leave in inbox/papers — decide and document in Conventions).
- [ ] Delete the inbox stub on successful extraction.
- [ ] `pipeline/requirements.txt` + a short `pipeline/README.md` with usage.

## Phase 3 — Claude Code refinement pass (literature notes → atoms + links)

Goal: the intelligent step — distill each draft literature note into atomic ideas wired into the graph.

- [x] Write `pipeline/refine_prompt.md`: for a given literature note, (1) identify each distinct idea; (2) for each, either update an existing atom (add evidence, references, nuances — *default*) or create a new atom from the template (*only if genuinely new*); (3) add links both ways and update the relevant MOC; (4) fill the literature note's "Atoms extracted" and critique sections; (5) set literature `status: extracted`.
- [x] Guardrails in the prompt: never duplicate an atom under a synonym (search `20-Atoms/` first); every new atom gets ≥2 links; keep one idea per note.
- [ ] Process the 3 seed literature notes' references as the first real batch (Stoikov 2018 microprice, Budish et al. 2015, Tóth et al. 2011, López de Prado 2018 chapters are natural next ingests).

## Phase 4 — Recombination (atoms → `30-Signals/`)

Goal: systematically mine the graph for new signal ideas.

- [x] Write `pipeline/recombine_prompt.md`: review the atom graph for adjacent-but-unlinked atoms, atoms sharing tags but never co-cited, and conditioning opportunities ("X works better when Y"); draft signal candidates from the Signal Candidate Template with explicit economics (horizon, capacity, cost hurdle).
- [x] Seed candidates already visible: gamma regime × intraday momentum; OFI gated by VPIN; auction imbalance × leveraged-ETF rebalance flows; option-flow lead into single-stock reversal. *All four written to `30-Signals/` on 2026-11-04.*
- [x] Define the promotion checklist (mirrors `40-MOCs/Research Methodology MOC.md`): mechanism stated, labels defined, trials budget declared, cost hurdle computed — before any code is written. *Baked into recombine_prompt.md Step 3 and the signal template's validation section.*

## Phase 5 — Vault maintenance and quality

- [x] Link-integrity check (script or periodic Claude pass): no orphan atoms, no broken wikilinks, every atom in ≥1 MOC. *`pipeline/check_vault.py` — also checks the ≥2-atom-links rule and frontmatter `type:`. Run after every refine/recombine pass.*
- [ ] Promote seed atoms: each `status: seed` atom should reach `developing` by acquiring evidence from ≥2 literature notes.
- [ ] Decide on Dataview dashboards (e.g., reading queue, seed-atom list, signal pipeline board) and add them to `40-MOCs/Home.md`.
- [ ] Revisit folder structure once >100 atoms: consider domain subfolders only if navigation actually degrades (prefer flat + MOCs).

## Open decisions

- Whether to commit `.obsidian/` config for a consistent graph/plugin setup across machines.
- PDF storage policy: in-repo (simple, but repo grows) vs. gitignored local folder + URL-only references.
- Whether sweep sessions run manually or on a schedule (and where that schedule lives).
