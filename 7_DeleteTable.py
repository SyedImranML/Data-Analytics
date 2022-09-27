import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="Ngcc@123",database="Booklist")

dbCursor = db.cursor()

dbCursor.execute("DELETE FROM bookdetail WHERE Rating=3")

db.commit()
