# Membuat Database
import mysql.connector

db = mysql.connector.connect(
  host="192.168.10.5",
  user="root",
  passwd=""
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE pares_staff")

print("Database berhasil dibuat!")