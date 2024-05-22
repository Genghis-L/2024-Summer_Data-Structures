class Point:
    """2D Point Class"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __eq__(self, other) -> bool:
        """equal"""
        return self.x == other.x and self.y == other.y

    def __add__(self, other) -> "Point":
        """adding"""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> "Point":
        """substract"""
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, lamda: float) -> "Point":
        """multuply"""
        return Point(self.x * lamda, self.y * lamda)

    def distance(self, other) -> float:
        """distance"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def midPoint(self, other, lamda=0.5) -> "Point":
        """point in between"""
        return other - (other - self) * lamda


def check_order(p1: "Point", p2: "Point", p3: "Point") -> bool:
    """check if the points A, B, and C are listed in counterclockwise order"""
    return (p3.y - p1.y) * (p2.x - p1.x) > (p2.y - p1.y) * (p3.x - p1.x)


def intersect(p1: "Point", p2: "Point", p3: "Point", p4: "Point") -> bool:
    """check if line segment p1p2 and p3p4 intersect"""
    return check_order(p1, p3, p4) != check_order(p2, p3, p4) and check_order(
        p1, p2, p3
    ) != check_order(p1, p2, p4)
