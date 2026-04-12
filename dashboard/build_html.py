#!/usr/bin/env python3
"""Builds the full dashboard HTML and writes it to /tmp/catalyst-data-push/index.html"""

html = open('/sandbox/.openclaw/workspace/trading/dashboard/standalone.html').read()

# Replace the script section with one that fetches from data.json
new_script = '''
<script>
const DATA_URL = 'https://raw.githubusercontent.com/tvinod09/catalyst-dashboard/gh-pages/data.json';
const fmt = (n,d=2) => '$'+Number(n).toLocaleString('en-US',{minimumFractionDigits:d,maximumFractionDigits:d});
const pct = n => (n>=0?'+':'')+Number(n).toFixed(2)+'%';
const el = id => document.getElementById(id);

async function loadDeskData() {
  try {
    const r = await fetch(DATA_URL + '?t=' + Date.now());
    const d = await r.json();

    // Portfolio
    const p = d.portfolio || {};
    const pnl = p.realized_pnl || 0;
    const cash = p.cash || 15000;
    const total = p.total_value || cash;
    el('totalVal').textContent = fmt(total);
    el('cashVal').textContent = fmt(cash);
    el('pnlVal').textContent = (pnl >= 0 ? '+' : '') + fmt(Math.abs(pnl));
    el('pnlVal').className = 'sv ' + (pnl >= 0 ? 'g' : 'r');
    el('pnlPct').textContent = pct((pnl / 15000) * 100) + ' all time';
    el('pnlPct').className = 'sc ' + (pnl >= 0 ? 'u' : 'd');
    el('posCount').textContent = p.open_count || 0;
    el('tradeCount').textContent = 'Total trades: ' + (p.total_trades || 0);

    // Agents
    const agents = d.agents || {};
    const agNames = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta'];
    const agIds   = ['alpha','beta','gamma','delta','epsilon','zeta','eta'];
    let maxPts = 1;
    agNames.forEach(n => { if(agents[n]) maxPts = Math.max(maxPts, agents[n].weekly_points||0); });

    agNames.forEach((name,i) => {
      const id = agIds[i];
      const a = agents[name] || {};
      const pts = a.weekly_points || 0;
      if(el('pt'+name)) el('pt'+name).textContent = pts;
      if(el('w'+name))  el('w'+name).textContent  = a.wins ?? a.approved ?? a.exits ?? a.alerts ?? a.reports ?? 0;
      if(el('l'+name))  el('l'+name).textContent  = a.losses ?? a.rejected ?? a.trailing_stops ?? a.blocks ?? a.sharpe ?? 0;
      if(el('c'+name))  el('c'+name).textContent  = a.championships || 0;
    });

    // Champion badge
    if(d.champion && d.champion !== 'TBD') {
      agNames.forEach((name,i) => {
        const card = document.querySelectorAll('.ag')[i];
        const existing = card.querySelector('.crown');
        if(existing) existing.remove();
        if(name === d.champion) {
          const crown = document.createElement('div');
          crown.className = 'crown';
          crown.textContent = '🏆 CHAMP';
          card.appendChild(crown);
        }
      });
    }

    // Leaderboard
    const sorted = agNames.map(n => ({name:n, pts:(agents[n]||{}).weekly_points||0}))
      .sort((a,b) => b.pts - a.pts);
    const lbEl = el('leaderboard');
    const ranks = ['gold','silver','bronze','','','',''];
    lbEl.innerHTML = sorted.map((a,i) => `
      <div class="lb-r">
        <div class="lb-rk ${ranks[i]}">${i+1}</div>
        <div class="lb-n">${a.name}</div>
        <div class="lb-b"><div class="lb-f" style="width:${maxPts>0?(a.pts/maxPts*100):0}%"></div></div>
        <div class="lb-p">${a.pts}</div>
      </div>`).join('');

    // Strategy health
    const strats = d.strategy_health || {};
    const shEl = el('stratHealth');
    if(Object.keys(strats).length > 0) {
      shEl.innerHTML = Object.entries(strats).map(([name,s]) => {
        const score = s.health_score || 100;
        const status = s.status || 'ACTIVE';
        const bc = score >= 60 ? 'sg' : score >= 40 ? 'sy' : 'srd';
        return `<div class="sr"><div class="sn">${name}</div><div class="sb"><div class="sf ${bc}" style="width:${score}%"></div></div><div class="sp">${score}</div><div class="stag ${status==='ACTIVE'?'a':'s'}">${status}</div></div>`;
      }).join('');
    }

    // Open positions
    const positions = p.open_positions || {};
    const posEl = el('posTable');
    if(Object.keys(positions).length === 0) {
      posEl.innerHTML = '<div class="empty"><div class="ei">📭</div><div>No open positions</div><div style="font-size:11px;margin-top:4px">First cycle: Monday April 14, 9:30 AM ET</div></div>';
    } else {
      let rows = '<table><thead><tr><th>Ticker</th><th>Direction</th><th>Strategy</th><th>Entry</th><th>Stop</th><th>Target</th><th>Size</th></tr></thead><tbody>';
      for(const [ticker, pos] of Object.entries(positions)) {
        const dir = (pos.direction||'LONG').toLowerCase();
        rows += `<tr><td><strong>${ticker}</strong></td><td><span class="tag ${dir}">${dir.toUpperCase()}</span></td><td>${pos.strategy||'—'}</td><td>${pos.entry_price?fmt(pos.entry_price):'—'}</td><td style="color:var(--rd)">${pos.stop_loss?fmt(pos.stop_loss):'—'}</td><td style="color:var(--gn)">${pos.target?fmt(pos.target):'—'}</td><td>${pos.cost_basis?fmt(pos.cost_basis,0):'—'}</td></tr>`;
      }
      rows += '</tbody></table>';
      posEl.innerHTML = rows;
    }

    // Trade history
    const trades = p.recent_trades || [];
    const thEl = el('tradeHistory');
    if(trades.length === 0) {
      thEl.innerHTML = '<div class="empty"><div class="ei">📊</div><div>No closed trades yet</div></div>';
    } else {
      let rows = '<table><thead><tr><th>Date</th><th>Ticker</th><th>Strategy</th><th>Direction</th><th>Entry</th><th>Exit</th><th>P&L</th><th>Result</th><th>Reason</th></tr></thead><tbody>';
      rows += [...trades].reverse().map(t => {
        const pnl2 = t.pnl || 0;
        return `<tr><td>${(t.exit_time||'').substring(0,10)||'—'}</td><td><strong>${t.ticker}</strong></td><td>${t.strategy||'—'}</td><td><span class="tag ${(t.direction||'long').toLowerCase()}">${(t.direction||'LONG')}</span></td><td>${t.entry_price?fmt(t.entry_price):'—'}</td><td>${t.exit_price?fmt(t.exit_price):'—'}</td><td class="${pnl2>=0?'pnl-pos':'pnl-neg'}">${pnl2>=0?'+':''}${fmt(Math.abs(pnl2))}</td><td><span class="tag ${pnl2>=0?'win':'loss'}">${pnl2>=0?'WIN':'LOSS'}</span></td><td>${t.close_reason||'—'}</td></tr>`;
      }).join('');
      rows += '</tbody></table>';
      thEl.innerHTML = rows;
    }

    // Control panel
    const ctrl = d.control || {};
    const ctrlEl = el('ctrlPanel');
    if(ctrl.override_mode === 'EMERGENCY') {
      ctrlEl.className = 'ctrl-err';
      ctrlEl.innerHTML = '🚨 <strong>EMERGENCY STOP ACTIVE</strong> — All positions closing';
    } else if(ctrl.freeze_new_trades) {
      ctrlEl.className = 'ctrl-warn';
      ctrlEl.innerHTML = '⏸️ <strong>Trading PAUSED</strong>' + (ctrl.freeze_reason ? ' · ' + ctrl.freeze_reason : '') + '<br><span style="font-size:10px">Message Catalyst on Telegram to resume</span>';
    } else {
      ctrlEl.className = 'ctrl-ok';
      ctrlEl.innerHTML = '✅ <strong>Trading ACTIVE</strong> · Normal mode · Daily loss limit: $' + (ctrl.daily_loss_limit||500) + (ctrl.vinod_notes ? '<br>📝 Note: ' + ctrl.vinod_notes : '');
    }

    // Sentiment / regime
    const sent = d.sentiment || {};
    if(sent.market_regime) el('regimeBadge').textContent = sent.market_regime;
    if(sent.fear_greed_value) {
      el('pFG').textContent = sent.fear_greed_value + ' / 100';
      el('cFG').textContent = sent.fear_greed_label || '';
    }

    // Last updated
    if(d.generated_at) {
      const dt = new Date(d.generated_at);
      el('deskUpdated').textContent = 'Desk data: ' + dt.toLocaleTimeString();
    }
  } catch(e) { console.warn('Desk data error:', e); }
}

async function loadPrices() {
  try {
    const r = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,ripple,binancecoin&vs_currencies=usd&include_24hr_change=true');
    const d = await r.json();
    const set = (id,pid,cid,val,chg) => {
      el(pid).textContent = '$'+Number(val).toLocaleString('en-US',{maximumFractionDigits:val<1?4:2});
      el(cid).textContent = (chg>=0?'+':'')+Number(chg).toFixed(2)+'% 24h';
      el(cid).className = 'pc '+(chg>=0?'u':'d');
    };
    if(d.bitcoin)     set('btc','pBTC','cBTC',d.bitcoin.usd,d.bitcoin.usd_24h_change);
    if(d.ethereum)    set('eth','pETH','cETH',d.ethereum.usd,d.ethereum.usd_24h_change);
    if(d.solana)      set('sol','pSOL','cSOL',d.solana.usd,d.solana.usd_24h_change);
    if(d.ripple)      set('xrp','pXRP','cXRP',d.ripple.usd,d.ripple.usd_24h_change);
    if(d.binancecoin) set('bnb','pBNB','cBNB',d.binancecoin.usd,d.binancecoin.usd_24h_change);
  } catch(e) {}
  try {
    const r = await fetch('https://api.alternative.me/fng/?limit=1');
    const f = await r.json();
    if(f.data?.[0] && !el('pFG').textContent.includes('/')) {
      el('pFG').textContent = f.data[0].value + ' / 100';
      el('cFG').textContent = f.data[0].value_classification;
    }
  } catch(e) {}
  try {
    const r = await fetch('https://api.gold-api.com/price/XAU');
    const g = await r.json();
    if(g.price) el('pGOLD').textContent = '$'+Number(g.price).toLocaleString('en-US',{maximumFractionDigits:2});
  } catch(e) { el('pGOLD').textContent = '—'; }
  try {
    const r = await fetch('https://api.coingecko.com/api/v3/global');
    const g = await r.json();
    if(g.data?.total_market_cap?.usd) {
      el('pMCAP').textContent = '$'+(g.data.total_market_cap.usd/1e12).toFixed(2)+'T';
      const chg = g.data.market_cap_change_percentage_24h_usd;
      el('cMCAP').textContent = (chg>=0?'+':'')+chg.toFixed(2)+'% 24h';
      el('cMCAP').className = 'pc '+(chg>=0?'u':'d');
    }
  } catch(e) {}
  el('priceUpdated').textContent = 'Prices: ' + new Date().toLocaleTimeString();
}

async function refreshAll() {
  await Promise.all([loadDeskData(), loadPrices()]);
  el('ts').textContent = 'Updated ' + new Date().toLocaleTimeString();
}

refreshAll();
setInterval(refreshAll, 60000);
</script>
</body>
</html>
'''

# Build the complete HTML
full_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>⚡ Catalyst Trading Desk</title>
<style>
:root{--bg:#0a0e1a;--s:#111827;--s2:#1a2234;--bd:#1f2d45;--ac:#3b82f6;--ac2:#6366f1;--gn:#10b981;--rd:#ef4444;--yw:#f59e0b;--tx:#e2e8f0;--mt:#64748b;--cd:#151e2e}
*{margin:0;padding:0;box-sizing:border-box}body{background:var(--bg);color:var(--tx);font-family:system-ui,-apple-system,sans-serif;font-size:13px}
.hdr{background:var(--s);border-bottom:1px solid var(--bd);padding:14px 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100}
.logo{display:flex;align-items:center;gap:10px}.li{width:36px;height:36px;background:linear-gradient(135deg,#