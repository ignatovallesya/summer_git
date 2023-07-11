#2.1
import random

# Список доступных цветов
colors = ["красный", "синий", "зеленый", "желтый", "оранжевый"]

while True:
    # Случайный выбор цвета программой
    program_color = random.choice(colors)

    # Вывод названий цветов
    print("Названия цветов:", ", ".join(colors))

    while True:
        # Предложение выбрать цвет пользователю
        user_color = input("Выберите цвет: ")

        if user_color == program_color:
            print("Отлично!")
            break
        else:
            hint = program_color[0] + ("*" * (len(program_color)-1))
            print("Не угадали! Но вот намек:", hint)
            print("Попробуйте еще раз.")

    play_again = input("Хотите сыграть еще раз? (да/нет): ")
    if play_again.lower() != "да":
        break