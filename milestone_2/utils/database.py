

books_file = 'books.txt'


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},False\n')


def get_all_books():

    try:
        with open(books_file, 'r') as file:
          #  print(file.readlines())
            lines = [line.strip().split(',') for line in file.readlines()]

            return [
                {'name': line[0], 'author': line[1], 'read': line[2]}
                for line in lines
            ]
    except FileNotFoundError:
        with open(books_file, 'w'):
            return []


def read_book(name):
    books = get_all_books()

    for book in books:
        if book['name'] == name:
            book['read'] = 'True'

    _save_all_books(books)


def _save_all_books(books):

    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):

    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)




