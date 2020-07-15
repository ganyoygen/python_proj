# koneksi mysql
import mysql.connector

db = mysql.connector.connect(
  host="loclhost",
  user="root",
  passwd=""
)
if db.is_connected():
      print("Berhasil terhubung ke database")
else:
    print("SQL Log: {}".format(mysql.connector.Error))
    print('ok')



