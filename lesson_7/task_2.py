"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    total_material = 0

    def __init__(self, title):
        self.title = title
        Clothes.total_material += self.material_consumption

    @abstractmethod
    def material_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, title, size):
        self.size = size
        super().__init__(title)

    @property
    def material_consumption(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, title, height):
        self.height = height
        super().__init__(title)

    @property
    def material_consumption(self):
        return self.height*2 + 0.3


my_coat = Coat('Пальто', 52)
print(f'Для {my_coat.title} {my_coat.size} размера, расход ткани составит {my_coat.material_consumption} м.')

my_suit = Suit('Костюм', 1.80)
print(f'Для {my_suit.title} {my_suit.height} роста, расход ткани составит {my_suit.material_consumption} м.')

print(f'Общий расход ткани {Clothes.total_material} м. ')
