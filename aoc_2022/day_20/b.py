from dataclasses import dataclass
from functools import cached_property

from aoc_2022.day_20.models import CircularLinkedList
from aoc_2022.day_20.parser import Parser


@dataclass
class Day20PartBSolver:
    values: list[int]

    @property
    def solution(self) -> int:
        nodes = self.linked_list_nodes(self.linked_list)
        for _ in range(10):
            for start in nodes:
                node = start
                if node.value < 0:
                    node.move(-(abs(node.value) % (self.length - 1)))
                elif node.value > 0:
                    node.move(node.value % (self.length - 1))

        node = self.linked_list.rotate_to(0)
        output = 0
        for _ in range(1000):
            node = node.right
        output += node.value
        for _ in range(1000):
            node = node.right
        output += node.value
        for _ in range(1000):
            node = node.right
        output += node.value

        return output

    def linked_list_nodes(
        self, linked_list: CircularLinkedList
    ) -> list[CircularLinkedList]:
        output = []
        for _ in range(self.length):
            output.append(linked_list)
            linked_list = linked_list.right
        return output

    def values_from(self, linked_list: CircularLinkedList) -> list[int]:
        output: list[int] = []
        for _ in range(self.length):
            output.append(linked_list.value)
            linked_list = linked_list.right
        return output

    @cached_property
    def linked_list(self) -> CircularLinkedList:
        values = self.multiplied_values
        head = CircularLinkedList(values[0])
        node = head

        for value in values[1:]:
            node = node.add(value)

        return head

    @cached_property
    def multiplied_values(self) -> list[int]:
        return [x * 811589153 for x in self.values]

    @cached_property
    def length(self) -> int:
        return len(self.values)

    @cached_property
    def half_length(self) -> int:
        return self.length // 2


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day20PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_20/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
