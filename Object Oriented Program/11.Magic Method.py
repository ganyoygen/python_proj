# #clear screen
import os
os.system("cls")

class Mangga:

	#magic method
	def __init__(self,nama,jumlah):
		self.nama = nama
		self.jumlah = jumlah

    # __repr__ / __str__ 
	def __repr__(self):
		return "Debug - Mangga: {} dengan jumlah: {}".format(self.nama,self.jumlah)

	def __str__(self):
		return "Mangga: {} dengan jumlah: {}".format(self.nama,self.jumlah)

	def __add__(self,objek): #untuk menjumlahkan objek
		return self.jumlah + objek.jumlah 

	@property
	def __dict__(self): #mengubah dictionary default harus ditambah @property diatas
		return "objek ini mempunyai nama dan jumlah"


belanja1 = Mangga("arumanis",10) 
belanja2 = Mangga("mana lagi",30)

# jika tidak menggunakan __repr__ / __str__ 
# akan muncul seperti <__main__.Mangga object at 0x01E47190>
print(belanja1)
print(belanja2)


print(belanja1 + belanja2) # penambahan dari magic __add__
print(belanja1.__dict__)