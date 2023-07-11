#2.9
def find_max_digit(number):
    max_index = 0
    max_digit = int(number[0])

    # Находим индекс и значение максимальной цифры
    for i in range(1, len(number)):
        digit = int(number[i])
        if digit > max_digit:
            max_digit = digit
            max_index = i

    # Вычисляем порядковый номер максимальной цифры от конца числа
    reverse_index = len(number) - max_index

    # Вычисляем порядковый номер максимальной цифры от начала числа
    forward_index = max_index + 1

    return reverse_index, forward_index

# Пример использования функции
number = input("Введите натуральное число, в котором все цифры различны: ")
reverse_index, forward_index = find_max_digit(number)
print("Порядковый номер максимальной цифры от конца числа:", reverse_index)
print("Порядковый номер максимальной цифры от начала числа:", forward_index)