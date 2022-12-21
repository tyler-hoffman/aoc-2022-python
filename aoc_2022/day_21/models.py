from dataclasses import dataclass


@dataclass
class ConstantMonkey:
    name: str
    value: int


@dataclass
class OperationMonkey:
    name: str
    a: str
    b: str
    operation: str


Monkey = ConstantMonkey | OperationMonkey
