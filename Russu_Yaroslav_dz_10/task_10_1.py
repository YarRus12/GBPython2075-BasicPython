from typing import List

class Matrix:
    def __init__(self, matrix: List[List[int]]):
        len_row = len(matrix[0])
        for row in matrix:
            if len(row) != len_row:
                raise ValueError(f'fail initialization matrix')
        self.matrix = matrix

    def __str__(self):
        """реализовать перегрузку метода __str__() для вывода матрицы в привычном виде"""
        s = ''
        for i in range(len(self.matrix)):
            s += f' | {" ".join(map(str, self.matrix[i]))} |'+'\n'
        return s

    def __add__(self, other):
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                raise ValueError('Матрицы не совпадают')
        """Запишу себе этот пример как best practice"""
        return Matrix([list(map(sum,zip(row_1, row_2)))
                       for row_1, row_2 in zip(self.matrix,other.matrix)])

if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(first_matrix + second_matrix)

    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """