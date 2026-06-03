# Agent Eval Harness

Benchmark and release-readiness harness for evaluating AI agents and RAG workflows on task success, evidence, latency, cost, safety, and governance.

## Business problem

Enterprises are building agents faster than they can evaluate them. Teams compare prompts, frameworks, and models through demos, but release decisions often lack consistent metrics, hard gates, and business-readable evidence.

## Why it matters

Agent and RAG failures are rarely only model failures. They are operating failures: missing evidence, uncontrolled cost, latency breaches, skipped approvals, safety incidents, and too much manual rework. Leaders need a repeatable way to decide whether an agent is ready to pilot, scale, or stop.

## Method / solution overview

Agent Eval Harness provides a transparent evaluation workflow:

- CSV benchmark packs capture agent runs
- YAML metric profiles define weights and hard gates
- The scoring engine normalizes success, evidence, latency, cost, approval, safety, and rework
- Release-readiness rules prevent high scores from hiding failed controls
- Text and Markdown reports make results usable in architecture and leadership reviews
- Tests and CI validate benchmark behavior

## Results / expected impact

This project helps teams:

- Compare agent designs with consistent metrics
- Create release gates for agent and RAG workflows
- Expose tradeoffs between quality, speed, cost, and governance
- Turn evaluation into an operating discipline instead of an ad hoc review
- Give enterprise stakeholders a clear scorecard for AI readiness

## Repository structure

```text
agent_eval/             CLI, scoring engine, metric profiles, reports
configs/profiles/       Evaluation profiles for enterprise and RAG quality use cases
data/                   Sample support-agent and RAG-agent benchmark runs
demo/                   One-command benchmark demo
docs/                   Architecture, business case, roadmap, executive POV
tests/                  Scoring and leaderboard tests
.github/workflows/      CI workflow
```

## Setup

```bash
python -m venv .venv
pip install -r requirements.txt
pytest -q
python demo/run_demo.py
```

Run a benchmark:

```bash
python -m agent_eval.cli score --input data/rag_agent_runs.csv --profile configs/profiles/rag_quality.yml --format markdown
```

## Roadmap

- Add JSONL trace import for agent frameworks
- Add HTML/GitHub Pages leaderboard publishing
- Add evaluator plugin hooks
- Add benchmark packs for finance, legal, customer support, and compliance
- Add trend reports across benchmark runs