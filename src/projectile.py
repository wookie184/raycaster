from vector import vector, point, Tuple
from typing import NamedTuple

class Projectile(NamedTuple):
    position: Tuple
    velocity: Tuple

class Environment(NamedTuple):
    gravity: Tuple
    wind: Tuple


def main():
    proj = Projectile(
        position=point(0, 1, 0),
        velocity=vector(1, 1, 0).normalize()
    )
    env = Environment(
        vector(0, -0.1, 0),
        vector(-0.01, 0, 0)
    )

    while proj.position.y > 0:
        position = proj.position + proj.velocity
        velocity = proj.velocity + env.gravity + env.wind
        proj = Projectile(position, velocity)
        print(proj.position)


if __name__ == "__main__":
    main()