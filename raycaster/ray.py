from __future__ import annotations

from .matrix import Matrix
from .vector import Tuple, point


class Ray:
    def __init__(self, origin: Tuple, direction: Tuple) -> None:
        self.origin = origin
        self.direction = direction

    def position(self, t: float) -> Tuple:
        return self.origin + self.direction * t

    def intersect(self, s: Sphere):
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

    def transform(self, t: Matrix) -> Ray:
        return Ray(
            t * self.origin,
            t * self.direction,
        )


class Sphere:
    def __init__(self) -> None:
        self.transform = Matrix.identity()

    def set_transform(self, t: Matrix) -> None:
        self.transform = t

    def normal_at(self, world_point: Tuple) -> Tuple:
        object_point = self.transform.inverse() * world_point
        object_normal = object_point - point(0, 0, 0)
        world_normal = self.transform.inverse().transpose() * object_normal
        world_normal.w = 0
        return world_normal.normalize()


class Intersection:  # noqa: SIM119
    def __init__(self, t: float, obj: Sphere) -> None:
        self.t = t
        self.obj = obj


class Intersections:
    def __init__(self, *intersections: Intersection) -> None:
        self.intersections = sorted(intersections, key=lambda x: x.t)

    def hit(self) -> Intersection | None:
        return next((i for i in self.intersections if i.t > 0), None)

    def __getitem__(self, n: int) -> Intersection:
        return self.intersections[n]

    @property
    def count(self) -> int:
        return len(self.intersections)
