# #Medic Class
import random
from sys import path
path += 'Users/alsu/Documents/code/DC2017/py/hero-rpg'
from .base import Base

class Medic(Base):
    def __init__(self, name = '<Medic>'):  
        super().__init__(name)
        self.MAX_HEALTH = self.health
    
    def recuperate_chance(self):
        if random.randint(1,5) == 2:
            return 2
        else:
            return 0

    def defense(self):
        if self.health < self.MAX_HEALTH and self.recuperate_chance() == 2:
            self.health += 2
        return int(self.armor + self.dexterity ** self.luck)

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

