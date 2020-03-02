"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class ByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


# a, b = map(int, input('Введите делимое и делитель через пробел: ').split())

a = 10
b = 0

try:
    if not b:
        raise ByZeroError('На ноль делить совсем нельзя')
    print(a/b)
except ByZeroError as err:
    print(err)
