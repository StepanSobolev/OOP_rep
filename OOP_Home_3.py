import math
from point_class import Point


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return super().__str__()[:-1] + f', radius={self.radius})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __sub__(self, other):
        if self.radius == other.radius:
            x = self.x - other.x
            y = self.y - other.y
            return Point(x, y)
        else:
            x = self.x - other.x
            y = self.y - other.y
            radius = abs(self.radius - other.radius)
            return Circle(radius, x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius**2)


a = Circle(3, 10, 12)
b = Circle(3, 8, 5)

print(a-b)