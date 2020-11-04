# Так как деление может быть не целочисленное, то решил использовать везде float
def func_div(a: float, b: float) -> float:
    """
    The function divides the first parameter by the second and returns the result of this division
    :param a: dividend, float digit
    :param b: divider, float digit
    :return: float digit
    """
    return a / b


while True:
    num_list = input("Введите два числа через пробел. Сначала делимое, потом делитель. Либо q для выхода:\n").split(' ')
    try:
        second_param = float(num_list[1])
        first_param = float(num_list[0])
        result = func_div(first_param, second_param)
        print(result)
        break
    except IndexError as error:
        if (len(num_list) == 1) & (num_list[0] == 'q'):
            print("Работа программы завершена!")
            break
        else:
            print("Ошибка ввода!")
            continue
    except ValueError as error:
        print("Ошибка ввода! Введите числа!")
        continue
    except ZeroDivisionError as error:
        print("Неправильно введены параметры! На ноль делить нельзя!")
        continue
