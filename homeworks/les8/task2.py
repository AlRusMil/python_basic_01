"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class ZeroDiv(Exception):

    def __init__(self, text: str = ''):
        self.text = text


def my_div(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDiv("На ноль делить нельзя!!!")
    return a / b


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

try:
    print('Result: ', my_div(a, b))
except ZeroDiv as zd:
    print(zd)

print('Program works!')
