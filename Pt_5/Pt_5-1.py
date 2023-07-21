# 5.1
import csv

# Заданные данные о книгах
books = [
    {'Title': 'Чародол', 'Author': 'Наталья Щерба', 'Year': '2008'},
    {'Title': 'Вино из одуванчиков', 'Author': 'Рэй Брэдбери', 'Year': '1957'},
    {'Title': 'Призрак оперы', 'Author': 'Гастон Леру', 'Year': '1909'},
    {'Title': 'Мастер', 'Author': 'Булгаков', 'Year': '1937'},
]

# Открываем файл books.csv для записи
with open('books.csv', 'w', newline='') as file:
    # Создаем объект writer для записи данных в файл
    writer = csv.DictWriter(file, fieldnames=['Title', 'Author', 'Year'])

    # Записываем заголовки столбцов
    writer.writeheader()

    # Записываем данные о книгах
    for book in books:
        writer.writerow(book)

print("Файл books.csv успешно создан.")
