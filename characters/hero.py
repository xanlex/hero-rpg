#Hero class
import random
from sys import path
path += 'Users/alsu/Documents/code/DC2017/py/hero-rpg', 'Users/alsu/Documents/code/DC2017/py/hero-rpg/characters/'
from .base import Base

class Hero(Base):
        def __init__(self, name = '<Hero>'):
            super().__init__(name)

        def attack_multiplier(self):
            if random.randint(1,5) == 2:
                return 2
            else:
                return 1 
        def attack(self, defender):
            s_atk = self.attack * self.attack_multiplier()
            atk =  int(s_atk + self.skill ** self.luck)
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

