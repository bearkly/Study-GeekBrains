# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

input_sec = int(input("Введите время в секундах: "))

hours = input_sec // 3600
modulo_hours = input_sec % 3600

minutes = modulo_hours // 60

seconds = modulo_hours % 60

print("\nТекущее время в формате чч:мм:сс")
print(hours, minutes, seconds, sep=":")
