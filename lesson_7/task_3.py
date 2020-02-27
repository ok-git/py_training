"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все
оставшиеся.
"""


class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        result = self.nucleus - other.nucleus
        if result < 0:
            print('The difference is less than zero')
        else:
            return Cell(result)

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(self.nucleus // other.nucleus)

    def __str__(self):
        return str(self.nucleus)

    # Variant 1
    def make_order(self, in_row):
        result = list('*' * self.nucleus)
        for idx in range(self.nucleus // in_row):
            result.insert(in_row * (idx+1) + idx, '\n')
        return "".join(map(str, result))

    # Variant 2
    def make_order_2(self, in_row):
        result = []
        for idx in range(self.nucleus // in_row):
            result.extend(['*' * in_row, '\n'])
        result.extend(['*' * (self.nucleus % in_row)])
        return "".join(map(str, result))


cell_1 = Cell(15)
cell_2 = Cell(2)
print(f'Клетка 1-  {cell_1} яч., клетка 2 - {cell_2} яч.')
print('Сумма -', cell_1 + cell_2)
print('Разность -', cell_1 - cell_2)
print('Произведение -', cell_1 * cell_2)
print('Деление -', cell_1 / cell_2)
print('Меньше нуля -', cell_2 - cell_1)

print(cell_1.make_order(4))
print()
print(cell_1.make_order_2(7))
print()
print(cell_1.make_order_2(5))
