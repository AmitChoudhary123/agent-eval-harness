# Benchmark Design

The harness is designed for small, understandable benchmark packs that business and engineering stakeholders can both inspect.

## Benchmark row

Each row represents one agent attempt against one task. The minimum fields are:

- agent
- task
- task_success
- evidence_coverage
- latency_ms
- latency_budget_ms
- cost_usd
- cost_budget_usd
- approval_compliant

## Extension ideas

- Add task categories
- Add severity and domain tags
- Add trace IDs
- Add evaluator model outputs
- Export leaderboard HTML for GitHub Pages