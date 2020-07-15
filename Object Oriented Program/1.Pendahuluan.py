class hero: # template
    pass

hero1 = hero() # object / instansce (instansiate)
hero2 = hero()
hero3 = hero()

hero1.name = "sniper"
hero1.health = 100

hero2.name = "traxex"
hero2.health = 150

hero3.name = "sven"
hero3.health = 200

print(hero1.__dict__)
print(hero1)
print(hero1.name)
print(hero1.health)

