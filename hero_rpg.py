#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Creature:
    def __init__(self, name, power, health, dexterity, armor, skill):
        self.name = name
        self.power = power
        self.health = health
        self.dexterity = dexterity
        self.armor = armor
        self.skill = skill
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def attack(self, target):
        if 'Creature' in isinstance(target):
            target.health = target.health - self.power
class Hero(Creature):
    def __init__(self, name, power, health, dexterity, armor, skill):
        self.hero_power = power
        self.hero_health = health
        super().__init__(name, power, health, dexterity, armor, skill)

class Goblin(Creature):
    def __init__(self, name, power, health ,dexterity, armor, skill):
        self.goblin_power = power
        self.goblin_health = health
        super().__init__(name, power, health, dexterity, armor, skill)


def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    while goblin_health > 0 and hero_health > 0:
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblin_health -= hero_power
            print("You do {} damage to the goblin.".format(hero_power))
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")

main()
