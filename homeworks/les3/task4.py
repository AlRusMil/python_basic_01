def my_func_1(x: float, y: int) -> float:
    """
    The function raises the number 'x' to the power of 'y'
    :param x: real positive number
    :param y: negative integer
    :return: exponentiation result
    """
    return x ** y


def my_func_2(x: float, y: int) -> float:
    """
    The function raises the number 'x' to the power of 'y'
    :param x: real positive number
    :param y: negative integer
    :return: exponentiation result
    """
    y *= -1
    result = 1

    i = 0
    while i < y:
        result /= x
        i += 1

    return result

while True:
    mas_digits = input("Введите через пробел действительное положительное число и целое отрицательное "
                       "либо q для выхода:\n").split(' ')
    try:
        power_number = int(mas_digits[1])
        number = float(mas_digits[0])

        if (number <= 0) | (power_number >= 0):
            print("Ошибка ввода! Введите числа, удовлетворяющие условиям!")
            continue

        print("Результат при использовании **: ", my_func_1(number, power_number))
        print("Результат при использовании цикла: ", my_func_2(number, power_number))
    except IndexError as error:
        if (len(mas_digits) == 1) & (mas_digits[0] == 'q'):
            print("Работа программы завершена!")
            break
        else:
            print("Ошибка ввода!")
            continue
    except ValueError as error:
        print("Ошибка ввода! Введите числа!")
        continue
