from dataclasses import dataclass
from typing import Mapping

from aoc_2022.day_05.parser import Parser
from aoc_2022.day_05.shared import Move


@dataclass
class Day05PartASolver:
    starting_stacks: Mapping[int, list[str]]
    moves: list[Move]

    @property
    def solution(self) -> str:
        for move in self.moves:
            for _ in range(move.count):
                from_stack = self.starting_stacks[move.from_stack]
                to_stack = self.starting_stacks[move.to_stack]
                to_stack.append(from_stack.pop())

        tops = [
            self.starting_stacks[i][-1] for i in range(1, len(self.starting_stacks) + 1)
        ]
        return "".join(tops)


def solve(input: str) -> str:
    data = Parser.parse(input)
    solver = Day05PartASolver(data.starting_stacks, data.moves)

    return solver.solution


def get_solution() -> str:
    with open("aoc_2022/day_05/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
