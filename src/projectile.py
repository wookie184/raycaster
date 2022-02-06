import contextlib
from typing import NamedTuple

from raycaster.canvas import Canvas
from raycaster.vector import Colour, Tuple, point, vector


class Projectile(NamedTuple):
    position: Tuple
    velocity: Tuple


class Environment(NamedTuple):
    gravity: Tuple
    wind: Tuple


def main():
    proj = Projectile(position=point(0, 1, 0), velocity=vector(1, 0.5, 0).normalize())
    env = Environment(vector(0, -0.0001, 0), vector(-0.00005, 0, 0))

    canvas = Canvas(10000, 1500)

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

    canvas.save_ppm("./projectile_plot.ppm")


if __name__ == "__main__":
    main()
