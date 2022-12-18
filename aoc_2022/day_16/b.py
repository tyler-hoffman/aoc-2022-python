from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterator, Mapping

from aoc_2022.day_16.models import Valve
from aoc_2022.day_16.parser import Parser


@dataclass(frozen=True)
class Day16PartBSolver:
    valves: dict[str, Valve] = field(hash=False)
    total_minutes: int = 26

    @property
    def solution(self) -> int:
        return max(
            self.get_total_flows(
                "AA",
                "AA",
                self.total_minutes,
                self.total_minutes,
                0,
                self.valves_that_can_flow,
            )
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

    @cached_property
    def keys_seen(self) -> set[tuple]:
        return set()

    def create_key(
        self, pos_a: str, pos_b: str, min_a: int, min_b: int, so_far: int
    ) -> tuple:
        if pos_a < pos_b:
            return (pos_a, pos_b, min_a, min_b, so_far)
        elif pos_a > pos_b:
            return (pos_b, pos_a, min_b, min_a, so_far)
        elif min_a < min_b:
            return (pos_a, pos_b, min_a, min_b, so_far)
        else:
            return (pos_b, pos_a, min_b, min_a, so_far)

    def get_total_flows(
        self,
        you: str,
        elephant: str,
        you_minutes_remaining: int,
        elephant_minutes_remaining: int,
        flow_so_far: int,
        remaining: set[str],
    ) -> Iterator[int]:
        key = self.create_key(
            you,
            elephant,
            you_minutes_remaining,
            elephant_minutes_remaining,
            flow_so_far,
        )
        if key in self.keys_seen:
            return

        self.keys_seen.add(key)

        for dest in remaining:

            you_dist = self.dist_map[you][dest]
            new_you_minutes_remaining = you_minutes_remaining - you_dist - 1

            if new_you_minutes_remaining > 0:
                new_flow_so_far = (
                    flow_so_far + new_you_minutes_remaining * self.flow_rate_map[dest]
                )
                remaining.remove(dest)
                yield new_flow_so_far
                yield from self.get_total_flows(
                    dest,
                    elephant,
                    new_you_minutes_remaining,
                    elephant_minutes_remaining,
                    new_flow_so_far,
                    remaining,
                )
                remaining.add(dest)

            elephant_dist = self.dist_map[elephant][dest]
            new_elephant_minutes_remaining = (
                elephant_minutes_remaining - elephant_dist - 1
            )
            if new_elephant_minutes_remaining > 0:
                new_flow_so_far = (
                    flow_so_far
                    + new_elephant_minutes_remaining * self.flow_rate_map[dest]
                )
                remaining.remove(dest)
                yield new_flow_so_far
                yield from self.get_total_flows(
                    you,
                    dest,
                    you_minutes_remaining,
                    new_elephant_minutes_remaining,
                    new_flow_so_far,
                    remaining,
                )
                remaining.add(dest)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day16PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_16/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
