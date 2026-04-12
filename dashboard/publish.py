#!/usr/bin/env python3
"""
Catalyst Dashboard Data Publisher
Reads all trading desk files, builds data.json, pushes via git to GitHub Pages.
Called by agents every 30 minutes and after every trade.
"""

import json
import os
import subprocess
from datetime import datetime, timezone

WORKSPACE = "/sandbox/.openclaw/workspace/trading"
GH_TOKEN  = "YOUR_GITHUB_TOKEN_HERE"
GH_REPO   = "https://tvinod09:{TOKEN}@github.com/tvinod09/catalyst-dashboard.git".format(TOKEN="YOUR_GITHUB_TOKEN_HERE")
GIT_DIR   = "/tmp/catalyst-data-push"

def read_json(path, default=None):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return default or {}

def read_text(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return ""

def git(*args, cwd=GIT_DIR):
    result = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

def ensure_repo():
    if not os.path.isdir(os.path.join(GIT_DIR, ".git")):
        os.makedirs(GIT_DIR, exist_ok=True)
        git("init", "-b", "gh-pages", cwd=GIT_DIR)
        git("remote", "add", "origin", GH_REPO)
    # Always fetch latest
    git("fetch", "origin", "gh-pages")
    git("checkout", "gh-pages")
    git("reset", "--hard", "origin/gh-pages")

def build_data():
    portfolio = read_json(f"{WORKSPACE}/positions/portfolio.json", {
        "cash": 15000, "positions": {}, "realized_pnl": 0,
        "unrealized_pnl": 0, "trades": []
    })
    scores    = read_json(f"{WORKSPACE}/rewards/scores.json", {})
    health    = read_json(f"{WORKSPACE}/intelligence/strategy-health.json", {})
    sentiment = read_json(f"{WORKSPACE}/intelligence/sentiment.json", {})
    risk      = read_json(f"{WORKSPACE}/intelligence/risk-state.json", {})
    control   = read_json(f"{WORKSPACE}/VINOD_CONTROL.json", {
        "trading_active": True, "override_mode": "NORMAL",
        "freeze_new_trades": False, "daily_loss_limit": 500,
        "daily_loss_current": 0, "vinod_notes": ""
    })
    playbook  = read_text(f"{WORKSPACE}/learning/PLAYBOOK.md")
    regimes   = read_text(f"{WORKSPACE}/learning/MARKET_REGIMES.md")

    # Today's activity log
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log   = read_text(f"{WORKSPACE}/logs/{today}.md")
    activity = [l.lstrip("# ").strip() for l in log.split("\n") if l.startswith("## ") or l.startswith("### ")][-10:]

    cash     = portfolio.get("cash", 15000)
    pnl      = portfolio.get("realized_pnl", 0)
    upnl     = portfolio.get("unrealized_pnl", 0)
    positions = portfolio.get("positions", {})
    trades   = portfolio.get("trades", [])
    open_pos = {k: v for k, v in positions.items() if v.get("status") == "OPEN"}
    closed   = [t for t in trades if t.get("status") == "CLOSED"]

    # Portfolio value
    pos_value = sum(p.get("current_value", p.get("cost_basis", 0)) for p in open_pos.values())
    total_val = cash + pos_value

    # Agent scores
    agent_names = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta"]
    agents_out  = {}
    for name in agent_names:
        a = scores.get("agents", {}).get(name, {})
        agents_out[name] = {
            "weekly_points":  a.get("weekly_points", 0),
            "all_time_points": a.get("all_time_points", 0),
            "championships":  a.get("championships", 0),
            "wins":           a.get("wins", 0),
            "losses":         a.get("losses", 0),
            "approved":       a.get("approved", 0),
            "rejected":       a.get("rejected", 0),
            "exits":          a.get("exits", 0),
            "trailing_stops": a.get("trailing_stops_set", 0),
            "alerts":         a.get("alerts_fired", 0),
            "blocks":         a.get("blocks", 0),
            "risk_score":     a.get("risk_score"),
            "reports":        a.get("reports", 0),
            "sharpe":         a.get("sharpe"),
        }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "portfolio": {
            "cash":           round(cash, 2),
            "realized_pnl":   round(pnl, 2),
            "unrealized_pnl": round(upnl, 2),
            "total_value":    round(total_val if total_val > 0 else cash, 2),
            "open_count":     len(open_pos),
            "total_trades":   len(trades),
            "open_positions": open_pos,
            "recent_trades":  closed[-20:],
        },
        "agents":           agents_out,
        "champion":         scores.get("current_champion", {}).get("name", "TBD"),
        "week_number":      scores.get("current_week", 1),
        "strategy_health":  health.get("strategies", {}),
        "sentiment": {
            "fear_greed_value":  sentiment.get("crypto_fear_greed", {}).get("value"),
            "fear_greed_label":  sentiment.get("crypto_fear_greed", {}).get("label"),
            "market_regime":     sentiment.get("market_regime") or risk.get("current_regime", "Unknown"),
            "overall":           sentiment.get("overall", "Neutral"),
        },
        "control": {
            "trading_active":    control.get("trading_active", True),
            "override_mode":     control.get("override_mode", "NORMAL"),
            "freeze_new_trades": control.get("freeze_new_trades", False),
            "freeze_reason":     control.get("freeze_reason"),
            "daily_loss_limit":  control.get("daily_loss_limit", 500),
            "daily_loss_current": control.get("daily_loss_current", 0),
            "vinod_notes":       control.get("vinod_notes", ""),
        },
        "activity": activity,
    }

def publish():
    ts = lambda: datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts()}] Ensuring git repo...")
    ensure_repo()

    print(f"[{ts()}] Building data...")
    data = build_data()

    # Write data.json into the repo
    out_path = os.path.join(GIT_DIR, "data.json")
    with open(out_path, "w") as f:
        json.dump(data, f, indent=2, default=str)

    print(f"[{ts()}] Committing and pushing...")
    git("config", "user.email", "catalyst@trading.desk")
    git("config", "user.name",  "Catalyst")
    git("add", "data.json")

    out, err = git("diff", "--cached", "--stat")
    if not out:
        print(f"[{ts()}] No changes — skipping push")
        return

    git("commit", "-m", f"data: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC")
    out, err = git("push", "origin", "gh-pages")
    if err and "error" in err.lower():
        print(f"[{ts()}] Push error: {err}")
    else:
        print(f"[{ts()}] ✅ Published! https://tvinod09.github.io/catalyst-dashboard/")

if __name__ == "__main__":
    publish()
