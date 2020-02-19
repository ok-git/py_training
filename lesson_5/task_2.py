"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
слов в каждой строке.
"""

with open("test_2.txt", 'r', encoding='utf-8') as f_obj:
    for idx, line in enumerate(f_obj, 1):
        print(f'Строка № {idx}, слов в строке - {len(line.split())}. Строка - {line.strip()}')
