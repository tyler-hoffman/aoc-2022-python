from dataclasses import dataclass
from typing import Optional

from aoc_2022.day_10.models import Operation, State
from aoc_2022.day_10.non_artifiial_intelligence import HumanService
from aoc_2022.day_10.parser import Parser
from aoc_2022.day_10.shared import get_state_at_time


@dataclass
class Day10PartBSolver:
    instructions: list[Operation]
    human_service: HumanService

    @property
    def solution(self) -> str:
        chars: list[str] = []
        states = [s for s in get_state_at_time(self.instructions)]
        for s in states:
            chars.append("#" if self.overlaps(s) else ".")

        rows = [(chars[i * 40 : (i + 1) * 40]) for i in range(6)]
        view = "\n".join(["".join(r) for r in rows])

        return self.human_service.query(view)

    def overlaps(self, s: State) -> bool:
        y = (s.t - 1) % 40
        return s.x in range(y - 1, y + 2)


def solve(input: str, human_service: HumanService) -> str:
    data = Parser.parse(input)
    solver = Day10PartBSolver(data, human_service)

    return solver.solution


def get_solution(human_service: Optional[HumanService] = None) -> str:
    with open("aoc_2022/day_10/input.txt", "r") as f:
        input = f.read()
    return solve(input, human_service or HumanService())


if __name__ == "__main__":
    print(get_solution())
