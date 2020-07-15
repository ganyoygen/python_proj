# Membuat tabel

import mysql.connector

db = mysql.connector.connect(
  host="192.168.10.5",
  user="root",
  passwd="",
  database='pares_staff'
)

cursor = db.cursor()
sql = """CREATE TABLE staff (
  uid INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(20),
  password VARCHAR(255),
  full_name VARCHAR(255),
  tag_dept VARCHAR(10),
  department Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel staff berhasil dibuat!")