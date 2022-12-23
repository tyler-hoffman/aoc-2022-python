from dataclasses import dataclass, field
from functools import cached_property

from aoc_2022.shared.models import Point
from aoc_2022.shared.utils import frequency_map

DIRECTIONS = [
    Point(0, -1),
    Point(0, 1),
    Point(-1, 0),
    Point(1, 0),
]


@dataclass(frozen=True)
class Move:
    from_point: Point
    to_point: Point


@dataclass
class Day23Solver:
    elf_start_positions: set[Point]
    direction_index: int = field(default=0, init=False)
    round_number: int = field(default=0, init=False)

    def do_round(self) -> bool:
        propsed_moves = self.get_proposed_moves(self.elf_positions)
        proposed_destination_freq_map = frequency_map(
            [m.to_point for m in propsed_moves]
        )
        double_booked_spots = {
            k for k, v in proposed_destination_freq_map.items() if v > 1
        }

        new_state: set[Point] = set()
        for move in propsed_moves:
            if move.to_point in double_booked_spots:
                new_state.add(move.from_point)
            else:
                new_state.add(move.to_point)

        changed = new_state == self.elf_positions

        self.elf_positions.clear()
        self.elf_positions.update(new_state)

        self.update_direction()

        return changed

    def update_direction(self) -> None:
        self.direction_index += 1
        self.direction_index %= 4

    def get_proposed_moves(self, elves: set[Point]) -> set[Move]:
        output: set[Move] = set()
        for p in elves:
            neighbor_points = self.get_neighbors(p)
            neighbor_elves = neighbor_points & elves
            if neighbor_elves:
                proposed = False
                for d_offset in range(4):
                    d = DIRECTIONS[(self.direction_index + d_offset) % 4]
                    next_pos = Point(p.x + d.x, p.y + d.y)
                    if d.x:
                        if not {n for n in neighbor_elves if n.x == next_pos.x}:
                            output.add(Move(p, next_pos))
                            proposed = True
                            break
                    elif d.y:
                        if not {n for n in neighbor_elves if n.y == next_pos.y}:
                            output.add(Move(p, next_pos))
                            proposed = True
                            break
                    else:
                        raise Exception("Hmmmmm")
                if not proposed:
                    output.add(Move(p, p))
            else:
                output.add(Move(p, p))
        return output

    def get_neighbors(self, p: Point) -> set[Point]:
        output: set[Point] = set()
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x or y:
                    output.add(Point(p.x + x, p.y + y))
        return output

    @property
    def empty_spaces_in_bounding_box(self) -> int:
        width = self.x_max + 1 - self.x_min
        height = self.y_max + 1 - self.y_min

        return width * height - self.elf_count

    @cached_property
    def elf_count(self) -> int:
        return len(self.elf_start_positions)

    @property
    def x_min(self) -> int:
        return min({p.x for p in self.elf_positions})

    @property
    def x_max(self) -> int:
        return max({p.x for p in self.elf_positions})

    @property
    def y_min(self) -> int:
        return min({p.y for p in self.elf_positions})

    @property
    def y_max(self) -> int:
        return max({p.y for p in self.elf_positions})

    @cached_property
    def elf_positions(self) -> set[Point]:
        return self.elf_start_positions.copy()
