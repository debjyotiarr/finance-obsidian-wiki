# Recombine Prompt — mining the atom graph for signal candidates

Standing instructions for a Claude Code session run from the vault root ("run the recombine pass per pipeline/recombine_prompt.md"). This is the step that produces *new* ideas: it reads only the vault and writes only to `30-Signals/`.

---

## Task

Review the atom graph in `20-Atoms/` and draft new signal candidates in `30-Signals/` from combinations of atoms. Do not modify atoms, literature notes, or MOCs (one exception in Step 4).

## Step 1 — Load the graph

1. Read `90-Meta/Conventions.md` and the Signal Candidate Template.
2. Read every note in `20-Atoms/` (they are short). Build a mental map: for each atom, its domain, its outgoing links, and its "Practical notes" caveats — the caveats are where conditioning ideas hide.
3. Read existing `30-Signals/` notes to avoid duplicating a candidate that already exists under another name.

## Step 2 — Hunt in four patterns

Look for combinations in this order of fruitfulness:

1. **Conditioning** ("X works when Y"): one atom is a return predictor, another describes a regime, flow state, or participant constraint that should modulate it. The caveat sentences inside atoms often state these outright. *Example in vault: gamma regime conditioning intraday momentum.*
2. **Gating / veto** ("don't take X when Y"): a risk or toxicity measure that identifies when a harvesting strategy's losses occur. *Example: option-flow gate on short-term reversal.*
3. **Shared mechanism, unlinked atoms**: two atoms citing the same economic mechanism (dealer hedging, index flows, queue dynamics) that no note yet connects. Check atoms sharing frontmatter tags but never linking to each other.
4. **Predictable-flow collision**: two independently forecastable flows hitting the same instrument at the same time (auction flows, ETF rebalances, option expiry, roll periods) — the overlap and the *surprise vs predicted* component are both candidates.

Prefer combinations where the two atoms come from *different domains* (frontmatter `domain`) — same-domain pairs are usually already in the literature.

## Step 3 — Qualify before writing

A candidate earns a note only if you can state all four:
- **Mechanism**: why the combination has edge and who loses to it.
- **Measurability**: every input is computable from obtainable data (name the dataset).
- **Horizon and capacity class**: seconds (HFT infrastructure required) vs intraday vs days; rough capacity logic via [[Square-Root Law of Market Impact]].
- **Falsifiability**: a kill criterion that would make you drop it.

If a combination is interesting but fails one of these, add it as a bullet to the relevant atom's "Practical notes" instead of creating a half-baked signal note — that is the only write outside `30-Signals/` this pass may make.

## Step 4 — Write the candidates

Use `90-Meta/templates/Signal Candidate Template.md` in full: hypothesis, construction, economics, validation plan (labels, sample, **declared trials budget** per [[Backtest Overfitting and Deflated Sharpe]], kill criteria), status log. Set `status: idea`, list constituent atoms in frontmatter `atoms:`, and link the atoms in the body. 2–5 candidates per pass; quality over count.

## Step 5 — Report

Summarize: candidates created (name, one-line hypothesis, horizon), near-misses parked as atom bullets, and any *pairs of atoms that should be linked but aren't* (hand these to the maintenance pass; do not edit atoms to add links yourself beyond Step 3's provision).

---

## Notes for the operator

- Run this after each batch of literature is refined into atoms — fresh atoms create fresh adjacencies.
- Periodically prune `30-Signals/`: an `idea` untouched for months either gets a research slot or gets `status: retired` with a one-line reason. A graveyard with reasons is itself useful.
