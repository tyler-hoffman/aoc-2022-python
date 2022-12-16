import re

from aoc_2022.day_16.models import Valve


class Parser(object):
    regex_pattern = re.compile(
        r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)"
    )

    @staticmethod
    def parse(input: str) -> dict[str, Valve]:
        lines = input.strip().splitlines()
        valve_list = [Parser.parse_line(line) for line in lines]
        return {v.name: v for v in valve_list}

    @staticmethod
    def parse_line(line: str) -> Valve:
        match = Parser.regex_pattern.match(line)
        assert match is not None

        name = match.group(1)
        rate = match.group(2)
        leads_to = match.group(3)

        return Valve(name=name, flow_rate=int(rate), leads_to=leads_to.split(", "))
