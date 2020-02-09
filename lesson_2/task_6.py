"""
*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
"""

items_from_task = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
                   (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
                   (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'})]

# answer_dict for self check
answer_dict = {'название': ['компьютер', 'принтер', 'сканер'],
               'цена': [20000, 6000, 2000],
               'количество': [5, 2, 7],
               'ед': ['шт.']}

# Input user dictionary
# items_dict = dict.fromkeys(['название', 'цена', 'количество', 'ед'])  # init keys

# user_input = [(i, {key: input(f"Введите {key}: ") for key in items_dict})
#               for i in range(int(input("Количество товаров: ")))]  # dict generator inside of the list generator

# print("\nВведённый словарь:")
# for item in user_input:
#     print(item)

print("\nСловарь из задания:")
for item in items_from_task:
    print(item)

# form my_result_dict with analytics for the task
my_result_dict = {}  # init my_result_dict
for item in items_from_task:
    _, dict_item = list(item)
    for key, value in dict_item.items():
        if my_result_dict.get(key) and key != 'ед':
            my_result_dict[key] += [value]  # add to existing value
        else:
            my_result_dict[key] = [value]  # create key:value
print("\nРезультирующий словарь:\n", my_result_dict, sep="")
print("Сравнение с ответом из задания: ", answer_dict == my_result_dict)
