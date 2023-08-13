import pytest

from DZ14.matrix import Matrix
from DZ14.exception import ValFormatError


# проверка сложения матриц 
def test_sum():

   assert (str(Matrix([[0, 3], [7, 7]]) + Matrix([[0, 9], [17, 12]]))) == '[12, -10][40, -5]', "Неверная сумма"

# проверка произведение матриц 
def test_mul():

    assert (str(Matrix([[0, 3], [7, 7]]) * Matrix([[0, 9], [17, 12]]))) == '[-19, -8][200, -200]', "Неверное произведение"

# негативная проверка по формату
def test_format():

    with pytest.raises(ValFormatError):
        Matrix([[1, -2], [25, -5]]) + Matrix([[11, -8], [15, 0], [16, 10]])
        Matrix([[1, -2], [25, -5]]) * Matrix([[11, -8], [15, 0], [16, 10]])


if __name__ == '__main__':
    pytest.main(["-v"])