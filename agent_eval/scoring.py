from __future__ import annotations

import csv
from pathlib import Path


def score_run(row: dict) -> dict:
    success = 1.0 if str(row["task_success"]).lower() == "true" else 0.0
    evidence = float(row["evidence_coverage"])
    latency = max(0.0, 1 - (float(row["latency_ms"]) / float(row["latency_budget_ms"])))
    cost = max(0.0, 1 - (float(row["cost_usd"]) / float(row["cost_budget_usd"])))
    approval = 1.0 if str(row["approval_compliant"]).lower() == "true" else 0.0
    score = (0.35 * success) + (0.25 * evidence) + (0.15 * latency) + (0.15 * cost) + (0.10 * approval)
    return {**row, "score": round(score, 3), "release_ready": score >= 0.75 and success == 1.0 and approval == 1.0}


def load_runs(path: str | Path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def leaderboard(rows: list[dict]) -> list[dict]:
    return sorted([score_run(row) for row in rows], key=lambda row: row["score"], reverse=True)