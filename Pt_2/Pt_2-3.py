# 2.3
num = (int(input("Введите число: ")))
nums = str(num)
sum = 0
n = len(nums)
for digit in nums:
    sum += int(digit) ** n
if num == sum:
    print(num, "является числом Армстронга")
else:
    print(num, "не является числом Армстронга")

# Проверяем, является ли число числом Армстронга
if is_armstrong_number(number):
    print(number, "является числом Армстронга.")
else:
    print(number, "не является числом Армстронга.")
