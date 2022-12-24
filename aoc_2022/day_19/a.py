import math
from dataclasses import dataclass, field
from functools import cached_property
from typing import Any

from aoc_2022.day_19.models import (
    Blueprint,
    Resource,
    ResourceMap,
    create_resource_map,
    tuplize,
)
from aoc_2022.day_19.parser import Parser


@dataclass
class Day19PartASolver:
    blueprints: list[Blueprint]

    @property
    def solution(self) -> int:
        quality_checkers = [QualityChecker(blueprint) for blueprint in self.blueprints]
        quality_levels = [quality_checker.level for quality_checker in quality_checkers]
        return sum(quality_levels)


@dataclass
class QualityChecker:
    blueprint: Blueprint
    max_time = 24
    seen: dict[Any, int] = field(default_factory=dict, init=False)

    @property
    def level(self) -> int:
        x = self.blueprint.name * self.max_geodes
        return x

    @cached_property
    def max_geodes(self) -> int:
        return self.get_max_geodes(0, create_resource_map(), create_resource_map(ore=1))

    def get_max_geodes(
        self, minute: int, resources: ResourceMap, robots: ResourceMap
    ) -> int:
        key = (minute, tuplize(resources), tuplize(robots))

        if key in self.seen:
            return self.seen[key]

        best = 0
        could_get = self.robots_we_could_someday_afford(robots)
        should_get = self.robots_under_the_max(robots)
        to_do = could_get & should_get
        for r in to_do:
            time_to_buy = self.time_until_we_can_buy(r, resources, robots)
            skip_time = time_to_buy + 1
            new_minute = minute + skip_time
            if new_minute >= self.max_time:
                minutes_left = self.max_time - minute
                count = (
                    resources[Resource.GEODE] + minutes_left * robots[Resource.GEODE]
                )
                best = max(best, count)
            else:
                cost = self.blueprint.robot_costs[r]
                for robot_type, count in robots.items():
                    resources[robot_type] += count * skip_time
                for r2, amt in cost.items():
                    resources[r2] -= amt
                robots[r] += 1

                best_for_resource = self.get_max_geodes(new_minute, resources, robots)
                best = max(best, best_for_resource)

                robots[r] -= 1
                for r2, amt in cost.items():
                    resources[r2] += amt
                for robot_type, count in robots.items():
                    resources[robot_type] -= count * skip_time

        self.seen[key] = best
        return best

    def time_until_we_can_buy(
        self,
        robot_type: Resource,
        resources: ResourceMap,
        robots: ResourceMap,
    ) -> int:
        highest_time = 0
        cost = self.blueprint.robot_costs[robot_type]
        for r in Resource:
            if robots[r] == 0:
                if cost[r] > 0:
                    raise Exception("WAT")
            else:
                time = math.ceil((cost[r] - resources[r]) / robots[r])
                highest_time = max(highest_time, time)
        return highest_time

    def robots_we_could_someday_afford(self, robots: ResourceMap) -> set[Resource]:
        output = {Resource.ORE, Resource.CLAY}
        if robots[Resource.CLAY] > 0:
            output.add(Resource.OBSIDIAN)
        if robots[Resource.OBSIDIAN] > 0:
            output.add(Resource.GEODE)
        return output

    def robots_under_the_max(self, robots: ResourceMap) -> set[Resource]:
        return {r for r, amt in robots.items() if amt < self.max_robots[r]}

    @cached_property
    def max_robots(self) -> ResourceMap:
        output: ResourceMap = {r: 0 for r in Resource}
        for r in Resource:
            for cost in self.blueprint.robot_costs.values():
                output[r] = max(output[r], cost[r])
        output[Resource.GEODE] = self.max_time
        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day19PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_19/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
