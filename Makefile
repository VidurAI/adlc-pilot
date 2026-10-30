# Thin wrapper over `adlc`. `make all` reproduces every number in the report.
SHELL := /bin/zsh
ROOT  := $(abspath .)
KIT   := $(ROOT)/adlc-kit
ADLC  := $(KIT)/.venv/bin/adlc
ENV   := source $(ROOT)/.toolchain/env.sh;
REPOS := kestrel-services kestrel-web kestrel-ops
export GRAPHIFY_BACKEND=none

.PHONY: all org kit init doctor baseline federate tasks tier1 tier2 tier3 scorecard monitor adoption clean-runs

kit:               ## install the kit into its own venv (editable) and lock
	cd $(KIT) && uv venv -q -p 3.12 .venv && uv pip install -q -p .venv/bin/python -e ".[dev]" && uv lock -q && .venv/bin/adlc pins && .venv/bin/pytest -q

org:               ## Phase 1 acceptance: build all Kestrel repos from scratch, all suites green
	$(ENV) cd repos/kestrel-services/booking && mvn -q test
	$(ENV) cd repos/kestrel-services/pricing && dotnet test --nologo -v q
	cd repos/kestrel-services/gateway && uv venv -q -p 3.12 .venv && uv pip install -q -p .venv/bin/python -e ".[dev]" && .venv/bin/pytest -q
	cd repos/kestrel-web && npm ci --silent && npm test --silent
	@for r in $(REPOS); do echo "$$r: $$(git -C repos/$$r rev-list --count HEAD) commits"; done

init:              ## Phase 2: onboard every Kestrel repo via the kit (never by hand)
	for r in $(REPOS); do $(ADLC) init --repo repos/$$r --yes; done

doctor:
	for r in $(REPOS); do (cd repos/$$r && $(ADLC) doctor); done

baseline:          ## build + stamp L0 graphs
	for r in $(REPOS); do (cd repos/$$r && $(ADLC) baseline); done

federate:          ## L1 project graph + L2 org graph
	cd org/kestrel-project && $(ADLC) federate && $(ADLC) federate --level org --out ../.github-private

tasks:
	$(ADLC) eval --lint

tier1:
	$(ADLC) eval --tier 1 --runs 3 --results results

tier2:
	$(ADLC) eval --tier 2 --runs 3 --results results

tier3:
	$(ADLC) eval --tier 3 --runs 3 --results results

scorecard:
	$(ADLC) scorecard --results results --out results/scorecard.md --html results/scorecard.html

monitor:
	$(ADLC) stale --all; $(ADLC) regress --dry-run; $(ADLC) scorecard --trend --results results

adoption:
	$(ADLC) eval --adoption-test repos/kestrel-notify

all: kit org init doctor baseline federate tasks tier1 scorecard

clean-runs:
	rm -rf results/runs
