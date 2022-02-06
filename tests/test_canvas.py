import pytest

from ..src.raycaster.canvas import Canvas
from ..src.raycaster.vector import Colour


class TestCanvas:
    def test_canvas(self):
        c = Canvas(40, 10)
        assert c.height == 10
        assert c.width == 40

        c = Canvas(1000, 500)
        assert c.height == 500
        assert c.width == 1000

    def test_read_write(self):
        c = Canvas(10, 40)
        col1 = Colour(0.5, 0.4, 0.3)
        c.write(2, 5, col1)
        assert c.get(2, 5) == col1

        assert c.get(0, 0) == Colour(0, 0, 0)
        assert c.get(9, 39) == Colour(0, 0, 0)

        col2 = Colour(1, 0, 0)
        c.write(9, 39, col2)
        c.write(0, 0, col2)

        assert c.get(0, 0) == col2
        assert c.get(9, 39) == col2

    def test_out_of_bounds_read(self):
        c = Canvas(10, 10)
        with pytest.raises(IndexError):
            c.get(0, 10)

        with pytest.raises(IndexError):
            c.get(-1, 0)

        with pytest.raises(TypeError):
            c.get(0.5, 0)

    def test_out_of_bounds_write(self):
        c = Canvas(10, 10)
        col = Colour(0, 0, 0)
        with pytest.raises(IndexError):
            c.write(10, 0, col)

        with pytest.raises(IndexError):
            c.write(0, -1, col)

        with pytest.raises(TypeError):
            c.write(0, 0.5, col)

    def test_ppm(self):
        c = Canvas(2, 1)

        assert c.as_ppm_string() == "P3\n2 1\n255\n0 0 0 0 0 0\n"

        c.write(0, 0, Colour(-0.1, 0.456, 1.1))
        assert c.as_ppm_string() == "P3\n2 1\n255\n0 116 255 0 0 0\n"

        c = Canvas(5, 3)

        c.write(0, 0, Colour(1.5, 0, 0))
        c.write(2, 1, Colour(0, 0.5, 0))
        c.write(4, 2, Colour(-0.5, 0.5, 1))

        assert c.as_ppm_string().splitlines(True)[3:6] == [
            "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n",
            "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 128 255\n",
        ]

        c = Canvas(9, 2)
        for x in range(c.width):
            for y in range(c.height):
                c.write(x, y, Colour(1, 0.8, 0.6))

        assert c.as_ppm_string().splitlines(True)[3:7] == [
            "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153\n",
            "255 204 153 255 204 153 255 204 153 255 204 153\n",
            "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153\n",
            "255 204 153 255 204 153 255 204 153 255 204 153\n",
        ]
        assert c.as_ppm_string().endswith("\n")
