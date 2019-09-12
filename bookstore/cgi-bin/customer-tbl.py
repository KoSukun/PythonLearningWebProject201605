import sqlite3

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

cursor.execute("drop table customer_tbl")
connection.commit()

cursor.execute("""CREATE TABLE customer_tbl (
                        id    TEXT   NOT NULL,
                        name    TEXT   NOT NULL,
                        password   TEXT  NOT NULL,
                        telephone  TEXT   NOT NULL,
                        address TEXT NOT NULL,
                        points INTEGER NULL,
                        used INTEGER NULL)""")
connection.commit()
connection.close()
