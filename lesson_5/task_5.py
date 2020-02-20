"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

with open("test_5.txt", 'w', encoding='utf-8') as f_obj:
    f_obj.write(' '.join([str(random.randint(1, 100)) for _ in range(10)]))

with open("test_5.txt", 'r', encoding='utf-8') as f_obj:
    numbers = f_obj.readline()

print(sum(map(int, numbers.split())))
