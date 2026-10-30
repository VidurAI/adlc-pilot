#!/bin/zsh
# Waits for the running Tier 1 evals to finish, then runs Tier 2 and Tier 3 detached.
# Idempotent/resumable: `adlc eval` skips run_ids already present in the out file.
cd /Users/hpatil/ADLC && source .toolchain/env.sh
export COPILOT_GITHUB_TOKEN="${COPILOT_GITHUB_TOKEN:-$(gh auth token)}"
K=adlc-kit/.venv/bin/adlc
while pgrep -f "adlc eval --tier 1" >/dev/null; do sleep 60; done
echo "$(date -u +%FT%TZ) tier1 finished; starting tier2" >> results/logs/tiers.log
$K eval --tier 2 --runs 3 --arms baseline,serena,graphify,graphify-guard --results results --out 2026-10-30-tier2.jsonl --timeout 1500 >> results/logs/tier2.log 2>&1
echo "$(date -u +%FT%TZ) tier2 finished; starting tier3" >> results/logs/tiers.log
$K eval --tier 3 --runs 3 --arms baseline,graphify,graphify-federated --results results --out 2026-10-30-tier3.jsonl --timeout 1500 >> results/logs/tier3.log 2>&1
echo "$(date -u +%FT%TZ) tier3 finished" >> results/logs/tiers.log
