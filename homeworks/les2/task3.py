list_months = ['winter', 'winter', 'spring',
               'spring', 'spring', 'summer',
               'summer', 'summer', 'autumn',
               'autumn', 'autumn', 'winter']

dict_months = {1: 'winter', 2: 'winter', 3: 'spring',
               4: 'spring', 5: 'spring', 6: 'summer',
               7: 'summer', 8: 'summer', 9: 'autumn',
               10: 'autumn', 11: 'autumn', 12: 'winter',}

while True:
    current_month = input("Введите номер месяца (от 1 до 12):\n>>> ")
    if current_month.isdigit():
        current_month = int(current_month)
        break
    print("Ошибка! Введите число!")

print("Использование списка")
print("Текущее время года: ", list_months[current_month - 1])

print("Использование словаря")
print("Текущее время года: ", dict_months[current_month])