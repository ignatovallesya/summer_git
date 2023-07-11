#5.2
import csv

# Записи книг в список
def add_books(books_count):
    books = []
    for _ in range(books_count):
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги: ")
        books.append({'Title': title, 'Author': author, 'Year': year})

    # Записываем данные в файл books.csv
    with open('books.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Author', 'Year'])
        writer.writeheader()
        writer.writerows(books)

    return books

# Поиск книг по автору
def search_books(author):
    with open('books.csv', 'r') as file:
        reader = csv.DictReader(file)
        found_books = []
        for row in reader:
            if row['Author'] == author:
                found_books.append(row)

        if len(found_books) == 0:
            print("Книги этого автора не найдены.")
        else:
            print("Найдены книги автора", author)
            for book in found_books:
                print(book)

# Запрашиваем количество книг, которые пользователь хочет добавить
books_count = int(input("Сколько книг вы хотите добавить? "))

# Добавляем книги и получаем список книг
books = add_books(books_count)

# Запрашиваем автора для поиска
author = input("Введите автора, чтобы найти его книги: ")

# Ищем книги указанного автора
search_books(author)