# Usage Guide

Score support agent runs:

```bash
python -m agent_eval.cli score --input data/support_agent_runs.csv --profile configs/profiles/enterprise_default.yml
```

Score RAG agent runs with a quality-heavy profile:

```bash
python -m agent_eval.cli score --input data/rag_agent_runs.csv --profile configs/profiles/rag_quality.yml --format markdown
```

## Add your own benchmark

Create a CSV with these columns:

```text
agent,task,task_success,evidence_coverage,latency_ms,latency_budget_ms,cost_usd,cost_budget_usd,approval_compliant,safety_incidents,rework_minutes
```

Then create or reuse a YAML profile from `configs/profiles/`.