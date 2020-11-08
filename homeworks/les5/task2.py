"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

"""
Пример файла:
sdsdsdsd fefege gegegwer
rerere weee tereroer
wrwr rwrw rrrrrr
w w w w w w w
wewewe rerer ytyt tytyty
rrrr

"""

file_name = 'fortask2.txt'
result_list = []

with open(file_name, 'r', encoding='UTF-8') as file:
    for str_buf in file:
        result_list.append(len(str_buf.split(' ')))

print(f'Всего строк в файле: {len(result_list)}')
for i, itm in enumerate(result_list, 1):
    print(f'В строке {i} содержится {itm} слов')
