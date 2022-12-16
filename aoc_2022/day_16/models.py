from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Valve:
    name: str
    flow_rate: int
    leads_to: list[str]
    distance_to_valves: dict[str, int] = field(default_factory=dict)
