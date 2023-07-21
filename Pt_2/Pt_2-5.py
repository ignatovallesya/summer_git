# 2.5
import random
game = ["0", "1"]
temp = random.choice(game)
sum = 0
wins = 0
losses = 0
while sum < 3:
    s = str(input("Выберете орел - 0 или решку - 1:"))
    if temp == s:
        print("Ты угадал!")
        wins += 1
        sum = 0
    elif s not in temp:
        print("Конец игры")
        break
    else:
        losses += 1
        sum += 1
        print("Ты не угадал!")

    print("Счет: побед -", wins, ", поражений —", losses)
else:
    print("Игра завершена")
