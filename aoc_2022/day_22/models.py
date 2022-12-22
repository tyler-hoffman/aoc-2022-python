from __future__ import annotations

import math
from dataclasses import dataclass
from functools import cached_property
from typing import Mapping, Sequence

from aoc_2022.shared.models import Point

DIRECTIONS: Sequence[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]


@dataclass(frozen=True)
class PointAtDirection:
    point: Point
    direction: Point


@dataclass(frozen=True)
class Segment:
    start: Point
    end: Point

    def __repr__(self) -> str:
        return f"({self.start} -> {self.end})"

    @property
    def points(self) -> list[Point]:
        start, end = self.start, self.end

        if end.y == start.y and end.x > start.x:
            return [Point(x, start.y) for x in range(start.x, end.x + 1)]
        elif end.y == start.y and end.x < start.x:
            return [Point(x, start.y) for x in range(start.x, end.x - 1, -1)]
        elif end.x == start.x and end.y > start.y:
            return [Point(start.x, y) for y in range(start.y, end.y + 1)]
        elif end.x == start.x and end.y < start.y:
            return [Point(start.x, y) for y in range(start.y, end.y - 1, -1)]
        else:
            raise Exception("Wat")

    @property
    def reverse(self) -> Segment:
        return Segment(self.end, self.start)

    @property
    def length(self) -> Point:
        return Point(self.end.x - self.start.x, self.end.y - self.start.y)

    @property
    def direction(self) -> Point:
        x = min(1, max(-1, self.length.x))
        y = min(1, max(-1, self.length.y))
        return Point(x, y)


@dataclass(frozen=True)
class Turn:
    direction: str


@dataclass(frozen=True)
class Move:
    distance: int


Instruction = Turn | Move


