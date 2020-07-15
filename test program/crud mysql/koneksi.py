# koneksi mysql
import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root"
)

if db.is_connected():
    print("Berhasil terhubung ke database")
    print("SQL Log:",mysql.connector.errors.ProgrammingError())




