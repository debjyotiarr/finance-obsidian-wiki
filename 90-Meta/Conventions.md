---
type: meta
tags: [meta, conventions]
created: 2026-11-03
---

# Vault Conventions

## Note types (frontmatter `type`)
- `atom` — one idea per note, in `20-Atoms/`. Named as a noun phrase ("Order Flow Imbalance"), not a sentence.
- `literature` — one paper per note, in `10-Literature/`. Named `Author Year - Short Title`.
- `signal` — one signal candidate per note, in `30-Signals/`.
- `moc` — hub notes in `40-MOCs/`.
- `source` — websites/feeds/datasets in `50-Sources/`.

## Status lifecycle
- Atoms: `seed` (stub from initial import or extraction) → `developing` (has evidence from 2+ literature notes) → `mature` (stable, well-linked).
- Literature: `unread` → `skimmed` → `extracted` (all atoms pulled out, safe to archive).
- Signals: `idea` → `researching` → `backtested` → `live` / `retired`.

## Linking rules
- Every atom links to ≥2 other atoms. An unlinked atom is a bug.
- Literature notes link *to* atoms (never the reverse except in "Key references").
- Signals list their constituent atoms in frontmatter `atoms:` for Dataview queries.

## Tags
Domains live in frontmatter `domain`; tags are cross-cutting facets (`orderflow`, `volatility`, `market-making`, `alpha`, `risk`, `machine-learning`, ...). Don't duplicate the folder structure in tags.
