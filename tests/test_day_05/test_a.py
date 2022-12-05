from aoc_2022.day_05.a import get_solution, solve


def test_solve():
    with open("tests/test_day_05/sample.txt", "r") as f:
        data = f.read()
        assert solve(data) == "CMZ"


def test_my_solution():
    assert get_solution() == "SPFMVDTZT"
