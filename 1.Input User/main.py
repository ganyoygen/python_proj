#Input User
print("")
print("=== Input User===")
data = input("Masukan data: ") #data masuk pasti string
print("Data:",data, "- Tipe:", type(data))

print("=== Input Angka===")
#jika ingin mengambil int
angka = int(input("Masukan angka: ")) #data masuk pasti integer (bilangan bulat)
print("Data:",angka, "- Tipe:", type(angka))

print("=== Input boolean===")
#jika ingin mengambil int
biner = bool(int(input("Masukan angka: "))) #data masuk pasti biner 
print("Data:",biner, "- Tipe:", type(biner))

# float = bilangan pecahan (1.2, 10.5, dst)