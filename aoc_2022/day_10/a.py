from dataclasses import dataclass
from typing import Iterable

from aoc_2022.day_10.models import Addx, Noop, Operation
from aoc_2022.day_10.parser import Parser


@dataclass
class State:
    t: int
    x: int

    @property
    def signal_strength(self) -> int:
        return self.t * self.x


@dataclass
class Day10PartASolver:
    instructions: list[Operation]

    @property
    def solution(self) -> int:
        states = [s for s in self.get_state_at_time() if (s.t - 20) % 40 == 0]
        signal_strengths = [s.signal_strength for s in states]
        return sum(signal_strengths)

    def get_state_at_time(self) -> Iterable[State]:
        t = 1
        x = 1

        yield State(t, x)
        for instruction in self.instructions:
            match instruction:
                case Noop():
                    t += 1
                    yield State(t, x)
                case Addx(amount):
                    t += 1
                    yield State(t, x)
                    t += 1
                    x += amount
                    yield State(t, x)


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
