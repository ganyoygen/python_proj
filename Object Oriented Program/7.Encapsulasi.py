# #clear screen
import os
os.system("cls")

class Hero:
    def __init__(self,name,health,atkpw):
        # encapsulasi membuat nilai attribute agar tidak bisa dirubah dari luar class
        # dibutuhkan getter dan setter
        self.__name = name
        self.__health = health
        self.__atkpw = atkpw

    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health

    # setter
    def diserang(self,atkpw):
        self.__health -= atkpw

    
# awal dari game
earthshaker = Hero("Earthshaker",10,5)

# print(earthshaker.__name)
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(7)
print(earthshaker.getHealth())