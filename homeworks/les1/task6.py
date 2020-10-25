# Названия переменных взял из задания

a = int(input("Введите количество км в первый день: "))
b = int(input("Введите количество км, которое нужно достигнуть: "))

day_number = 1
print(f'{day_number}-й день: {a}')
while a < b:
    day_number += 1
    a = round( a * 1.1, 2)
    print(f'{day_number}-й день: {a}')
print(f"На {day_number}-й день спортсмен достиг результата не менее {b} км")