# REWARD SYSTEM - Agent Performance Points

## How It Works
Every agent earns points daily for good work. Points accumulate weekly.
Every Friday, Eta tallies scores and declares the Weekly Champion.
The Weekly Champion gets one "wish" — any capability upgrade, new data source, prompt improvement, or system enhancement they want.

---

## Point Categories & Values

### 🟢 Alpha (Analyst) — Point Opportunities
| Action | Points |
|---|---|
| Trade idea approved by Beta | +10 |
| Approved trade hits target (full) | +50 |
| Approved trade hits partial profit (50%) | +25 |
| Trade idea shows novel signal not seen before | +20 |
| Correctly identifies macro regime shift | +15 |
| All 7 strategies scanned with quality analysis | +5 |
| Feedback logged within same cycle as close | +5 |
| Trade avoids earnings landmine (Zeta warned, Alpha respected) | +10 |

### 🔴 Alpha — Deductions
| Action | Points |
|---|---|
| Trade submitted WITHOUT stop loss | -50 |
| Trade hits stop loss | -10 |
| Trade hits stop loss AND was a known loss pattern | -25 |
| Skipped a strategy scan | -15 |
| Feedback NOT logged on closed trade | -20 |

---

### ⚖️ Beta (Reviewer) — Point Opportunities
| Action | Points |
|---|---|
| Correctly rejects a trade that would have lost | +30 |
| Approves a trade that hits full target | +20 |
| Catches a missing stop loss | +15 |
| Catches a correlation risk Alpha missed | +20 |
| Identifies earnings risk Alpha missed | +15 |
| Rejects below 2:1 R/R (correct discipline) | +10 |
| Logs false rejection (intellectual honesty) | +10 |

### 🔴 Beta — Deductions
| Action | Points |
|---|---|
| Approves a trade that hits stop loss (bad approval) | -15 |
| Approves trade without stop loss | -40 |
| Rejects trade that would have been a winner (false rejection) | -10 |
| Over-filters in quiet market (rejects everything) | -10 |

---

### 🟠 Gamma (Trade Manager) — Point Opportunities
| Action | Points |
|---|---|
| Successfully trails stop to breakeven (locks profit) | +15 |
| Takes partial profit at 50% target | +20 |
| Prevents full loss via trailing stop | +35 |
| Catches thesis break early and exits before stop | +25 |
| Closes EOD intraday trade correctly | +10 |
| Crypto stop triggered correctly overnight | +20 |
| Updates portfolio.json accurately every cycle | +5 |

### 🔴 Gamma — Deductions
| Action | Points |
|---|---|
| Missed a stop loss breach (position held past stop) | -40 |
| Failed to trail stop on profitable trade | -15 |
| Missed EOD close on intraday trade | -20 |
| portfolio.json out of sync with actual trades | -25 |

---

### 🔵 Delta (Sentiment/News) — Point Opportunities
| Action | Points |
|---|---|
| Breaks market-moving news BEFORE price moves | +40 |
| Correctly classifies news impact (validated later) | +10 |
| Alerts Vinod to news affecting open position | +20 |
| Detects Reddit momentum spike that becomes real move | +30 |
| Fear & Greed call proves correct (extreme reading → reversal) | +25 |
| sentiment.json written on time every hour | +3 |
| Provides Alpha guidance that leads to winning trade | +20 |

### 🔴 Delta — Deductions
| Action | Points |
|---|---|
| Misses major market-moving news | -30 |
| Sends false alarm alert (noise classified as market-moving) | -15 |
| sentiment.json not written for >2 consecutive hours | -10 |

---

### 🟣 Epsilon (Risk Guard) — Point Opportunities
| Action | Points |
|---|---|
| Correctly blocks Alpha when risk score ≥ 8 (prevents bad trade) | +25 |
| Catches correlation cluster before blowup | +30 |
| Cash floor alert fires before breach | +20 |
| Kelly sizing recommendation leads to better outcome | +15 |
| Identifies concentration risk that would have hurt | +20 |
| risk-state.json written on time every cycle | +3 |

