# Architecture

Agent Eval Harness is a small evaluation pipeline that turns benchmark runs into release-readiness decisions.

## Evaluation flow

```text
Benchmark CSV -> Metric profile YAML -> Normalized metrics -> Weighted score -> Hard gates -> Leaderboard -> Report
```

## Core components

- `load_runs`: reads benchmark rows from CSV
- `load_profile`: reads YAML metric weights and hard gates
- `normalized_metrics`: converts raw fields into comparable scores
- `score_run`: applies weights and release-readiness rules
- `leaderboard`: ranks candidate agent runs
- `reports`: renders text and Markdown outputs
- `cli`: executes repeatable benchmark scoring from terminal or CI

## Design decisions

- Inputs are plain CSV/YAML so business and technical stakeholders can inspect them
- Hard gates prevent averages from hiding governance failures
- Metric profiles make evaluation context-specific
- Reports are designed for release reviews, not only developer debugging
- The default path is deterministic and does not require API keys

## Extension model

Teams can add:

- New benchmark packs
- New metric profiles
- New scoring dimensions
- JSONL trace adapters
- HTML/GitHub Pages reporting
- Evaluator plugins for LLM-as-judge or RAG quality checks