---
type: literature
status: unread   # unread | skimmed | extracted
title:
authors: []
year:
venue:           # arXiv | SSRN | journal name
url:
pdf:             # 10-Literature/pdfs/<same name>.pdf (not committed)
maths:           # light | moderate | heavy
costs_discussed: # yes | no
latency_discussed: # yes | no
tags: []
created: {{date}}
---

# {{title}}

Normally created by `pipeline/extract.py`; use this by hand only for papers without a PDF. The focus is what a trading project needs. Skip the maths unless the idea cannot be built without it.

## One-line summary
What the paper claims, in one sentence.

## Abstract

## Implementation: how it is built
The decision rule, features, model and parameters, concretely enough to code.

## Data used
Universe, sample period, granularity (ticks, L1/L2/L3 book, bars).

## Costs and frictions
What costs the paper assumes (fees, spread, impact, slippage). If none, say so: results are gross.

## Latency and infrastructure
Speed the edge needs, any latency sensitivity shown. If none, say so.

## Reported results

## Implementation checklist
- Signal / decision rule in one line:
- Inputs and data granularity needed:
- Key parameters and how they are set:
- Horizon and turnover:
- Cost assumption vs. what we would actually pay:
- Latency needed for the edge to exist:
- What would break it:

## Atoms extracted
- [[Atom Name]] — what this paper contributed to that atom

## Critique / open questions
