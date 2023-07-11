#4.6
# Функция для шифрования текста шифром Цезаря
def caesar_cipher(text, shift):
    encrypted_text = ''

    for char in text:
        # Проверяем, является ли символ буквой алфавита
        if char.isalpha():
            # Определяем новую позицию символа с учетом сдвига
            new_position = (ord(char) - ord('a') + shift) % 26 + ord('a')
            encrypted_text += chr(new_position)
        else:
            # Символ не является буквой алфавита, оставляем его без изменений
            encrypted_text += char

    return encrypted_text


# Получаем строку для шифрования от пользователя
text = input("Введите текст для шифрования: ")

# Получаем сдвиг от пользователя
shift = int(input("Введите сдвиг: "))

# Вызываем функцию для шифрования текста
encrypted_text = caesar_cipher(text, shift)

# Выводим зашифрованный текст
print("Зашифрованный текст: ", encrypted_text)