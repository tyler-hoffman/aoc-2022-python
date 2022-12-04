from dataclasses import dataclass

from aoc_2022.day_04.parser import Parser
from aoc_2022.day_04.shared import Range


@dataclass
class Day04PartASolver:
    pairs: list[tuple[Range, Range]]

    @property
    def solution(self) -> int:
        full_overlaps = [
            self.fully_contains(a, b) or self.fully_contains(b, a)
            for a, b in self.pairs
        ]
        return len([x for x in full_overlaps if x])

    def fully_contains(self, a: Range, b: Range) -> bool:
        return a.start <= b.start and a.end >= b.end


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day04PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_04/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
