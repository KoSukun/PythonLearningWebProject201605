import sqlite3
import datetime
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

d = datetime.date.today()
sumOfpoint = 0

The_Form = cgi.FieldStorage()
custid = The_Form['id'].value
custname = The_Form['custname'].value


print("Content-type : text/html \n")
print("<html><head><title>Python bookstore</title> ")
print("<style> table  { font-size : 13px; color : Maroon; font-weight : bold; }</style></head>")
print("<body><br><br><br>")

print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
print("There are book list which " + custname + " buys until now  <br><br>")



bookOfpurchase = []
cursor.execute("SELECT a.name, b.name, c.purdate, c.point from customer_tbl a, books_tbl b, purchase_tbl c where a.id = '" + custid + "' and a.id = c.id and c.bookid = b.id order by c.purdate")
bookOfpurchase = cursor.fetchall()


print("<table ><tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td><table border = '1'>")
for book in bookOfpurchase:
    print("<tr><td>" + book[0] + "</td><td>" + book[1] + "</td><td>" + book[2] + "</td><td>" + str(book[3]) + "</td><tr>")
connection.commit()   
print("</table></td></tr></table>")


   
print("</body></html>")


   
connection.close()









