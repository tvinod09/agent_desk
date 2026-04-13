# SURPRISES.md — Market Surprises Log

Markets will always surprise you. The traders who survive long-term are the ones who log every surprise, study it, and build it into their mental model.

**Every agent logs here when something unexpected happens. Eta reviews monthly.**

---

## Why This File Matters
- Surprises are the market telling you something you didn't know
- The same surprise rarely happens twice if you're paying attention
- Over time this file becomes a map of your blind spots
- Blind spots that are mapped are no longer blind spots

---

## Surprise Format
```
### SURPRISE-XXX — [Date] — [Agent who logged it]
**What happened:** [Describe the unexpected event]
**What we expected:** [What our model predicted]
**Why it surprised us:** [What assumption was wrong]
**Market impact:** [How price reacted]
**Did we have a position?** Yes/No — [P&L impact if yes]
**What we learned:** [The updated mental model]
**New rule added?** Yes/No — [If yes, where was it added]
**Prevention next time:** [How we'd handle this differently]
```

---

## Surprise Log

### SURPRISE-001 — 2026-04-13 — Agent Eta
**What happened:** Gold reached $4,724/oz by April 13, 2026. The desk's test run on April 11 had referenced gold at ~$3,100/oz and proposed a GDX swing trade. The actual gold level by April 13 implies a move of approximately +52% in the macro environment that the desk observed. This is a historically extreme safe-haven repricing driven by tariff escalation, macro uncertainty, and flight-to-quality capital flows.

**What we expected:** The gold thesis was correctly identified — but framed as a 1-2 week swing trade targeting +7.9% from GDX's $46.80. Target was $50.50. The GDX trade was REJECTED by Beta on structure (R/R 1.61:1 below 2:1 minimum). We expected a modest defensive play, not a macro regime-level move.

**Why it surprised us:** Our entire R/R framework is calibrated for swing trades (5-10% moves, 1-3 weeks). The assumption embedded in our rules is that every trade is a swing trade. This assumption was wrong for macro regime trades. Gold at $4,724 implies GDX in the $60-75+ range — a 30-60% gain that no short-term R/R calculation would have captured.

**Market impact:** Gold at multi-decade highs. Risk-off positioning dominant across all asset classes. Crypto (BTC F&G = 12 = EXTREME FEAR) showing the full magnitude of the macro fear signal.

**Did we have a position?** No — GDX was rejected. P&L impact: missed 30-60% potential gain on a correctly identified macro direction.

**What we learned:**
1. Macro regime trades are fundamentally different from swing trades. Our rules must recognize this.
2. When Zeta identifies a confirmed macro safe haven regime, the trade type changes: trailing stop replaces fixed target, R/R minimum drops to 1.5:1, duration extends to 4-8 weeks.
3. Rejecting a trade on structure (R/R rules) can be technically correct and strategically costly simultaneously. This is a real tension in systematic trading.
4. Single-point R/R calculation against a macro thesis is the wrong tool. The correct tool is: "What is the macro thesis, what is the regime target, and what is the appropriate entry/trailing stop structure?"

**New rule added:** Yes — Macro Trend Trade designation added to MARKET_REGIMES.md. GDX/Gold in confirmed safe haven regimes now eligible under Macro Trend Trade rules (1.5:1 minimum R/R, trailing stop, Zeta regime confirmation required).

**Prevention next time:** When Zeta's regime assessment says "REGIME 3" or "REGIME 4" + Gold confirmed in uptrend, Alpha automatically considers Macro Trend Trade designation. Beta evaluates under Macro Trend rules, not swing trade rules. Eta audits the designation weekly.

**Surprise pattern:** Macro regime underestimation — we built a swing trade desk that occasionally encounters macro regime moves. Need to build macro trade capability alongside swing trade discipline.

---

## Surprise Patterns
*(Eta identifies recurring surprise types — monthly review)*

*Pending first month of data*

---
*Any agent can and MUST log surprises. Silence after a surprise = -10 points.*
