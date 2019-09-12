import sqlite3

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE purchase_tbl (
                        id    TEXT   NOT NULL,
                        bookid    TEXT   NOT NULL,
                        purdate  TEXT   NOT NULL,
                        point  integer   NOT NULL)""")
connection.commit()
connection.close()
