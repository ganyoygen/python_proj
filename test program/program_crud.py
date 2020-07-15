# ===== MINI PROGRAM CRUD =======

# Variabel list global untuk menyimpan data buah
buah = ["apel", "anggur", "mangga", "jeruk"]

# fungsi untuk menampilkan semua data
def show_data():
    if len(buah) <= 0:
        print ("BELUM ADA DATA")
    else:
        for indeks in range(len(buah)):
            print ("[%d] %s" % (indeks, buah[indeks]))


# fungsi cek input = data list
def check_data(data):
    for index in range(len(buah)):
        if (buah[index].lower() == data.lower()):
            return "sama"

# fungsi untuk menambah data 
def insert_data():
    buah_baru = input("Judul buah: ")
    if check_data(buah_baru) == "sama":
        print("GAGAL INSERT. Buah", buah_baru, "sudah terdaftar")
    else:
        buah.append(buah_baru)
        print("telah berhasil menambahkan", buah_baru)

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = input("Inputkan ID buah: ")
    if indeks.isdigit():
        indeks = int(indeks)
        if (indeks >= len(buah)):
            print ("ID salah")
        else:
            judul_baru = input("Judul baru: ")
            if check_data(judul_baru) == "sama":
                print("GAGAL EDIT. Buah", judul_baru, "sudah terdaftar")
            else:
                buah[indeks] = judul_baru
    else:
        print("Masukan ID yang benar")

# fungsi untuk hapus data
def delete_data():
    show_data()
    indeks = input("Inputkan ID buah: ")
    if indeks.isdigit():
        indeks = int(indeks)
        if (indeks >= len(buah)):
            print ("ID salah")
        else:
            print("buah",buah[indeks],"telah dihapus")
            buah.remove(buah[indeks])
    else:
        print("Masukan ID yang benar")

# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU ----------")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    
    menu = input("PILIH MENU> ")
    print ("\n")
    if menu == '1':
        show_data()
    elif menu == '2':
        insert_data()
    elif menu == '3':
        edit_data()
    elif menu == '4':
        delete_data()
    elif menu == '5':
        exit()
    else:
        print ("Salah pilih!")


if __name__ == "__main__":

    while(True):
        show_menu()

# test run 16/07/2020 00:15