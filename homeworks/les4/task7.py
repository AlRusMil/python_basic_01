"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fact(n: int):
    """
    Function returns the factorial of all numbers up to "n"
    :param n: up to what number need to search for the factorial
    """

    current_factorial = 1

    # Так как в условии говорится про вывод факториала с единицы, то начинаем от факториала 1
    i = 1
    while i <= n:
        current_factorial = current_factorial * i
        yield current_factorial
        i += 1


fact_number = 10
for i, el in enumerate(fact(fact_number)):
    print(f"{i + 1}! = {el}")
