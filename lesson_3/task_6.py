"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()
"""


def int_func(string):
    return chr(ord(string[:1])-32)+string[1:]


# text_string = input("Введите строку: ")
text_string = 'the quick brown fox jumps over the lazy dog'
print(text_string)
print(*list(map(int_func, text_string.split())))
print(int_func('one'))


# ver - 2 using *args
def int_func_v2(*args):
    return " ".join([chr(ord(el[:1])-32)+el[1:] for el in args])


text_string = 'the quick brown fox jumps over the lazy dog'
print(text_string)
print(int_func_v2(*text_string.split()))
print(int_func_v2('one'))
print(int_func_v2('one', 'two'))
