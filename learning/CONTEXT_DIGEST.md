## CONTEXT DIGEST — Generated 2026-04-14 21:00 UTC
_Alpha: read this instead of raw PLAYBOOK/EDGES/LOSS_PATTERNS. Falls back to raw files if this is >28h old._

---

## LOSS PATTERNS (last 30 days)

**Top Rejection Reasons (by frequency):**

| # | Pattern | Count | Label |
|---|---------|-------|-------|
| 1 | Mean reversion in unresolved fundamental downtrend | 1 | — |

_Note: Desk is in Month Zero — only 1 pattern documented. Table will expand as live trading begins._

**Last 10 Beta Rejections:**

| Date | Ticker | Reason |
|------|--------|--------|
| 2026-04-13 | NVDA | Mean reversion LONG submitted during active, unresolved chip tariff catalyst — no confirmed catalyst resolution |

_Only 1 Beta rejection logged to date (test cycle). No patterns at 3+ occurrences yet._

**⚠️ KNOWN BAD SETUP (3+ occurrences):** None yet — PATTERN-001 at 1 occurrence. Promote to KNOWN BAD when count ≥ 3.

**PATTERN-001 Quick Rule (enforce every cycle):**
Before submitting ANY mean reversion LONG → ask: *"Is the downtrend catalyst RESOLVED?"*
If answer is "uncertain" or "ongoing" → **DO NOT SUBMIT.** Tag: `mean-reversion-falling-knife`

---

## ACTIVE EDGES

| Edge | Win Rate | Avg R | Works In Regime | Last Seen | Status |
|------|----------|-------|-----------------|-----------|--------|
| EDGE-001: Energy Sector Defensive Rotation | TBD (0 real trades) | TBD (target ≥2.5:1) | VIX 20-28, Risk-Off | 2026-04-13 (simulated) | CANDIDATE |
| EDGE-002: Gold/GDX Macro Trend | TBD (0 real trades) | TBD (target 1.5:1 + trail) | Regime 3/4, F&G ≤30, Gold > 50MA | 2026-04-13 (simulated) | CANDIDATE — **PRIORITY** |

_No CONFIRMED edges yet (requires 5+ real trades, 60%+ WR). No DEGRADING flags applicable._

**EDGE-002 Activation Criteria:** Zeta confirms Regime 3 or 4 + Gold above 50-day MA + F&G ≤ 30 → trigger Macro Trend Trade designation.

---

## PLAYBOOK SNAPSHOT

**CURRENT REGIME:** Regime 3 + Regime 6 (Bear/Risk-Off + Macro Uncertainty | VIX 18-24, F&G ~12, tariff-driven)

**TRADE IN THIS REGIME:**
1. **Multi-Asset Macro** — Gold/GDX safe-haven trend trade (EDGE-002, PRIORITY). Macro Trend Trade rules: enter on intraday pullback, trailing stop, no fixed target.
2. **Carry / Income** — Premium collection via defined-risk spreads (no naked short options). Elevated VIX = elevated premium. Watch for trend days that blow out short premium.
3. **Swing Trading (Defensive)** — Energy sector rotation (XOM, CVX, OXY) on MA dips when sector outperforming SPY 2+ consecutive sessions (EDGE-001). Tight stops required.

**AVOID IN THIS REGIME:**
1. **Momentum + News** — Current regime (F&G=12, Risk-Off) is worst environment. Do not force momentum trades. Wait for Regime 1 or 2.
2. **Index Futures / Leveraged ETFs** — VIX 18-24 + Regime 3 = extreme volatility destroys leveraged positions. AVOID until regime improves. Max 2x leverage rule hard cap.

**SPECIAL NOTES:**
- ⚠️ **Earnings season active** — avoid binary event options plays; no directional long calls around earnings
- ⚠️ **Mean Reversion: PATTERN-001 active** — confirm ALL downtrend catalyst resolutions before any mean-reversion submission
- ⚠️ **Options in Regime 6** — carry/hedge structures ONLY (time decay, protective puts). No directional long calls.
- 🏅 **Gold at $4,724** — macro safe haven thesis confirmed. Multi-Asset Macro is the desk's best-fit strategy in current regime.
- ℹ️ PLAYBOOK has no confirmed plays yet (template only) — all active guidance derives from EDGES.md candidate observations and strategy-health regime notes.

---

## STRATEGY HEALTH

**SUSPENDED:** None

**WEAK (<40% win rate):** None (all strategies at baseline — zero closed trades as of 2026-04-13. Meaningful health scoring begins Week 2, ~Apr 21.)

**Strategy Regime Fit Summary (current Regime 3+6):**

| Strategy | Regime Fit | Action |
|----------|-----------|--------|
| Multi-Asset Macro | ✅ BEST | Prioritize |
| Carry / Income | ✅ Good | Active (defined-risk structures) |
| Swing Trading | ⚠️ Caution | Defensive names only, tight stops |
| Mean Reversion | ⚠️ Watch | PATTERN-001 enforcement mandatory |
| Options | ⚠️ Restricted | Carry/hedge only, no directional |
| Momentum + News | ❌ WORST | Do not activate |
| Index Futures/Lev. ETFs | ❌ Avoid | Avoid until regime improves |

---

## DIGEST META

Generated: 2026-04-14T21:00:00Z
Source sizes: PLAYBOOK (1.7kb), EDGES (4.3kb), LOSS_PATTERNS (1.9kb)
Next full review: 2026-04-17 (Friday)
_Digest authored by Agent Eta — Nightly Context Digest job_
