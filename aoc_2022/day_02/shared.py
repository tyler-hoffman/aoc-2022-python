from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping


@dataclass
class Match:
    a: ABC
    b: XYZ


class Result(Enum):
    LOSE = 0
    TIE = 3
    WIN = 6


class ABC(Enum):
    A = 1
    B = 2
    C = 3

    @staticmethod
    def from_string(s: str) -> ABC:
        match s:
            case "A":
                return ABC.A
            case "B":
                return ABC.B
            case "C":
                return ABC.C
        assert False


class XYZ(Enum):
    X = 1
    Y = 2
    Z = 3

    @staticmethod
    def from_string(s: str) -> XYZ:
        match s:
            case "X":
                return XYZ.X
            case "Y":
                return XYZ.Y
            case "Z":
                return XYZ.Z
        assert False


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


ABC_TO_MOVE_MAP: Mapping[ABC, Move] = {
    ABC.A: Move.ROCK,
    ABC.B: Move.PAPER,
    ABC.C: Move.SCISSORS,
}

XYZ_TO_MOVE_MAP: Mapping[XYZ, Move] = {
    XYZ.X: Move.ROCK,
    XYZ.Y: Move.PAPER,
    XYZ.Z: Move.SCISSORS,
}

XYZ_TO_RESULT_MAP: Mapping[XYZ, Result] = {
    XYZ.X: Result.LOSE,
    XYZ.Y: Result.TIE,
    XYZ.Z: Result.WIN,
}

WHAT_BEATS_WHAT_MAP: Mapping[Move, Move] = {
    Move.ROCK: Move.SCISSORS,
    Move.SCISSORS: Move.PAPER,
    Move.PAPER: Move.ROCK,
}


WHAT_LOSES_TO_WHAT_MAP: Mapping[Move, Move] = {
    v: k for k, v in WHAT_BEATS_WHAT_MAP.items()
}
