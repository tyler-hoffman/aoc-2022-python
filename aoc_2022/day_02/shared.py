from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass
class Match:
    a: Selection
    b: Selection


class Selection(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def from_abc(s: str) -> Selection:
        match s:
            case "A":
                return Selection.ROCK
            case "B":
                return Selection.PAPER
            case "C":
                return Selection.SCISSORS
        assert False

    @staticmethod
    def from_xyz(s: str) -> Selection:
        match s:
            case "X":
                return Selection.ROCK
            case "Y":
                return Selection.PAPER
            case "Z":
                return Selection.SCISSORS
        assert False

    @staticmethod
    def score(selection: Selection) -> int:
        match selection:
            case Selection.ROCK:
                return 1
            case Selection.PAPER:
                return 2
            case Selection.SCISSORS:
                return 3
