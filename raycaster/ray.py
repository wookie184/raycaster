from .matrix import Matrix
from .vector import Tuple, point


class Ray:
    def __init__(self, origin: Tuple, direction: Tuple):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t

    def intersect(self, s):
        sphere_to_ray = self.origin - point(0, 0, 0)
        a = self.direction.dot(self.direction)
        b = 2 * self.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1

        discrim = b**2 - 4 * a * c
        if discrim < 0:
            return Intersections()

        t1 = (-b - discrim**0.5) / (2 * a)
        t2 = (-b + discrim**0.5) / (2 * a)
        return Intersections(
            Intersection(t1, s),
            Intersection(t2, s),
        )

    def transform(self, t):
        return Ray(
            t * self.origin,
            t * self.direction,
        )


class Sphere:
    def __init__(self):
        self.transform = Matrix.identity()

    def set_transform(self, t: Matrix):
        self.transform = t


class Intersection:  # noqa: SIM119
    def __init__(self, t, obj):
        self.t = t
        self.obj = obj


class Intersections:
    def __init__(self, *intersections):
        self.intersections = sorted(intersections, key=lambda x: x.t)

    def hit(self):
        return next((i for i in self.intersections if i.t > 0), None)

    def __getitem__(self, n):
        return self.intersections[n]

    @property
    def count(self):
        return len(self.intersections)
