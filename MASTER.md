# Trading System - Master State

## Configuration
- **Initial Capital:** $15,000.00
- **Paper Trading:** Yes (no real money)
- **Start Date:** 2026-04-11
- **Trade Fee per transaction:** $0.65 (options) / $0.00 (stocks, Robinhood-style) — modeled at $1.00 flat per trade for conservatism
- **Short-term capital gains tax rate:** 37% (held < 1 year, worst case)
- **Long-term capital gains tax rate:** 20% (held > 1 year)

## Current Portfolio
```json
{
  "cash": 15000.00,
  "positions": {},
  "realized_pnl": 0.00,
  "unrealized_pnl": 0.00,
  "total_fees_paid": 0.00,
  "total_tax_liability": 0.00,
  "trade_count": 0
}
```

## Agents
- **Alpha (Analyst):** Runs every 30 min during market hours, generates trade ideas
- **Beta (Reviewer):** Reviews Alpha's suggestions, debates, finalizes
- **Catalyst (Orchestrator):** Tracks positions, sends daily reports

## Market Hours (ET)
- Pre-market: 4:00 AM - 9:30 AM
- Regular: 9:30 AM - 4:00 PM
- After-hours: 4:00 PM - 8:00 PM
- Daily report: ~4:30 PM ET (21:30 UTC)
