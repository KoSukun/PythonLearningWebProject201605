import sqlite3
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()


print("Content-type : text/html \n")
print("<html><head><title>python bookstore admin </title> </head>")
print("<body>   <h2> 도서 갱신  </h2>")


The_Form = cgi.FieldStorage()
bookid = The_Form['bookid'].value

cursor.execute("SELECT * from books_tbl where id = '" + bookid + "'")

book=[]
book = cursor.fetchall()

if book != []:
    print("<form action='bookmanage.py' method='get'>")
    print("<input type='hidden' name='bookid' value='"+bookid+"'>")
    print("<input type='hidden' name='id' value='admin'>")
    print("<input type='hidden' name='insert' value='update'>")
    print("<table>")
    print("<tr><th align='left'>Book Name&nbsp;&nbsp;</th><td><input type='text' name='bookname' value = '" + book[0][1] + "'></td></tr>")
    print("<tr><th align='left'>Price&nbsp;&nbsp;</th><td><input type='text' name='price' value = '" + book[0][2] + "'></td></tr>")
    print("<tr><th align='left'>Publish Date&nbsp;&nbsp;</th><td><input type='text' name='pubdate' value = '" + book[0][3] + "'></td></tr>")
    print("<tr><th align='left'>Publisher&nbsp;&nbsp;</th><td><input type='text' name='publisher' value = '" + book[0][4] + "'></td></tr>")
    print("<tr><th align='left'>Image Path&nbsp;&nbsp;</th><td><input type='text' name='image' value = '" + book[0][5] + "'></td></tr>")
    print("<tr><th align='left'>Stock&nbsp;&nbsp;</th><td><input type='number' name='stock' value = " + str(book[0][6])+ "></td></tr>")
    print("<tr><td colspan='2' height ='20'></td></tr>")
    print("<tr><td align='middle' colspan='2'><input type='submit' name='update' value='Update' ></td></tr>")
    print("</table></form>")

else:
    print("There is no data of " + bookid)

print("</body></html>")
connection.commit()
connection.close()
