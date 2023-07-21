# 2.4
a = (int(input("Введите a: ")))
b = (int(input("Введите b : ")))
c = (int(input("Введите c : ")))
d = b ** 2 - 4 * a * c
if d < 0:
    print("Корней нет")
if d == 0:
    print("Корень 1")
    print(-b / (2 * a))
if d > 0:
    print("2 корня")
    print(-b + d ** 0.5 / (2 * a))
    print(-b - d ** 0.5 / (2 * a))
