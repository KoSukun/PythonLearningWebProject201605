import sqlite3
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()



The_Form = cgi.FieldStorage()
idv = The_Form['id'].value
insert = The_Form['insert'].value

   

print("Content-type : text/html \n")
print("<html><head><title>python bookstore admin </title> </head>")
print("<body>   <h2> 도서 입력 </h2>")

"""for att in The_Form.keys():
    print(att)"""
 

if idv == 'admin':

    print("<form action='bookmanage.py' method='get'>")
    print("<input type='hidden' name='id' value='"+idv+"'>")
    print("<input type='hidden' name='insert' value='ok'>")
    print("<table>")
    print("<tr><th align='left'>Book Id&nbsp;&nbsp;</th><td><input type='text' name='bookid'></td></tr>")
    print("<tr><th align='left'>Book Name&nbsp;&nbsp;</th><td><input type='text' name='bookname'></td></tr>")
    print("<tr><th align='left'>Price&nbsp;&nbsp;</th><td><input type='text' name='price'></td></tr>")
    print("<tr><th align='left'>Publish Date&nbsp;&nbsp;</th><td><input type='text' name='pubdate'></td></tr>")
    print("<tr><th align='left'>Publisher&nbsp;&nbsp;</th><td><input type='text' name='publisher' ></td></tr>")
    print("<tr><th align='left'>Image Path&nbsp;&nbsp;</th><td><input type='text' name='image' ></td></tr>")
    print("<tr><th align='left'>Stock&nbsp;&nbsp;</th><td><input type='number' name='stock' value = '0'></td></tr>")
    print("<tr><td colspan='2' height ='20'></td></tr>")
    print("<tr><td align='middle' colspan='2'><input type='submit' name='send' value='input' ></td></tr>")
    print("</table></form>")

    if insert == 'ok':
        bookid = The_Form['bookid'].value
        bookname = The_Form['bookname'].value
        price = The_Form['price'].value
        publisher = The_Form['publisher'].value
        pubdate = The_Form['pubdate'].value
        image = The_Form['image'].value
        stock = int(The_Form['stock'].value)

        cursor.execute("INSERT INTO books_tbl VALUES('" + bookid + "','" + bookname + "','" + price + "','" + pubdate + "','" + publisher + "','" + image +"'," + stock +")")

        connection.commit()
    elif insert == 'update' :
        bookid = The_Form['bookid'].value
        bookname = The_Form['bookname'].value
        price = The_Form['price'].value
        publisher = The_Form['publisher'].value
        pubdate = The_Form['pubdate'].value
        image = The_Form['image'].value
        stock = int(The_Form['stock'].value)

        cursor.execute("UPDATE books_tbl set name = '" + bookname + "' , price = '" + price + "', pubdate = '" + pubdate + "', publisher = '" + publisher + "', image = '" + image + "', stock = " + str(stock) + " where id = '" + bookid + "'" )

        connection.commit()
        
    elif insert == 'del':
        for att in The_Form.keys():
            if att != 'id' and att != 'insert' and att != 'delete':
                cursor.execute("DELETE from books_tbl where id = '" + att + "'")
                connection.commit()

 
    cursor.execute("SELECT * from books_tbl")

    tbl=[]
    tbl = cursor.fetchall()
   
    print("<form action = 'bookmanage.py' method = 'POST'>")
    print("<table ><tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td><table border = '1'>")
    for book in tbl:
        print("<tr>")
        print("<td width = '60' align = 'middle'><a href='bookupdate.py?bookid="+book[0]+"'>" + book[0] + "</a></td>")
        print("<td>" + book[1] + "</td><td>" + book[2] + "</td>")
        print("<td>" + book[3] + "</td><td>" + book[4] + "</td>")
        print("<td>" + book[5] +"</td>")
        print("<td width='30' align = 'right'>" + str(book[6]) + "</td>")
        print("<td><input type='checkbox' name='" + book[0] + "'></td>")
        print("<tr>")  
    connection.commit()   
    print("</table></td></tr></table>")

    
    print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    print("<input type='submit' name='delete' value = '삭제'>")
    
    print("<input type='hidden' name='id' value='"+idv+"'>")
    print("<input type='hidden' name='insert' value = 'del'>")
    print("</form>")
    print("</body></html>")
    connection.commit()
    connection.close()

        

    
else:
    print("관리자가 아니십니다. 관리자만이 들어올 수 있는 화면 입니다")
    










