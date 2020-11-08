"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

file_name = 'fortask5.txt'
# набор чисел
number_list = [100, 83, 23, 44, 55, 64, 98, 12, 33]
# итоговая сумма, после считывания из файла
total_sum = 0

# запись чисел в файл
with open(file_name, 'w', encoding='UTF-8') as file:
    for i in number_list:
        file.write(f'{i} ')

# считывание из файла
with open(file_name, 'r', encoding='UTF-8') as file:
    str_buf = ''  # буфер, в котором будет "накапливаться" число
    for_stop = -1  # число, которое будет использоваться для определения конца файла
    while True:
        buf = file.read(1)
        if buf == ' ':
            total_sum += float(str_buf)
            str_buf = ''
        # Своеобразный поиск конца файла
        elif buf == '':
            # если в процессе работы позиция указателя в файле не меняется, значит достигнут конец файла
            if (for_stop == file.tell()):
                break
            else:
                for_stop = file.tell()
        else:
            str_buf += buf

print("Сумма чисел в файле составляет: ", total_sum)

