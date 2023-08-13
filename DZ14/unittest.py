from DZ14.matrix import Matrix
import unittest


class TestMatrix(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(str(Matrix([[3, 9], [12, 7]]) + Matrix([[1, 4], [27, 0]])))

    def test_mul(self):
        self.assertEqual(str(Matrix([[3, 9], [12, 7]]) * Matrix([[1, 4], [27, 0]])))


if __name__ == '__main__':
    unittest.main(verbosity=2)