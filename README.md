# Agent Desk — Catalyst Paper Trading System

8-agent AI trading desk. Paper trading only. $15,000 starting capital.

## Agents
| Agent | Role | File |
|-------|------|------|
| Alpha | MD-level analyst — generates trade ideas every 30 min | ALPHA_PROMPT.md |
| Beta | MD-level risk manager — approves/rejects every trade | BETA_PROMPT.md |
| Gamma | Trade manager — trailing stops, position exits, 24/7 crypto | GAMMA_PROMPT.md |
| Delta | Market intelligence — sentiment, news, Reddit | DELTA_PROMPT.md |
| Epsilon | Risk guard — portfolio correlation, Kelly sizing | EPSILON_PROMPT.md |
| Zeta | Macro strategist — earnings calendar, FOMC, sector flows | ZETA_PROMPT.md |
| Eta | Performance analyst — benchmarks, weekly reports, optimizer | ETA_PROMPT.md |
| Theta | Execution specialist — fill quality, slippage, order timing | THETA_PROMPT.md |

## Structure
- `*_PROMPT.md` — Agent system prompts (MD-level seniority)
- `MASTER.md` — System architecture and rules
- `VINOD_CONTROL.json` — Live control panel (pause/stop/notes)
- `learning/` — Collective memory: PLAYBOOK, EDGES, SURPRISES, MARKET_REGIMES
- `intelligence/` — Live agent comms and strategy health
- `positions/` — Portfolio state and trade log
- `rewards/` — Championship scoring system
- `dashboard/` — GitHub Pages publisher scripts

## Dashboard
Live: https://tvinod09.github.io/catalyst-dashboard/

## Rules
- Max loss per trade: $750
- Cash floor: $3,000 (20%)
- Stop loss mandatory on every position
- R/R minimum: 2:1
- No market orders 3:30–4:00 PM ET
