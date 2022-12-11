from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    index: int
    items: list[int]
    operation: Callable[[int], int]
    divisible_test: int
    on_true: int
    on_false: int
    yeets: int = 0
