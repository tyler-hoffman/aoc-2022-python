import pytest

from aoc_2022.day_24.a import get_solution, solve

SAMPLE_DATA = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 18


@pytest.mark.skip
def test_my_solution():
    assert get_solution() == "NOT THIS"
