from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point3D:
    """Representation of the center of a 1x1x1 cube"""

    x: int
    y: int
    z: int

    @property
    def neighbors(self) -> set[Point3D]:
        x = self.x
        y = self.y
        z = self.z

        return {
            Point3D(x, y, z - 1),
            Point3D(x, y, z + 1),
            Point3D(x, y - 1, z),
            Point3D(x, y + 1, z),
            Point3D(x - 1, y, z),
            Point3D(x + 1, y, z),
        }

    @property
    def sides(self) -> set[SidePosition3D]:
        x = self.x
        y = self.y
        z = self.z

        return {
            SidePosition3D(x * 2, y * 2, z * 2 - 1),
            SidePosition3D(x * 2, y * 2, z * 2 + 1),
            SidePosition3D(x * 2, y * 2 - 1, z * 2),
            SidePosition3D(x * 2, y * 2 + 1, z * 2),
            SidePosition3D(x * 2 - 1, y * 2, z * 2),
            SidePosition3D(x * 2 + 1, y * 2, z * 2),
        }


@dataclass(frozen=True)
class SidePosition3D:
    """Representation of side position

    Footgun alert: the scale here is 2x that of Point3D.

    Imagine we cubes with centers at (1, 1, 1) and (1, 1, 2).
    They share the side between them whose center is at (1, 1, 1.5).
    For a given cube at point (0, 0, 0), then, we could consider the
    sides to be at points (0, 0, -0.5), (0, 0, 0.5), (0, -0.5, 0),
    (0, 0.5, 0), (-0.5, 0, 0), and (0.5, 0, 0).

    To avoid dealing with floating point division, we will just store
    all of these points as their true value times 2. So e.g.
    (1, 1, 1.5) becomes (2, 2, 3).

    We could reuse Point3D for this, but using separate types
    should prevent us from accidentally using them interchangeably,
    since their scales are different.
    """

    x: int
    y: int
    z: int
