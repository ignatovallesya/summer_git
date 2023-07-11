#1.3
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

max_num = max(num1, num2, num3)

print("Наибольшее число: ", max_num)

sorted_nums = sorted([num1, num2, num3], reverse=True)
print("Числа в порядке убывания:", sorted_nums)