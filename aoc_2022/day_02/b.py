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
            match (m.a, m.b.value):
                case Selection.ROCK, 1:
                    output += 0 + Selection.SCISSORS.value
                case Selection.ROCK, 2:
                    output += 3 + Selection.ROCK.value
                case Selection.ROCK, 3:
                    output += 6 + Selection.PAPER.value
                case Selection.PAPER, 1:
                    output += 0 + Selection.ROCK.value
                case Selection.PAPER, 2:
                    output += 3 + Selection.PAPER.value
                case Selection.PAPER, 3:
                    output += 6 + Selection.SCISSORS.value
                case Selection.SCISSORS, 1:
                    output += 0 + Selection.PAPER.value
                case Selection.SCISSORS, 2:
                    output += 3 + Selection.SCISSORS.value
                case Selection.SCISSORS, 3:
                    output += 6 + Selection.ROCK.value
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
