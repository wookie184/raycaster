from vector import Colour
import os

def chunk(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i: i+n]

class Canvas:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.pixels = [
            Colour(0, 0, 0) for _ in range(width*height)
        ]

    def write(self, x: int, y: int, colour: Colour):
        self.pixels[y*self.width + x] = colour

    def get(self, x: int, y: int):
        return self.pixels[y*self.width + x]

    def save_to_ppm_string(self):
        header = (
            "P3\n",
            f"{self.width} {self.width}\n",
            "255\n"
        )
        body = '\n'.join(
            ' '.join(line)
            for line in
            chunk(
                (f'{p.x*255} {p.y*255} {p.z*255}' for p in self.pixels),
                 15
            )
        )
        return header + body + "\n"

    def save_ppm(self,path: os.PathLike):
        data = self.save_to_ppm_string()
        with open(path, "w") as f:
            f.write(data)

    