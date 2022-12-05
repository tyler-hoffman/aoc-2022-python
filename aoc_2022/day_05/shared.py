from dataclasses import dataclass


@dataclass
class Move:
    count: int
    from_stack: int
    to_stack: int
