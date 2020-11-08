"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

"""
Пример файла:
Иванов 25000
Петров 30000
Катов 15000
Лошков 10000
Бенов 21000
Гятов 18000
Васильев 14000
Баранов 50000
"""

file_name = 'fortask3.txt'

low_salary_dict = {}
total_salary_sum = 0
total_count = 0

with open(file_name, 'r', encoding='UTF-8') as file:
    for str_buf in file:
        list_buf = str_buf.split(' ')
        # Добавил небольшую проверку корректности данных. Код ошибки взял просто отличный от нуля (неуспех).
        # В случае ошибки работа программы прекращается.
        try:
            salary = float(list_buf[1])
        except ValueError:
            print("Ошибка считывания данных! Проверьте корректность содержимого файла!")
            exit(1)

        total_salary_sum += salary
        total_count += 1

        if salary < 20000:
            low_salary_dict[list_buf[0]] = salary

print(f'Средний доход сотрудников составляет {total_salary_sum / total_count}')
print('Следующее сотрудники имеют оклад ниже 20000: ')
for i, (key, value) in enumerate(low_salary_dict.items(), 1):
    print(f'{i}. {key} - {value}')
