"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки', end=' ')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Пишем карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')


my_pen = Pen('Parker')
my_pen.draw()

my_pencil = Pencil('Koh-i-Noor')
my_pencil.draw()

my_handle = Handle('просто маркер')
my_handle.draw()



