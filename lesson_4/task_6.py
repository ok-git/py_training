"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count
from itertools import cycle

for el in count(10):
    if el > 19:
        break
    print(el)

# Variant - 1
result_list = []
for el in cycle(['список', 'определённый ', 'заранее']):
    result_list.append(el)
    if len(result_list) == 10:
        break
print(result_list)

# Variant - 2
iter_obj = cycle(['список', 'определённый ', 'заранее'])
result_list = []
while len(result_list) != 10:
    result_list.append(next(iter_obj))
print(result_list)
