# Metrics

Agent Eval Harness converts raw run data into normalized metrics.

## Metrics

- `task_success`: 1 when the agent completed the task
- `evidence_coverage`: citation/evidence quality, from 0 to 1
- `latency_budget`: how much latency budget remains
- `cost_budget`: how much cost budget remains
- `approval_compliance`: whether required human approval was followed
- `safety`: penalty for safety incidents
- `low_rework`: penalty for manual rework minutes

## Hard gates

Profiles can define hard gates. If a hard gate fails, the run cannot be release-ready even with a high weighted score.

This is important for enterprise AI because some failures are not averageable. For example, missing approval on a regulated action should block release.