import csv


# Загрузка данных из файла books.csv
def load_books():
    books = []
    with open('books.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books


# Поиск книг в заданном промежутке времени
def search_books(books, start_year, end_year):
    found_books = []
    for book in books:
        year = int(book['Year'])
        if start_year <= year <= end_year:
            found_books.append(book)

    # Вывод результатов поиска
    if len(found_books) == 0:
        print("Книги в заданном промежутке времени не найдены.")
    else:
        print("Найдены книги в промежутке времени", start_year, "-", end_year)
        for book in found_books:
            print("Название:", book['Title'], "Автор:", book['Author'], "Год издания:", book['Year'])


# Загрузка данных из файла books.csv
books = load_books()

# Запрос начального и конечного года у пользователя
start_year = int(input("Введите начальный год: "))
end_year = int(input("Введите конечный год: "))

# Поиск книг в заданном промежутке времени
search_books(books, start_year, end_year)