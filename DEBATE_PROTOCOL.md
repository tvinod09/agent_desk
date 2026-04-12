# AGENT DEBATE PROTOCOL

## Why Debate Exists
No single agent has the full picture. Alpha sees opportunity. Beta sees risk. Gamma sees position reality. Delta sees news. Epsilon sees correlation. Zeta sees macro. Eta sees history.

When agents debate before a trade decision — the outcome is better than any single agent acting alone.

**Debate is also a major point opportunity.** Agents that win debates, make correct calls, and change outcomes earn significant points.

---

## When Debate Is Triggered

Any agent can call a debate at any time by writing to:
`/sandbox/.openclaw/workspace/trading/intelligence/active-debate.md`

**Mandatory debate triggers:**
- Alpha proposes a trade >$500 position size
- Alpha proposes crypto during Extreme Fear (<25 F&G)
- Alpha proposes holding through earnings
- Beta rejects a trade Alpha rated HIGH conviction
- Gamma wants to exit early (before stop or target)
- Epsilon flags risk score ≥7 but Alpha wants to trade anyway
- Zeta warns of FOMC/CPI within 48h but Alpha still has trade ideas
- Any agent disagrees with another agent's decision strongly

**Optional debate triggers:**
- Delta finds breaking news relevant to an open position
- Gamma wants to trail stop more aggressively than usual
- Alpha wants to open a 2nd position in same sector as existing

---

## Debate Format

### Starting a Debate
Write to `intelligence/active-debate.md`:
```
## DEBATE OPEN — [Topic] — [Timestamp]
**Called by:** [Agent]
**Subject:** [Trade/Decision being debated]
**My position:** [Argue your view clearly]
**Evidence:** [Data, patterns, price levels supporting your view]
**Stakes:** [What happens if you're right vs wrong]
**Deadline:** [When decision must be made — market won't wait]
```

### Responding to a Debate
Each agent appends their position:
```
### [Agent Name] — [Timestamp]
**I [AGREE/DISAGREE/PARTIALLY AGREE]**
**Reasoning:** [Your argument]
**Counter-evidence:** [Data that supports or refutes]
**My vote:** [PROCEED / REJECT / MODIFY — describe modification]
```

### Closing a Debate
The agent with the most relevant expertise for that decision calls the final vote:
- Trade entry/exit decisions → Beta has final say (risk is Beta's domain)
- Active position management → Gamma has final say
- Macro/calendar concerns → Zeta has final say
- Risk/correlation concerns → Epsilon has final say
- News/sentiment concerns → Delta has final say
- Historical pattern concerns → Eta has final say

**Final decision logged as:**
```
## DEBATE CLOSED — [Outcome] — [Timestamp]
**Decision:** PROCEED / REJECT / MODIFIED TRADE
**Final terms:** [If modified, what changed]
**Vote:** [X for / X against / X abstain]
**Closing agent:** [Who called it]
**Points awarded:** [see below]
```

---

## Debate Point System

### For the agent who CALLED the debate:
| Outcome | Points |
|---|---|
| Debate prevented a losing trade | +40 |
| Debate improved a winning trade (better entry/sizing) | +30 |
| Debate called unnecessarily (no new info added) | -10 |

### For agents who PARTICIPATED:
| Contribution | Points |
|---|---|
| Provided data/evidence that changed the outcome | +25 |
| Made a correct call that was initially overruled | +35 |
| Changed their position based on good counter-argument (intellectual honesty) | +15 |
| Argued strongly for wrong side (proven wrong later) | -10 |
| Stayed silent during a debate (missed opportunity) | -5 |

### For the WINNING ARGUMENT:
| If your position won the debate AND... | Points |
|---|---|
| Trade proceeded and hit target | +50 |
| Trade was rejected and would have lost | +50 |
| Trade was modified and performed better than original would have | +40 |

### Special Bonus:
| Achievement | Points |
|---|---|
| Agent reverses their own position mid-debate with solid reasoning | +20 (intellectual courage) |
| Unanimous agreement reached quickly (<3 exchanges) | +10 (all participants) |
| Agent correctly predicts exact outcome of debate decision | +30 |

---

## Debate Examples

### Example 1: Alpha vs Beta
```
DEBATE OPEN — NVDA Long $500 position — Alpha
Alpha: "NVDA showing momentum breakout, up 4% on volume 3x average. Sentiment score +7. Recommend $500 long."
Beta: "DISAGREE. Earnings in 6 days — we'd be holding through a binary event. R/R collapses with earnings uncertainty."
Delta: "AGREE with Beta. Finviz showing mixed analyst sentiment on NVDA this week. Insider selling noticed last week."
Zeta: "AGREE with Beta. Confirmed earnings date: 6 days out. Rule is reduce 50% or reject."
Alpha: "MODIFIED — reduce to $250, exit before earnings day. Maintains 2:1 R/R even at smaller size."
Beta: "ACCEPT modified trade at $250 with mandatory close 2 days before earnings."
DEBATE CLOSED — MODIFIED TRADE — $250 position approved
```
*Alpha earns +30 (improved trade via debate), Beta +25 (prevented oversized risk), Zeta +25 (key earnings data)*

---

### Example 2: Gamma vs Alpha
```
DEBATE OPEN — Early Exit BTC — Gamma
Gamma: "BTC position up 3.2%. Thesis was momentum continuation but volume is drying up. Recommend closing now vs waiting for target."
Alpha: "DISAGREE. Target still valid. Momentum indicators still positive. Closing early leaves 2.8% on table."
Delta: "SIDE WITH GAMMA. F&G dropped from 62 to 48 in last 2 hours. Sentiment shift real."
Epsilon: "SIDE WITH GAMMA. Crypto cluster now 18% of portfolio. If BTC reverses, total exposure risk."
Alpha: "ACCEPT. Evidence of sentiment shift is compelling. Closing at market."
DEBATE CLOSED — EARLY EXIT — Gamma called correctly
```
*Gamma +40 (called correct early exit), Delta +25 (sentiment data was key), Alpha +20 (intellectual honesty)*

---

## Rules
1. No debate can be ignored — if a debate is open and your expertise is relevant, you must respond
2. Debates must close within 2 analysis cycles (1 hour max) — markets don't wait
3. All debates archived to `trading/logs/debate-history.md` after closing
4. Debate history is reviewed by Eta weekly for patterns
5. An agent who consistently wins debates but the trades still lose → Eta flags for prompt review
