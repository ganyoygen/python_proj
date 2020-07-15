# Membuat Database
import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE pares_staff")

print("Database berhasil dibuat!")