#!/usr/bin/env python3
"""
Daily sync: push all agent configs, prompts, learning files to agent_desk GitHub repo.
Runs at 6:00 PM ET (23:00 UTC) Mon-Sun.
"""

import os
import subprocess
import shutil
from datetime import datetime, timezone

WORKSPACE = "/sandbox/.openclaw/workspace/trading"
GH_TOKEN  = "GH_TOKEN_REDACTED"
GH_REPO   = f"https://tvinod09:{GH_TOKEN}@github.com/tvinod09/agent_desk.git"
GIT_DIR   = "/tmp/agent_desk_sync"

def run(cmd, cwd=GIT_DIR, check=True):
    env = os.environ.copy()
    env["https_proxy"] = "http://10.200.0.1:3128"
    env["HTTPS_PROXY"] = "http://10.200.0.1:3128"
    env["GIT_TERMINAL_PROMPT"] = "0"
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, env=env)
    if r.stdout.strip():
        print(r.stdout.strip())
    if r.stderr.strip() and ("error" in r.stderr.lower() or "fatal" in r.stderr.lower()):
        print("STDERR:", r.stderr.strip())
    return r

def ts():
    return datetime.now(timezone.utc).strftime("%H:%M:%S")

def ensure_repo():
    if not os.path.isdir(os.path.join(GIT_DIR, ".git")):
        os.makedirs(GIT_DIR, exist_ok=True)
        run(f"git clone {GH_REPO} .", cwd=GIT_DIR)
    else:
        run("git fetch origin main")
        run("git checkout main")
        run("git reset --hard origin/main")

def copy_files():
    W = WORKSPACE

    def cp(src, dst=None):
        if dst is None:
            dst = os.path.basename(src)
        dst_path = os.path.join(GIT_DIR, dst)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        try:
            shutil.copy2(src, dst_path)
        except FileNotFoundError:
            print(f"  skip (not found): {src}")

    def cpdir(src_dir, dst_dir):
        src = os.path.join(W, src_dir)
        dst = os.path.join(GIT_DIR, dst_dir)
        os.makedirs(dst, exist_ok=True)
        if os.path.isdir(src):
            for f in os.listdir(src):
                fp = os.path.join(src, f)
                if os.path.isfile(fp):
                    shutil.copy2(fp, os.path.join(dst, f))

    # Root agent files
    for name in ["ALPHA", "BETA", "GAMMA", "DELTA", "EPSILON", "ZETA", "ETA", "THETA"]:
        cp(f"{W}/{name}_PROMPT.md")

    for f in ["MASTER.md", "AUTONOMOUS_CHARTER.md", "DEBATE_PROTOCOL.md",
              "VINOD_CONTROL.json", "VINOD_CONTROL.md", "STATUS.md"]:
        cp(f"{W}/{f}")

    # Directories
    cpdir("learning", "learning")
    cpdir("intelligence", "intelligence")
    cpdir("positions", "positions")
    cpdir("rewards", "rewards")
    cpdir("logs", "logs")

    # Dashboard scripts only (scrub token from publish.py)
    dash_dst = os.path.join(GIT_DIR, "dashboard")
    os.makedirs(dash_dst, exist_ok=True)
    for f in ["publish.py", "serve.sh", "build_html.py"]:
        src = os.path.join(W, "dashboard", f)
        if os.path.exists(src):
            content = open(src).read()
            # Scrub any hardcoded token
            content = content.replace(GH_TOKEN, "YOUR_GITHUB_TOKEN_HERE")
            open(os.path.join(dash_dst, f), "w").write(content)

def push():
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    run("git config user.email 'catalyst@trading.desk'")
    run("git config user.name 'Catalyst'")
    run("git add -A")

    # Check if anything changed
    r = run("git diff --cached --stat")
    if not r.stdout.strip():
        print(f"[{ts()}] Nothing changed — skipping push")
        return

    run(f'git commit -m "Daily sync: {now_utc}"')
    r = run(f"git push origin main")
    if r.returncode == 0:
        print(f"[{ts()}] ✅ Pushed to https://github.com/tvinod09/agent_desk")
    else:
        print(f"[{ts()}] ❌ Push failed")

if __name__ == "__main__":
    print(f"[{ts()}] Starting agent_desk sync...")
    ensure_repo()
    copy_files()
    push()
    print(f"[{ts()}] Done.")
