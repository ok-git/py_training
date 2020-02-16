"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

import sys


def salary(hours, rate, reward=0):
    return hours * rate + reward


try:
    print(f'Salary is: {salary(*map(int, sys.argv[1:4]))}')
except TypeError:
    print("Not enough arguments")
except ValueError:
    print("Wrong argument")

# Testing:
# python task_1.py 10
#    Not enough arguments

# python task_1.py 10 20
#    Salary is: 200

# python task_1.py 10 20 5
#    Salary is: 205

# python task_1.py 10 20 5 1
#    Salary is: 205

# python task_1.py 10 20 q
#    Wrong argument
