"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
file_name = "fortask1.txt"

with open(file_name, "w", encoding='UTF-8') as file:
    print("Вводите требуемые данные. Они будут записаны в файл.")
    while True:
        buf = input()
        if len(buf) == 0:
            break
        file.write(buf + '\n')
