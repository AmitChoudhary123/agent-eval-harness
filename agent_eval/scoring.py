from __future__ import annotations

import csv
from pathlib import Path

from .profiles import MetricProfile


def _bool(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def _float(row: dict, key: str, default: float = 0.0) -> float:
    value = row.get(key, default)
    return float(value if value not in {None, ""} else default)


def normalized_metrics(row: dict) -> dict[str, float]:
    latency_budget = max(_float(row, "latency_budget_ms", 1), 1)
    cost_budget = max(_float(row, "cost_budget_usd", 0.01), 0.01)
    rework = min(_float(row, "rework_minutes", 0) / 60, 1)
    safety_incidents = min(_float(row, "safety_incidents", 0), 3)
    return {
        "task_success": 1.0 if _bool(row.get("task_success")) else 0.0,
        "evidence_coverage": _float(row, "evidence_coverage"),
        "latency_budget": max(0.0, 1 - (_float(row, "latency_ms") / latency_budget)),
        "cost_budget": max(0.0, 1 - (_float(row, "cost_usd") / cost_budget)),
        "approval_compliance": 1.0 if _bool(row.get("approval_compliant")) else 0.0,
        "safety": max(0.0, 1 - (safety_incidents / 3)),
        "low_rework": max(0.0, 1 - rework),
    }


def hard_gate_passed(row: dict, profile: MetricProfile) -> bool:
    metrics = normalized_metrics(row)
    for gate in profile.hard_gates:
        if metrics.get(gate, 0.0) < 1.0:
            return False
    return True


def score_run(row: dict, profile: MetricProfile) -> dict:
    metrics = normalized_metrics(row)
    score = sum(metrics.get(metric, 0.0) * weight for metric, weight in profile.weights.items())
    gates_ok = hard_gate_passed(row, profile)
    release_ready = score >= profile.release_threshold and gates_ok
    reasons = []
    if not gates_ok:
        reasons.append("failed hard gate")
    if score < profile.release_threshold:
        reasons.append("below release threshold")
    if not reasons:
        reasons.append("release candidate")
    return {**row, "profile": profile.name, "metrics": metrics, "score": round(score, 3), "release_ready": release_ready, "decision_reason": "; ".join(reasons)}


def load_runs(path: str | Path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def leaderboard(rows: list[dict], profile: MetricProfile) -> list[dict]:
    return sorted([score_run(row, profile) for row in rows], key=lambda row: row["score"], reverse=True)