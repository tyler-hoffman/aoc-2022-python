from dataclasses import dataclass
from functools import cached_property

from aoc_2022.day_15.models import Point, Range, Sensor
from aoc_2022.day_15.parser import Parser


@dataclass
class Day15PartASolver:
    sensors: list[Sensor]
    y: int

    @property
    def solution(self) -> int:
        ranges = self.covered_x_ranges_for_y(self.y)
        beacon_xs = {p.x for p in self.beacons_at_y(self.y)}

        range_total = sum(r.count for r in ranges)
        return range_total - len(beacon_xs)

    @cached_property
    def beacon_positions(self) -> set[Point]:
        return {s.closest_beacon for s in self.sensors}

    def beacons_at_y(self, y: int) -> list[Point]:
        return [s.closest_beacon for s in self.sensors if s.closest_beacon.y == y]

    def covered_x_ranges_for_y(self, y: int) -> list[Range]:
        sensor_ranges = [s.covered_x_range_for_y(y) for s in self.sensors]
        return self.merge_ranges([r for r in sensor_ranges if r])

    def merge_ranges(self, ranges: list[Range]) -> list[Range]:
        if ranges == []:
            return ranges
        ranges = sorted(ranges, key=lambda r: r.low)
        output = ranges[:1]
        for r in ranges[1:]:
            if r.low <= output[-1].high + 1:
                output[-1].high = max(r.high, output[-1].high)
            else:
                output.append(r)
        return output


def solve(input: str, y: int) -> int:
    data = Parser.parse(input)
    solver = Day15PartASolver(data, y)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_15/input.txt", "r") as f:
        input = f.read()
    return solve(input, 2000000)


if __name__ == "__main__":
    print(get_solution())
