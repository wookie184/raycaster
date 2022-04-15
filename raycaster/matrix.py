import math

from .vector import Tuple


class Matrix:
    def __init__(self, data):
        self.data = [float(el) for el in data]
        self.size = int(len(self.data) ** 0.5)

    def __getitem__(self, index):
        match index:
            case int() as row:
                return self.data[
                    (row % self.size) * self.size : (row % self.size) * self.size
                    + self.size
                ]
            case slice() as rows:
                return [
                    self.data[n * self.size : n * self.size + self.size]
                    for n in range(self.size)[rows]
                ]
            case (int() as row, int() as col):
                return self.data[(row % self.size) * self.size + col % self.size]
            case (slice() as rows, int() as col):
                return [
                    self.data[n * self.size : n * self.size + self.size][col]
                    for n in range(self.size)[rows]
                ]
            case (int() as row, slice() as cols):
                return [self.data[n :: self.size][row] for n in range(self.size)[cols]]
        return ValueError("Cannot understand that getitem format")

    def __setitem__(self, index, val):
        match index:
            case int() as row:
                self.data[
                    (row % self.size) * self.size : (row % self.size) * self.size
                    + self.size
                ] = val
            case slice() as rows:
                for n, new in zip(range(self.size)[rows], val):
                    self.data[n * self.size : n * self.size + self.size] = new
            case (int() as row, int() as col):
                self.data[(row % self.size) * self.size + col % self.size] = val
            case (slice() as rows, int() as col) if rows == slice(None):
                self.data[col % self.size :: self.size] = val
            case (int() as row, slice() as cols) if cols == slice(None):
                self.data[
                    (row % self.size) * self.size : (row % self.size) * self.size
                    + self.size
                ] = val
        return ValueError("Cannot understand that setitem format")

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            assert self.size == other.size == 4
            new_data = []
            for row in range(4):
                for col in range(4):
                    new_data.append(sum(self[row, i] * other[i, col] for i in range(4)))
            return self.__class__(new_data)
        elif isinstance(other, Tuple):
            return Tuple(
                sum(a * b for a, b in zip(self[0], other)),
                sum(a * b for a, b in zip(self[1], other)),
                sum(a * b for a, b in zip(self[2], other)),
                sum(a * b for a, b in zip(self[3], other)),
            )
        raise NotImplementedError

    def transpose(self):
        return self.__class__(el for row in zip(*self[:]) for el in row)

    def determinant(self):
        if self.size == 2:
            return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]

        return sum(self.cofactor(0, pos) * el for pos, el in enumerate(self[0]))

    def submatrix(self, row, column):
        return self.__class__(
            [
                el
                for pos, el in enumerate(self.data)
                if pos % self.size != column and pos // self.size != row
            ]
        )

    def minor(self, row, column):
        return self.submatrix(row, column).determinant()

    def cofactor(self, row, column):
        return self.minor(row, column) * (1 if (row + column) % 2 == 0 else -1)

    def is_invertible(self):
        return self.determinant() != 0

    def inverse(self):
        new_data = []
        det = self.determinant()
        for row in range(self.size):
            for col in range(self.size):
                c = self.cofactor(row, col)
                new_data.append(c / det)
        return self.__class__(new_data).transpose()

    def __repr__(self):
        res = []
        for i, el in enumerate(self.data):
            if i % self.size == 0:
                res.append("\n ")
            res.append(f"{el:<7.2f}")
        return "[" + "".join(res).strip() + "]"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.is_close(other, abs_tol=1e-10)
        return NotImplemented

    def is_close(self, other, abs_tol=1e-5):
        if self.size != other.size:
            return False
        return all(
            math.isclose(a, b, abs_tol=abs_tol) for a, b in zip(self.data, other.data)
        )

    @classmethod
    def identity(cls):
        # fmt: off
        return cls([
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        ])
        # fmt: on
