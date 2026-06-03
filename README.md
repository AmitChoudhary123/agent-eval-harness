# Agent Eval Harness

A practical benchmark harness for evaluating AI agents and RAG workflows on task success, latency, cost, evidence, and governance.

## Why this exists

The AI agent ecosystem is noisy. Teams need a simple way to compare agents, prompts, tools, and retrieval strategies using repeatable tasks and transparent metrics.

## What it evaluates

- Task success
- Evidence or citation coverage
- Latency budget
- Cost budget
- Human approval compliance
- Overall release readiness

## Demo

```bash
python demo/run_demo.py
```

The demo scores three sample agent runs and prints a small leaderboard.

## Repository structure

```text
agent_eval/           Scoring and leaderboard engine
data/                 Sample task results
demo/                 Runnable benchmark demo
docs/                 Metrics and benchmark design
tests/                Unit tests
```

## Quick start

```bash
python -m venv .venv
pip install -r requirements.txt
pytest -q
python demo/run_demo.py
```

## Community roadmap

- Add JSONL benchmark format
- Add adapters for AutoGPT-style and LangGraph-style traces
- Add RAGAS/custom evaluator hooks
- Add GitHub Pages leaderboard output
- Add sample benchmark packs for support, finance, and compliance agents

## Enterprise relevance

This project gives AI leaders a reusable way to ask: should this agent be shipped, monitored, improved, or stopped?