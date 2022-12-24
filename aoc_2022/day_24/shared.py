from dataclasses import dataclass
from functools import cached_property, total_ordering
from queue import PriorityQueue
from typing import Any

from aoc_2022.day_24.models import Blizzard, Direction, Map
from aoc_2022.shared.models import Point


@total_ordering
@dataclass(frozen=True)
class State:
    position: Point
    time: int

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, State):
            return self.time < other.time
        else:
            return False


@dataclass
class Day24Solver:
    starting_map: Map

    @property
    def solution(self) -> int:
        start = State(self.starting_map.start, 0)
        return self.get_min_time_for_journey(start, self.starting_map.end)

    def get_min_time_for_journey(self, start: State, end: Point) -> int:
        seen: set[State] = set()
        queue: PriorityQueue[tuple[int, State]] = PriorityQueue()

        seen.add(start)
        queue.put((self.compute_optimistic_time(start), start))

        while queue:
            _, state = queue.get()

            possible_next_points = state.position.neighbors_without_diagonals | {
                state.position
            }
            for neighbor in possible_next_points:
                next_state = State(neighbor, state.time + 1)
                if next_state not in seen:
                    seen.add(next_state)
                    if self.is_valid_state(next_state):
                        queue.put(
                            (self.compute_optimistic_time(next_state), next_state)
                        )

            if state.position == end:
                return state.time

        raise Exception("How'd we get here?")

    def compute_optimistic_time(self, state: State) -> int:
        return state.time + state.position.dist(self.starting_map.end)

    def is_valid_state(self, state: State) -> bool:
        pos = state.position
        special_places = {self.starting_map.start, self.starting_map.end}

        if pos not in special_places and any(
            {
                pos.x < 0,
                pos.x >= self.starting_map.width,
                pos.y < 0,
                pos.y >= self.starting_map.height,
            }
        ):
            return False

        # east
        x = (pos.x + state.time) % self.starting_map.width
        y = pos.y
        if Blizzard(Point(x, y), Direction.WEST) in self.starting_blizzards:
            return False

        # west
        x = (pos.x - state.time) % self.starting_map.width
        y = pos.y
        if Blizzard(Point(x, y), Direction.EAST) in self.starting_blizzards:
            return False

        # north
        x = pos.x
        y = (pos.y - state.time) % self.starting_map.height
        if Blizzard(Point(x, y), Direction.SOUTH) in self.starting_blizzards:
            return False

        # south
        x = pos.x
        y = (pos.y + state.time) % self.starting_map.height
        if Blizzard(Point(x, y), Direction.NORTH) in self.starting_blizzards:
            return False

        return True

    @cached_property
    def starting_blizzards(self) -> set[Blizzard]:
        return set(self.starting_map.blizzards)
