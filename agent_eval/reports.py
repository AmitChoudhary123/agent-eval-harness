from __future__ import annotations


def render_text(rows: list[dict]) -> str:
    lines = ["Agent leaderboard", "================="]
    for index, row in enumerate(rows, 1):
        lines.append(f"{index}. {row['agent']} | score={row['score']:.3f} | ready={row['release_ready']} | {row['decision_reason']}")
    return "\n".join(lines)


def render_markdown(rows: list[dict]) -> str:
    lines = ["# Agent Evaluation Leaderboard", "", "| Rank | Agent | Task | Score | Ready | Reason |", "| --- | --- | --- | ---: | --- | --- |"]
    for index, row in enumerate(rows, 1):
        lines.append(f"| {index} | {row['agent']} | {row['task']} | {row['score']:.3f} | {row['release_ready']} | {row['decision_reason']} |")
    lines.extend(["", "## Metric Detail"])
    for row in rows:
        lines.append(f"### {row['agent']}")
        for metric, value in row["metrics"].items():
            lines.append(f"- {metric}: {value:.3f}")
    return "\n".join(lines)