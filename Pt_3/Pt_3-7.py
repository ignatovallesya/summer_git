#3.7
# Функция для проверки, является ли буква гласной
def is_vowel(letter):
    vowels = "aeioyuAEIOYU"
    return letter in vowels

# Вводим строку
string = input("Введите строку: ")

# Создаем пустой словарь
letter_dict = {}

# Используем цикл for для прохода по каждой букве в строке
for letter in string:
    # Вызываем функцию is_vowel для проверки, является ли буква гласной
    is_vowel_letter = is_vowel(letter)
    # Добавляем пару ключ-значение в словарь
    letter_dict[letter] = is_vowel_letter

# Выводим словарь на экран
print("Словарь с гласными и согласными буквами:")
for key, value in letter_dict.items():
    print(key, ":", value)