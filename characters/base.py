class Base:
    import random
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
        return (self.health > 0)
    def attack(self):
        return self.power + self.skill ** self.luck
    def defense(self):
        return self.armor + self.dexterity ** self.luck
    def __str__(self):
        return 
        (self.name,
        self.power,
        self.health,
        self.dexterity,
        self.armor,
        self.skill,
        self.bounty,
        self.luck,
        self.attack(),
        self.defense(),
        self.alive())
a = Base('asdf',)
print(a.luck)

