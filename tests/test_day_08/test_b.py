import pytest

from aoc_2022.day_08.b import Day08PartBSolver, get_solution
from aoc_2022.day_08.parser import Parser
from aoc_2022.shared.models import Point

SAMPLE_DATA = """
30373
25512
65332
33549
35390
"""


@pytest.mark.parametrize(
    "point, expected",
    [
        (Point(2, 1), 4),
        (Point(2, 3), 8),
    ],
)
def test_scenic_score(point: Point, expected: int):
    solver = Day08PartBSolver(Parser.parse(SAMPLE_DATA))
    assert solver.scenic_score(point) == expected


def test_my_solution():
    assert get_solution() == 410400
