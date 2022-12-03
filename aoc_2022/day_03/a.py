from dataclasses import dataclass

from aoc_2022.day_03.parser import Parser
from aoc_2022.day_03.shared import CHAR_PRIORITY_MAP, Rucksack


@dataclass
class Day03PartASolver:
    rucksacks: list[Rucksack]

    @property
    def solution(self) -> int:
        duplicates = [self.find_duplicate(r) for r in self.rucksacks]
        priorities = [CHAR_PRIORITY_MAP[d] for d in duplicates]
        return sum(priorities)

    def find_duplicate(self, rucksack: Rucksack) -> str:
        intersection = list(
            set(rucksack.first_half).intersection(set(rucksack.second_half))
        )
        assert len(intersection) == 1, "Should only have one"
        return intersection[0]


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day03PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_03/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
