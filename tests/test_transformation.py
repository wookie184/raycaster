import math

from ..src.raycaster.transformation import (
    rotation_x,
    rotation_y,
    rotation_z,
    scaling,
    shearing,
    translation,
)
from ..src.raycaster.vector import point, vector


class TestTransformations:
    def test_translate_point(self):
        t = translation(5, -3, 2)
        p = point(-3, 4, 5)
        assert t * p == point(2, 1, 7)

    def test_inverse_translate_point(self):
        t = translation(5, -3, 2).inverse()
        p = point(-3, 4, 5)
        assert t * p == point(-8, 7, 3)

    def test_translate_vector(self):
        t = translation(5, -3, 2)
        v = vector(-3, 4, 5)
        assert t * v == v

    def test_scale_point(self):
        t = scaling(2, 3, 4)
        p = point(-4, 6, 8)
        assert t * p == point(-8, 18, 32)

    def test_scale_vector(self):
        t = scaling(2, 3, 4)
        v = vector(-4, 6, 8)
        assert t * v == vector(-8, 18, 32)

    def test_inverse_scale_vector(self):
        t = scaling(2, 3, 4).inverse()
        v = vector(-4, 6, 8)
        assert t * v == vector(-2, 2, 2)

    def test_reflection(self):
        t = scaling(-1, 1, 1)
        p = point(2, 3, 4)
        assert t * p == point(-2, 3, 4)

    def test_rotation_x(self):
        p = point(0, 1, 0)
        half_quarter = rotation_x(math.pi / 4)
        full_quarter = rotation_x(math.pi / 2)

        assert half_quarter * p == point(0, (2**0.5) / 2, (2**0.5) / 2)
        assert full_quarter * p == point(0, 0, 1)

    def test_rotation_x_inverse(self):
        p = point(0, 1, 0)
        half_quarter_inv = rotation_x(math.pi / 4).inverse()
        assert half_quarter_inv * p == point(0, (2**0.5) / 2, -(2**0.5) / 2)

    def test_rotation_y(self):
        p = point(0, 0, 1)
        half_quarter = rotation_y(math.pi / 4)
        full_quarter = rotation_y(math.pi / 2)

        assert half_quarter * p == point((2**0.5) / 2, 0, (2**0.5) / 2)
        assert full_quarter * p == point(1, 0, 0)

    def test_rotation_z(self):
        p = point(0, 1, 0)
        half_quarter = rotation_z(math.pi / 4)
        full_quarter = rotation_z(math.pi / 2)

        assert half_quarter * p == point(-(2**0.5) / 2, (2**0.5) / 2, 0)
        assert full_quarter * p == point(-1, 0, 0)

    def test_shear_x_prop_y(self):
        t = shearing(1, 0, 0, 0, 0, 0)
        p = point(2, 3, 4)
        assert t * p == point(5, 3, 4)

    def test_shear_x_prop_z(self):
        t = shearing(0, 1, 0, 0, 0, 0)
        p = point(2, 3, 4)
        assert t * p == point(6, 3, 4)

    def test_shear_y_prop_x(self):
        t = shearing(0, 0, 1, 0, 0, 0)
        p = point(2, 3, 4)
        assert t * p == point(2, 5, 4)

    def test_shear_y_prop_z(self):
        t = shearing(0, 0, 0, 1, 0, 0)
        p = point(2, 3, 4)
        assert t * p == point(2, 7, 4)

    def test_shear_z_prop_x(self):
        t = shearing(0, 0, 0, 0, 1, 0)
        p = point(2, 3, 4)
        assert t * p == point(2, 3, 6)

    def test_shear_z_prop_y(self):
        t = shearing(0, 0, 0, 0, 0, 1)
        p = point(2, 3, 4)
        assert t * p == point(2, 3, 7)

    def test_multiple_transformations(self):
        p = point(1, 0, 1)
        a = rotation_x(math.pi / 2)
        b = scaling(5, 5, 5)
        c = translation(10, 5, 7)

        p2 = a * p
        assert p2 == point(1, -1, 0)

        p3 = b * p2
        assert p3 == point(5, -5, 0)

        p4 = c * p3
        assert p4 == point(15, 0, 7)

    def test_chained_transformations(self):
        p = point(1, 0, 1)
        a = rotation_x(math.pi / 2)
        b = scaling(5, 5, 5)
        c = translation(10, 5, 7)

        t = c * b * a
        assert t * p == point(15, 0, 7)