@dataclass(frozen=True)
class Map:
    spaces: set[Point]
    walls: set[Point]

    @cached_property
    def all_points(self) -> set[Point]:
        return self.spaces | self.walls

    @cached_property
    def points_by_x(self) -> Mapping[int, set[Point]]:
        output: dict[int, set[Point]] = {}
        for p in self.all_points:
            if p.x not in output:
                output[p.x] = set()
            output[p.x].add(p)
        return output

    @cached_property
    def points_by_y(self) -> Mapping[int, set[Point]]:
        output: dict[int, set[Point]] = {}
        for p in self.all_points:
            if p.y not in output:
                output[p.y] = set()
            output[p.y].add(p)
        return output

    @cached_property
    def xs(self) -> set[int]:
        return set(self.points_by_x.keys())

    @cached_property
    def ys(self) -> set[int]:
        return set(self.points_by_y.keys())

    @cached_property
    def min_x_by_y(self) -> Mapping[int, int]:
        return {y: min([p.x for p in self.points_by_y[y]]) for y in self.ys}

    @cached_property
    def max_x_by_y(self) -> Mapping[int, int]:
        return {y: max([p.x for p in self.points_by_y[y]]) for y in self.ys}

    @cached_property
    def max_x(self) -> int:
        return max([p.x for p in self.all_points])

    @cached_property
    def max_y(self) -> int:
        return max([p.y for p in self.all_points])

    @cached_property
    def min_y_by_x(self) -> Mapping[int, int]:
        return {x: min([p.y for p in self.points_by_x[x]]) for x in self.xs}

    @cached_property
    def max_y_by_x(self) -> Mapping[int, int]:
        return {x: max([p.y for p in self.points_by_x[x]]) for x in self.xs}

    @cached_property
    def side_size(self) -> int:
        point_count = len(self.all_points)
        points_per_side = point_count // 6
        return math.floor(0.001 + math.sqrt(points_per_side))

    def point_to_corner_id(self, point: Point) -> Point:
        return Point((point.x + 1) // self.side_size, (point.y + 1) // self.side_size)

    @cached_property
    def clockwise_segments(self) -> set[Segment]:
        output: set[Segment] = set()
        for x in range(1, self.max_x + 1, self.side_size):
            for y in range(1, self.max_y + 1, self.side_size):
                top_left = Point(x, y)
                if top_left in self.all_points:
                    top_right = Point(x + self.side_size - 1, y)
                    bottom_left = Point(x, y + self.side_size - 1)
                    bottom_right = Point(x + self.side_size - 1, y + self.side_size - 1)

                    output.add(Segment(top_left, top_right))
                    output.add(Segment(top_right, bottom_right))
                    output.add(Segment(bottom_right, bottom_left))
                    output.add(Segment(bottom_left, top_left))

        return output

    def segments_to_id_segments(self, segment: Segment) -> Segment:
        return Segment(
            self.point_to_corner_id(segment.start),
            self.point_to_corner_id(segment.end),
        )

    @cached_property
    def clockwise_id_segments(self) -> list[Segment]:
        as_set: set[Segment] = set()
        for segment in self.clockwise_segments:
            id_segment = self.segments_to_id_segments(segment)
            as_set.add(id_segment)

        output = [[s for s in as_set if s.start.y == 0][0]]
        while output[-1].end != output[0].start:
            got_it = False
            prev = output[-1]
            diff = Point(prev.start.x - prev.end.x, prev.start.y - prev.end.y)
            diff_direction_index = DIRECTIONS.index(diff)
            for i in range(1, 4):
                maybe_direction = DIRECTIONS[(diff_direction_index + i) % 4]
                maybe_end = Point(
                    prev.end.x + maybe_direction.x, prev.end.y + maybe_direction.y
                )
                maybe_segment = Segment(prev.end, maybe_end)
                if maybe_segment in as_set:
                    output.append(maybe_segment)
                    got_it = True
                    break
            assert got_it
        return output

    @cached_property
    def id_points_to_number_map(self) -> Mapping[Point, int]:
        concave_points: set[Point] = set()
        number = 1
        id_point_to_number: dict[Point, int] = {}

        # initial fold of convex points
        id_segments = self.clockwise_id_segments
        prev = id_segments[-1]
        for curr in id_segments:
            assert curr.start == prev.end
            if self.is_concave(prev, curr):
                concave_points.add(curr.start)
                id_point_to_number[curr.start] = number
                number += 1
                id_point_to_number[prev.start] = number
                id_point_to_number[curr.end] = number
                number += 1
            prev = curr

        clockwise_id_points = [s.start for s in self.clockwise_id_segments]
        count = len(clockwise_id_points)
        for i in range(1, count):
            for center in concave_points:
                center_index = clockwise_id_points.index(center)
                index_a = (center_index + i) % count
                index_b = (center_index - i) % count
                a = clockwise_id_points[index_a]
                b = clockwise_id_points[index_b]
                if (
                    id_point_to_number.get(a) is None
                    and id_point_to_number.get(b) is None
                ):
                    id_point_to_number[a] = number
                    id_point_to_number[b] = number
                    number += 1
        for i in range(1, count):
            for center in concave_points:
                center_index = clockwise_id_points.index(center)
                index_a = (center_index + i) % count
                index_b = (center_index - i) % count
                a = clockwise_id_points[index_a]
                b = clockwise_id_points[index_b]
                if id_point_to_number.get(a) is None:
                    id_point_to_number[a] = id_point_to_number[b]
                elif id_point_to_number.get(b) is None:
                    id_point_to_number[b] = id_point_to_number[a]

        return id_point_to_number

    @cached_property
    def side_map(self) -> Mapping[PointAtDirection, PointAtDirection]:
        id_points_to_number_map = self.id_points_to_number_map
        number_to_segments: dict[tuple[int, int], Segment] = {}
        for segment in self.clockwise_segments:
            id_segment = self.segments_to_id_segments(segment)
            a = id_points_to_number_map[id_segment.start]
            b = id_points_to_number_map[id_segment.end]
            key = (a, b)
            number_to_segments[key] = segment

        output: dict[PointAtDirection, PointAtDirection] = {}
        for (a, b), segment_a in number_to_segments.items():
            segment_b = number_to_segments[(b, a)]
            reversed_b = segment_b.reverse
            a_direction = segment_a.direction
            from_direction = DIRECTIONS[(DIRECTIONS.index(a_direction) + 3) % 4]
            b_direction = reversed_b.direction
            to_direction = DIRECTIONS[(DIRECTIONS.index(b_direction) + 3) % 4]
            for point_a, point_b in zip(segment_a.points, reversed_b.points):
                key = PointAtDirection(point_a, from_direction)
                value = PointAtDirection(point_b, to_direction)
                if key in output:
                    raise Exception("Oh no")
                output[key] = value

        return output

    @staticmethod
    def is_concave(a: Segment, b: Segment) -> bool:
        assert a.end == b.start

        index_a = DIRECTIONS.index(a.length)
        index_b = DIRECTIONS.index(b.reverse.length)

        return index_b == index_a + 1 or index_b == 0 and index_a == 3

    @cached_property
    def segments(self) -> set[Segment]:
        output: set[Segment] = set()
        for segment in self.clockwise_segments:
            output.add(segment)
            output.add(segment.reverse)
        return output

    @cached_property
    def id_segments(self) -> set[Segment]:
        output: set[Segment] = set()
        for segment in self.clockwise_id_segments:
            output.add(segment)
            output.add(segment.reverse)
        return output

    @cached_property
    def corner_ids(self) -> set[Point]:
        output: set[Point] = set()
        for segment in self.segments:
            output.add(self.point_to_corner_id(segment.start))
            output.add(self.point_to_corner_id(segment.end))
        return output

    @cached_property
    def segments_by_corner_id(self) -> dict[Point, set[Segment]]:
        output: dict[Point, set[Segment]] = {
            corner_id: set() for corner_id in self.corner_ids
        }

        for segment in self.segments:
            output[self.point_to_corner_id(segment.start)].add(segment)

        return output

    @cached_property
    def edge_point_map(self) -> dict[Point, Point]:
        output: dict[Point, Point] = {}
        segments_by_corner_ids = {
            k: v.copy() for k, v in self.segments_by_corner_id.items()
        }

        while [x for x in segments_by_corner_ids.values() if len(x) == 6]:
            print("wat")

        return output
