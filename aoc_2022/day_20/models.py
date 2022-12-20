from __future__ import annotations

from typing import Optional


class CircularLinkedList:
    value: int
    left: CircularLinkedList
    right: CircularLinkedList

    def __init__(
        self,
        value: int,
        left: Optional[CircularLinkedList] = None,
        right: Optional[CircularLinkedList] = None,
    ) -> None:
        self.value = value
        self.left = left or self
        self.right = right or self

    def remove(self) -> None:
        left = self.left
        right = self.right
        left.right = right
        right.left = left

    def add(self, value: int) -> CircularLinkedList:
        new_node = CircularLinkedList(value, left=self, right=self.right)
        self.right.left = new_node
        self.right = new_node
        return new_node

    def rotate_to(self, value: int) -> CircularLinkedList:
        node = self
        while node.value != value:
            node = node.right
        return node
