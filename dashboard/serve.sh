#!/bin/bash
# Auto-start dashboard server
# Runs python3 HTTP server on port 8765 from the trading directory
# Restart it if it dies

TRADING_DIR="/sandbox/.openclaw/workspace/trading"
PORT=8765

while true; do
  echo "[$(date -u +%H:%M:%S)] Starting dashboard server on port $PORT..."
  cd "$TRADING_DIR" && python3 -m http.server $PORT --bind 0.0.0.0
  echo "[$(date -u +%H:%M:%S)] Server died — restarting in 5s..."
  sleep 5
done
