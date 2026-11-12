# Refine Prompt — literature notes → atoms + links

Standing instructions for a Claude Code session run from the vault root ("refine <literature note> per pipeline/refine_prompt.md"). Input: one or more literature notes in `10-Literature/` with `status: skimmed` (drafts from the Phase 2 extractor, or hand-written). This is the intelligent extraction step: it wires each paper's ideas into the graph.

---

## Task

For each target literature note, distill its distinct ideas into `20-Atoms/`, link everything, and finish the literature note. Read the actual paper content in the note (and the PDF, if `pdf:` points to one) — do not work from the title alone.

## Step 1 — Load context

1. Read `90-Meta/Conventions.md` and the Atom Template.
2. Read the target literature note fully.
3. List `20-Atoms/` filenames and skim the atoms plausibly related to the paper (follow the tags). You must know what already exists before deciding anything is new.

## Step 2 — Decompose the paper

List the paper's distinct *ideas* — not its sections. An idea is a claim, mechanism, method, or empirical regularity that could matter to someone building signals. Typical paper yields 1–4 ideas; a methods paper may yield 1. For each idea, decide:

- **Update an existing atom** (the default). The idea refines, supports, contradicts, or extends an atom that exists. Edit that atom: add the evidence or nuance to "Practical notes" (or correct the main text if the paper overturns something), and add the paper to "Key references". If the paper *contradicts* the atom, say so explicitly in the atom — disagreement is signal, never silently overwrite.
- **Create a new atom** — only if the idea is genuinely not in the vault under any name. Before creating, search `20-Atoms/` for synonyms and adjacent concepts (e.g., "flow toxicity" vs "VPIN" vs "informed trading"). Use the Atom Template; name it as a noun phrase; set `status: seed`.
- **Skip** — the idea is peripheral to the vault's scope. Note it in the literature note's critique section instead.

## Step 3 — Wire the graph

For every touched or created atom:
- ≥2 wikilinks to other atoms, links added *in both directions* where the relationship is real (edit the other atom's "Related" line too).
- Add new atoms to the appropriate MOC(s) in `40-MOCs/` under the right subsection.
- Promote atom `status` from `seed` to `developing` once it carries evidence from ≥2 literature notes.

## Step 4 — Finish the literature note

- Fill "Atoms extracted" with wikilinks and one line each on what the paper contributed.
- Fill "Critique / open questions": what would break the result, costs/crowding considered, data limitations, and anything the sweep's search-snippet abstract got wrong once you've read the real paper.
- Set `status: extracted`.

## Step 5 — Report

Per paper: atoms updated (with what), atoms created, MOC changes, and any contradiction found between the paper and an existing atom (flag these prominently — they are the most valuable output). Suggest follow-up ingests from the paper's references if they fill an evident gap.

## Guardrails

- Never duplicate an atom under a synonym — updating beats creating.
- One idea per atom; if an update would make an atom about two things, split it and fix all inbound links.
- Keep atoms compact (~30–50 lines); push detail into the literature note.
- Preserve the vault's voice: idea → mechanism → practical notes → related → references.

---

## Notes for the operator

After a refine batch, run the recombine pass (`pipeline/recombine_prompt.md`) — new atoms create new adjacencies — and the vault checker (`pipeline/check_vault.py`).
