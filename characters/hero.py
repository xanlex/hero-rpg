#Hero class
import random
from sys import path
path += 'Users/alsu/Documents/code/DC2017/py/hero-rpg'
from base import Base

class Hero(Base):
        def __init__(self):
            super().__init__(self)

        def attack_multiplier(self):
            if random.randint(1,5) == 2:
                return 2
            else:
                return 1 
        def attack(self, defender):
            return Base.attack(self) * self.attack_multiplier()
                
        atk =  int(self.power + self.skill ** self.luck)
        dfnse = defender.defense() - atk
        if dfnse < 0:
            return defender.health - dfnse
        def __str__(self):
            return str([self.name,
            self.power,
            self.health,
            self.dexterity,
            self.armor,
            self.skill,
            self.bounty,
            self.luck,
            # self.attack(),
            self.defense(),
            self.alive()
            ])

a = Hero( "name")
# print ( a.name,
#         a.power,
#         a.health,
#         a.dexterity,
#         a.armor,
#         a.skill,
#         a.bounty,
#         a.luck,
#         a.attack(),
#         a.defense(),
#         a.alive())

for i in list(range(1,10)):
    if a.attack_multiplier() ==  2:
        print ("\n\n",i, a, a.attack_multiplier(), "\t", a.attack())
        break