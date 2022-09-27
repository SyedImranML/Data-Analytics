import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="Ngcc@123")

dbCursor = db.cursor()
dbCursor.execute("Create database Booklist") #Create Database

dbCursor.execute("Show databases")#Show Database
for i in dbCursor:
  print(i)
