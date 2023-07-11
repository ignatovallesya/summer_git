#2.4
import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Вычисляем дискриминант
D = b**2 - 4*a*c

# Проверяем значение дискриминанта
if D < 0:
    print("Корней нет")
elif D == 0:
    x = -b / (2*a)
    print("Один корень: x =", x)
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Два корня: x1 =", x1, " x2 =", x2)