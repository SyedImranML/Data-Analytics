import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="Ngcc@123",database="Booklist")

dbCursor = db.cursor()

dbCursor.execute("Select Book from bookdetail")

result = dbCursor.fetchall()

for i in result:
    print(i)
