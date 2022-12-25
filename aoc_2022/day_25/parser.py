class Parser(object):
    @staticmethod
    def parse(input: str) -> list[str]:
        return input.strip().splitlines()
