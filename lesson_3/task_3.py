"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


# ver - 1
def my_func(num1, num2, num3):
    return sum(sorted([num1, num2, num3])[-2:])


print(my_func(1, 2, 3))
print(my_func(4, 1, 5))


# ver - 2 with map
def my_func(num1, num2, num3):
    return sum(sorted(map(int, [num1, num2, num3]))[-2:])


print(my_func(10, 20, 30))
print(my_func(400, 100, 500))
print(my_func('400', '100', '500'))
