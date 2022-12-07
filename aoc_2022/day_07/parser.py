from dataclasses import dataclass


class TerminalLine:
    ...


@dataclass
class CD(TerminalLine):
    to: str


@dataclass
class LS(TerminalLine):
    ...


@dataclass
class FileData(TerminalLine):
    name: str
    size: int


@dataclass
class DirData(TerminalLine):
    name: str


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[TerminalLine]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> TerminalLine:
        if line == "$ ls":
            return LS()
        elif line.startswith("$ cd"):
            return CD(line.split()[-1])
        elif line.startswith("dir"):
            return DirData(line.split()[-1])
        else:
            size, name = line.split()
            return FileData(name, int(size))
