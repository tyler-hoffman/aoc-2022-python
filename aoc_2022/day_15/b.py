from dataclasses import dataclass
from functools import cached_property

from aoc_2022.day_15.models import Point, Range, Sensor
from aoc_2022.day_15.parser import Parser


@dataclass
class Day15PartBSolver:
    sensors: list[Sensor]
    max_coordinate: int
    min_coordinate: int = 0

    @property
    def solution(self) -> int:
        for y in range(self.min_coordinate, self.max_coordinate + 1):
            x_ranges = self.covered_x_ranges_for_y(y)
            if len(x_ranges) == 2:
                return self.tuning_fequency(Point(x_ranges[0].high + 1, y))
        assert False, "We shouldn't get here lol"

    def tuning_fequency(self, point: Point) -> int:
        return point.x * 4000000 + point.y

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


def solve(input: str, max_coordinate: int) -> int:
    data = Parser.parse(input)
    solver = Day15PartBSolver(data, max_coordinate)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_15/input.txt", "r") as f:
        input = f.read()
    return solve(input, 4000000)


if __name__ == "__main__":
    print(get_solution())
