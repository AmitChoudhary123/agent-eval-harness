# Report Example

Run:

```bash
python -m agent_eval.cli score --input data/rag_agent_runs.csv --profile configs/profiles/rag_quality.yml --format markdown
```

Example interpretation:

- `rag-hybrid-rerank` wins because evidence coverage is high while cost and latency remain acceptable.
- `rag-agent-no-citations` fails even if it is fast because evidence coverage is too low for a RAG quality profile.
- `rag-fast-cheap` shows why low cost is not enough when task success fails.

Use this style of report in architecture reviews, release readiness meetings, and model/provider comparisons.