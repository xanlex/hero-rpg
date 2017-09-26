# make a Zombie character that doesn't die even if his health is below zero
from sys import path
path += 'Users/alsu/Documents/code/DC2017/py/hero-rpg'
from .base import Base

class Zombie(Base):
    # pass

    def alive(self):
        return True