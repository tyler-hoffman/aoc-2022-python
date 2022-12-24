import re
from typing import Mapping

from aoc_2022.day_19.models import Blueprint, Resource, create_resource_map


class Parser(object):
    re_pattern = re.compile(
        r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."  # noqa: E501
    )

    @staticmethod
    def parse(input: str) -> Mapping[int, Blueprint]:
        lines = input.strip().splitlines()
        blueprints = [Parser.parse_line(line) for line in lines]
        return {b.name: b for b in blueprints}

    @staticmethod
    def parse_line(line: str) -> Blueprint:
        match = Parser.re_pattern.match(line)
        assert match is not None

        return Blueprint(
            name=int(match.group(1)),
            robot_costs={
                Resource.ORE: create_resource_map(ore=int(match.group(2))),
                Resource.CLAY: create_resource_map(ore=int(match.group(3))),
                Resource.OBSIDIAN: create_resource_map(
                    ore=int(match.group(4)),
                    clay=int(match.group(5)),
                ),
                Resource.GEODE: create_resource_map(
                    ore=int(match.group(6)),
                    obsidian=int(match.group(7)),
                ),
            },
        )
