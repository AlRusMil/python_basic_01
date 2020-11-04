def fun_sum_numbers(current_sum: float, string_for_sum: str) -> list:
    """
    The function sums the numbers in the string
    :param current_sum: current amount
    :param string_for_sum: a string with numbers to add to the current amount
    :return: a list consisting of the sum of numbers and the sign of the end of the program
    """
    new_sum = current_sum
    flag_to_stop = False

    list_numbers = string_for_sum.split(' ')
    for numb in list_numbers:
        try:
            numb = float(numb)
            new_sum += numb
        except ValueError:
            flag_to_stop = True
            break
    return [new_sum, flag_to_stop]


result_sum = 0

while True:
    string_number = input("Введите строку с числами через пробел. Для прекращения работы программы вместо"
                          "числа укажите любой другой символ(ы):\n")
    result = fun_sum_numbers(result_sum, string_number)
    if result[1]:
        print("Сумма введенных чисел составляет: ", result[0])
        break
    result_sum = result[0]

