import sqlite3
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()



The_Form = cgi.FieldStorage()
idv = The_Form['id'].value
find = The_Form['find'].value


   

print("Content-type : text/html \n")
print("<html><head><title>python bookstore admin </title> </head>")
print("<body>   <h2> 판매량 관리 </h2>")


if idv == 'admin':

    
    print("<table>")
    print("<tr><td></td><td></td><td></td><td></td><td></td>")
    print("<tr><td><a href='custmanage.py?id=admin&find=d'>날짜별 도서별 판매량</a></td><td width='40'></td>")
    print("<td><a href='custmanage.py?id=admin&find=c'>고객별 판매량</a></td><td width='40'></td>")
    print("<td><a href='custmanage.py?id=admin&find=b'>도서별 판매량</a></td></tr></table>")
    
    if find == 'd':
        print("<h3> 날짜별 도서별 판매량 </h3>")
        cursor.execute("SELECT a.purdate, b.name, count(a.purdate) from purchase_tbl a, books_tbl b where a.bookid = b.id group by a.purdate , a.bookid, b.name")
        count = []
        count = cursor.fetchall()

        print("<table border = '1'>")
        print("<tr><th> 날짜 </th><th> 도서명 </th><th> 판매량 </th></tr>")
        
        for howmany in count:
            print("<tr><td width = '100' align = 'middle'>"+howmany[0] + "</td><td width = '200' align = 'left'>" + howmany[1] + "</td><td width = '80' align = 'right'>" + str(howmany[2]) + "</td></tr>")
        print("</table>")
    elif find == 'c':
        print("<h3> 고객별 판매량 </h3>")
        cursor.execute("SELECT  b.name, count(b.id) from purchase_tbl a, customer_tbl b where a.id = b.id group by b.id, b.name")
        count = []
        count = cursor.fetchall()

        print("<table border = '1'>")
        print("<tr><th > 고객 </th><th> 판매량 </th></tr>")
        
        for howmany in count:
            print("<tr><td width = '150' align = 'left'>"+howmany[0] + "</td><td width = '80' align = 'right'>" + str(howmany[1]) + "</td></tr>")
        print("</table>")
    elif find == 'b':
        print("<h3> 도서별 판매량 </h3>")

        cursor.execute("SELECT b.name, count(a.bookid) from purchase_tbl a, books_tbl b where a.bookid = b.id group by a.bookid, b.name")
        count = []
        count = cursor.fetchall()

        print("<table border = '1'>")
        print("<tr><th> 도서명 </th><th> 판매량 </th></tr>")
        
        for howmany in count:
            print("<tr><td width = '200' align = 'left'>"+howmany[0] + "</td><td width = '80' align = 'right'>" + str(howmany[1]) + "</td></tr>")
            
        print("</table>")
        
    
else:
    print("관리자가 아니십니다. 관리자만이 들어올 수 있는 화면 입니다")

print("</body></html>")










