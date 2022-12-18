from dataclasses import dataclass
from functools import cached_property
from typing import Collection

from aoc_2022.day_18.models import Point3D
from aoc_2022.day_18.parser import Parser


@dataclass
class Day18PartBSolver:
    points: list[Point3D]

    @property
    def solution(self) -> int:
        outside_sides = self.sides(self.outside_points)
        lava_sides = self.sides(self.points)

        return len(outside_sides.intersection(lava_sides))

    @cached_property
    def outside_points(self) -> set[Point3D]:
        seen: set[Point3D] = set()
        to_check: list[Point3D] = []

        for x in range(self.bounds_min.x - 1, self.bounds_max.x + 2):
            for y in range(self.bounds_min.y - 1, self.bounds_max.y + 2):
                for z in range(self.bounds_min.z - 1, self.bounds_max.z + 2):
                    if any(
                        [
                            x == self.bounds_min.x - 1,
                            x == self.bounds_max.x + 1,
                            y == self.bounds_min.y - 1,
                            y == self.bounds_max.y + 1,
                            z == self.bounds_min.z - 1,
                            z == self.bounds_max.z + 1,
                        ]
                    ):
                        p = Point3D(x, y, z)
                        if p not in seen:
                            seen.add(p)
                            to_check.append(p)

        while to_check:
            start = to_check.pop()
            for p in self.neighbors(start):
                if all(
                    [
                        p not in seen,
                        self.in_bounds(p),
                        p not in self.points_set,
                    ]
                ):
                    seen.add(p)
                    to_check.append(p)

        return seen

    def neighbors(self, p: Point3D) -> list[Point3D]:
        return [
            Point3D(p.x, p.y, p.z - 1),
            Point3D(p.x, p.y, p.z + 1),
            Point3D(p.x, p.y - 1, p.z),
            Point3D(p.x, p.y + 1, p.z),
            Point3D(p.x - 1, p.y, p.z),
            Point3D(p.x + 1, p.y, p.z),
        ]

    def in_bounds(self, p: Point3D) -> bool:
        return all(
            [
                p.x >= self.bounds_min.x - 1,
                p.x <= self.bounds_max.x + 1,
                p.y >= self.bounds_min.y - 1,
                p.y <= self.bounds_max.y + 1,
                p.z >= self.bounds_min.z - 1,
                p.z <= self.bounds_max.z + 1,
            ]
        )

    @cached_property
    def bounds_min(self) -> Point3D:
        x = min({s.x for s in self.points})
        y = min({s.y for s in self.points})
        z = min({s.z for s in self.points})
        return Point3D(x, y, z)

    @cached_property
    def bounds_max(self) -> Point3D:
        x = max({s.x for s in self.points})
        y = max({s.y for s in self.points})
        z = max({s.z for s in self.points})
        return Point3D(x, y, z)

    @cached_property
    def points_set(self) -> set[Point3D]:
        return {p for p in self.points}

    def sides(self, points: Collection[Point3D]) -> set[Point3D]:
        output: set[Point3D] = set()
        for p in points:
            output.add(Point3D(p.x * 2, p.y * 2, p.z * 2 - 1))
            output.add(Point3D(p.x * 2, p.y * 2, p.z * 2 + 1))
            output.add(Point3D(p.x * 2, p.y * 2 - 1, p.z * 2))
            output.add(Point3D(p.x * 2, p.y * 2 + 1, p.z * 2))
            output.add(Point3D(p.x * 2 - 1, p.y * 2, p.z * 2))
            output.add(Point3D(p.x * 2 + 1, p.y * 2, p.z * 2))
        return output

    @cached_property
    def expanded_points(self) -> list[Point3D]:
        return [Point3D(p.x * 2, p.y * 2, p.z * 2) for p in self.points]


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day18PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_18/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
