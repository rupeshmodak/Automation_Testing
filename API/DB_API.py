import mysql.connector

#conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='pappumaster')
#print(conn.is_connected())
from utilities.configuration import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
rowAll = cursor.fetchall()
print(rowAll)
print("Course name is " + rowAll[2][0])
summ = 0
for row in rowAll:
    print(row[2])
    summ = summ + row[2]
print(summ)

query = "update CustomerInfo set Location = %s where CourseName = %s"
data = ("Bharat", "Protractor")
cursor.execute(query, data)
conn.commit()

#cursor.execute('INSERT INTO CustomerInfo values("selenium",CURRENT_DATE(),120,"Africa")')
#conn.commit()

conn.close()
