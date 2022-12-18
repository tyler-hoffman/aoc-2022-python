from dataclasses import dataclass
from typing import Iterator

from aoc_2022.day_18.models import Point3D
from aoc_2022.day_18.parser import Parser


@dataclass
class Day18PartASolver:
    points: list[Point3D]

    @property
    def solution(self) -> int:
        freq_map: dict[Point3D, int] = {}
        for side in self.sides():
            if side not in freq_map:
                freq_map[side] = 0
            freq_map[side] += 1

        return len([count for count in freq_map.values() if count == 1])

    def sides(self) -> Iterator[Point3D]:
        for p in self.points:
            yield Point3D(p.x * 2, p.y * 2, p.z * 2 - 1)
            yield Point3D(p.x * 2, p.y * 2, p.z * 2 + 1)
            yield Point3D(p.x * 2, p.y * 2 - 1, p.z * 2)
            yield Point3D(p.x * 2, p.y * 2 + 1, p.z * 2)
            yield Point3D(p.x * 2 - 1, p.y * 2, p.z * 2)
            yield Point3D(p.x * 2 + 1, p.y * 2, p.z * 2)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day18PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_18/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
