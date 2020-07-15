# #clear screen
import os
os.system("cls")

class Hero:
    jumlah = 0 # class variable
    
    def __init__(self, name, health):
        self.name = name
        self.health = health

        # instance variable private
        self.__test = "priv" # setelah titik (.) tambahkan __

lina = Hero('Lina',100)
print(lina.__dict__)
print(lina.__test)
lina.__test = "test"
print(lina.__dict__)
print(lina.__test)

