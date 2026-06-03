from pathlib import Path

from agent_eval.profiles import load_profile
from agent_eval.reports import render_text
from agent_eval.scoring import leaderboard, load_runs

if __name__ == "__main__":
    rows = leaderboard(
        load_runs(Path("data/support_agent_runs.csv")),
        load_profile(Path("configs/profiles/enterprise_default.yml")),
    )
    print(render_text(rows))