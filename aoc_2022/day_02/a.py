from dataclasses import dataclass

from aoc_2022.day_02.parser import Parser

from .shared import ABC_TO_MOVE_MAP, WHAT_BEATS_WHAT_MAP, XYZ_TO_MOVE_MAP, Match


@dataclass
class Day02PartASolver:
    matches: list[Match]

    @property
    def solution(self) -> int:
        output = 0
        for m in self.matches:
            a = ABC_TO_MOVE_MAP[m.a]
            b = XYZ_TO_MOVE_MAP[m.b]

            output += b.value
            if a == b:
                output += 3
            elif WHAT_BEATS_WHAT_MAP[b] == a:
                output += 6

        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day02PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
