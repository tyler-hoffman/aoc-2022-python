from dataclasses import dataclass


@dataclass
class Movement:
    direction: str
    amount: int


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0
