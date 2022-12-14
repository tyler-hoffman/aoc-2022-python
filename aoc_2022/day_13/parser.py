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
        """An overengineered packet parser (given the problem)

        We could just as easily just return eval(line), but
        that's not so great in general, so we're doing it the
        hard way
        """

        packet, length = Parser.parse_subpacket(line, 0)
        assert length == len(line)
        return packet

    @staticmethod
    def parse_subpacket(line: str, index: int) -> tuple[Packet, int]:
        assert line[index] == "["

        output: Packet = []
        index += 1

        while line[index] != "]":
            if line[index] == "[":
                element, index = Parser.parse_subpacket(line, index)
                output.append(element)
            elif line[index] == ",":
                index += 1
            else:
                terminal_indices = [line.find(ch, index) for ch in {",", "[", "]"}]
                end = min([x for x in terminal_indices if x >= 0])
                output.append(int(line[index:end]))
                index = end

        index += 1
        return output, index
