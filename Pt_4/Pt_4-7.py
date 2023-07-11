#4.7
def permutations(lst):
    # Если список пустой, возвращаем пустой список (базовый случай рекурсии)
    if len(lst) == 0:
        return [[]]

    # Инициализируем переменную для хранения всех перестановок
    result = []

    # Проходим по каждому элементу списка
    for i in range(len(lst)):
        # Извлекаем текущий элемент из списка
        current_element = lst[i]

        # Построение нового списка без текущего элемента
        remaining_list = lst[:i] + lst[i+1:]

        # Рекурсивно находим все перестановки для оставшегося списка
        for p in permutations(remaining_list):
            # Добавляем текущий элемент в начало каждой перестановки
            result.append([current_element] + p)

    return result

# Заданный список
lst = [1, 2, 3]

# Находим все перестановки заданного списка
permutations_list = permutations(lst)

# Выводим результат
for perm in permutations_list:
    print(perm)