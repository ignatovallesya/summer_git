#4.5
def find_paths(graph, start, end, path=[]):
    # Добавляем текущую вершину в путь
    path = path + [start]

    # Если текущая вершина является конечной, добавляем путь в список путей
    if start == end:
        return [path]

    # Если текущая вершина не существует в графе, возвращаем пустой список путей
    if start not in graph:
        return []

    # Инициализируем список путей
    paths = []

    # Для каждой смежной вершины вызываем функцию рекурсивно
    for vertex in graph[start]:
        new_paths = find_paths(graph, vertex, end, path)
        paths.extend(new_paths)

    return paths

# Заданный граф
graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': [],
 'E': ['F'],
 'F': []
}

# Заданные начальная и конечная вершины
start = 'A'
end = 'F'

# Находим все пути от заданной вершины до заданной вершины
paths = find_paths(graph, start, end)

# Выводим результат
for path in paths:
    print(' -> '.join(path))