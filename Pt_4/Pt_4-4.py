#4.4
# Задаем список чисел
numbers = [1, 2, 3, 4, 5]

# Задаем целевую сумму
target_sum = 7

# Создаем функцию для поиска комбинаций чисел
def find_combinations(numbers, target_sum):
    # Создаем пустой список для хранения комбинаций
    combinations = []

    # Создаем вспомогательную функцию для рекурсивного поиска комбинаций
    def find_combinations_recursive(numbers, target_sum, current_sum, current_combination, start_index):
        # Если текущая сумма равна целевой сумме, добавляем текущую комбинацию в список
        if current_sum == target_sum:
            combinations.append(current_combination)

        # Если текущая сумма больше целевой суммы, прекращаем поиск
        if current_sum > target_sum:
            return

        # Используем цикл для перебора чисел, начиная с заданного индекса
        for i in range(start_index, len(numbers)):
            # Добавляем текущее число к текущей сумме
            new_sum = current_sum + numbers[i]
            # Создаем новую комбинацию, добавляя текущее число
            new_combination = current_combination + [numbers[i]]
            # Рекурсивно вызываем функцию для поиска комбинаций
            find_combinations_recursive(numbers, target_sum, new_sum, new_combination, i)

    # Вызываем вспомогательную функцию для начала поиска комбинаций
    find_combinations_recursive(numbers, target_sum, 0, [], 0)

    # Возвращаем список всех найденных комбинаций
    return combinations

# Вызываем функцию и выводим результаты на экран
print(find_combinations(numbers, target_sum))
