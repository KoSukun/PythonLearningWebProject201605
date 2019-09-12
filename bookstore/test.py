import sqlite3

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()


cursor.execute("SELECT * from books_tbl where id = '00001'")

bookid=[]
bookid = cursor.fetchall()

print(bookid)

if bookid == []:
    print("bookid is null")
else:
    print("bookid is not null")
