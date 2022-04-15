import math

from raycaster.vector import Colour, Tuple, point, vector


class TestTuple:
    def test_point(self):
        """A tuple with w=1.0 is a point"""
        a = Tuple(4.3, -4.2, 3.1, 1.0)
        assert a.x == 4.3
        assert a.y == -4.2
        assert a.z == 3.1
        assert a.is_point()

    def test_vector(self):
        """A tuple with w=0.0 is a vector"""
        a = Tuple(4.3, -4.2, 3.1, 0.0)
        assert a.x == 4.3
        assert a.y == -4.2
        assert a.z == 3.1
        assert not a.is_point()

    def test_equality(self):
        a = Tuple(1.555, 2, 3.2, 0.0)
        b = Tuple(1.555, 2, 3.2, 0.0)
        assert a == b

        c = Tuple(1.555, 2.01, 3.2, 0.0)
        assert c != b

        d = Tuple(1.555, 2, 3.2, 1)
        assert d != b
        assert d != c

        # Should allow if very close (e.g. by floating point innacuracy)
        e = Tuple(1.5550000001, 2, 3.2, 0.0)
        assert a == e

    def test_is_close(self):
        a = Tuple(1.234556, 2, 3.2, 0.0)
        b = Tuple(1.23456, 2, 3.2, 0.0)
        c = Tuple(1.234, 2.1, 3.2, 0.0)

        assert a.is_close(b)
        assert b.is_close(a)

        assert not a.is_close(c)
        assert not c.is_close(a)

    def test_add(self):
        a = Tuple(3, -2, 5, 1)
        b = Tuple(-2, 3, 1, 0)
        c = Tuple(1, 1, 6, 1)
        assert a + b == c

    def test_sub_point_point(self):
        a = point(3, 2, 1)
        b = point(5, 6, 7)
        c = vector(-2, -4, -6)
        assert a - b == c

    def test_sub_point_vec(self):
        a = point(3, 2, 1)
        b = vector(5, 6, 7)
        c = point(-2, -4, -6)
        assert a - b == c

    def test_sub_vec_vec(self):
        a = vector(3, 2, 1)
        b = vector(5, 6, 7)
        assert a - b == vector(-2, -4, -6)

    def test_neg(self):
        a = Tuple(1, -2, 3, -4)
        assert -a == Tuple(-1, 2, -3, 4)

    def test_scalar_mul(self):
        a = Tuple(1, -2, 3, -4)
        assert a * 3.5 == Tuple(3.5, -7, 10.5, -14)
        assert a * 0.5 == Tuple(0.5, -1, 1.5, -2)

    def test_scalar_div(self):
        a = Tuple(1, -2, 3, -4)
        assert a / 2 == Tuple(0.5, -1, 1.5, -2)

    def test_magnitude_simple(self):
        a = vector(1, 0, 0)
        assert a.magnitude() == 1

        b = vector(0, 1, 0)
        assert b.magnitude() == 1

        c = vector(0, 0, 1)
        assert c.magnitude() == 1

    def test_magnitude_float(self):
        a = vector(1, 2, 3)
        assert math.isclose(a.magnitude(), math.sqrt(14))

        b = vector(-1, -2, -3)
        assert math.isclose(b.magnitude(), math.sqrt(14))

    def test_normalize_simple(self):
        a = vector(4, 0, 0)
        assert a.normalize() == vector(1, 0, 0)

    def test_normalize_float(self):
        a = vector(1, 2, 3)
        sqrt14 = math.sqrt(14)
        assert a.normalize() == vector(1 / sqrt14, 2 / sqrt14, 3 / sqrt14)

        assert a.normalize().magnitude() == 1

    def test_dot_product(self):
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        assert a.dot(b) == 20
        assert b.dot(a) == 20

    def test_cross_product(self):
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        assert a.cross(b) == vector(-1, 2, -1)
        assert b.cross(a) == vector(1, -2, 1)

    def test_repr(self):
        p = point(1, 2, 3)
        assert repr(p) == "point(x=1.00, y=2.00, z=3.00)"
        v = vector(1, 2, 3)
        assert repr(v) == "vector(x=1.00, y=2.00, z=3.00)"

        p = point(0.1234567, 1234.8765, -10.5)
        assert repr(p) == "point(x=0.12, y=1234.88, z=-10.50)"


class TestColour:
    def test_add_colour(self):
        a = Colour(0.9, 0.6, 0.75)
        b = Colour(0.7, 0.1, 0.25)
        assert a + b == Colour(1.6, 0.7, 1.0)

    def test_sub_colour(self):
        a = Colour(0.9, 0.6, 0.75)
        b = Colour(0.7, 0.1, 0.25)
        assert a - b == Colour(0.2, 0.5, 0.5)

    def test_mul_colour_scalar(self):
        a = Colour(0.2, 0.3, 0.4)
        assert a * 2 == Colour(0.4, 0.6, 0.8)

    def test_mul_colour_colour(self):
        a = Colour(1, 0.2, 0.4)
        b = Colour(0.9, 1, 0.1)
        assert a * b == Colour(0.9, 0.2, 0.04)

    def test_repr(self):
        c = Colour(0, 0.6, 0.7)
        assert repr(c) == "Colour(r=0.00, g=0.60, b=0.70)"
