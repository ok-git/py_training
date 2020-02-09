"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо
запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем
же значением должен разместиться после них.
"""

import random

my_list = [7, 5, 3, 3, 2]
print("Вариант 1 - с сортировкой")
print("Текущий рейтинг: ", *my_list)
# user_rating = input("Введите рейтинг: ")
user_rating = random.randrange(1, 10)
print(f"Новое значение: {user_rating}")
my_list.append(user_rating)
my_list.sort(reverse=True)
print("Новый рейтинг: ", *my_list)

my_list = [7, 5, 3, 3, 2]
print("\nВариант 2 - без сортировки, с реверсом и вставкой")
print("Текущий рейтинг: ", *my_list)
print(f"Новое значение: {user_rating}")
new_list = my_list[::-1]  # reverse list first
old_len = len(new_list)
for idx, el in enumerate(my_list[::-1]):
    if user_rating <= el:
        new_list.insert(idx, user_rating)  # if user_rating is found in the list then insert it by idx
        break
if len(new_list) == old_len:  # if user_rating not found in the list then append new value
    new_list.append(user_rating)
my_list = new_list[::-1]  # reverse back
print("Новый рейтинг: ", *my_list)
