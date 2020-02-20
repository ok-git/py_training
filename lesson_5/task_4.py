"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

numeral_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

result = []
with open("test_4_in.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        numeral, *value = line.split()
        result.append(" ".join([numeral_dict[numeral], *value, '\n']))

with open("test_4_out.txt", 'w', encoding='utf-8') as f_obj:
    f_obj.writelines(result)
