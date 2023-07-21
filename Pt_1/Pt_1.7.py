# 1.7
def toggle_case(input_string):
    toggled_string = ""
    for char in input_string:
        if char.islower():
            toggled_string += char.upper()
        elif char.isupper():
            toggled_string += char.lower()
        else:
            toggled_string += char
    return toggled_string

input_string = input("Введите строку: ")

result = toggle_case(input_string)

print("Результат:", result)
