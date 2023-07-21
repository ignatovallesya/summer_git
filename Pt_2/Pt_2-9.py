# 2.9
num = str(input('Введите натуральное число, в котором все цифры различны: '))
print(num.index(max(num)) + 1)
n = num[::-1]
print(n.index(max(n)) + 1)
