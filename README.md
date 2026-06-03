# Agent Eval Harness

Agent Eval Harness is a practical benchmark and release-readiness tool for AI agents and RAG workflows.

It helps teams answer one question clearly: **which agent run is good enough to ship, and why?**

## Why people should care

AI agent projects are moving fast, but most teams still compare them with anecdotes. This repo provides a small, transparent, reusable harness for scoring agent runs on business-relevant dimensions:

- Task success
- Evidence or citation coverage
- Latency budget
- Cost budget
- Approval compliance
- Safety incidents
- Rework required

## What you can run today

```bash
pip install -r requirements.txt
pytest -q
python -m agent_eval.cli score --input data/support_agent_runs.csv --profile configs/profiles/enterprise_default.yml
python -m agent_eval.cli score --input data/rag_agent_runs.csv --profile configs/profiles/rag_quality.yml --format markdown
```

## Demo

```bash
python demo/run_demo.py
```

The demo prints a leaderboard and shows which runs are release-ready.

## Features

- CSV benchmark input format
- YAML metric profiles
- Weighted scoring engine
- Release-readiness gates
- Markdown report renderer
- Sample benchmark packs for support agents and RAG agents
- Tests and CI
- Docs for designing repeatable agent evaluations

## Repository map

```text
agent_eval/              Scoring, profiles, reports, CLI
configs/profiles/        Metric weighting profiles
data/                    Sample benchmark runs
demo/                    One-command demo
docs/                    Metrics, benchmark design, usage, roadmap
tests/                   Unit and benchmark tests
```

## Community roadmap

- JSONL trace format
- GitHub Pages leaderboard publishing
- LangGraph / AutoGPT-style trace adapters
- RAGAS and custom evaluator hooks
- Domain benchmark packs for finance, legal, operations, and customer support

## Enterprise relevance

This project makes agent evaluation reviewable by engineers, product leaders, risk teams, and executives. It turns agent quality from opinion into a repeatable scorecard.