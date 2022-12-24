from aoc_2022.day_24.b import get_solution, solve

SAMPLE_DATA = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 54


def test_my_solution():
    assert get_solution() == 747
