# 4.6
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


text = input("Введите текст для шифрования: ")

shift = int(input("Введите сдвиг: "))

encrypted_text = caesar_cipher(text, shift)

print("Зашифрованный текст: ", encrypted_text)
