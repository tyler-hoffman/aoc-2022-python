from dataclasses import dataclass
from functools import cached_property

from aoc_2022.day_20.models import CircularLinkedList


@dataclass
class Day20Solver:
    values: list[int]
    multiplier: int = 1
    rounds: int = 1

    @property
    def solution(self) -> int:
        nodes = self.linked_list_nodes(self.linked_list)
        for _ in range(self.rounds):
            for start in nodes:
                node = start
                if node.value < 0:
                    to_move_left = abs(node.value) % (self.length - 1)
                    node.move(-to_move_left)
                elif node.value > 0:
                    to_move_right = node.value % (self.length - 1)
                    node.move(to_move_right)

        node = self.linked_list.rotate_to(0)
        output = 0
        for _ in range(3):
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
        return [x * self.multiplier for x in self.values]

    @cached_property
    def length(self) -> int:
        return len(self.values)

    @cached_property
    def half_length(self) -> int:
        return self.length // 2
