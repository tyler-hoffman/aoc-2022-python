from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import cached_property
from typing import Mapping


class Resource(Enum):
    ORE = 1
    CLAY = 2
    OBSIDIAN = 3
    GEODE = 4


ResourceMap = dict[Resource, int]


def create_resource_map(ore=0, clay=0, obsidian=0, geode=0) -> ResourceMap:
    return {
        Resource.ORE: ore,
        Resource.CLAY: clay,
        Resource.OBSIDIAN: obsidian,
        Resource.GEODE: geode,
    }


def tuplize(resource_map: ResourceMap) -> tuple[int, int, int, int]:
    return (
        resource_map[Resource.ORE],
        resource_map[Resource.CLAY],
        resource_map[Resource.OBSIDIAN],
        resource_map[Resource.GEODE],
    )


@dataclass
class Blueprint:
    name: int
    robot_costs: Mapping[Resource, Mapping[Resource, int]]

    @cached_property
    def max_robots_needed(self) -> Mapping[Resource, int]:
        output: dict[Resource, int] = {}
        for r in Resource:
            output[r] = max({self.robot_costs[r2][r] for r2 in Resource})
        output[Resource.GEODE] = 1000
        return output
