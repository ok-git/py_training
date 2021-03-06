"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
"""


def print_user_kwargs(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}", end=" ")
    print("")  # print CR


# var 1
user_data = {
    'Имя': 'Иван',
    'Фамилия': 'Иванов',
    'год. р.': '1980',
    'город': 'Канавинск',
    'email': 'my@email.com',
    'телефон': '1234567890'}
print_user_kwargs(**user_data)

# var 2
print_user_kwargs(name='Иван', surname='Иванов', year='1980',
                  city='Канавинск', email='my@email.com', phone='1234567890')
