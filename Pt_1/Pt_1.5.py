#1.5
points = int(input("Введите количество очков команды: "))

if points == 3:
    result = "выигрыш"
elif points == 0:
    result = "проигрыш"
else:
    result = "ничья"