
# Shadow Class
# Make a character called Shadow who 
# has only 1 starting health but will
# only take damage about once out of 
# every ten times he is attacked.
from sys import path
path += 'Users/alsu/Documents/code/DC2017/py/hero-rpg'
from .base import Base
import random

class Shadow(Base):
    def __init__(self, name='<unnamed_shadow>'):
        super().__init__(name)
        self.health = 1

    def shadow_fail(self):
        if random.randint(1,11) == 10:
            return True
        else:
            return False

    def defense(self):
        if self.shadow_fail():
            return int(self.armor + self.dexterity ** self.luck)
        else:
            return int(self.armor + 100 ** 10)
