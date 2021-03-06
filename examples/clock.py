import math
from pathlib import Path

from raycaster.canvas import Canvas
from raycaster.transformation import rotation_z
from raycaster.vector import Colour, point, vector

FILE_DIR = Path(__file__).parent.parent / "renders"
FILE_DIR.mkdir(exist_ok=True)


def main() -> None:
    c = Canvas(500, 500)
    top = point(0, 1, 0) * 200
    for rot in range(12):
        theta = rot * (math.pi / 6)
        rotation = rotation_z(theta)

        res = rotation * top + vector(250, 250, 0)
        c.write(int(res.x), int(res.y), Colour(255, 0, 0))
    c.save_ppm(FILE_DIR / "clock_render.ppm")


if __name__ == "__main__":
    main()
