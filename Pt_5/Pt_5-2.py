# 5.2
import csv

file = open("books.csv", "a")
num = int(input("Сколько записей вы хотите добавить в список: "))
for i in range(num):
    book = input("Введите название книги: ")
    author = input("Введите автора: ")
    year_release = input("Введите год издания: ")
    new_record = book + ", " + author + ", " + year_release + "\n"
    file.write(str(new_record))
file.close()

file = open("books.csv", "r")
find_author = input("Введите автора для поиска: ")
count = 0
row: str
for row in file:
    if find_author in str(row):
        count += 1
    print(row)
if count == 0:
    print("В списке нет ни одной книги этого автора")
file.close()
