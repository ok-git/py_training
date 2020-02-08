"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
элементов необходимо использовать функцию input().
"""

# user_list = [input(f"Введите значение {i+1}: ") for i in range(int(input("Длина списка: ")))]
user_list = ['1', '2', '3', '4', '5', '6', '7']
print(user_list)
new_list = []
for idx, items in enumerate(zip(user_list[1:], user_list)):
    new_list.extend(items) if idx % 2 == 0 else None
new_list.extend(user_list[-1]) if len(user_list) % 2 != 0 else None
user_list = new_list
print(user_list)
