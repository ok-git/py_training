"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.
Пример:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) —  10(лаб)
Физкультура: —  30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


# Variant 1 - with function
def convert_digits(str_line):
    result = ''.join([el for el in str_line if el.isdigit()])
    return int(result) if result else 0


result_dict = {}
with open("test_6.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        subj, *value = line.split()
        result_dict[subj[:-1]] = sum(list(map(convert_digits, value)))
print(result_dict)


# Variant 2 - short, in one line conversion
result_dict = {}
with open("test_6.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        subj, *value = line.split()
        result_dict[subj[:-1]] = sum([int(el.split('(')[0]) for el in value if el != '—'])
print(result_dict)

