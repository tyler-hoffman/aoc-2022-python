from dataclasses import dataclass


@dataclass
class Movement:
    direction: str
    amount: int
