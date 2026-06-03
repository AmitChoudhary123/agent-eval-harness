from pathlib import Path
from agent_eval import leaderboard, load_runs, score_run


def test_score_requires_approval_for_release():
    row = {
        "agent": "x",
        "task": "risky task",
        "task_success": "true",
        "evidence_coverage": "0.95",
        "latency_ms": "1000",
        "latency_budget_ms": "3000",
        "cost_usd": "0.01",
        "cost_budget_usd": "0.05",
        "approval_compliant": "false",
    }
    assert score_run(row)["release_ready"] is False


def test_leaderboard_orders_runs():
    rows = leaderboard(load_runs(Path("data/sample_agent_runs.csv")))
    assert rows[0]["agent"] == "support-agent-v1"
    assert rows[0]["release_ready"] is True