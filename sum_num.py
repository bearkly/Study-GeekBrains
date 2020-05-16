# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = str(input("Введите число: "))

first_num = number
second_num = first_num + number
third_num = second_num + number

int_first_num = int(first_num)
int_second_num = int(second_num)
int_third_num = int(third_num)

sum_num = int_first_num + int_second_num + int_third_num
print("\n Считаем:\n", first_num, "+", second_num, "+", third_num, "=", sum_num)
