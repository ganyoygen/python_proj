#its works :D

import mysql.connector

try:
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
    )
  # cursor = db.cursor()
  # cursor.execute("SELECT * FORM employees")   # Syntax error in query
  db.close()
except mysql.connector.Error as err:
  print("SQL Log: {}".format(err))
  print('ok')


# try:
#   db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd=""
#     )
#   # cursor = db.cursor()
#   # cursor.execute("SELECT * FORM employees")   # Syntax error in query
#   db.close()
# except mysql.connector.Error as err:
#   print("SQL Log: {}".format(err))
#   print('ok')
