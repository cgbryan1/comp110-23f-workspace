"""CQ07 challenge question, mutating points."""

from __future__ import annotations

__author__ = "730657997"


class Point:
    """Attributes I need for this point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Initiating my object."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scales the original point by input factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Makes a new, scaled point from the original."""
        new_point: Point = Point(self.x, self.y)
        new_point.x = self.x * factor
        new_point.y = self.y * factor
        return new_point