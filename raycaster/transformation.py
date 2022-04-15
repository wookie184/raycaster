import math

from .matrix import Matrix


def translation(x: float, y: float, z: float) -> Matrix:
    mat = Matrix.identity()
    mat[0, 3] = x
    mat[1, 3] = y
    mat[2, 3] = z
    return mat


def scaling(x: float, y: float, z: float) -> Matrix:
    mat = Matrix.identity()
    mat[0, 0] = x
    mat[1, 1] = y
    mat[2, 2] = z
    return mat


def rotation_x(r: float) -> Matrix:
    mat = Matrix.identity()
    mat[1, 1] = math.cos(r)
    mat[1, 2] = -math.sin(r)
    mat[2, 1] = math.sin(r)
    mat[2, 2] = math.cos(r)
    return mat


def rotation_y(r: float) -> Matrix:
    mat = Matrix.identity()
    mat[0, 0] = math.cos(r)
    mat[0, 2] = math.sin(r)
    mat[2, 0] = -math.sin(r)
    mat[2, 2] = math.cos(r)
    return mat


def rotation_z(r: float) -> Matrix:
    mat = Matrix.identity()
    mat[0, 0] = math.cos(r)
    mat[0, 1] = -math.sin(r)
    mat[1, 0] = math.sin(r)
    mat[1, 1] = math.cos(r)
    return mat


def shearing(
    xy: float, xz: float, yx: float, yz: float, zx: float, zy: float
) -> Matrix:
    mat = Matrix.identity()
    mat[0, 1] = xy
    mat[0, 2] = xz
    mat[1, 0] = yx
    mat[1, 2] = yz
    mat[2, 0] = zx
    mat[2, 1] = zy
    return mat
