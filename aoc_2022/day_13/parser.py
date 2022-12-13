from aoc_2022.day_13.models import Packet


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[tuple[Packet, Packet]]:
        output: list[tuple[Packet, Packet]] = []
        lines = input.strip().splitlines()
        for i in range(0, len(lines), 3):
            output.append(
                (Parser.parse_packet(lines[i]), Parser.parse_packet(lines[i + 1]))
            )
        return output

    @staticmethod
    def parse_packet(line: str) -> Packet:
        return eval(line)
