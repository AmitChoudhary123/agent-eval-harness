from pathlib import Path

from agent_eval.profiles import load_profile
from agent_eval.scoring import leaderboard, load_runs, score_run


def test_score_requires_approval_for_release():
    profile = load_profile(Path("configs/profiles/enterprise_default.yml"))
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
        "safety_incidents": "0",
        "rework_minutes": "0",
    }
    assert score_run(row, profile)["release_ready"] is False


def test_support_leaderboard_orders_runs():
    profile = load_profile(Path("configs/profiles/enterprise_default.yml"))
    rows = leaderboard(load_runs(Path("data/support_agent_runs.csv")), profile)
    assert rows[0]["agent"] == "support-agent-v1"
    assert rows[0]["release_ready"] is True


def test_rag_profile_rewards_evidence():
    profile = load_profile(Path("configs/profiles/rag_quality.yml"))
    rows = leaderboard(load_runs(Path("data/rag_agent_runs.csv")), profile)
    assert rows[0]["agent"] == "rag-hybrid-rerank"
    assert rows[-1]["release_ready"] is False