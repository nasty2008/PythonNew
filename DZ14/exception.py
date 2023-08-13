class ValFormatError(Exception):
    def __str__(self):
        return f"Error: Нет возможности сравнить. Матрицы разных размеров"