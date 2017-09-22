from sys import path
path += 'Users/alsu/Documents/code/DC2017/py/hero-rpg/'
from characters import medic, hero, shadow

medic1 = medic.Medic(name = 'Mary')
medic1.health = 2
print (medic1)
for i in list(range(1,10)):
    if medic1.recuperate_chance() ==  2:
        print ("\n\n",i, medic1, "\t", medic1.MAX_HEALTH, 
                medic1.defense())
        break
shadow1 = shadow.Shadow(name = 'Swifty')

hero1 = hero.Hero(name = 'Arthur')
for a in [hero1, medic1, shadow1]:
        print ("{} is of {}\n{}'s attributes: {}".format(a.name, type(a), a.name, str(
        [
        a.name,
        a.power,
        a.health,
        a.dexterity,
        a.armor,
        a.skill,
        a.bounty,
        a.luck,
        # a.attack(),
        a.defense(),
        a.alive()]
        )))

# for i in list(range(1,10)):
#     if a.attack_multiplier() ==  2:
#         print ("\n\n",i, a, a.attack_multiplier())
#         break