from dataclasses import dataclass, field
from functools import cache, cached_property

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


@cache
def get_neighbors(p: Point) -> set[Point]:
    output: set[Point] = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x or y:
                output.add(Point(p.x + x, p.y + y))
    return output


@dataclass
class Day23Solver:
    elf_positions: set[Point]
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

        valid_moves = {
            m for m in propsed_moves if m.to_point not in double_booked_spots
        }
        for move in valid_moves:
            if move.to_point not in double_booked_spots:
                self.elf_positions.remove(move.from_point)
                self.elf_positions.add(move.to_point)

        self.update_direction()

        return len(valid_moves) > 0

    def update_direction(self) -> None:
        self.direction_index += 1
        self.direction_index %= 4

    def get_proposed_moves(self, elves: set[Point]) -> set[Move]:
        output: set[Move] = set()
        for p in elves:
            neighbor_points = get_neighbors(p)
            neighbor_elves = neighbor_points & elves
            if neighbor_elves:
                for d_offset in range(4):
                    d = DIRECTIONS[(self.direction_index + d_offset) % 4]
                    next_pos = Point(p.x + d.x, p.y + d.y)
                    if d.x:
                        if not {n for n in neighbor_elves if n.x == next_pos.x}:
                            output.add(Move(p, next_pos))
                            break
                    elif d.y:
                        if not {n for n in neighbor_elves if n.y == next_pos.y}:
                            output.add(Move(p, next_pos))
                            break
                    else:
                        raise Exception("Hmmmmm")
        return output

    @property
    def empty_spaces_in_bounding_box(self) -> int:
        width = self.x_max + 1 - self.x_min
        height = self.y_max + 1 - self.y_min

        return width * height - self.elf_count

    @cached_property
    def elf_count(self) -> int:
        return len(self.elf_positions)

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
