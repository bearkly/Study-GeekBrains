# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.


def salary_func():
    try:
        time = float(input("Введите общее время работы: "))
        salary = int(input("Введите ставку в час: "))
        plus = int(input("Введите премию сотрудника: "))
        final = time * salary + plus
        print(f'Зарплата сотрудника равна: {round(final)} рублей.')
    except ValueError:
        return print('Вы ввели недопустимое значение!')


salary_func()
