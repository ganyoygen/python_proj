class Hero:
    def __init__(self,name,health,attack,armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def serang(self,musuh):
        print(self.name,"Menyerang",musuh.name)
        musuh.diserang(self, self.attack)

    def diserang(self,musuh,atkmusuh):
        # print(self.name,"Diserang",musuh.name)
        damage = atkmusuh / self.armor
        self.health -= damage
        print("Damage: ", str(damage), self.name, "Health", str(self.health))

     

sniper = Hero('Sniper',10,10,5)
traxex = Hero('Traxex',10,8,7)

print('\r\n')
sniper.serang(traxex)
traxex.serang(sniper)
# print('\r\n')
# sniper.serang(traxex)
# traxex.serang(sniper)
# print('\r\n')
# sniper.serang(traxex)
# traxex.serang(sniper)
# print('\r\n')
# sniper.serang(traxex)
# traxex.serang(sniper)
# print('\r\n')
# sniper.serang(traxex)
# traxex.serang(sniper)
# print('\r\n')
# sniper.serang(traxex)
# traxex.serang(sniper)
# print('\r\n')
# sniper.serang(traxex)
# traxex.serang(sniper)

