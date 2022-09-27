import mysql.connector 
db = mysql.connector.connect(host="localhost",user="root",password="Ngcc@123")
if db:
  print("Connection successful")
else:
  print("Connection Failed")
