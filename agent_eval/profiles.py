from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class MetricProfile:
    name: str
    weights: dict[str, float]
    release_threshold: float
    hard_gates: list[str]


def load_profile(path: str | Path) -> MetricProfile:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return MetricProfile(
        name=data["name"],
        weights={key: float(value) for key, value in data["weights"].items()},
        release_threshold=float(data.get("release_threshold", 0.75)),
        hard_gates=list(data.get("hard_gates", [])),
    )