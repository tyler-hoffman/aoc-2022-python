import pytest

from aoc_2022.day_06.a import get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
        ("aabcd", 5),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 1361
