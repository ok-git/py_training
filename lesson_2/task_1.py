"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

my_list = [0, 87, 5e8, 0.1, -5.3, 'abc', None, True, ['it is list'], (111, 222), {'python', 'ruby'}, {'cpu': 'intel'}]

for element in my_list:
    print(f"The type of element {element}, is {type(element)}")
