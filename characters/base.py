import random
class Base(object):
    def __init__(self, name = '<undefined>', power = 5, health = 5, dexterity = 5, 
    armor = 5, skill = 5, bounty = 5,
    luck = random.randrange(-2,3,1)):
        self.name = name
        self.power = power
        self.health = health
        self.dexterity = dexterity
        self.armor = armor
        self.skill = skill 
        self.bounty = bounty
        self.luck = luck # range [-2:2]
    def alive(self):
        return True if (self.health > 0) else False
    def attack(self, defender):
        atk =  int(self.power + self.skill ** self.luck)
        dfnse = defender.defense() - atk
        if dfnse < 0:
            return defender.health - dfnse
    def defense(self):
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


# print("%r", a)