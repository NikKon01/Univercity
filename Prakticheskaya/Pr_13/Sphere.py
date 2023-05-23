import math

class Sphere:
    def __init__(self, r, x, y, z):
        self.radius = r
        self.center = (x, y, z)

    def get_volume(self):
        return 4 / 3 * 3.14159265359 * self.radius ** 3

    def get_square(self):
        return 4 * 3.14159265359 * self.radius ** 2
    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        distance = (x - self.center[0]) ** 2 + (y - self.center[1]) ** 2 + (z - self.center[2]) ** 2
        return distance <= self.radius ** 2

    def __str__(self):
        return f"radius: {self.radius} center: ({self.center})"

s = Sphere(3.0, 1.0, 2.0, 3.0)

print(s.get_radius())
print(s.get_center())
print(s.get_volume())
print(s.get_square())

s.set_radius(3.5)
s.set_center(0.0, 0.0, 0.0)

print(s.is_point_inside(1.0, 2.0, 3.0))
print(s.is_point_inside(0.0, 0.0, 2.5))