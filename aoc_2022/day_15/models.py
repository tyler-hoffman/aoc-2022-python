from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class Sensor:
    position: Point
    closest_beacon: Point

    @property
    def range(self) -> int:
        return abs(self.position.x - self.closest_beacon.x) + abs(
            self.position.y - self.closest_beacon.y
        )
