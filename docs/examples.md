# Examples

## Support agent benchmark

```bash
python -m agent_eval.cli score --input data/support_agent_runs.csv --profile configs/profiles/enterprise_default.yml
```

Use this to compare support automation agents on task completion, evidence, cost, latency, approval compliance, incidents, and rework.

## RAG quality benchmark

```bash
python -m agent_eval.cli score --input data/rag_agent_runs.csv --profile configs/profiles/rag_quality.yml --format markdown
```

Use this to compare retrieval and answer-generation strategies where evidence quality matters more than speed.

## Create a custom profile

Copy a YAML file under `configs/profiles/` and adjust weights. Example: make latency more important for voice agents, or evidence more important for regulated knowledge workflows.