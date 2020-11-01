# В силу интуитивной понятности параметров не стал описывать каждый параметр в документации.
# Решил, что функция сама ничего не выводит. Она только формирует строку,
# а вывод производится из тела основной программы
def func_user_info(name, surname, year_of_birth, city, email, phone):
    """
    The function takes user information as parameters and prints it on the screen
    :param name:
    :param surname:
    :param year_of_birth:
    :param city:
    :param email:
    :param phone:
    :return:
    """
    result = f"Пользователь {name} {surname}, {year_of_birth} г.р." \
             f"Проживает в городе {city}, email - {email}. Контактный телефон - {phone}"
    return result


# Учитывая, что требовалось продемонстрировать работу с именованными аргументами, сам процесс ввода решил упростить
# Учитывая, что вводятся строковые данные, проверки не добавлял.
print("Введите последовательно через ENTER следующую информацию: имя, фамилия, год рождения, город проживания"
      "email и контактный телефон")
list_user_info = []

while len(list_user_info) < 6:
    list_user_info.append(input())

print(func_user_info(name=list_user_info[0], surname=list_user_info[1], year_of_birth=list_user_info[2],
                     city=list_user_info[3], email=list_user_info[4], phone=list_user_info[5]))
