import sqlite3

connection = sqlite3.connect("person.sqlite")
cursor = connection.cursor()


cursor.execute("INSERT INTO prs_tbl VALUES(1,'Kim amoogae','20000620','20000620')")

cursor.execute("INSERT INTO prs_tbl VALUES(2,'Yang Dongi','19830403','19830403')")

cursor.execute("INSERT INTO prs_tbl VALUES(3,'Kang simjang','19850715','19850715')")

cursor.execute("INSERT INTO prs_tbl VALUES(4,'Seo Soul','19891230','19891230')")

connection.commit()
connection.close()
