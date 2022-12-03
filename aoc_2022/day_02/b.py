from dataclasses import dataclass

from aoc_2022.day_02.parser import Parser

from .shared import (
    ABC_TO_MOVE_MAP,
    WHAT_BEATS_WHAT_MAP,
    WHAT_LOSES_TO_WHAT_MAP,
    XYZ_TO_RESULT_MAP,
    Match,
    Move,
    Result,
)


@dataclass
class Day02PartASolver:
    matches: list[Match]

    @property
    def solution(self) -> int:
        output = 0
        for m in self.matches:
            a = ABC_TO_MOVE_MAP[m.a]
            result = XYZ_TO_RESULT_MAP[m.b]
            b = self.move_for_result(a, result)

            output += result.value + b.value

        return output

    def move_for_result(self, opponent_move: Move, result: Result) -> Move:
        match result:
            case Result.LOSE:
                return WHAT_BEATS_WHAT_MAP[opponent_move]
            case Result.TIE:
                return opponent_move
            case Result.WIN:
                return WHAT_LOSES_TO_WHAT_MAP[opponent_move]


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
