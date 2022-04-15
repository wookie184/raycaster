from __future__ import annotations

import math
import numbers


class Tuple:
    __slots__ = ("x", "y", "z", "w")

    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def is_point(self) -> bool:
        """Returns True if the tuple represents a point (self.w==1)."""
        return self.w == 1

    def __add__(self, other: Tuple) -> Tuple:
        "Add the tuple's elements to another elementwise."
        if isinstance(other, self.__class__):
            return self.__class__(
                x=self.x + other.x,
                y=self.y + other.y,
                z=self.z + other.z,
                w=self.w + other.w,
            )
        return NotImplemented

    def __getitem__(self, i: int) -> float:
        return (self.x, self.y, self.z, self.w)[i]

    def __sub__(self, other: Tuple) -> Tuple:
        "Subtract another tuple's elements elementwise."
        if isinstance(other, self.__class__):
            return self.__class__(
                x=self.x - other.x,
                y=self.y - other.y,
                z=self.z - other.z,
                w=self.w - other.w,
            )
        return NotImplemented

    def __mul__(self, other: float) -> Tuple:
        """Multiply the tuple's elements by a scalar."""
        if isinstance(other, numbers.Number):
            return self.__class__(
                x=self.x * other,
                y=self.y * other,
                z=self.z * other,
                w=self.w * other,
            )
        return NotImplemented

    def __truediv__(self, other: float) -> Tuple:
        """Divide the tuple's elements by a scalar."""
        if isinstance(other, numbers.Number):
            return self.__class__(
                x=self.x / other,
                y=self.y / other,
                z=self.z / other,
                w=self.w / other,
            )
        return NotImplemented

    def __neg__(self) -> Tuple:
        """Negate the tuple's elements."""
        return self.__class__(x=-self.x, y=-self.y, z=-self.z, w=-self.w)

    def dot(self, other: Tuple) -> float:
        """Calculates the dot product of the tuple."""
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def normalize(self) -> Tuple:
        """Normalizes a vector."""
        assert not self.is_point()

        total = (self.x**2 + self.y**2 + self.z**2) ** 0.5
        return self.__class__(
            x=self.x / total,
            y=self.y / total,
            z=self.z / total,
            w=self.w / total,
        )

    def magnitude(self) -> float:
        """Calculates the magnitude of the vector."""
        assert not self.is_point()

        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def cross(self, other: Tuple) -> Tuple:
        """Calculates the cross product of two vectors."""
        assert not self.is_point()

        return self.__class__(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
            0,
        )

    def is_close(self, other: Tuple, abs_tol: float = 1e-5) -> bool:
        return (
            all(
                math.isclose(a1, a2, abs_tol=abs_tol)
                for a1, a2 in zip((self.x, self.y, self.z), (other.x, other.y, other.z))
            )
            and self.is_point() == other.is_point()
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            abs_tol = 1e-10
            return self.is_close(other, abs_tol)

        return NotImplemented

    def __repr__(self) -> str:
        name = "point" if self.is_point() else "vector"
        return f"{name}(x={self.x:.2f}, y={self.y:.2f}, z={self.z:.2f})"


def clamp(n: float, lo: float, hi: float) -> float:
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

    def __repr__(self) -> str:
        return f"Colour(r={self.x:.2f}, g={self.y:.2f}, b={self.z:.2f})"


def point(x: float = 0, y: float = 0, z: float = 0):
    return Tuple(x, y, z, 1)


def vector(x: float = 0, y: float = 0, z: float = 0):
    return Tuple(x, y, z, 0)
