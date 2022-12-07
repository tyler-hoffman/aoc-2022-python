from dataclasses import dataclass
from functools import cached_property

from aoc_2022.day_07.parser import Parser, TerminalLine
from aoc_2022.day_07.shared import Directory, terminal_lines_to_directories


@dataclass
class Day07PartASolver:
    terminal_lines: list[TerminalLine]

    @property
    def solution(self) -> int:
        return sum([d.size for d in self.root.all_dirs if d.size <= 100000])

    @cached_property
    def root(self) -> Directory:
        return terminal_lines_to_directories(self.terminal_lines)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day07PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_07/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
