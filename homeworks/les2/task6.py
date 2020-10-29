template = {
    'название': 'Введите название товара\n>>> ',
    'цена': 'Укажите цену товара за единицу\n>>> ',
    'количество': 'Укажите количество товара в наличии\n>>> ',
    'ед': 'Укажите в чем измеряется единица товара\n>>> '
}

products = []
dict_analytics = {}

product_number = 0
while True:
    if input("Если все товары добавлены, то введите символ 'q', в противном случае нажмите ENTER: ") == 'q':
        print("Итоговый список товаров")
        print(products)
        break

    product_number += 1
    products.append((product_number, {}))

    for key, value in template.items():
        tmp = input(value)
        if tmp.isdigit():
            tmp = int(tmp)

        products[product_number - 1][1][key] = tmp
        dict_analytics[key] = []

print('-' * 10)

for item_list in products:
    for key, value in item_list[1].items():
        if value not in dict_analytics[key]:
            dict_analytics[key].append(value)

print("Словарь для аналитики")
print(dict_analytics)
