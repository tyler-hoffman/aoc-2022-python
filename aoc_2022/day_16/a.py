from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterator, Mapping

from aoc_2022.day_16.models import Valve
from aoc_2022.day_16.parser import Parser


@dataclass(frozen=True)
class Day16PartASolver:
    valves: dict[str, Valve] = field(hash=False)
    total_minutes: int = 30

    @property
    def solution(self) -> int:
        return max(
            self.get_total_flows("AA", self.total_minutes, 0, self.valves_that_can_flow)
        )

    @cached_property
    def names(self) -> list[str]:
        return list(self.valves.keys())

    @cached_property
    def flow_rate_map(self) -> Mapping[str, int]:
        return {v.name: v.flow_rate for v in self.valves.values()}

    @cached_property
    def valves_that_can_flow(self) -> set[str]:
        return {name for name, flow_rate in self.flow_rate_map.items() if flow_rate > 0}

    @cached_property
    def dist_map(self) -> Mapping[str, Mapping[str, int]]:
        output: dict[str, dict[str, int]] = {name: {name: 0} for name in self.names}
        for start_name in self.names:
            for dest in self.valves[start_name].leads_to:
                output[start_name][dest] = 1
                output[dest][start_name] = 1

        changing = True
        while changing:
            changing = False
            for start_name in self.names:
                start = output[start_name]
                for mid_name in list(start.keys()):
                    mid = output[mid_name]
                    for end_name in list(mid.keys()):
                        new_length = start[mid_name] + mid[end_name]
                        if end_name not in start or new_length < start[end_name]:
                            output[end_name][start_name] = new_length
                            output[start_name][end_name] = new_length
                            changing = True

        return output

    def get_total_flows(
        self,
        current: str,
        minutes_remaining: int,
        flow_so_far: int,
        remaining: set[str],
    ) -> Iterator[int]:
        for dest in remaining:
            dist = self.dist_map[current][dest]
            new_minutes_remaining = minutes_remaining - dist - 1
            if new_minutes_remaining > 0:
                new_flow_so_far = (
                    flow_so_far + new_minutes_remaining * self.flow_rate_map[dest]
                )
                remaining.remove(dest)
                yield new_flow_so_far
                yield from self.get_total_flows(
                    dest, new_minutes_remaining, new_flow_so_far, remaining
                )
                remaining.add(dest)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day16PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_16/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
