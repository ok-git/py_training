"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
import random

# user_month = int(input("Номер месяца в году: "))
user_month = random.randrange(1, 12)
# Variant 1 using List
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
months = [[1, 2, 12],
          [3, 4, 5],
          [6, 7, 8],
          [9, 10, 11]]
for month, season in zip(months, seasons):
    if user_month in month:
        print(f"Месяц {user_month} это {season}")

# Variant 2 using List
seasons = ['Зима'] * 2 + ['Весна'] * 3 + ['Лето'] * 3 + ['Осень'] * 3 + ['Зима']
print(f"Месяц {user_month} это {seasons[user_month-1]}")

# Variant 2 using Dict
seasons_dict = {(1, 2, 12): 'Зима',
                (3, 4, 5): 'Весна',
                (6, 7, 8): 'Лето',
                (9, 10, 11): 'Осень'}
for key in seasons_dict.keys():
    if user_month in key:
        print(f"Месяц {user_month} это {seasons_dict[key]}")
