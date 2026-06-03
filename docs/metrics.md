# Metrics

Agent Eval Harness uses a transparent weighted score:

- Task success: 35%
- Evidence coverage: 25%
- Latency budget: 15%
- Cost budget: 15%
- Approval compliance: 10%

A run is release-ready only when the score is at least 0.75, the task succeeded, and required approval controls were followed.