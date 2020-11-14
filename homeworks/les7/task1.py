"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы
и т.д.
"""


def my_zip(*args):
    # Минимальная длина списка из числа переданных функции
    min_len = len(sorted(args, key=len)[0])
    return (tuple([args[index][index2] for index in range(len(args))]) for index2 in range(min_len))


def my_easy_map(func, collect):
    return [func(item) for item in collect]


class Matrix:

    def __init__(self, matrix_data: list):
        self.__matrix_data = matrix_data
        self.check_dimension()

    def check_dimension(self):
        standard = len(self.__matrix_data[0])
        for index, tmp_list in enumerate(self.__matrix_data, 1):
            if len(tmp_list) != standard:
                raise ValueError(f'Wrong dimension in {index} row of matrix!\n')

    @property
    def matrix_data(self):
        return self.__matrix_data

    def __str__(self):
        result_str = ''
        for tmp_list in self.__matrix_data:
            for item in tmp_list:
                result_str += str(item) + '  '
            result_str += '\n'
        return result_str

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.matrix_data) != len(other.matrix_data):
                raise TypeError("Different number of rows in matrices!\n")
            elif len(self.matrix_data[0]) != len(other.matrix_data[0]):
                raise TypeError("Different number of columns in matrices!\n")
            else:
                # Сделал с помощью list comprehensions
                return Matrix([my_easy_map(lambda x: x[0] + x[1], my_zip(row, other.matrix_data[index]))
                               for index, row in enumerate(self.matrix_data)])

                # Здесь более удобочитаемая реализация формирования суммы матриц
                # matrix_sum = []
                # for index, row in enumerate(self.matrix_data):
                    # matrix_sum.append(list(map(lambda x: x[0] + x[1], zip(row, other.matrix_data[index]))))
                    # matrix_sum.append(my_easy_map(lambda x: x[0] + x[1], my_zip(row, other.matrix_data[index])))
                # return Matrix(matrix_sum)
        else:
            raise TypeError("Attempt to add a type another than 'Matrix'\n")


# Неправильная размерность одной из строк матрицы.
try:
    matrix = Matrix([[1, 2, 4, 5], [3, 4, 7, 8], [2, 4], [2, 54, 44, 66]])
except ValueError as ve:
    print('1')
    print(ve)

matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[21, -8], [13, -3], [9, -6]])
matrix12 = matrix1 + matrix2
print('2')
print(matrix12)

matrix3 = Matrix([[23, -7, 32, 2], [12, 44, -8, 4], [1, 32, 33, 4]])
matrix4 = Matrix([[32, 7, 8, 3], [13, -44, -2, 1], [4, 3, -3, 1]])
matrix34 = matrix3 + matrix4
print('3')
print(matrix34)

try:
    matrix5 = matrix1 + 5
except TypeError as te:
    print('4')
    print(te)

matrix6 = Matrix([[1, 2, 3], [2, 3, 4], [4, 5, 7]])
matrix7 = Matrix([[1, 2, 4], [3, 5, 6], [3, 4, 5], [6, 5, 7]])
matrix8 = Matrix([[1, 3, 4, 5], [4, 5, 5, 6], [1, 1, 2, 3], [3, 5, 6, 7]])

try:
    matrix67 = matrix6 + matrix7
except TypeError as te:
    print('5')
    print(te)

try:
    matrix78 = matrix7 + matrix8
except TypeError as te:
    print('6')
    print(te)
