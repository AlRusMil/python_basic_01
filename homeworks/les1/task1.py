str_var_1 = "this is a string"
int_var_1 = 10

print(str_var_1)
print(int_var_1)

str_var_2_name = input("Введите имя: ")
str_var_2_surn = input("Введите фамилию: ")

int_var_2_age = int(input("Введите возраст: "))
int_var_2 = int(input("Введите число: "))

print(f"Ваше имя {str_var_2_name}, фамилия - {str_var_2_surn}")
print(f"Ваш возраст: {int_var_2_age}, если прибавить второе число, то будет {int_var_2_age + int_var_2}")