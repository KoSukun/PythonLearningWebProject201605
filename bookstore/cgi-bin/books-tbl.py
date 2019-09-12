import sqlite3

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE books_tbl (
                        id    TEXT   NOT NULL,
                        name    TEXT   NOT NULL,
                        price   TEXT  NOT NULL,
                        pubdate  TEXT   NOT NULL,
                        publisher  TEXT   NOT NULL,
                        image TEXT NOT NULL)""")
connection.commit()
connection.close()
