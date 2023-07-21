# 4.2
def find_p(mes):
    answer = []
    for i in range(len(mes)):
        for j in range(i + 1, len(mes) + 1):
            subst = mes[i:j]
            if subst == subst[::-1] and len(subst) > 1:
                answer.append(subst)
    return answer


st = input("Строка: ")
palind = find_p(st)
print("Палиндромы:", palind)
