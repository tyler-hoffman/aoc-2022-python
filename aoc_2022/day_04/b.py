from dataclasses import dataclass

from aoc_2022.day_04.parser import Parser
from aoc_2022.day_04.shared import Range


@dataclass
class Day04PartBSolver:
    pairs: list[tuple[Range, Range]]

    @property
    def solution(self) -> int:
        full_overlaps = [
            self.partially_contains(a, b) or self.partially_contains(b, a)
            for a, b in self.pairs
        ]
        return len([x for x in full_overlaps if x])

    def partially_contains(self, a: Range, b: Range) -> bool:
        return a.start <= b.end and a.end >= b.start


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day04PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_04/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
