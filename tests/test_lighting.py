import math

from raycaster.ray import Sphere
from raycaster.transformation import rotation_z, scaling, translation
from raycaster.vector import point, vector


class TestLighting:
    def test_normal_x_axis(self):
        s = Sphere()
        n = s.normal_at(point(1, 0, 0))
        assert n == vector(1, 0, 0)

    def test_normal_y_axis(self):
        s = Sphere()
        n = s.normal_at(point(0, 1, 0))
        assert n == vector(0, 1, 0)

    def test_normal_z_axis(self):
        s = Sphere()
        n = s.normal_at(point(0, 0, 1))
        assert n == vector(0, 0, 1)

    def test_normal_nonaxial(self):
        ROOT_3_OVER_3 = (3**0.5) / 3
        s = Sphere()
        n = s.normal_at(point(ROOT_3_OVER_3, ROOT_3_OVER_3, ROOT_3_OVER_3))
        assert n == vector(ROOT_3_OVER_3, ROOT_3_OVER_3, ROOT_3_OVER_3)

    def test_normal_is_normalized(self):
        s = Sphere()
        n = s.normal_at(point(1, 2, 3))
        assert n == n.normalize()

    def test_normal_after_translation(self):
        s = Sphere()
        s.set_transform(translation(0, 1, 0))
        n = s.normal_at(point(0, 1.70711, -0.70711))
        assert n.is_close(vector(0, 0.70711, -0.70711))

    def test_normal_after_transformation(self):
        s = Sphere()
        s.set_transform(scaling(1, 0.5, 1) * rotation_z(math.pi / 5))
        n = s.normal_at(point(0, (2**0.5) / 2, -(2**0.5) / 2))
        assert n.is_close(vector(0, 0.97014, -0.24254))
