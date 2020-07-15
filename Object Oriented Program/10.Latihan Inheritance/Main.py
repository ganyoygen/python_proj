from Hero import HeroIntelligent,HeroStrength

# #clear screen
import os
os.system("cls")


lina = HeroIntelligent('lina')
slardar = HeroStrength('slardar')

lina.show_info()
slardar.show_info()

lina.gainExp = 200
slardar.gainExp = 250

lina.show_info()
slardar.show_info()