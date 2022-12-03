from dataclasses import dataclass
from functools import cached_property

from aoc_2022.day_03.parser import Parser
from aoc_2022.day_03.shared import CHAR_PRIORITY_MAP, Rucksack

RucksackGroup = tuple[Rucksack, Rucksack, Rucksack]


@dataclass
class Day03PartBSolver:
    rucksacks: list[Rucksack]

    @property
    def solution(self) -> int:
        duplicates = [self.find_duplicate(r) for r in self.rucksack_groups]
        priorities = [CHAR_PRIORITY_MAP[d] for d in duplicates]
        return sum(priorities)

    def find_duplicate(self, rucksacks: RucksackGroup) -> str:
        a, b, c = [set(r.contents) for r in rucksacks]

        intersection = list(a.intersection(b).intersection(c))
        assert len(intersection) == 1, "Should only have one"
        return intersection[0]

    @cached_property
    def rucksack_groups(self) -> list[RucksackGroup]:
        group_count = len(self.rucksacks) // 3
        return [tuple(self.rucksacks[i * 3 : (i + 1) * 3]) for i in range(group_count)]


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day03PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_03/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
