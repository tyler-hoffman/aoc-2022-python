from aoc_2022.day_23.parser import Parser
from aoc_2022.day_23.shared import Day23Solver


class Day23DayASolver(Day23Solver):
    @property
    def solution(self) -> int:
        for _ in range(10):
            self.do_round()
            self.round_number += 1
        return self.empty_spaces_in_bounding_box


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day23DayASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_23/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
