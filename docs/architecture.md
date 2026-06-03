# Architecture

Agent Eval Harness is a transparent scoring layer for agent and RAG workflow results.

## Flow

```text
Benchmark rows -> Scoring engine -> Release readiness rules -> Leaderboard -> Improvement backlog
```

## Components

- `load_runs`: reads benchmark rows from CSV
- `score_run`: applies weighted task, evidence, latency, cost, and approval metrics
- `leaderboard`: ranks candidate agents by score
- `demo/run_demo.py`: prints a reviewable leaderboard
- `docs/metrics.md`: explains metric weights and release-readiness rules

## Design principles

- Benchmarks should be readable by business and engineering stakeholders
- Governance should be measured, not buried in prose
- Scores should be explainable enough to challenge
- Adapters can be added later for traces from popular agent frameworks