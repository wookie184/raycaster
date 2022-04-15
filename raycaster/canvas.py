import os
from typing import Generator

from .vector import Colour


def chunk(seq: list[str], n: int) -> Generator[list[str]]:
    for i in range(0, len(seq), n):
        yield seq[i : i + n]


class Canvas:
    def __init__(self, width: int, height: int) -> None:
        self.height = height
        self.width = width
        self.pixels = [[Colour(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def write(self, x: int, y: int, colour: Colour) -> None:
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError("Canvas write out of range")
        self.pixels[y][x] = colour

    def get(self, x: int, y: int) -> Colour:
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError("Canvas read out of range")
        return self.pixels[y][x]

    def as_ppm_string(self) -> str:
        header = f"P3\n{self.width} {self.height}\n255\n"
        body = "\n".join(
            "\n".join(
                " ".join(line)
                for line in chunk(
                    [
                        f"{pixel.r*255:.0f} {pixel.g*255:.0f} {pixel.b*255:.0f}"
                        for pixel in row
                    ],
                    5,
                )
            )
            for row in self.pixels
        )
        return header + body + "\n"

    def save_ppm(self, path: os.PathLike) -> None:
        data = self.as_ppm_string()
        with open(path, "w") as f:
            f.write(data)
