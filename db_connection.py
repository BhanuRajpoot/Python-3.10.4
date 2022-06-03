import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='python1')

mycursor = mydb.cursor()

mycursor.execute("select * from student")
result = mycursor.fetchone()

for i in result:
    print(i)