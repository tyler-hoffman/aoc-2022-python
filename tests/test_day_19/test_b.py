from aoc_2022.day_19.b import get_solution, solve

SAMPLE_DATA = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""  # noqa: E501


def test_solve():
    # NOTE: my implementation happens to just fall back to
    # using all blueprints if there are less than 3
    assert solve(SAMPLE_DATA) == 56 * 62


def test_my_solution():
    assert get_solution() == 29348
