# #clear screen
import os
os.system("cls")

#inheritance dan super (pewarisan)
class Hero:
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def showInfo(self):
		print ("{} dengan health: {}".format(self.name,self.health))

# ini pewarisan class dari Hero
class Hero_intelligent(Hero): 
	def __init__(self,name):
		#Hero.__init__(self, name, 100)
		super().__init__(name, 100) #lebih simpel
		super().showInfo()
class Hero_strength(Hero):
	def __init__(self,name):
		super().__init__(name, 200)
		super().showInfo()


lina = Hero_intelligent('lina')
axe = Hero_strength('axe')