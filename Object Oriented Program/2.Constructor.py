class Hero: # template
    jumlah = 0 # class variable
    def __init__(self, inputname, inputhealth, inputpower, inputarmor):
        # instance variable
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        Hero.jumlah += 1
        print("Membuat hero dengan nama", inputname)


hero1 = Hero("sniper",100,10,4) # object / instansce (instansiate)
print(Hero.jumlah)
hero2 = Hero("mirana",100,8,4)
print(Hero.jumlah)
hero3 = Hero("sven",150,7,10)
print(Hero.jumlah)


print("Dictionary:\r\n",hero1.__dict__)
print(hero1)
print(hero3.armor)
print(hero1.health)

