while True:
    item_count = input("Введите количество элементов списка:\n>>> ")
    if item_count.isdigit():
        item_count = int(item_count)
        break
    print("Ошибка! Введите число!")

some_list = []
for item_index in range(item_count):
    some_list.append(input(f'Введите {item_index}й элемент: '))

print("Исходный список")
print(some_list)

for index_pair in range(item_count // 2):
    current_index = 2 * index_pair
    some_list[current_index], some_list[current_index + 1] = some_list[current_index + 1], some_list[current_index]

    # tmp = some_list[current_index]
    # some_list[current_index] = some_list[current_index + 1]
    # some_list[current_index + 1] = tmp

print("Итоговый список")
print(some_list)