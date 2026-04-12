# MARKET_REGIMES.md — What Works When

Different market conditions demand different strategies. This file maps which plays and strategies perform best in each regime. Agents check this every cycle to know WHAT to prioritize given current conditions.

**Updated weekly by Eta. Read by Alpha every cycle (fed via macro-calendar.json).**

---

## Current Regime Assessment
```
Last updated: 2026-04-12
Regime: [TBD — will be set by Zeta on first cycle]
VIX level: [TBD]
Trend: [TBD]
Bias: [TBD]
```

---

## Regime Definitions & Strategy Mapping

### 🟢 REGIME 1: Bull Trend + Low VIX (<15)
**Characteristics:** SPY making higher highs, VIX calm, risk-on
**Best strategies:**
- Momentum + News (⭐⭐⭐⭐⭐) — trends extend, ride them
- Swing Trading (⭐⭐⭐⭐) — pullbacks recover fast
- Index/Leveraged ETFs long (⭐⭐⭐⭐) — QQQ/SPY calls work
**Avoid:** Mean reversion shorts, Gold longs, defensive plays
**Position sizing:** Full size — best conditions
**Stop loss style:** Wider stops (2.5-3%) — don't get shaken out

---

### 🟡 REGIME 2: Bull Trend + High VIX (15-25)
**Characteristics:** Uptrend intact but choppy, uncertainty elevated
**Best strategies:**
- Swing Trading (⭐⭐⭐⭐) — wait for confirmed bounces
- Multi-Asset Macro (⭐⭐⭐) — diversified positions
- Carry/Income (⭐⭐⭐⭐) — collect premium in chop
**Avoid:** Aggressive momentum, leveraged ETFs
**Position sizing:** 75% normal size
**Stop loss style:** Normal (2%)

---

### 🔴 REGIME 3: Bear Trend + High VIX (>25)
**Characteristics:** SPY making lower lows, fear elevated, risk-off
**Best strategies:**
- Mean Reversion (⭐⭐⭐⭐) — oversold bounces violent
- Gold/USD Long (⭐⭐⭐⭐⭐) — safe haven flows
- Short positions on weak sectors (⭐⭐⭐)
**Avoid:** Momentum longs, crypto longs, growth stocks
**Position sizing:** 50% normal size — capital preservation mode
**Stop loss style:** Tight (1.5%) — losses compound in bear markets

---

### ⚫ REGIME 4: Extreme Fear + Capitulation (VIX >35)
**Characteristics:** Panic selling, everything down, VIX spike
**Best strategies:**
- Mean Reversion (⭐⭐⭐⭐⭐) — extreme oversold = violent snapback
- Gold (⭐⭐⭐) — may peak as capitulation hits
- Cash preservation — wait for signal
**Avoid:** Adding to losers, leveraged ETFs, new longs
**Position sizing:** 25% max — only highest conviction plays
**Stop loss style:** Very tight — protect capital above all

---

### 🔵 REGIME 5: Sideways + Low VIX (Range Bound)
**Characteristics:** SPY between support/resistance, boring market
**Best strategies:**
- Carry/Income (⭐⭐⭐⭐⭐) — best regime for this strategy
- Mean Reversion (⭐⭐⭐⭐) — trade the range
- Forex Carry (⭐⭐⭐⭐) — low vol = carry works
**Avoid:** Momentum, breakout trades (fakeouts common)
**Position sizing:** Normal, but take profits faster
**Stop loss style:** Tight — range breaks happen fast

---

### 🟣 REGIME 6: Macro Uncertainty (FOMC/CPI/NFP week)
**Characteristics:** Any regime + major event within 48h
**Best strategies:**
- Carry/Income (⭐⭐⭐) — collect time decay
- Very selective Mean Reversion only
**Avoid:** Everything else — binary event risk destroys R/R
**Position sizing:** 50% max, reduce all existing positions
**Stop loss style:** Tighter than normal — gaps happen

---

### 🟠 REGIME 7: Crypto Bull (BTC F&G > 60)
**Characteristics:** Crypto greed elevated, BTC making highs
**Best strategies:**
- Momentum on BTC/ETH (⭐⭐⭐⭐)
- Alt-coin swing trades (⭐⭐⭐)
**Avoid:** Shorting crypto, FOMO entries at extreme greed (>80)
**Position sizing:** Normal, never exceed 20% crypto cap

---

### 🔵 REGIME 8: Crypto Bear (BTC F&G < 30)
**Characteristics:** Crypto fear elevated, BTC declining
**Best strategies:**
- Mean reversion only on extreme fear (<20) for bounce
- Gold/USD as safe haven
**Avoid:** Crypto longs in downtrend
**Position sizing:** Minimal crypto exposure

---

## Regime History
| Date | Regime | Duration | Best Strategy | Notes |
|---|---|---|---|---|
| 2026-04-12 | TBD | - | - | System launch |

---
*Updated weekly by Eta | Read by Alpha + Zeta every cycle*
