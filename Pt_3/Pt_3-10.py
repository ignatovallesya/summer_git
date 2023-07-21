# 3.10
# Задаем строку
text = "Hello, how are you today?"

# Создаем пустой словарь
letter_count = {}

# Используем цикл для перебора каждого символа в строке
for letter in text:
    # Если символ - буква и не является пробелом
    if letter.isalpha() and letter != " ":
        # Если символ уже есть в словаре, увеличиваем его значение на 1
        if letter in letter_count:
            letter_count[letter] += 1
        # Если символа еще нет в словаре, добавляем его со значением 1
        else:
            letter_count[letter] = 1

# Выводим полученный словарь на экран
print(letter_count)
