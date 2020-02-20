"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).
Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""

from functools import reduce
from lesson_5.task_6 import convert_digits

company_dict = {}
with open("test_7.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        company, *value = line.split()
        company_dict[company] = reduce(lambda x, y: x - y, list(map(convert_digits, value[1:])))
profit = [profit for profit in company_dict.values() if profit > 0]
result_list = [company_dict, {'average_profit': round(sum(profit)/len(profit), 2)}]
print(result_list)
