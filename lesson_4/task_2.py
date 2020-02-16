"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

user_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# variant 1
result_list = [el_2 for el_1, el_2 in zip(user_list, user_list[1:]) if el_1 < el_2]
print(result_list)

# variant 2
result_list = [el for idx, el in enumerate(user_list) if el > user_list[idx-1] and idx > 0]
print(result_list)
