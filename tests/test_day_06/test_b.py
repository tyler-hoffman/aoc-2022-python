import pytest

from aoc_2022.day_06.b import get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


@pytest.mark.skip
def test_my_solution():
    assert get_solution() == 3263
