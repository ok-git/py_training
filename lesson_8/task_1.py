"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_string):
        self.date_string = date_string  # DD-MM-YYYY :str

    def __str__(self):
        return self.date_string

    # Не использовал cls, хотя заявлен метод класса - не до конца понял задание. См. следующий метод.
    # @classmethod
    # def convert_to_int(cls, date_string):
    #     day = month = year = 0
    #     try:
    #         day, month, year = map(int, date_string.split('-'))
    #     except ValueError as err:
    #         print(err)
    #     return day, month, year

    @classmethod
    def create_from_int(cls, day, month, year):
        return cls('-'.join(map(str, [day, month, year])))

    @staticmethod
    def date_validation(date_string):
        day = month = year = 0
        try:
            day, month, year = map(int, date_string.split('-'))
        except ValueError as err:
            print(err)
        return day in range(1, 32) and\
            month in range(1, 13) and\
            year in range(2000, 2021)


my_date = Date('20-2-2020')
print(my_date)
print(f'Дата валидна - {my_date.date_validation(my_date.date_string)}\n')

not_valid_date = Date('10-14-2020')
print(not_valid_date)
print(f'Дата валидна - {not_valid_date.date_validation(not_valid_date.date_string)}\n')

# call class method through the class name
# print(Date.convert_to_int('20-02-2020'), '\n')

# create object through the class method
my_date_2 = Date.create_from_int(21, 3, 2020)
print(my_date_2)


