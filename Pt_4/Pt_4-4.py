# 4.4
from itertools import combinations

numbs = [1, 3, 4, 7, 8, 2]
a = int(input("Введите число: "))
uniq_com = []
sum_com = []

for r in range(1, len(numbs) + 1):
    combs = list(map(list, combinations(numbs, r)))
    uniq_com.extend(combs)

for combination in uniq_com:
    if sum(combination) == a:
        sum_com.append(combination)

print(f'Подходящие коомбинации: {sum_com}')