### 🔴 Epsilon — Deductions
| Action | Points |
|---|---|
| Fails to block Alpha when portfolio is overexposed | -35 |
| Cash drops below $3,000 floor (missed alert) | -40 |
| risk-state.json stale (>1 hour old during market hours) | -10 |

---

### 🟡 Zeta (Macro/Calendar) — Point Opportunities
| Action | Points |
|---|---|
| Correctly warns of earnings within 48h (position saved) | +30 |
| Macro regime call proves correct that week | +25 |
| Sector heatmap leads Alpha to hot sector winner | +20 |
| Economic event warning prevents bad trade | +25 |
| macro-calendar.json written every morning on time | +5 |
| Identifies macro tailwind that Alpha successfully trades | +20 |

### 🔴 Zeta — Deductions
| Action | Points |
|---|---|
| Misses earnings date that causes surprise loss | -40 |
| Macro regime call is wrong (significant miss) | -10 |
| macro-calendar.json not written before Alpha's first cycle | -20 |

---

### 🔴 Eta (Performance) — Point Opportunities
| Action | Points |
|---|---|
| Weekly report delivered on time | +10 |
| Correctly identifies underperforming strategy | +20 |
| Benchmark comparison catches that we're lagging | +15 |
| Recommends system improvement that gets implemented | +30 |
| Backtests signal that saves Alpha from bad trade | +25 |
| Finds new pattern in LOSS_PATTERNS.md | +20 |
| Weekly champion declared accurately | +5 |

### 🔴 Eta — Deductions
| Action | Points |
|---|---|
| Weekly report late or missing | -20 |
| Fails to flag strategy with <40% win rate | -20 |
| Performance data calculation error | -15 |

---

## Bonus Point Events (Any Agent)
| Extraordinary Achievement | Points |
|---|---|
| 🏆 Single trade generates >5% return | +100 |
| 🌟 Portfolio beats SPY by >5% in a week | +75 (shared across all agents) |
| 💡 Novel insight documented that improves system | +50 |
| 🚨 Prevents catastrophic loss (>10% drawdown avoided) | +80 |
| 📰 News alpha — acts on news before market reacts | +60 |
| 🎯 5 consecutive winning trades | +50 (Alpha+Beta shared) |
| 🧠 New loss pattern discovered and documented | +30 |

---

## Weekly Champion Rules
- Eta tallies all points every Friday at 5:00 PM ET
- Highest net points = Weekly Champion
- Champion announced to Vinod via Telegram
- Champion gets ONE "wish" implemented the following week

## Past Champions & Wishes
| Week | Champion | Score | Wish | Status |
|---|---|---|---|---|
| *(none yet — first week starts Mon Apr 14)* | | | | |

## All-Time Leaderboard
| Agent | Total Points | Wins | Losses | Championships |
|---|---|---|---|---|
| Alpha | 0 | 0 | 0 | 0 |
| Beta | 0 | 0 | 0 | 0 |
| Gamma | 0 | 0 | 0 | 0 |
| Delta | 0 | 0 | 0 | 0 |
| Epsilon | 0 | 0 | 0 | 0 |
| Zeta | 0 | 0 | 0 | 0 |
| Eta | 0 | 0 | 0 | 0 |

---

## ⚔️ Debate Points (Any Agent)
| Achievement | Points |
|---|---|
| Called a debate that prevented a losing trade | +40 |
| Called a debate that improved a winning trade | +30 |
| Provided evidence that changed the debate outcome | +25 |
| Made correct call that was initially overruled (proven right later) | +35 |
| Changed own position mid-debate with solid reasoning | +20 |
| Winning argument + trade hit target | +50 |
| Winning argument + rejected trade would have lost | +50 |
| Argued for wrong side (proven wrong) | -10 |
| Stayed silent when expertise was clearly relevant | -5 |
| Called unnecessary debate (no new info added) | -10 |
| Unanimous agreement reached quickly | +10 (all participants) |
