"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""

user_input = ' '
with open("test_1.txt", 'w', encoding='utf-8') as f_obj:
    while user_input:
        user_input = input('Enter string: ')
        if user_input:
            f_obj.write(f"{user_input}\n")
