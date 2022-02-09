from __future__ import annotations

import math
import numbers


class Tuple:
    __slots__ = ("x", "y", "z", "w")

    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def is_point(self):
        """Returns True if the tuple represents a point (self.w==1)."""
        return self.w == 1

    def __add__(self, other):
        "Add the tuple's elements to another elementwise."
        if isinstance(other, self.__class__):
            return self.__class__(
                x=self.x + other.x,
                y=self.y + other.y,
                z=self.z + other.z,
                w=self.w + other.w,
            )
        return NotImplemented

    def __getitem__(self, i):
        return (self.x, self.y, self.z, self.w)[i]

    def __sub__(self, other):
        "Subtract another tuple's elements elementwise."
        if isinstance(other, self.__class__):
            return self.__class__(
                x=self.x - other.x,
                y=self.y - other.y,
                z=self.z - other.z,
                w=self.w - other.w,
            )
        return NotImplemented

    def __mul__(self, other):
        """Multiply the tuple's elements by a scalar."""
        if isinstance(other, numbers.Number):
            return self.__class__(
                x=self.x * other,
                y=self.y * other,
                z=self.z * other,
                w=self.w * other,
            )
        return NotImplemented

    def __truediv__(self, other):
        """Divide the tuple's elements by a scalar."""
        if isinstance(other, numbers.Number):
            return self.__class__(
                x=self.x / other,
                y=self.y / other,
                z=self.z / other,
                w=self.w / other,
            )
        return NotImplemented

    def __neg__(self):
        """Negate the tuple's elements."""
        return self.__class__(x=-self.x, y=-self.y, z=-self.z, w=-self.w)

    def dot(self, other: Tuple):
        """Calculates the dot product of the tuple."""
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def normalize(self):
        """Normalizes a vector."""
        assert not self.is_point()

        total = (self.x**2 + self.y**2 + self.z**2) ** 0.5
        return self.__class__(
            x=self.x / total,
            y=self.y / total,
            z=self.z / total,
            w=self.w / total,
        )

    def magnitude(self):
        """Calculates the magnitude of the vector."""
        assert not self.is_point()

        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def cross(self, other):
        """Calculates the cross product of two vectors."""
        assert not self.is_point()

        return self.__class__(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
            0,
        )

    def __eq__(self, other):
        abs_tol = 1e-10
        if isinstance(other, self.__class__):
            return (
                math.isclose(self.x, other.x, abs_tol=abs_tol)
                and math.isclose(self.y, other.y, abs_tol=abs_tol)
                and math.isclose(self.z, other.z, abs_tol=abs_tol)
                and self.is_point() == other.is_point()
            )
        return NotImplemented

    def __repr__(self):
        name = "point" if self.is_point() else "vector"
        return f"{name}(x={self.x:.2f}, y={self.y:.2f}, z={self.z:.2f})"


def clamp(n, lo, hi):
    return lo if n <= lo else hi if n >= hi else n


class Colour(Tuple):
    __slots__ = ("x", "y", "z", "w")

    @property
    def r(self) -> float:
        """Returns the red value of the colour, clamped between 0 and 1."""
        return clamp(self.x, 0, 1)

    @property
    def g(self) -> float:
        """Returns the green value of the colour, clamped between 0 and 1."""
        return clamp(self.y, 0, 1)

    @property
    def b(self) -> float:
        """Returns the blue value of the colour, clamped between 0 and 1."""
        return clamp(self.z, 0, 1)

    def __mul__(self, other):
        """Calculates the hadamard product of two colours."""
        if isinstance(other, self.__class__):
            return self.__class__(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z,
            )
        return super().__mul__(other)

    def __repr__(self):
        return f"Colour(r={self.x:.2f}, g={self.y:.2f}, b={self.z:.2f})"


def point(x: float = 0, y: float = 0, z: float = 0):
    return Tuple(x, y, z, 1)


def vector(x: float = 0, y: float = 0, z: float = 0):
    return Tuple(x, y, z, 0)
