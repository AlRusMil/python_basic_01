"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

# С какого номера начинает работу итератор "а"
start_number = 57

# Условие для остановки итератора "а"
stop_number = 100

# Условие для остановки итератора "b"
repeat_numbers = 15
# Список для повторения
list_for_repeat = [1, 2, 3, 4, 5, 6]

# Итераторы "а" и "б" соответственно
iter_count = count(start_number)
iter_cycle = cycle(list_for_repeat)

print("First iterator (with count)")
for itm in iter_count:
    if itm <= stop_number:
        print("Current item: ", itm)
    else:
        print("Executing stopped!")
        break
print("-" * 30)

print("Second iterator (with cycle)")
current_repeats = 0
for itm in iter_cycle:
    if current_repeats < repeat_numbers:
        print(itm)
        current_repeats += 1
    else:
        print("Executing stopped!")
        break
print("-" * 30)