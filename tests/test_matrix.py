from ..src.raycaster.vector import Tuple
from ..src.raycaster.matrix import Matrix

class TestMatrix:
    def test_create(self):
        m = Matrix([0]*16)

    def test_create_2x2(self):
        # fmt: off
        m = Matrix([
            -3,  5,
             1, -2,
        ])
        # fmt: on
        assert m[0, 0] == -3
        assert m[0, 1] == 5
        assert m[1, 0] == 1
        assert m[1, 1] == -2
    
    def test_get_row(self):
        m = Matrix(range(16))
        assert m[0] == [0, 1, 2, 3]
        assert m[1] == [4, 5, 6, 7]
        assert m[-1] == [12, 13, 14, 15]

    def test_equality(self):
        a = Matrix(range(16))
        b = Matrix(range(16))
        c = Matrix([0]*16)
        d = Matrix([0]*9)

        assert a == b
        assert b != c
        assert c != d

        a[-1, -1] = 1
        assert a != b
        b[-1, -1] = 1
        assert a == b

    def test_equality_float(self):
        a = Matrix([0, 100, 1e-50, 0])
        b = Matrix([0, 100 + 1e-10, 0, 0])
        assert a == b

    def test_get_col(self):
        m = Matrix(range(16))
        assert m[:, 0] == [0, 4, 8, 12]
        assert m[:, 1] == [1, 5, 9, 13]
        assert m[:, -1] == [3, 7, 11, 15]

    def test_get_elem(self):
        m = Matrix(range(16))
        assert m[0, 0] == 0
        assert m[2, 1] == 9
        assert m[1, 2] == 6
        assert m[-1, -1] == 15

    def test_get_row_slice(self):
        m = Matrix(range(16))
        assert m[0, :] == [0, 1, 2, 3]
        assert m[1, :] == [4, 5, 6, 7]
        assert m[-1, :] == [12, 13, 14, 15]

    def test_set_row(self):
        m = Matrix([0]*16)

        m[0] = [0, 1, 2, 3]
        assert m[0] == [0, 1, 2, 3]
        m[1] = [4, 5, 6, 7]
        assert m[1] == [4, 5, 6, 7]
        m[-1] = [12, 13, 14, 15]
        assert m[-1] == [12, 13, 14, 15]

    def test_set_element(self):
        m = Matrix([0]*16)
        m[0, 0] = 1
        assert m[0, 0] == 1
        m[2, 1] = 6
        assert m[2, 1] == 6
        m[1, 2] = 9
        assert m[1, 2] == 9
        m[-1, -1] = 15
        assert m[-1, -1] == 15
    
    def test_set_column(self):
        m = Matrix([0]*16)
        m[:, 0] = [0, 4, 8, 12]
        assert m[:, 0] == [0, 4, 8, 12]
        m[:, 1] = [1, 5, 9, 13]
        assert m[:, 1] == [1, 5, 9, 13]
        m[:, -1] = [3, 7, 11, 15]
        assert m[:, -1] == [3, 7, 11, 15]

    def test_set_row_slice(self):
        m = Matrix([0]*16)
        m[0, :] = [0, 1, 2, 3]
        assert m[0, :] == [0, 1, 2, 3]
        m[1, :] = [4, 5, 6, 7]
        assert m[1, :] == [4, 5, 6, 7]
        m[-1, :] = [12, 13, 14, 15]
        assert m[-1, :] == [12, 13, 14, 15]

    def test_multiply_self(self):
        # fmt: off
        a = Matrix([
            1, 2, 3, 4,
            5, 6, 7, 8, 
            9, 8, 7, 6, 
            5, 4, 3, 2,
        ])
        b = Matrix([
            -2,  1,  2,  3,
             3,  2,  1, -1,
             4,  3,  6,  5,
             1,  2,  7,  8,
        ])
        assert a * b == Matrix([
            20,  22,  50,  48,
            44,  54, 114, 108,
            40,  58, 110, 102,
            16,  26,  46,  42,
        ])
        # fmt: on

    def test_multiply_tuple(self):
        # fmt: off
        a = Matrix([
            1, 2, 3, 4,
            2, 4, 4, 2,
            8, 6, 4, 1,
            0, 0, 0, 1,
        ])
        # fmt: on
        b = Tuple(1, 2, 3, 1)
        assert a * b == Tuple(18, 24, 33, 1)

    def test_multiply_identity(self):
        # fmt: off
        a = Matrix([
            0,  1,  2,  4,
            1,  2,  4,  8,
            2,  4,  8, 16,
            4,  8, 16, 32,
        ])
        # fmt: on
        b = Matrix.identity()
        assert a * b == a
        
        c = Tuple(1,2,3,4)
        assert b * c == c

    def test_transpose(self):
        # fmt: off
        a = Matrix([
            0, 9, 3, 0, 
            9, 8, 0, 8, 
            1, 8, 5, 3, 
            0, 0, 5, 8,
        ])
        b = Matrix([
            0, 9, 1, 0, 
            9, 8, 8, 0, 
            3, 0, 5, 5, 
            0, 8, 3, 8,
        ])
        # fmt: on

        assert a.transpose() == b

    def test_transpose_identity(self):
        assert Matrix.identity().transpose() == Matrix.identity()

    def test_determinant_2x2(self):
        # fmt: off
        a = Matrix([
             1, 5,
            -3, 2,
        ])
        # fmt: off
        assert a.determinant() == 17

    def test_submatrix(self):
        # fmt: off
        a = Matrix([
             1,  5,  0,
            -3,  2,  7,
             0,  6, -3,
        ])
        assert a.submatrix(0, 2) == Matrix([
            -3, 2,
             0, 6,
        ])

        b = Matrix([
            -6,  1,  1,  6,
            -8,  5,  8,  6,
            -1,  0,  8,  2,
            -7,  1, -1,  1,
        ])

        assert b.submatrix(2, 1) == Matrix([
            -6,  1,  6,
            -8,  8,  6,
            -7, -1,  1,
        ])
        # fmt: on

    def test_minor(self):
        # fmt: off
        a = Matrix([
             3,  5,  0,
             2, -1, -7,
             6, -1,  5,
        ])
        # fmt: on
        b = a.submatrix(1, 0)

        assert b.determinant() == 25
        assert a.minor(1, 0) == 25

    def test_cofactor(self):
        # fmt: off
        a = Matrix([
             3,  5,  0, 
             2, -1, -7, 
             6, -1,  5,
        ])
        # fmt: on

        assert a.minor(0, 0) == -12
        assert a.cofactor(0, 0) == -12

        assert a.minor(1, 0) == 25
        assert a.cofactor(1, 0) == -25

    def test_determinant_3x3(self):
        # fmt: off
        a = Matrix([
             1,  2,  6, 
            -5,  8, -4, 
             2,  6,  4,
        ])
        # fmt: on

        assert a.cofactor(0, 0) == 56
        assert a.cofactor(0, 1) == 12
        assert a.cofactor(0, 2) == -46
        assert a.determinant() == -196

    def test_determinant_4x4(self):
        # fmt: off
        a = Matrix([
            -2, -8,  3,  5,
            -3,  1,  7,  3,
             1,  2, -9,  6,
            -6,  7,  7, -9,
        ])
        # fmt: on
        assert a.cofactor(0, 0) == 690
        assert a.cofactor(0, 1) == 447
        assert a.cofactor(0, 2) == 210
        assert a.cofactor(0, 3) == 51
        assert a.determinant() == -4071

    def test_invertability(self):
        # fmt: off
        a = Matrix([
             6,  4,  4,  4, 
             5,  5,  7,  6,
             4, -9,  3, -7, 
             9,  1,  7, -6,
        ])
        # fmt: on
        assert a.determinant() == -2120
        assert a.is_invertible()
        
        # fmt: off
        b = Matrix([
            -4,  2, -2, -3,
             9,  6,  2,  6,
             0, -5,  1, -5, 
             0,  0,  0,  0,
        ])
        # fmt: on
        assert b.determinant() == 0
        assert not b.is_invertible()

    def test_inverse(self):
        # fmt: off
        a = Matrix([
            -5,  2,  6, -8, 
             1, -5,  1,  8, 
             7,  7, -6, -7, 
             1, -3,  7,  4,
        ])
        # fmt: on
        b = a.inverse()

        assert a.determinant() == 532

        assert a.cofactor(2, 3) == -160
        assert b[3, 2] == -160/532
        assert a.cofactor(3, 2) == 105
        assert b[2, 3] == 105/532

        # fmt: off
        exp = Matrix([
             0.21805,  0.45113,  0.24060, -0.04511,
            -0.80827, -1.45677, -0.44361,  0.52068, 
            -0.07895, -0.22368, -0.05263,  0.19737,
            -0.52256, -0.81391, -0.30075,  0.30639,
        ])
        # fmt: on
        assert b.is_close(exp)
        assert not a.is_close(exp)

    def test_more_inverse(self):
        # fmt: off
        a = Matrix([
             8, -5,  9,  2,
             7,  5,  6,  1, 
            -6,  0,  9,  6, 
            -3,  0, -9, -4,
        ])
        exp = Matrix([
            -0.15385, -0.15385, -0.28205, -0.53846,
            -0.07692,  0.12308,  0.02564,  0.03077,
             0.35897,  0.35897,  0.43590,  0.92308,
            -0.69231, -0.69231, -0.76923, -1.92308,
        ])
        # fmt: on
        assert a.inverse().is_close(exp)

        # fmt: off
        b = Matrix([
             9,  3,  0,  9, 
            -5, -2, -6, -3, 
            -4,  9,  6,  4, 
            -7,  6,  6,  2,
        ])
        exp = Matrix([
            -0.04074, -0.07778,  0.14444, -0.22222,
            -0.07778,  0.03333,  0.36667, -0.33333,
            -0.02901, -0.14630, -0.10926,  0.12963,
             0.17778,  0.06667, -0.26667,  0.33333,
        ])
        # fmt: on
        assert b.inverse().is_close(exp)

    def test_mul_inverse(self):
        # fmt: off
        a = Matrix([
             3, -9,  7,  3, 
             3, -8,  2, -9, 
            -4,  4,  4,  1, 
            -6,  5, -1,  1,
        ])
        b = Matrix([
             8,  2,  2,  2,
             3, -1,  7,  0,
             7,  0,  5,  4, 
             6, -2,  0,  5,
        ]) 
        # fmt: on
        c = a * b
        assert c * b.inverse() == a

    def test_repr(self):
        m = Matrix(range(16))
        assert repr(m) == (
            "[0.00   1.00   2.00   3.00   \n"
            " 4.00   5.00   6.00   7.00   \n"
            " 8.00   9.00   10.00  11.00  \n"
            " 12.00  13.00  14.00  15.00]"
        )