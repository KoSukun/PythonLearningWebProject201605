import sqlite3
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()




The_Form = cgi.FieldStorage()
idv = The_Form['id'].value
password = The_Form['password'].value
name = The_Form['name'].value
telephone = The_Form['telephone'].value
address = The_Form['address'].value


cursor.execute("SELECT count(id) from customer_tbl WHERE id = '" + idv + "'")

tbl=[]
tbl = cursor.fetchall()
#rows = cursor.rowcount
idvalue = tbl[0][0]

if idvalue  == 0 :

    connection.commit()
    #connection.close()

    #connection = sqlite3.connect("bookstore.sqlite")
    #cursor = connection.cursor()

    cursor.execute("INSERT INTO customer_tbl VALUES('" + idv + "','" + name + "','" + password + "','" + telephone + "','" + address + "',0,0)")
    print("Content-type : text/html \n")
    print("<html><head><title>python bookstore</title> </head>")
    print("<body><p> Thank you for registration<br>")
    print(idv + "  is registrated. <br>")
    print("<a href = '../login.html'> go Login </a><br>")
    print("</p></body></html>")

    connection.commit()
    connection.close()

else:
    print("Content-type : text/html \n")
    print("<html><head><title>python bookstore</title> </head>")
    print("<body><p> ")
    print(idv + " is already existed id or You are already registrated.   <br>")
    print("<a href = '../registration.html'> return to registrate </a><br>")
    print("</p></body></html>")

#connection.commit()
#connection.close()









