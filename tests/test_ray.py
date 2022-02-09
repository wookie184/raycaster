from raycaster.matrix import Matrix
from raycaster.ray import Intersection, Intersections, Ray, Sphere
from raycaster.transformation import scaling, translation
from raycaster.vector import point, vector


class TestRay:
    def test_create(self):
        origin = point(1, 2, 3)
        direction = vector(4, 5, 6)
        ray = Ray(origin, direction)

        assert ray.origin == origin
        assert ray.direction == direction

    def test_position(self):
        r = Ray(point(2, 3, 4), vector(1, 0, 0))
        assert r.position(0) == point(2, 3, 4)
        assert r.position(1) == point(3, 3, 4)
        assert r.position(-1) == point(1, 3, 4)
        assert r.position(2.5) == point(4.5, 3, 4)

    def test_translate(self):
        r = Ray(point(1, 2, 3), vector(0, 1, 0))
        t = translation(3, 4, 5)
        r2 = r.transform(t)
        assert r2.origin == point(4, 6, 8)
        assert r2.direction == vector(0, 1, 0)

    def test_scale(self):
        r = Ray(point(1, 2, 3), vector(0, 1, 0))
        t = scaling(2, 3, 4)
        r2 = r.transform(t)
        assert r2.origin == point(2, 6, 12)
        assert r2.direction == vector(0, 3, 0)


class TestSphere:
    def test_create_sphere(self):
        s = Sphere()
        assert s.transform == Matrix.identity()

    def test_set_transform(self):
        s = Sphere()

        t = translation(2, 3, 4)
        s.set_transform(t)
        assert s.transform == t

        t2 = scaling(3, 4, 5)
        s.set_transform(t2)
        assert s.transform == t2


class TestIntersections:
    def test_create_intersection(self):
        s = Sphere()
        i = Intersection(3.5, s)
        assert i.t == 3.5
        assert i.obj == s

    def test_create_intersections(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections(i1, i2)
        assert xs.count == 2
        assert xs[0].t == 1
        assert xs[1].t == 2


class TestIntersect:
    def test_ray_sphere(self):
        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        assert xs.count == 2
        assert xs[0].t == 4.0
        assert xs[1].t == 6.0

    def test_ray_sphere_tangent(self):
        r = Ray(point(0, 1, -5), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        assert xs.count == 2
        assert xs[0].t == 5
        assert xs[1].t == 5

    def test_ray_sphere_miss(self):
        r = Ray(point(0, 2, -5), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        assert xs.count == 0

    def test_ray_inside_sphere(self):
        r = Ray(point(0, 0, 0), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        assert xs.count == 2
        assert xs[0].t == -1
        assert xs[1].t == 1

    def test_ray_in_front_of_sphere(self):
        r = Ray(point(0, 0, 5), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        assert xs.count == 2
        assert xs[0].t == -6
        assert xs[1].t == -4

    def test_object_is_set(self):
        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        assert xs.count == 2
        assert xs[0].obj == s
        assert xs[1].obj == s


class TestHit:
    def test_all_positive_t(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections(i1, i2)
        i = xs.hit()
        assert i == i1

    def test_some_negative_t(self):
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(1, s)
        xs = Intersections(i1, i2)
        i = xs.hit()
        assert i == i2

    def test_all_negative_t(self):
        s = Sphere()
        i1 = Intersection(-2, s)
        i2 = Intersection(-1, s)
        xs = Intersections(i1, i2)
        i = xs.hit()
        assert i is None

    def test_many_intersections(self):
        s = Sphere()
        i1 = Intersection(5, s)
        i2 = Intersection(7, s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2, s)
        xs = Intersections(i1, i2, i3, i4)
        i = xs.hit()
        assert i == i4
