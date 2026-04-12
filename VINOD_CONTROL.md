# VINOD CONTROL PANEL

This file gives Vinod direct control over the trading desk at any time.
**All agents check this file before every action.**

---

## How To Give Commands

Just tell Catalyst (me) in Telegram what you want. I will update VINOD_CONTROL.json immediately and all agents will obey on their next cycle.

---

## Available Commands

### 🛑 FREEZE — Stop all new trades
> "Freeze all trading" / "Pause the desk" / "Stop trading"

Sets `freeze_new_trades: true`. Alpha will not submit any new ideas. Existing positions still managed by Gamma.

### ▶️ UNFREEZE — Resume trading
> "Resume trading" / "Unfreeze the desk"

Sets `freeze_new_trades: false`. Normal operation resumes.

### ❌ CLOSE POSITION — Close a specific trade now
> "Close NVDA" / "Exit the BTC position" / "Close everything"

Adds ticker to `manual_close_requests`. Gamma closes it on next cycle (within 15 min).

### 💰 DAILY LOSS LIMIT — Set maximum loss for the day
> "Set daily loss limit to $300" / "Stop trading if we lose $500 today"

Sets `daily_loss_limit`. If daily losses hit this number, Alpha auto-freezes until next day.

### 📏 POSITION SIZE OVERRIDE — Change position sizing
> "Trade smaller today, max $300 per trade" / "Be aggressive, up to $1000 per trade"

Sets `max_position_size_override`. Overrides Kelly/Epsilon recommendations.

### 🔴 EMERGENCY STOP — Close everything immediately
> "Emergency stop" / "Close all positions NOW" / "Get to cash"

Sets `override_mode: EMERGENCY`. Gamma closes ALL open positions immediately. No new trades until manually reset.

### 📝 LEAVE A NOTE FOR THE DESK
> "Tell the agents to focus on gold today" / "Avoid tech stocks this week"

Sets `vinod_notes`. All agents read this every cycle. Expires after 24h unless renewed.

---

## Current Status
```
Trading Active: ✅ YES
Override Mode: NORMAL
Freeze New Trades: NO
Daily Loss Limit: $500
Vinod Notes: (none)
Manual Close Requests: (none)
```

---

## Agent Compliance Rules

Every agent MUST check VINOD_CONTROL.json at the start of every cycle:

```
IF freeze_new_trades = true → Alpha generates NO new trade ideas
IF override_mode = "EMERGENCY" → Gamma closes ALL positions immediately
IF manual_close_requests has tickers → Gamma closes them this cycle
IF daily_loss_current >= daily_loss_limit → freeze_new_trades auto-set to true
IF max_position_size_override is set → use it instead of Kelly recommendation
IF vinod_notes is not empty → read it, incorporate into analysis
```

Agents that ignore VINOD_CONTROL.json lose **-50 points** per violation.
