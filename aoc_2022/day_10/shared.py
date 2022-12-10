from typing import Iterable

from aoc_2022.day_10.models import Addx, Noop, Operation, State


def get_state_at_time(instructions: list[Operation]) -> Iterable[State]:
    t = 1
    x = 1

    yield State(t, x)
    for instruction in instructions:
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
