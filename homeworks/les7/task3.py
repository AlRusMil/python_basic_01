"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме
ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек
в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все
оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:

    def __init__(self, count: int):
        self.__cell_count = count

    @property
    def cell_count(self):
        return self.__cell_count

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.cell_count + other.cell_count)
        else:
            raise TypeError("Attempt to add another type than 'Cell'\n")

    def __sub__(self, other):
        if isinstance(other, Cell):
            if self.cell_count > other.cell_count:
                return Cell(self.cell_count - other.cell_count)
            else:
                raise ValueError("Incorrect value for subtraction. Result must be more than 0\n")
        else:
            raise TypeError("Attempt to add another type than 'Cell'\n")

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.cell_count * other.cell_count)
        else:
            raise TypeError("Attempt to add another type than 'Cell'\n")

    # Решил добавить проверку на предмет того, чтобы после деления результат был больше нуля.
    def __truediv__(self, other):
        if isinstance(other, Cell):
            result = round(self.cell_count / other.cell_count)
            if result != 0:
                return Cell(result)
            else:
                raise ValueError("Incorrect value for division. Result must be more than 0\n")
        else:
            raise TypeError("Attempt to add another type than 'Cell'\n")

    def make_order(self, cells_in_line):
        lines_count = self.cell_count // cells_in_line
        last_line = self.cell_count % cells_in_line
        return ('*' * cells_in_line + '\n') * lines_count + ('*' * last_line)


cell1 = Cell(15)
cell2 = Cell(20)
cell3 = Cell(6)

try:
    cell3 = cell1 + 10
except TypeError as te:
    print('1')
    print(te)

cell12 = cell1 + cell2
print('2')
print(cell12.cell_count, '\n')

try:
    cell12 = cell1 - cell2
except ValueError as ve:
    print('3')
    print(ve)

cell13 = cell1 - cell3
print('4')
print(cell13.cell_count, '\n')

cell12 = cell1 * cell3
print('5')
print(cell12.cell_count, '\n')

try:
    cell32 = cell3 / cell2
except ValueError as ve:
    print('6')
    print(ve)

cell23 = cell2 / cell3
print('7')
print(cell23.cell_count, '\n')

print('8')
print(cell1.make_order(5), '\n')
print('9')
print(cell2.make_order(6), '\n')

# Проверка корректности вывода в случае нулевого количества ячеек в экземпляре.
cell = Cell(0)
print('10')
print(cell.make_order(5))
