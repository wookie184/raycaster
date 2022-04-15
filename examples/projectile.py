import contextlib
from pathlib import Path
from typing import NamedTuple

from raycaster.canvas import Canvas
from raycaster.vector import Colour, Tuple, point, vector

FILE_DIR = Path(__file__).parent.parent / "renders"
FILE_DIR.mkdir(exist_ok=True)


class Projectile(NamedTuple):
    position: Tuple
    velocity: Tuple


class Environment(NamedTuple):
    gravity: Tuple
    wind: Tuple


def main() -> None:
    proj = Projectile(
        position=point(0, 1, 0), velocity=vector(1, 1, 0).normalize() * 1.3
    )
    env = Environment(vector(0, -0.001, 0), vector(-0.0005, 0, 0))

    canvas = Canvas(1000, 500)

    while proj.position.y >= 0:
        position = proj.position + proj.velocity
        velocity = proj.velocity + env.gravity + env.wind
        proj = Projectile(position, velocity)
        with contextlib.suppress(IndexError):
            canvas.write(
                int(proj.position.x),
                canvas.height - int(proj.position.y),
                Colour(1, 0, 0),
            )

    canvas.save_ppm(FILE_DIR / "projectile_plot.ppm")


if __name__ == "__main__":
    main()
