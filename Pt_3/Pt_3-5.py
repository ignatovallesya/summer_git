#3.5
# Определяем функцию для проверки числа на простоту
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Используем list comprehension для создания списка чисел, которые не являются простыми
not_prime_numbers = [number for number in range(1, 51) if not is_prime(number)]

# Выводим полученный список на экран
print("Список чисел, которые не являются простыми:")
print(not_prime_numbers)