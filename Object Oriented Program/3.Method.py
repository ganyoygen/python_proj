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

    # void function / method tanpa return tanpa argument
    def siapa(self):
        print("Namaku adalah", self.name)

    # method dengan argument tanpa return
    def heatlUp(self,up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("sniper",100,10,4) # object / instansce (instansiate)
print(Hero.jumlah)
hero2 = Hero("mirana",100,8,4)
print(Hero.jumlah)
hero3 = Hero("sven",150,7,10)
print(Hero.jumlah)

hero1.siapa()
print(hero1.health)
hero1.heatlUp(15)
print(hero1.getHealth())

