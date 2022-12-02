from dataclasses import dataclass

from aoc_2022.day_02.parser import Parser

from .shared import Match, Selection


@dataclass
class Day02PartASolver:
    matches: list[Match]

    @property
    def solution(self) -> int:
        output = 0
        for m in self.matches:
            output += m.b.value
            match (m.a, m.b):
                case Selection.ROCK, Selection.PAPER:
                    output += 6
                case Selection.ROCK, Selection.SCISSORS:
                    output += 0
                case Selection.ROCK, Selection.ROCK:
                    output += 3
                case Selection.PAPER, Selection.PAPER:
                    output += 3
                case Selection.PAPER, Selection.SCISSORS:
                    output += 6
                case Selection.PAPER, Selection.ROCK:
                    output += 0
                case Selection.SCISSORS, Selection.PAPER:
                    output += 0
                case Selection.SCISSORS, Selection.SCISSORS:
                    output += 3
                case Selection.SCISSORS, Selection.ROCK:
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
