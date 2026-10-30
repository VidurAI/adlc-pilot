# Adoption test — kestrel-notify

Started 2026-10-30T13:48:38+00:00 (UTC). Following ADOPT.md only.

## 0 install kit — OK — 0.1s

```
adlc 0.1.0
```

## 1 adlc init — OK — 0.1s

```
created  AGENTS.md
  created  .mcp.json
  created  .serena/adlc-context.yml
  created  .serena/project.yml
  created  .serena/memories/.gitkeep
  created  .serena/.gitignore
  created  .github/skills/graphify/SKILL.md
  created  .github/skills/graphify/.graphify_version
  created  .github/skills/graphify/references/transcribe.md
  created  .github/skills/graphify/references/github-and-merge.md
  created  .github/skills/graphify/references/query.md
  created  .github/skills/graphify/references/exports.md
  created  .github/skills/graphify/references/extraction-spec.md
  created  .github/skills/graphify/references/update.md
  created  .github/skills/graphify/references/hooks.md
  created  .github/skills/graphify/references/add-watch.md
  created  .graphifyrc
  created  .github/workflows/adlc.yml
  created  .devcontainer/devcontainer.json
  created  renovate.json
  updated  .gitignore
adlc init done — kestrel-notify (kit 0.1.0, schema 1). Fill the TODOs in AGENTS.md, then `adlc doctor`.
```

## 2 fill AGENTS.md prose — OK — 0.0s

```
prose filled from ADOPTION_PROSE.md
```

## 3 adlc doctor — OK — 0.2s

```
adlc doctor — kestrel-notify (kit 0.1.0)
  [32mOK [0m  contract lint                      1 warning(s)
  [32mOK [0m    lint warning                     artifact graphify-out/graph.json not built yet (`adlc baseline`)
  [32mOK [0m  AGENTS.md adlc block               schema 1, kit 0.1.0, context graphify,serena
  [32mOK [0m  env COPILOT_GITHUB_TOKEN           present
  [32mOK [0m  env GRAPHIFY_BACKEND               none
  [33mWARN[0m  no LLM API keys in env             OPENAI_API_KEY
  [32mOK [0m  graphify version == pin            0.9.97 vs 0.9.97
  [32mOK [0m  copilot CLI version == pin         GitHub Copilot CLI 1.0.105. vs 1.0.105
  [32mOK [0m  uvx available (Serena launcher)    /Users/hpatil/.local/bin/uvx
  [32mOK [0m  .mcp.json serena pin               ede329aaf0c8
  [32mOK [0m  language server: python            PATH:pyright
  [32mOK [0m  artifact freshness                 not built yet — run `adlc baseline`
  [32mOK [0m  .github/workflows/adlc.yml         
  [32mOK [0m  .devcontainer/devcontainer.json    
  [32mOK [0m  renovate.json                      
  [32mOK [0m  .graphifyrc                        
doctor: all green
```

## 4 adlc baseline — OK — 1.5s

```
baseline full: 317 nodes, 743 edges, 1.4s, stamped 0dcc40ccdd (dirty)
```

## 4b adlc stale — OK — 0.1s

```
[repo] FRESH: graphify-out/graph.json stamped 0dcc40ccdd, HEAD 0dcc40ccdd, 0 commits behind (threshold 10)
```

## 3b adlc doctor (after baseline) — OK — 0.2s

```
adlc doctor — kestrel-notify (kit 0.1.0)
  [32mOK [0m  contract lint                      0 warning(s)
  [32mOK [0m  AGENTS.md adlc block               schema 1, kit 0.1.0, context graphify,serena
  [32mOK [0m  env COPILOT_GITHUB_TOKEN           present
  [32mOK [0m  env GRAPHIFY_BACKEND               none
  [33mWARN[0m  no LLM API keys in env             OPENAI_API_KEY
  [32mOK [0m  graphify version == pin            0.9.97 vs 0.9.97
  [32mOK [0m  copilot CLI version == pin         GitHub Copilot CLI 1.0.105. vs 1.0.105
  [32mOK [0m  uvx available (Serena launcher)    /Users/hpatil/.local/bin/uvx
  [32mOK [0m  .mcp.json serena pin               ede329aaf0c8
  [32mOK [0m  language server: python            PATH:pyright
  [32mOK [0m  artifact freshness                 [repo] FRESH: graphify-out/graph.json stamped 0dcc40ccdd, HEAD 0dcc40ccdd, 0 commits behind (threshold 10)
  [32mOK [0m  .github/workflows/adlc.yml         
  [32mOK [0m  .devcontainer/devcontainer.json    
  [32mOK [0m  renovate.json                      
  [32mOK [0m  .graphifyrc                        
doctor: all green
```

## 6 commit — OK — 0.0s

```

```

## 5 one golden task in two arms — OK — 63.6s

```
nfy-001__baseline__r1: score=2 tokens=18+1351 calls=6 wall=25926ms
nfy-001__graphify__r1: score=2 tokens=13920+2178 calls=10 wall=27430ms
eval: 2 new run(s) → /Users/hpatil/ADLC/results/adoption-runs/adoption.jsonl
```

## Result

Elapsed **1.1 min**. Deviations: 0 (none)
