from dataclasses import dataclass


@dataclass
class Day06Solver:
    input: str
    unique_count: int

    @property
    def solution(self) -> int:
        n = self.unique_count
        for i in range(len(self.input) - (n - 1)):
            chunk = self.input[i : i + n]
            if len(set(chunk)) == n:
                return i + n
        assert False, "We shouldn't get here"
