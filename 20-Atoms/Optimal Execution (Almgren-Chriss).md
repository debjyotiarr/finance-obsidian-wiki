---
type: atom
status: seed
domain: execution
assets: [equities, futures]
tags: [execution, optimal-control, impact]
created: 2026-11-03
---

# Optimal Execution (Almgren-Chriss)

**Idea.** Executing a large order is a trade-off between impact cost (trade fast → pay more impact) and timing risk (trade slow → price drifts against you). Almgren & Chriss (2000) solve for the optimal schedule under linear temporary/permanent impact and mean-variance preferences: an exponentially front-loaded trajectory whose urgency rises with risk aversion.

**Practical notes.**
- The framework behind every "arrival price" algo; VWAP/TWAP are special cases (zero risk aversion / volume-weighted clock).
- Real impact is concave ([[Square-Root Law of Market Impact]]) and transient (propagator models) — modern schedulers adapt Almgren-Chriss intuition to those dynamics.
- Child-order placement (limit vs market, venue, queue) is a separate layer below the schedule — connects to [[Queue Position Value]] and [[Cross-Venue Fragmentation]].
- Adding a short-horizon alpha signal tilts the schedule: trade faster when the signal agrees with the order's direction.

**Related.** [[Implementation Shortfall]], [[Square-Root Law of Market Impact]], [[Price Impact and Kyle's Lambda]]

**Key references.** Almgren & Chriss (2000), *Optimal Execution of Portfolio Transactions*; Gatheral & Schied (2013) survey.
