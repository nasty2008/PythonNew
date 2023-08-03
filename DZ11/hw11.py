class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.data:
            result += " ".join(str(element) for element in row) + "\n"
        return result

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self.rows != other.rows or self.columns != other.columns:
            return False
        for i in range(self.rows):
            for j in range(self.columns):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Невозможно добавить данную нематрицу к матрице")
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Невозможно добавить матрицы разных размеров")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.data[i][j] = self.data[i][j] * other
            return result
        elif isinstance(other, Matrix):
            if self.columns != other.rows:
                raise ValueError("Невозможно умножить матрицы несовместимых размеров")
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise TypeError("Невозможно умножить матрицу на нематричную систему")


m1 = Matrix(2, 2)
m1.data = [[2, 3], [4, 5]]
m2 = Matrix(2, 2)
m2.data = [[5, 4], [3, 2]]
print(m1)
print(m1 == m2)
m3 = m1 + m2
print(m3)
m4 = m2 * 2
print(m4)
m5 = m1 * m2
print(m5)