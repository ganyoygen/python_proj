import mysql.connector
import os

def show_data(db):
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM staff"
        cursor.execute(sql)
        results = cursor.fetchall()
    
        if cursor.rowcount < 0:   
            print("Tidak ada data")
        else:
            for data in results:
                print(data)
        print('---',cursor.rowcount,'ditemukan ---')
    except mysql.connector.Error as err:
        print("SQL Log: {}".format(err))

def search_data(db):
    try:
        cursor = db.cursor()
        keyword = input("Kata kunci: ")
        sql = "SELECT * FROM staff WHERE username LIKE %s OR full_name LIKE %s"
        val = ("%{}%".format(keyword), "%{}%".format(keyword))
        cursor.execute(sql, val)
        results = cursor.fetchall()
        if cursor.rowcount < 0:   
            print("Tidak ada data")
        else:
            for data in results:
                print(data)
        print('---',cursor.rowcount,'ditemukan ---')
    except mysql.connector.Error as err:
        print("SQL Log: {}".format(err))

def insert_data(db):
    try:
        username = input("Masukan ID: ")
        fullname = input("Masukan Fullname: ")
        val = (username, fullname)
        cursor = db.cursor()
        sql = "INSERT INTO staff (username, full_name) VALUES (%s, %s)"
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil disimpan".format(cursor.rowcount))
    except mysql.connector.Error as err:
        print("SQL Log: {}".format(err))

def update_data(db):
    try:
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
    except mysql.connector.Error as err:
        print("SQL Log: {}".format(err))

def delete_data(db):
    try:
        cursor = db.cursor()
        show_data(db)
        uid = input("pilih id uid> ")
        sql = "DELETE FROM staff WHERE uid=%s"
        cursor.execute(sql, (uid,))
        db.commit()
        print("{} data berhasil dihapus".format(cursor.rowcount))
    except mysql.connector.Error as err:
        print("SQL Log: {}".format(err))

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
        db.close()
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while(True):
        try:
            # print('Conecting to server...')
            db = mysql.connector.connect(
                host="192.168.10.5",
                user="root",
                passwd="",
                database="pares_staff"
                )
            #   cursor = db.cursor()
            #   cursor.execute("SELECT * FORM employees")   # Syntax error in query
        except mysql.connector.Error as err:
            print("SQL Log: {}".format(err))
            # print('Program will exit')
            # exit()
        show_menu(db)