import pytest

from aoc_2022.day_18.b import get_solution, solve

SMALL_DATA = """
1,1,1
2,1,1
"""

SAMPLE_DATA = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""


@pytest.mark.parametrize(
    "input, expected",
    [
        (SMALL_DATA, 10),
        (SAMPLE_DATA, 58),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 2460
