list_rating = [7, 5, 3, 3, 2]
print("Исходный рейтинг: ", list_rating)
print("-"*10)

while True:
    current_number = input("Введите натуральное число либо символ 'q', чтобы закончить выполнение программы: ")

    if current_number == 'q':
        print("Работа программы прекращена! Текущий рейтинг:")
        print(list_rating)
        break

    if not current_number.isdigit():
        print("Ошибка! Введите натуральное число или 'q', чтобы выйти из программы!")
        continue
    current_number = int(current_number)
    # Можно добавить проверку
    if current_number in list_rating:
        list_rating.insert(list_rating.index(current_number) + list_rating.count(current_number),
                           current_number)
    elif current_number > list_rating[0]:
        list_rating.insert(0, current_number)
    elif current_number < list_rating[len(list_rating) - 1]:
        list_rating.append(current_number)
    else:
        for i in range(1, len(list_rating)):
            if current_number > list_rating[i]:
                list_rating.insert(i, current_number)
                break

    print(list_rating)