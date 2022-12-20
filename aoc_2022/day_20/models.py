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

    # def remove(self) -> None:
    #     old_left = self.left
    #     old_right = self.right
    #     old_left.right = old_right
    #     old_right.left = old_left

    def add(self, value: int) -> CircularLinkedList:
        new_node = CircularLinkedList(value, left=self, right=self.right)
        self.right.left = new_node
        self.right = new_node
        return new_node

    def move(self, amount: int) -> None:
        old_left = self.left
        old_right = self.right
        old_left.right = old_right
        old_right.left = old_left

        to_add_at = self.left
        if amount < 0:
            for _ in range(abs(amount)):
                to_add_at = to_add_at.left
        elif amount > 0:
            for _ in range(amount):
                to_add_at = to_add_at.right

        # self.remove()
        self.left = to_add_at
        self.right = to_add_at.right
        self.left.right = self
        self.right.left = self

    def rotate_to(self, value: int) -> CircularLinkedList:
        node = self
        while node.value != value:
            node = node.right
        return node
