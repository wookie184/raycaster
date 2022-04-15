from pathlib import Path

from raycaster.canvas import Canvas
from raycaster.ray import Ray, Sphere
from raycaster.transformation import shearing
from raycaster.vector import Colour, point

FILE_DIR = Path(__file__).parent.parent / "renders"
FILE_DIR.mkdir(exist_ok=True)


def main() -> None:
    size = 500
    print("Creating canvas...")
    c = Canvas(size, size)
    print("Canvas created")
    s = Sphere()
    t = shearing(0.5, 0, 0, 0, 0, 0.3)
    s.set_transform(t)

    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 7
    pixel_size = wall_size / size

    print("Rendering...")
    for x in range(size):
        for y in range(size):
            wy = -(wall_size / 2) + pixel_size * x
            wx = -(wall_size / 2) + pixel_size * y

            pos = point(wx, wy, wall_z)

            ray = Ray(ray_origin, (pos - ray_origin).normalize())
            ray = ray.transform(s.transform)
            xs = ray.intersect(s)
            if xs.count > 0:
                col = Colour(50, abs(xs.hit().t) * 10 % 1, 50)
                c.write(x, y, col)
    print("Saving...")
    c.save_ppm(FILE_DIR / "2d_cast.ppm")
    print("Done!")


if __name__ == "__main__":
    main()
