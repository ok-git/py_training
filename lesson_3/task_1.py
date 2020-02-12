"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
import random


def my_div(numerator, denominator):
    return round(numerator / denominator, 2) if denominator != 0 else None


# numerator = int(input("Введите числитель: "))
# denominator = int(input("Введите знаменатель: "))
numerator = random.randint(1, 10)
denominator = random.randint(1, 10)

print(f"Результат {numerator} / {denominator} = {my_div(numerator, denominator)}")

numerator = random.randint(1, 10)
denominator = 0

print(f"Результат {numerator} / {denominator} = {my_div(numerator, denominator)}")
