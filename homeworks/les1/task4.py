number = input("Введите число: ")

max_digit = number[0]

i = 1
while i < len(number):
    if(number[i] > max_digit):
        max_digit = number[i]
    i += 1

print("Максимальная цифра в числе: ", max_digit)

