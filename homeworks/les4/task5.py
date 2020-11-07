"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
"""

# В Ваших требованиях было сказано, что требуется написать свой аналог функции reduce() прежде чем ее использовать!
# Поэтому в выводе два результата: "штатная" reduce и самописная.

from functools import reduce

def func_reduce(func, some_list):
    it = iter(some_list)
    result_value = next(it)
    for itm in it:
        result_value = func(result_value, itm)
    return result_value


# Не стал добавлять в функцию reduce напрямую для сохранения удобочитаемости кода
result_list = [itm for itm in range(100, 1001) if not itm & 1]

#us_red = reduce(lambda x, y: x * y, result_list)
#my_red = func_reduce(lambda x, y: x * y, result_list)

#if us_red == my_red:
#    print(True)
#else:
#    print(False)

print("Reduce: ", reduce(lambda x, y: x * y, result_list))
print("My reduce: ", func_reduce(lambda x, y: x * y, result_list))


