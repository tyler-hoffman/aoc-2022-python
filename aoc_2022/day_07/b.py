from dataclasses import dataclass
from functools import cached_property

from aoc_2022.day_07.parser import Parser, TerminalLine
from aoc_2022.day_07.shared import Directory, terminal_lines_to_directories


@dataclass
class Day07PartBSolver:
    terminal_lines: list[TerminalLine]

    @property
    def solution(self) -> int:
        total = 70000000
        needed_for_update = 30000000
        max_used_disk = total - needed_for_update
        min_to_delete = self.root.size - max_used_disk

        return min([d.size for d in self.root.all_dirs if d.size >= min_to_delete])

    @cached_property
    def root(self) -> Directory:
        return terminal_lines_to_directories(self.terminal_lines)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day07PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_07/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
