# POSITION SIZING RULES

## Core Formula
shares = risk_per_trade / (entry_price - stop_loss)
risk_per_trade = min($500, portfolio_cash * 0.033)

## Examples
- Entry $100, Stop $95 → risk/share = $5 → shares = $500/$5 = 100 shares = $10,000 position
  BUT: cap at 8% of portfolio = $1,200 → max shares = $1,200/$100 = 12 shares
- Entry $50,000 (BTC), Stop $48,000 → risk/share = $2,000 → but max risk = $500 → size = 0.25 BTC

## Caps (non-negotiable)
- Max risk per trade: $500
- Max position value: 8% of current portfolio (approx $1,200 at $15K)
- Max concurrent positions: 6
- Max in one asset class: 35% of portfolio
- Max in one sector: 40% of portfolio
- Cash floor: $3,000 (20%)

## Correlation Limit
- If Epsilon risk-state.json shows correlation > 0.7 between a new idea and existing positions → reduce size by 50%
- If Epsilon shows portfolio risk_score > 7 → no new positions until score drops below 6
