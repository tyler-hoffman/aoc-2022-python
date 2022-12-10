from dataclasses import dataclass

from aoc_2022.day_10.models import Operation
from aoc_2022.day_10.parser import Parser
from aoc_2022.day_10.shared import get_state_at_time


@dataclass
class Day10PartASolver:
    instructions: list[Operation]

    @property
    def solution(self) -> int:
        states = [
            s for s in get_state_at_time(self.instructions) if self.is_target_time(s.t)
        ]
        signal_strengths = [s.signal_strength for s in states]
        return sum(signal_strengths)

    def is_target_time(self, t: int) -> bool:
        return (t - 20) % 40 == 0


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day10PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_10/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
