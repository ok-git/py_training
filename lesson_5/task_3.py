"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников.
"""

staff_list = []
salary_list = []
with open("test_3.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        person, salary = line.split()
        staff_list.append(person)
        salary_list.append(float(salary))

under20000 = [person for person, salary in zip(staff_list, salary_list) if salary < 20000]
print('Оклады до 20000:', *under20000)

print(f'Средний оклад: {sum(salary_list)/len(salary_list):.2f} \n')
