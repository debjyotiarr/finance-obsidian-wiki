# Daily Sweep Prompt — loose-filter inbox population

Instructions for the **scheduled daily sweep** (runs every morning in a fresh cloud session). It is a high-recall variant of `pipeline/sweep_prompt.md`: the goal is to *populate the inbox* so a human can select later, so the filter is deliberately loose. Where this file is silent, follow `sweep_prompt.md` (stub format, dedupe rules, PDF policy).

---

## Task

Check the sites listed in `50-Sources/Paper Sources.md` for papers posted since the last sweep, stage everything plausibly relevant in `00-Inbox/`, log the run, and push.

## Step 1 — Load context

1. Read `50-Sources/Paper Sources.md`. **This list is the source of truth for which sites to check** — it will change over time; check every site it lists, in order.
2. Read the last entry of `90-Meta/Sweep Log.md` to get the previous sweep date. Lookback = since that date, minimum 3 days (covers weekends and missed runs), maximum 14 days.
3. List `10-Literature/` and `00-Inbox/` for dedupe.

## Step 2 — Sweep

For each listed site, find papers posted in the lookback window. Prefer the site's own recent-listings page; if direct fetching is blocked by the network, fall back to web search scoped to that site (e.g. queries restricted to arxiv.org with the vault's themes and the current month). Record which sites were reached directly, via search fallback, or not at all.

## Step 3 — Loose relevance filter

**Stage it if it plausibly touches any of:** market microstructure, order books, order flow, market making, liquidity, HFT, execution and market impact, intraday or short-horizon return predictability, statistical arbitrage, lead-lag, futures, options and volatility, dealer positioning, trading-oriented ML (forecasting, RL for trading, LOB simulation), or backtesting methodology.

**When in doubt, stage it.** The human review is the real filter; a false positive costs a few seconds, a miss is gone.

**Only skip:** clear duplicates; papers with no trading/markets connection at all (pure insurance maths, corporate finance, macro policy, banking regulation); and crypto papers *only* if they are purely about token economics/DeFi protocol design (crypto microstructure papers are fine to stage — tag them `crypto`).

No quality bar beyond "a real paper". Flag unfamiliar venues or authors in "Why staged" rather than skipping.

Cap: **25 stubs per run.** If more pass, stage the 25 most relevant and list the overflow titles + URLs in the log entry.

## Step 4 — Stage

Write stubs exactly as in `sweep_prompt.md` Step 5, with one addition to frontmatter: `relevance: high | medium | low` (your quick judgment, to help the human triage). Keep "Why staged" to one sentence. If the abstract came from a search snippet rather than the real page, say so in the Abstract heading.

## Step 5 — Log

Append to `90-Meta/Sweep Log.md`:

```markdown
## YYYY-MM-DD
- Lookback: <from> → <to>
- Staged: N (high: a, medium: b, low: c)
- Sites: <site> — direct | search fallback | unreachable; ...
- Overflow / notes: <titles+URLs beyond cap, anything odd>
```

Log a run even when nothing is staged.

## Step 6 — Commit and push

Commit **only** new files in `00-Inbox/` and the log update, with message `Daily sweep YYYY-MM-DD: N papers staged`, and push to the branch named in the scheduled task's instructions. Do not touch atoms, literature notes, MOCs, signals, or any other file. If the push fails due to a non-fast-forward, pull with rebase and push again; never force-push.

## Step 7 — Report

Finish with a short summary: count staged by relevance, the top 3 titles, and any site that was unreachable.
