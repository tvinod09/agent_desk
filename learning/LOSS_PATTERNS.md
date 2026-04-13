# LOSS PATTERNS — Shared Memory (Alpha + Beta)

Both agents MUST read this before every cycle.
Both agents MUST update this after every losing trade.

## How Patterns Are Added
- After any closed loss: the responsible agent adds the pattern HERE
- Format must be consistent so future cycles can pattern-match quickly
- Beta-approved losses get tagged: "Beta approved — should have caught"

---

## Active Patterns

### PATTERN-001: Mean Reversion in Unresolved Fundamental Downtrend
**Added:** 2026-04-13 | **By:** Eta (post-mortem analysis) | **Source:** NVDA test cycle rejection
**Pattern description:** Submitting a mean-reversion LONG in a stock/sector where the downtrend driver (regulatory action, tariff, earnings miss, rating cut) is UNRESOLVED.
**What happens:** The "oversold" signal (RSI <35, X% drawdown) looks like a bounce setup, but the fundamental headwind continues to push the stock lower. The mean never reverts because the downtrend is driven by fundamentals, not temporary sentiment.
**Example:** NVDA down 8% from highs due to chip export tariff restrictions. RSI ~35. Alpha submitted as "oversold bounce" — but the tariff catalyst was unresolved. The stock could continue falling 15-20% more.
**Red flags to watch:**
- Downtrend driven by regulatory action, tariff, major competitor move, guidance cut
- No specific date for catalyst resolution (i.e., "tariff uncertainty" with no end date)
- MEDIUM conviction + single signal (RSI only)
**Rule:** Before submitting ANY mean reversion LONG, Alpha must confirm: "What is the catalyst for the downtrend, and has it been RESOLVED?" If the answer is "uncertain" or "ongoing" — DO NOT SUBMIT.
**Beta enforcement:** Reject any mean reversion trade where Alpha cannot identify a specific resolved catalyst for the prior downtrend.
**Tag:** `mean-reversion-falling-knife`

---

## Retired Patterns
_(patterns that no longer apply due to changed market conditions)_
