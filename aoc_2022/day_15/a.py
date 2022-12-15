from dataclasses import dataclass
from functools import cached_property

from aoc_2022.day_15.models import Point, Sensor
from aoc_2022.day_15.parser import Parser


@dataclass
class Day15PartASolver:
    sensors: list[Sensor]
    y: int

    @property
    def solution(self) -> int:
        all_points: set[Point] = set()
        for sensor in self.sensors:
            all_points.update(self.points_for_sensor(sensor))
        return len(all_points.difference(self.beacon_positions))

    def points_for_sensor(self, sensor: Sensor) -> set[Point]:
        points: set[Point] = set()
        dist = abs(self.y - sensor.position.y)
        to_expand = 1 + sensor.range - dist
        if to_expand > 0:
            for i in range(to_expand):
                points.add(Point(sensor.position.x - i, self.y))
                points.add(Point(sensor.position.x + i, self.y))

        return points

    @cached_property
    def beacon_positions(self) -> set[Point]:
        return {s.closest_beacon for s in self.sensors}


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
