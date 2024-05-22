from Point_2D import *
import math


class Rectangle:
    """2D Rectangle Class"""

    def __init__(self, corner_lb: Point, width: float, height: float):
        self.corner = corner_lb
        self.width = width
        self.height = height
        self.corners = {
            "corner_lb": self.corner,
            "corner_rt": Point(self.corner.x + self.width, self.corner.y + self.height),
            "corner_rb": Point(self.corner.x + self.width, self.corner.y),
            "corner_lt": Point(self.corner.x, self.corner.y + self.height),
        }

    def __repr__(self) -> str:
        return f"Rectangle({self.corner}, {self.width}, {self.height})"

    def __str__(self) -> str:
        return f"[Corner: {self.corner}, Width: {self.width}, Height: {self.height}]"

    def __mul__(self, lamda: float) -> "Rectangle":
        """scaling"""
        return Rectangle(self.corner, self.width * lamda, self.height * lamda)

    def __eq__(self, other) -> bool:
        """strict equality"""
        return (
            self.corner == other.corner
            and self.width == other.width
            and self.height == other.height
        )

    def is_same(self, other) -> bool:
        """geometric equality"""
        return self.width == other.width and self.height == other.height

    def is_similar(self, other) -> bool:
        """geometric similarity"""
        return self.width / self.height == other.width / other.height

    def grow(self, dw: float, dh: float) -> "Rectangle":
        """growing"""
        return Rectangle(self.corner, self.width + dw, self.height + dh)

    def move(self, dx: float, dy: float) -> "Rectangle":
        """moving"""
        new_corner = Point(self.corner.x + dx, self.corner.y + dy)
        return Rectangle(new_corner, self.width, self.height)

    def area(self) -> float:
        """area"""
        return self.width * self.height

    def perimeter(self) -> float:
        """perimeter"""
        return 2 * (self.width + self.height)

    def flip(self) -> "Rectangle":
        """swap width and height"""
        return Rectangle(self.corner, self.height, self.width)

    def contain(self: "Rectangle", other: "Point") -> bool:
        """determine whether the rectangle contains the point"""
        return (
            self.corner.x <= other.x <= self.corner.x + self.width
            and self.corner.y <= other.y <= self.corner.y + self.height
        )

    def collide(self, other: "Rectangle") -> bool:
        """determine whether two reactangles collide"""
        flag = False
        # check whether there exists a corner is contained
        for corner in self.corners.values():
            flag = flag or other.contain(corner)
        for corner in other.corners.values():
            flag = flag or self.contain(corner)
        # check whether the diagonal intersects
        flag = flag or intersect(
            self.corner,
            self.corners["corner_rt"],
            other.corner,
            other.corners["corner_rt"],
        )
        return flag


a1 = Point(1, 2)
a2 = Point(-2, 3)
R1 = Rectangle(a1, 10, 20)
R2 = Rectangle(a2, 20, 2)

print(R1.collide(R2))
