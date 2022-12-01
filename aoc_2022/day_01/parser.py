class Parser(object):
    @staticmethod
    def parse(input: str) -> list[list[int]]:
        output: list[list[int]] = []
        current_set: list[int] = []
        for line in input.strip().splitlines():
            if line.strip() == "":
                output.append(current_set)
                current_set = []
            else:
                current_set.append(int(line))
        output.append(current_set)
        return output
