import mysql.connector
import os

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="root",
    database="pares_staff"
)


def insert_data(db):
    username = input("Masukan ID: ")
    fullname = input("Masukan Fullname: ")
    val = (username, fullname)
    cursor = db.cursor()
    sql = "INSERT INTO staff (username, full_name) VALUES (%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM staff"
    cursor.execute(sql)
    results = cursor.fetchall()
  
    # if cursor.rowcount < 0:   
    #     print("Tidak ada data")
    # else:
    #     for data in results:
    #         print(data)
    for data in results:
        print(data)


def update_data(db):
    cursor = db.cursor()
    show_data(db)
    uid = input("pilih id uid> ")
    username = input("ID baru: ")
    fullname = input("Fullname baru: ")

    sql = "UPDATE staff SET username=%s, full_name=%s WHERE uid=%s"
    val = (username, fullname, uid)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    uid = input("pilih id uid> ")
    sql = "DELETE FROM staff WHERE uid=%s"
    val = (uid)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM staff WHERE username LIKE %s OR full_name LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()
    
    # if cursor.rowcount < 0:   
    #     print("Tidak ada data")
    # else:
    #     for data in results:
    #         print(data)
    for data in results:
        print(data)


def show_menu(db):
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    #clear screen
    os.system("cls")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while(True):
        show_menu(db)