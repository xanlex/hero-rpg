import os, sys
sys.path += 'Users/alsu/Documents/code/DC2017/py/hero-rpg'
from base import Base

class Hero(Base):
    # def __init__(self):
    #     super().__init__(self)
    pass

a = Hero( "name")
print ( a.name,
        a.power,
        a.health,
        a.dexterity,
        a.armor,
        a.skill,
        a.bounty,
        a.luck,
        a.attack(),
        a.defense(),
        a.alive())

print ("\n\n\n\n",a)