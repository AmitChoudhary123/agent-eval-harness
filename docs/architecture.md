# Architecture

Agent Eval Harness is a transparent scoring layer for agent and RAG workflow results.

```text
Benchmark CSV -> Metric profile YAML -> Scoring engine -> Gates -> Leaderboard -> Report
```

## Components

- `profiles.py`: loads metric weights and hard gates
- `scoring.py`: normalizes metrics and calculates release readiness
- `reports.py`: renders text and Markdown leaderboards
- `cli.py`: command-line interface for repeatable scoring
- `data/`: sample benchmark packs

## Extension points

- Add new CSV columns and normalized metrics
- Add new YAML profiles by domain
- Add JSONL trace importers
- Add provider-specific adapters
- Export HTML leaderboards for GitHub Pages