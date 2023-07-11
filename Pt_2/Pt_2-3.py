#2.3
def is_armstrong_number(number):
    # Переводим число в строку для подсчета количества цифр
    num_str = str(number)
    # Получаем количество цифр в числе
    num_digits = len(num_str)
    # Инициализируем переменную для суммы цифр, возведенных в степень
    sum_of_digits = 0

    # Проходим по каждой цифре числа
    for digit in num_str:
        # Преобразуем цифру обратно в число и возводим в степень
        sum_of_digits += int(digit) ** num_digits

    # Проверяем, равна ли сумма цифр исходному числу
    if sum_of_digits == number:
        return True
    else:
        return False

# Получаем число от пользователя
number = int(input("Введите число: "))

# Проверяем, является ли число числом Армстронга
if is_armstrong_number(number):
    print(number, "является числом Армстронга.")
else:
    print(number, "не является числом Армстронга.")