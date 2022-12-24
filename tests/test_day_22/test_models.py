import pytest

from aoc_2022.day_22.models import Map, Segment
from aoc_2022.shared.models import Point


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Segment(Point(0, 0), Point(0, 1)), Segment(Point(0, 1), Point(1, 1)), True),
        (Segment(Point(0, 1), Point(1, 1)), Segment(Point(1, 1), Point(1, 0)), True),
        (Segment(Point(0, 0), Point(0, 1)), Segment(Point(0, 1), Point(-1, 1)), False),
        (Segment(Point(2, 0), Point(3, 0)), Segment(Point(3, 0), Point(3, 1)), False),
    ],
)
def test_concave(a: Segment, b: Segment, expected: bool):
    assert Map.is_concave(a, b) == expected
