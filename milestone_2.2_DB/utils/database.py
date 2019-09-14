from typing import List, Dict, Union

import sqlite3

from .database_connection import DatabaseConnection


books_file = 'books.json'
database = 'data.db'


Book = Dict[str, Union[str, int]]


def create_book_table() -> None:

    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('create table if not exists books (name text primary key, author text, read integer)')


def add_book(name: str, author: str) -> None:

    with DatabaseConnection(database) as connection:

        cursor = connection.cursor()
        try:
            cursor.execute(f'insert into books values (? , ?, 0)', (name, author))
        except sqlite3.IntegrityError:
            print('The book is already in the list.  ')


def get_all_books() -> List[Book]:

    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('select * from books')
        books = [{'name': row[0], 'author': row[1], 'read':row[2]} for row in cursor.fetchall()]

        return books


def read_book(name: str) -> None:

    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute(f'update books set read = 1 where name = "{name}"')


def delete_book(name: str) -> None:

    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute(f'delete from books where name="{name}"')




