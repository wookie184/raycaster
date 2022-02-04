from __future__ import annotations
import math
import numbers

class Tuple:
    __slots__ = ('x', 'y', 'z', 'w')
    def __init__(self, x: float=0, y: float=0, z: float=0, w: float=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_point(self):
        return self.w == 1

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                x=self.x+other.x,
                y=self.y+other.y,
                z=self.z+other.z,
                w=self.w+other.w,
            )
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                x=self.x-other.x,
                y=self.y-other.y,
                z=self.z-other.z,
                w=self.w-other.w,
            )
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return self.__class__(
                x=self.x*other,
                y=self.y*other,
                z=self.z*other,
                w=self.w*other,
            )
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            return self.__class__(
                x=self.x/other,
                y=self.y/other,
                z=self.z/other,
                w=self.w/other,
            )
        return NotImplemented

    def __neg__(self):
        return self.__class__(
            x=-self.x,
            y=-self.y,
            z=-self.z,
            w=-self.w
        )

    def dot(self, other: Tuple):
        return (
            self.x*other.x +
            self.y*other.y +
            self.z*other.z +
            self.w*other.w
        )

    def normalize(self):
        assert not self.is_point()

        total = (self.x**2 + self.y**2 + self.z**2)**0.5
        return self.__class__(
            x=self.x/total,
            y=self.y/total,
            z=self.z/total,
            w=self.w/total,
        )

    def magnitude(self):
        assert not self.is_point()

        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def cross(self, other):
        assert not self.is_point()

        return self.__class__(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
            0
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y) and
                math.isclose(self.z, other.z) and
                self.w == other.w
            )
        return NotImplemented

    def __repr__(self):
        name = "point" if self.is_point() else "vector"
        return f"{name}(x={self.x}, y={self.y}, z={self.z})"

def clamp(n, lo, hi):
    return lo if n <= lo else hi if n >= hi else n

class Colour(Tuple):
    __slots__ = ('x', 'y', 'z', 'w')

    @property
    def r(self):
        return clamp(self.x, 0, 1)

    @property
    def g(self):
        return clamp(self.y, 0, 1)

    @property
    def b(self):
        return clamp(self.z, 0, 1)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z,
            )
        return super().__mul__(other)

    def __repr__(self):
        return f"Colour(r={self.x}, g={self.y}, b={self.z})"


def point(x: float=0, y: float=0, z: float=0):
    return Tuple(x, y, z, 1)

def vector(x: float=0, y: float=0, z: float=0):
    return Tuple(x, y, z, 0)
