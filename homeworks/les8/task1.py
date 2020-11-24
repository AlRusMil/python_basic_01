"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год».

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число».

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""
import re
from datetime import date


class Date:

    _dict_last_date = {}

    def __init__(self, date_param: str):
        if re.match(r'^\d\d-\d\d-((\d{2})|(\d{4}))$', date_param) is None:
            raise ValueError('Incorrect format of date!\n')
        self.__date = date_param

    @property
    def get_date(self):
        return self.__date

    @classmethod
    def converter(cls, date_param: str) -> dict:
        if cls.is_valid_date(date_param):
            date_list = date_param.split('-')
            cls._dict_last_date['Year'] = int(date_list[2])
            cls._dict_last_date['Month'] = int(date_list[1])
            cls._dict_last_date['Day'] = int(date_list[0])
            return cls._dict_last_date
        else:
            raise ValueError('Incorrect format of date!\n')

    # Вычисляет количество дней в месяце.
    @staticmethod
    def days_number(month: int, year: int) -> int:
        # Поправка на високосный год.
        leap_year = 1 if ((year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0)) else 0
        return 28 + (month + (month // 8)) % 2 + (2 % month) + (2 - leap_year) * ((1 + leap_year) // month)

    @staticmethod
    def is_valid_date(date_param: str) -> bool:
        date_list = date_param.split('-')

        # Проверяем формат даты.
        if len(date_list) != 3:
            return False

        # Проверяем, что составляющие даты являются числами (положительными).
        for item in date_list:
            if not item.isdigit():
                return False

        # Year
        # Вычисляем длину года. В случае, если в двузначном формате, то дополняем до 4 цифр.
        if len(date_list[2]) == 2:
            year = int(f'{str(date.today().year)[0:2]}{date_list[2]}')
        else:
            year = int(date_list[2])

        # Корректность года.
        if (year < 1900) | (year > date.today().year):
            return False

        # Month
        # Корректность месяца.
        month = int(date_list[1])
        if (month <= 0) | (month > 12):
            return False

        # Day
        # Корректность дня.
        if int(date_list[0]) > Date.days_number(month, year):
            return False

        return True


print('1 ', Date('12-12-2012').get_date)
print('2 ', Date('12-12-12').get_date)
print()

try:
    my_date = Date('12-02-433')
except ValueError as ve:
    print('3 ', ve)

try:
    my_date = Date('12-f3-12121')
except ValueError as ve:
    print('4 ', ve)

print('5')
my_date = Date('10-10-2010')
print('10-12-2019: ', Date.is_valid_date('10-12-2019'))
print('43-09-2000: ', Date.is_valid_date('43-09-2000'))
print('31-04-2015: ', Date.is_valid_date('31-04-2015'))
print('31-05-2015: ', Date.is_valid_date('31-05-2015'))
print('29-02-2003: ', my_date.is_valid_date('29-02-2003'))
print('29-02-2004: ', my_date.is_valid_date('29-02-2004'))
print()

my_date = Date('10-34-2010')
try:
    my_date.converter(my_date.get_date)
except ValueError as ve:
    print('6 ', ve)

my_date = Date('20-01-2000')
print('7')
print(my_date.converter(my_date.get_date))
print(my_date._dict_last_date)
print(Date._dict_last_date)
print()

my_date2 = Date('10-10-15')
print('8')
print(Date.converter(my_date2.get_date))
print(Date._dict_last_date)
print(my_date._dict_last_date)
print(my_date2._dict_last_date)
print()

print('9. Проверка правильности вычисления количества дней.')
print('1993')
print(Date.days_number(1, 1993))
print(Date.days_number(2, 1993))
print(Date.days_number(3, 1993))
print(Date.days_number(4, 1993))
print(Date.days_number(8, 1993))
print(Date.days_number(9, 1993))
print()
print('1996')
print(Date.days_number(1, 1996))
print(Date.days_number(2, 1996))
print(Date.days_number(3, 1996))
print(Date.days_number(4, 1996))
print(Date.days_number(8, 1996))
print(Date.days_number(9, 1996))
print()
print('2000')
print(Date.days_number(1, 2000))
print(Date.days_number(2, 2000))
print(Date.days_number(3, 2000))
print(Date.days_number(4, 2000))
print(Date.days_number(8, 2000))
print(Date.days_number(9, 2000))
print()
print('2100')
print(Date.days_number(1, 2100))
print(Date.days_number(2, 2100))
print(Date.days_number(3, 2100))
print(Date.days_number(4, 2100))
print(Date.days_number(8, 2100))
print(Date.days_number(9, 2100))
print()

