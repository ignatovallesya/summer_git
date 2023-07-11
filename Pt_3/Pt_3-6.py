#3.6
# Создаем пустой словарь
binary_dict = {}

# Используем цикл for для прохода по числам от 1 до 10
for num in range(1, 11):
    # Преобразуем число в его двоичное представление с помощью функции bin()
    binary = bin(num)
    # Добавляем пару ключ-значение в словарь
    binary_dict[num] = binary

# Выводим словарь на экран
for key, value in binary_dict.items():
    print(f"{key}: {value}")