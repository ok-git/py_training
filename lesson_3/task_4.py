"""
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.
"""


def my_pow(x, y):
    res = 1
    for i in range(abs(y)):
        res = res * x
    return 1/res if y < 0 else res


# x = int(input("Enter x="))
# y = int(input("Enter y="))
x, y = 2, -3

print(f"{x} ** {y} = {my_pow(x,y)}")
print(f"{x} ** {y} = {pow(x,y)}")

x, y = 2, 3

print(f"{x} ** {y} = {my_pow(x,y)}")
print(f"{x} ** {y} = {pow(x,y)}")
