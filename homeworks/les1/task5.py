proceed = int(input("Введите сумму выручки: "))
costs = int(input("Введите размер издержек: "))

if proceed > costs:
    print(f"Ваша фирма работает с прибылью. Ее размер составляет: {proceed - costs}")

    # Вывел просто соотношение. Исходя из условий задания, решил дополнительных манипуляций не производить.
    # Учитывая, что был только первый урок, решил с округлением не мудрить и оставил 4 знака после запятой.
    print(f"Рентабельность составляет: {round(proceed / costs, 4)}")
elif proceed < costs:
    print(f"Ваша фирма работает в убыток. Ее размер составляет: {costs - proceed}")
else:
    print("Ваша фирма не приносит Вам прибыль")

employees = int(input("Укажите численность сотрудников: "))

print(f"Прибыль в расчете на одного сотрудника составляет - {round(proceed / employees, 4)}")