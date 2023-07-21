# 4.7
from itertools import permutations
lst = input('Строчка для поиска перестановок: ').split(',')
permutations = permutations(lst)
for permutations in permutations:
    print(permutations)
