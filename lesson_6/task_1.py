"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

import time


# Variant 1
class TrafficLight:
    def __init__(self, scheme):
        self.__color = None
        self.scheme = scheme  # {'color_1': time_1, 'color_2': time_2, 'color_3': time_3}

    def running(self):
        for key, val in self.scheme.items():
            self._set_color(key)
            self._print_color()
            self.__print_timeout(val)
            print()

    def _set_color(self, color):
        self.__color = color

    def _print_color(self):
        print(self.__color, end=' ')

    @staticmethod
    def __print_timeout(timeout):
        for i in range(1, timeout + 1):
            print(i, end=' ')
            time.sleep(1)


# Variant 2
class TrafficLight2:
    scheme = 'Красный', 'Желтый', 'Зелёный'

    def __init__(self, time_1, time_2, time_3):
        self.__color = None
        self.timeouts = time_1, time_2, time_3

    def running(self):
        for color, timeout in zip(self.scheme, self.timeouts):
            self._set_color(color)
            self._print_color()
            self.__print_timeout(timeout)
            print()

    def _set_color(self, color):
        self.__color = color

    def _print_color(self):
        print(self.__color, end=' ')

    @staticmethod
    def __print_timeout(timeout):
        for i in range(1, timeout + 1):
            print(i, end=' ')
            time.sleep(1)


a = TrafficLight({'Красный': 7, 'Желтый': 2, 'Зелёный': 4})
a.running()

a2 = TrafficLight2(7, 2, 4)
a2.running()
