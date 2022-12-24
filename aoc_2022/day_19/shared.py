import math
from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterator

from aoc_2022.day_19.models import (
    Blueprint,
    Resource,
    ResourceMap,
    create_resource_map,
    tuplize,
)


@dataclass
class QualityChecker:
    blueprint: Blueprint
    max_time: int
    seen: set[tuple] = field(default_factory=set, init=False)

    @property
    def level(self) -> int:
        return self.blueprint.name * self.max_geodes

    @cached_property
    def max_geodes(self) -> int:
        resources = create_resource_map()
        robots = create_resource_map(ore=1)
        return max(self.get_max_geodes(0, resources, robots))

    def get_max_geodes(
        self,
        minute: int,
        resources: ResourceMap,
        robots: ResourceMap,
    ) -> Iterator[int]:
        key = (minute, tuplize(resources), tuplize(robots))

        if key not in self.seen:
            self.seen.add(key)

            remaining = self.max_time - minute
            could_get = self.robots_we_could_someday_afford(robots)
            should_get = self.should_get(remaining, resources, robots)
            to_do = could_get & should_get

            yield resources[Resource.GEODE] + remaining * robots[Resource.GEODE]

            for r in to_do:
                time_to_buy = self.time_until_we_can_buy(r, resources, robots)
                skip_time = time_to_buy + 1
                new_minute = minute + skip_time
                if new_minute < self.max_time:
                    cost = self.blueprint.robot_costs[r]
                    for robot_type, count in robots.items():
                        resources[robot_type] += count * skip_time
                    for r2, amt in cost.items():
                        resources[r2] -= amt
                    robots[r] += 1

                    yield from self.get_max_geodes(new_minute, resources, robots)

                    robots[r] -= 1
                    for r2, amt in cost.items():
                        resources[r2] += amt
                    for robot_type, count in robots.items():
                        resources[robot_type] -= count * skip_time

    def should_get(
        self,
        minutes_remaining: int,
        resources: ResourceMap,
        robots: ResourceMap,
    ) -> set[Resource]:
        output: set[Resource] = set()
        for r in Resource:
            current_potential = resources[r] + minutes_remaining * robots[r]
            max_desired = minutes_remaining * self.max_robots[r]
            if current_potential < max_desired:
                output.add(r)
        return output

    def time_until_we_can_buy(
        self,
        robot_type: Resource,
        resources: ResourceMap,
        robots: ResourceMap,
    ) -> int:
        highest_time: float = 0
        cost = self.blueprint.robot_costs[robot_type]
        for r in Resource:
            if robots[r] == 0:
                if cost[r] > 0:
                    raise Exception("WAT")
            else:
                time = (cost[r] - resources[r]) / robots[r]
                highest_time = max(highest_time, time)
        return math.ceil(highest_time)

    def robots_we_could_someday_afford(self, robots: ResourceMap) -> set[Resource]:
        output = {Resource.ORE, Resource.CLAY}
        if robots[Resource.CLAY] > 0:
            output.add(Resource.OBSIDIAN)
        if robots[Resource.OBSIDIAN] > 0:
            output.add(Resource.GEODE)
        return output

    @cached_property
    def max_robots(self) -> ResourceMap:
        output: ResourceMap = {r: 0 for r in Resource}
        for r in Resource:
            for cost in self.blueprint.robot_costs.values():
                output[r] = max(output[r], cost[r])
        output[Resource.GEODE] = self.max_time
        return output
