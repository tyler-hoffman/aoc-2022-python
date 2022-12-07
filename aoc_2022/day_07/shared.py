from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property

from aoc_2022.day_07.parser import CD, LS, DirData, FileData, TerminalLine


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    files: dict[str, File] = field(default_factory=dict)
    dirs: dict[str, Directory] = field(default_factory=dict)

    @cached_property
    def size(self) -> int:
        size_files = sum([f.size for f in self.files.values()])
        size_dirs = sum([d.size for d in self.dirs.values()])

        return size_files + size_dirs

    @cached_property
    def all_dirs(self) -> list[Directory]:
        output: list[Directory] = [self]
        for d in self.dirs.values():
            output += d.all_dirs
        return output


def terminal_lines_to_directories(lines: list[TerminalLine]) -> Directory:
    root = Directory("/")
    current_directory: list[Directory] = [root]

    for line in lines:
        match line:
            case LS():
                ...
            case CD("/"):
                current_directory = [root]
            case CD(".."):
                current_directory.pop()
            case CD(to):
                current_directory.append(current_directory[-1].dirs[to])
            case FileData(name, size):
                current_directory[-1].files[name] = File(name, size)
            case DirData(name):
                current_directory[-1].dirs[name] = Directory(name)
    return root
