import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="test"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM student")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
