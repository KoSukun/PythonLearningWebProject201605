import sqlite3
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()


The_Form = cgi.FieldStorage()
id_v = The_Form['id'].value
password_v = The_Form['password'].value

if id_v == 'admin' :
    print("Content-type : text/html \n")
    print("<html><head><title>Python bookstore</title> ")
    print("<style> table { font-size : 13px; color : Maroon; font-weight : bold; }</style></head>")
    print("<body><br><br>")
    print("<h2> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;관리자 화면 입니다. </h2>")
    print("<h2> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;원하는 메뉴를 선택하세요. </h2>")

    print("<table><tr><td width = '30'></td><td>")
    
    print("<ol>")
    print("<li><a href='custmanage.py?id=admin&find=n'>판매량 관리</a> </li>")
    print("<li><a href='bookmanage.py?id=admin&insert=no'>서적 관리</a> </li>")
    print("</ol>")

    print("</td><tr></table>")
    

else:
    cursor.execute("SELECT count(id) from customer_tbl where id = '" + id_v + "' and password = '" + password_v + "'")

    idOfcount = []
    idOfcount = cursor.fetchall()
    id_count = idOfcount[0][0]

    print("Content-type : text/html \n")
    print("<html><head><title>Python bookstore</title> ")
    print("<style> table { font-size : 13px; color : Maroon; font-weight : bold; }</style></head>")
    print("<body>")

    if int(id_count)  == 0 :
         print("Login id doesn't exist. Please confirm one more!!!")
         print("<a href = '../login.html'> Login screen </a>")
    
    else:

         cursor.execute("SELECT * from customer_tbl where id = '" + id_v + "' and password = '" + password_v + "'")
         nameOfid = []
         idOfcount = cursor.fetchall()
         custname = idOfcount[0][1]
    
         print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
         print(custname + "&nbsp; !!!  Welcome to Python Bookstore !!! ")
         print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <a href='myroom.py?id=" + id_v + "&custname=" + custname+"'>My Room</a><br><br>")

    
    
         books_tbl = []
         print("<form  action = 'pointpay.py' method = 'POST'><br>")
         print("<input type = 'hidden' name = 'custid' value = '" + id_v + "'>")
         print("<input type = 'hidden' name = 'custname' value = '" + custname + "'>")
         print("<table >")
         
         cursor.execute("SELECT * from books_tbl ")
         bookd_tbl = cursor.fetchall()
         
         i = 0 
         for book in bookd_tbl:
             if i % 3 == 0:
                 print("<tr>")
             print("<td><table>")
             print("<tr><td rowspan = '5'><img src = '/"+ book[5]+"' ></td><td>"+book[1]+"</td></tr>")
             print("<tr><td>출판사 : " + book[4] + "</td></tr>")
             print("<tr><td>출판일 : " + book[3] + "</td></tr>")
             print("<tr><td>가  격 : " + book[2] + "</td></tr>")
             print("<tr><td><input type = 'checkbox' name = '"+ book[0] + "'></td></tr>")
             print("<tr><td></td><td></td></tr>")
             print("<tr><td></td><td></td></tr>")
             print("</table></td>")
             i +=  1
             if i % 3 == 0:
                 print("</tr>")
                 
         if i % 3 != 0:
             print("</tr>")
           
         print("<tr><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;<input type = 'submit' name = 'submit' value = '결제'></td><td></td></tr>")
         print("</table>")
         print("</form>")
         connection.commit()
    
print("</body></html>")


   
connection.close()









