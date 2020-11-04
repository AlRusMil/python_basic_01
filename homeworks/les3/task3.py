def my_func(a: float, b: float, c: float) -> float:
    """
    The function takes three arguments as parameters and returns the sum of the largest two of them
    :param a: float digit
    :param b: float digit
    :param c: float digit
    :return: float digit
    """
    result = 0
    if a >= b:
        result += a
        if b >= c:
            result += b
            return result
        else:
            result += c
            return result
    else:
        result += b
        if a >= c:
            result += a
            return result
        else:
            result += c
            return result

while True:
    mas_digits = input("Введите через пробел три числа либо q для выхода:\n").split(' ')
    try:
        third_number = float(mas_digits[2])
        first_number = float(mas_digits[0])
        second_number = float(mas_digits[1])
        print("Сумма двух наибольших аргументов равна: ", my_func(first_number, second_number, third_number))
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

#print(my_func(5, 7, 13))
#print(my_func(0, 6, -3))
#print(my_func(-2, 7, 1))
#print(my_func(5, 5, 5))
#print(my_func(15, 1, 13))