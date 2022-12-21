from tests.test_day_21.models import ConstantMonkey, Monkey, OperationMonkey


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[Monkey]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Monkey:
        name, rest = line.split(": ")
        parts = rest.split()

        if len(parts) == 1:
            return ConstantMonkey(name, value=int(parts[0]))
        elif len(parts) == 3:
            a, operation, b = parts
            return OperationMonkey(name, a=a, operation=operation, b=b)
        else:
            assert False
