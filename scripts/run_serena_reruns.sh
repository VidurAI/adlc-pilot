#!/usr/bin/env bash
# Waits for the serena-forced Tier 1 run to exit, then re-runs the plain serena arm where it
# had been measured with Serena absent (kestrel-services Tier 1 + all of Tier 2). Sequential
# on purpose: wall-clock is a reported metric.
set -u
cd "$(dirname "$0")/.."
source .toolchain/env.sh
export COPILOT_GITHUB_TOKEN="${COPILOT_GITHUB_TOKEN:-$(gh auth token)}"
while pgrep -f "arms serena-forced" >/dev/null; do sleep 30; done
ADLC=adlc-kit/.venv/bin/adlc
$ADLC eval --tier 1 --arms serena --repo kestrel-services --runs 3 --results results --out 2026-11-01-tier1-serena-rerun.jsonl
$ADLC eval --tier 2 --arms serena --runs 3 --results results --out 2026-11-01-tier2-serena-rerun.jsonl
echo "SERENA RERUNS DONE"
