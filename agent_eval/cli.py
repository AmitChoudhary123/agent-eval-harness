from __future__ import annotations

import argparse

from .profiles import load_profile
from .reports import render_markdown, render_text
from .scoring import leaderboard, load_runs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score AI agent benchmark runs")
    sub = parser.add_subparsers(dest="command", required=True)
    score = sub.add_parser("score", help="Score benchmark rows")
    score.add_argument("--input", required=True, help="CSV benchmark file")
    score.add_argument("--profile", required=True, help="YAML metric profile")
    score.add_argument("--format", choices=["text", "markdown"], default="text")
    args = parser.parse_args(argv)

    if args.command == "score":
        rows = leaderboard(load_runs(args.input), load_profile(args.profile))
        print(render_markdown(rows) if args.format == "markdown" else render_text(rows))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())