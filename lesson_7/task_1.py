"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


# inherit class ArithmeticError exception
class MatrixException(ArithmeticError):
    pass


class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        result = ''
        for row in self.matrix_data:
            result += f'{" ".join(map(str, row))}\n'
        return result

    def __add__(self, other):
        try:
            if self != other:
                raise MatrixException('Warning! Matrix should have the same size.')
            else:
                result_matrix = []
                for row1, row2 in zip(self.matrix_data, other.matrix_data):
                    result_row = []
                    for el1, el2 in zip(row1, row2):
                        result_row.append(el1 + el2)
                    result_matrix.append(result_row)
                return Matrix(result_matrix)
        except MatrixException as err:
            print(err)

    # simple check of matrix size (rows and columns), without checking elements values
    def __eq__(self, other):
        return len(self.matrix_data) == len(other.matrix_data) and len(self.matrix_data[0]) == len(other.matrix_data[0])


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
m_3 = Matrix([[10, 10, 10], [20, 20, 20], [30, 30, 30]])
print(m_1)
print(m_2)
print(m_3)
print('Результат сложения трех матриц:\n', m_1 + m_2 + m_3, sep='')

# raise MatrixException
m_4 = Matrix([[1, 2], [3, 4]])
print(m_1 + m_4)
