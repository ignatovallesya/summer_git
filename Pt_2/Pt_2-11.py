#2.11
# Просим пользователя ввести значение a
a = int(input("Введите значение a: "))

# Просим пользователя ввести значение b
b = int(input("Введите значение b: "))

# Инициализируем переменную для хранения суммы
sum = 0

# Используем цикл for для прохода по всем числам от a до b включительно
for num in range(a, b+1):
    # Добавляем текущее число к сумме
    sum += num

# Выводим результат на экран
print("Сумма всех целых чисел от", a, "до", b, "включительно равна", sum)