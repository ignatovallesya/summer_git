#4.1
# Задаем число
number = 532978

# Преобразуем число в список цифр
digits = list(str(number))

# Сортируем цифры по убыванию
digits.sort(reverse=True)

# Преобразуем список цифр обратно в число
max_number = int(''.join(digits))

# Выводим наибольшее число на экран
print(max_number)