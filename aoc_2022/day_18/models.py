from dataclasses import dataclass


@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int
