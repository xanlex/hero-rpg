#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Creature:
    def __init__(self, name, power, health, dexterity = 5, armor = 5, skill = 5):
        self.name = name
        self.power = power
        self.health = health
        self.dexterity = dexterity
        self.armor = armor
        self.skill = skill

    def attack(self, target):
        if 'Creature' in isinstance(target):
            target.health = target.health - self.power
class Hero(Creature):
    def __init__(self, name, power, health, dexterity = 5, armor = 5, skill = 5):
        self.hero_power = power
        self.hero_health = health
        super().__init__(name, power, health, dexterity, armor, skill)
    def alive(self):
        if self.hero_health > 0:
            return True
        else:
            return False
class Goblin(Creature):

    def __init__(self, name, power, health ,dexterity = 5, armor = 5, skill = 5):
        self.goblin_power = power
        self.goblin_health = health
        super().__init__(name, power, health, dexterity, armor, skill)
    def alive(self):
        if self.goblin_health > 0:
            return True
        else:
            return False        

def main():
    hero = Hero('Arthur', power=5, health = 10)
    hero.hero_health = 7
    hero.hero_power = 2
    
    goblin = Goblin('Wario', health = 6, power = 2)
    goblin.goblin_health = 6
    goblin.goblin_power = 6

    while goblin.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero.hero_health, hero.hero_power))
        print("The goblin has {} health and {} power.".format( goblin.goblin_health,  goblin.goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblin.goblin_health -= hero.hero_power
            print("You do {} damage to the goblin.".format(hero.hero_power))
            if  goblin.goblin_health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            print ("Goblin's health is {}, \t Your's is {}".format(goblin.goblin_health, hero.hero_health))
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if  goblin.goblin_health > 0:
            # Goblin attacks hero
            hero.hero_health -=  goblin.goblin_power
            print("The goblin does {} damage to you.".format( goblin.goblin_power))
            if hero.hero_health <= 0:
                print("You are dead.")

    

if __name__ == '__main__':
    main()