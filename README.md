# Finance Obsidian Wiki

An Obsidian vault for connecting ideas in HFT and mid-frequency quantitative trading (equities, futures, options). Every markdown file is one idea; wikilinks between ideas are where new signals come from. Public research is ingested through a pipeline, distilled into atomic notes, and recombined into signal candidates.

Open this repository as a vault in Obsidian (File → Open folder as vault). Start at `40-MOCs/Home.md`.

## Folder structure

```
00-Inbox/        Landing zone for the ingestion pipeline. Untrusted, unlinked.
  papers/        Fetched PDFs.
10-Literature/   One note per paper (source of ideas). Named "Author Year - Title".
20-Atoms/        THE CORE. One atomic idea per note, densely wikilinked.
30-Signals/      Signal candidates: combinations of atoms promoted to testable hypotheses.
40-MOCs/         Maps of Content — hub notes that index the atoms by theme. Start at Home.
50-Sources/      Where papers come from: sites, journals, feeds.
90-Meta/         Conventions and note templates.
pipeline/        Ingestion tooling (sweep prompts + python extractor). See PLAN.md.
```

The numbering orders folders by pipeline stage: raw (00) → per-paper (10) → per-idea (20) → per-signal (30), with navigation (40) and reference (50, 90) behind.

## How information flows

1. **Sweep** — an agentic pass over the sources in `50-Sources/Paper Sources.md` finds candidate papers and writes a metadata stub + PDF into `00-Inbox/`.
2. **Review** — you hand-pick which inbox papers are worth extracting. Delete the rest. Nothing is auto-trusted.
3. **Extract** — the python extractor (`pipeline/`) turns a chosen PDF into a draft literature note in `10-Literature/` using the template.
4. **Refine and link** — a Claude Code pass reads the draft, pulls each distinct idea into `20-Atoms/` (updating existing atoms rather than duplicating), links it into the graph, and updates the relevant MOC.
5. **Recombine** — periodically review the atom graph for adjacent-but-unlinked ideas; promising combinations become notes in `30-Signals/` via the signal template. These brief actual backtests.

## Where to look

- **"What does the vault know about X?"** → the MOC for that theme in `40-MOCs/`, then follow links.
- **"Where did this claim come from?"** → the atom's *Key references* section → the literature note in `10-Literature/`.
- **"What should I read next?"** → `00-Inbox/` (pending review) and any atom with `status: seed` (needs development).
- **"What are the rules?"** → `90-Meta/Conventions.md` (note types, status lifecycle, linking rules, tags).
- **"What's left to build?"** → `PLAN.md`.

## Note anatomy

Atoms carry frontmatter (`type`, `status`, `domain`, `assets`, `tags`) for Dataview/graph filtering, then: the **idea** in one paragraph, the **mechanism** (why it persists), **practical notes** (measurement, pitfalls, regime-dependence), **related** links, and **key references**. One idea per note — if a note needs two ideas, split it.

The seed content is 38 atoms spanning market microstructure (order flow, market making, market structure), execution (impact, scheduling, TCA), mid-frequency signals (intraday patterns, reversal, stat arb, carry), options (flow, gamma, vol surface, VRP), and research methodology (labeling, overfitting, signal decay).

## Recommended Obsidian setup

- Core plugins: Graph view (color groups by `type` or folder), Backlinks, Templates (folder: `90-Meta/templates`).
- Community plugins (optional): **Dataview** — the frontmatter schema is designed for it (e.g., list all `status: seed` atoms, or all signals touching a given atom); **Templater** for the `{{date}}` fields.
- `.obsidian/` is gitignored except nothing — the vault config is local; commit it later if you want synced settings.
