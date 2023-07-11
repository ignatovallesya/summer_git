#4.2
# Задаем строку
string = "Hello, level radar racecar madam"

# Функция для проверки, является ли строка палиндромом
def is_palindrome(s):
    return s == s[::-1]

# Создаем пустой список для хранения палиндромов
palindromes = []

# Используем два вложенных цикла для создания всех возможных подстрок
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        # Проверяем, является ли подстрока палиндромом и добавляем в список, если да
        if is_palindrome(string[i:j]):
            palindromes.append(string[i:j])

# Выводим список палиндромов на экран
print(palindromes)