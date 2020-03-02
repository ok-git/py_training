"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class NonNumberError(Exception):
    pass


# Variant - 1 with own exception
user_input = ''
user_list = []

while user_input != 'q':
    user_input = input('Введите число (q для завершения ввода): ').lower()
    try:
        if user_input == 'q':
            continue
        elif not user_input.isdigit():
            raise NonNumberError('Вы ввели не число')
        else:
            user_list.append(int(user_input))
    except NonNumberError as err:
        print(err)
print(user_list)

# Variant - 2 with builtin exception
user_input = ''
user_list = []

while user_input != 'q':
    user_input = input('Введите число (q для завершения ввода): ').lower()
    try:
        if user_input == 'q':
            continue
        else:
            user_list.append(int(user_input))
    except ValueError as err:
        print(err)
print(user_list)
