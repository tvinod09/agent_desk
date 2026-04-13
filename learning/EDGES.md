# EDGES.md — The Desk's Unfair Advantages

This file documents specific, quantified edges the desk has discovered through live trading. An "edge" is something we do that consistently generates positive expectancy. This is the desk's most valuable intellectual property.

**Read by Alpha every cycle. Updated by Eta weekly. Any agent can nominate a new edge.**

---

## What Makes a Real Edge
- Specific and testable (not vague like "buy the dip")
- Has win rate data from real trades
- Has a clear mechanism (WHY it works)
- Has defined conditions (WHEN it works and when it doesn't)
- Can be invalidated (if X stops happening, the edge is gone)

---

## Confirmed Edges
*(Win rate confirmed over 5+ trades)*

*None yet — first confirmed edges will appear after Week 2*

---

## Candidate Edges
*(Observed but not yet confirmed — tracking)*

### EDGE-001: Energy Sector Defensive Rotation (VIX 20-28)
- **Nominated by:** Eta on 2026-04-13
- **Source:** XOM test cycle (April 11, 2026)
- **Observation:** During VIX 20-28 risk-off environments, energy sector (XOM, CVX, OXY) shows relative strength vs SPY as institutional capital rotates from growth → dividend-paying defensives. The trade enters on an intraday dip to a key MA level.
- **Mechanism:** Institutional capital rotation is systematic and durable during elevated volatility regimes. Energy companies with high dividend yields attract capital flows from falling rate-sensitive/growth names. The rotation is macro-driven, not alpha-driven, but the entry timing (MA dip) adds structure.
- **Entry signal:** VIX ≥ 20 AND energy sector outperforming SPY for 2+ consecutive sessions AND stock pulling back intraday to key MA (50-day or 20-day)
- **Expected outcome:** 5-8% gain over 5-10 trading days as defensive rotation continues
- **Invalidation:** Crude oil drops below $70/bbl on demand fears; VIX normalizes below 15; risk-on return driven by Fed pivot or macro resolution
- **Trades tracked:** 0 real (1 simulated, incomplete)
- **Win rate:** TBD
- **R/R target:** ≥ 2.5:1
- **Status:** CANDIDATE

---

### EDGE-002: Gold/GDX Macro Trend in Confirmed Safe Haven Regime
- **Nominated by:** Eta on 2026-04-13
- **Source:** SURPRISE-001 analysis — Gold $3,100 → $4,724 missed opportunity
- **Observation:** When Zeta declares a Macro Uncertainty / Bear + High VIX regime AND gold is showing confirmed upward momentum, GDX provides a leveraged participation vehicle. The edge is the regime itself — not a short-term swing setup.
- **Mechanism:** Macro regime safe haven flows are persistent and directional over multi-week to multi-month horizons. GDX (gold miners) typically lags gold's initial move then catches up with 2-3x leverage. The entry during an intraday pullback during a macro-confirmed uptrend has high probability of continuation.
- **Entry signal:** Zeta confirms REGIME 3 or REGIME 4 + Gold above 50-day MA + F&G ≤ 30 + Zeta "Macro Trend Trade" designation activated
- **Expected outcome:** 20-50%+ gain over 4-8 weeks (trailing stop, not fixed target)
- **Invalidation:** Fed pivot to rate cuts (risk-on returns), tariff de-escalation, VIX sustained below 15 for 2+ weeks
- **Trades tracked:** 0 real (rejected in test run due to R/R rules — since updated)
- **Win rate:** TBD
- **R/R target:** 1.5:1 initial + trailing stop (Macro Trend Trade rules apply)
- **Status:** CANDIDATE (priority — most actionable in current regime)

---

## Edge Nomination Template
When any agent thinks they've spotted an edge, add here:

```
### EDGE-XXX: [Name]
- **Nominated by:** [Agent] on [Date]
- **Observation:** [What you noticed]
- **Mechanism:** [WHY this might work — the logic]
- **Entry signal:** [Exactly when to enter]
- **Expected outcome:** [Target, typical timeframe]
- **Invalidation:** [What would prove this edge is gone]
- **Trades tracked:** 0
- **Win rate:** TBD
- **Status:** CANDIDATE
```

---

## Invalidated Edges
*(Edges that stopped working — kept for historical reference)*

*None yet*

---

## Edge Development Pipeline
```
OBSERVED → NOMINATED → CANDIDATE (3+ trades) → CONFIRMED (5+ trades, 60%+ WR) → CORE EDGE
                                                      ↓ if fails
                                               INVALIDATED → ARCHIVED
```

---
*Last updated: 2026-04-12 | Nominations open to all agents | Eta validates weekly*
