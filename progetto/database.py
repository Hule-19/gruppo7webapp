#libreria sql
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database = "parchi"
)
mycursor = mydb.cursor()

#cerco la tabella SIMBOLI
mycursor.execute("SELECT * FROM valeggio;")
valeggio = mycursor.fetchall()
