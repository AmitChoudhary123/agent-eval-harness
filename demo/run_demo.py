from pathlib import Path
from agent_eval import leaderboard, load_runs

if __name__ == "__main__":
    rows = leaderboard(load_runs(Path("data/sample_agent_runs.csv")))
    print("Agent leaderboard")
    for row in rows:
        print(f"{row['score']:.3f} | ready={row['release_ready']} | {row['agent']} | {row['task']}")