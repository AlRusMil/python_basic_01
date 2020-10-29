text = input("Введите строку: ")

list_from_text = text.split(' ')

for item_index in range(len(list_from_text)):
    print(f'{item_index + 1}. {list_from_text[item_index][:10]}')
