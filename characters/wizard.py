#Wizard Class

import random
from sys import path
path += 'Users/alsu/Documents/code/DC2017/py/hero-rpg'
from .base import Base

class Wizard(Base):
    def __init__(self, name = '<Wizard>'):  
        super().__init__(name)
    
    def power_chance(self):
        if random.randint(1,5) == 2:
            return 2
        else:
            return 0

    