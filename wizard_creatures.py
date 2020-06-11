import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level: {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12)*self.level


class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self, creature):
        print("The wizard {} attacks {}!\n".format(self.name, creature.name))

        my_roll = random.randint(1, 12)*self.level
        creature_roll = creature.get_defensive_roll()

        print("You rolled {}....".format(my_roll))
        print("{} rolled {}....\n".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard {} has defeated {}.\n".format(self.name, creature.name))
            return True
        else:
            print("Wizard {} has been DEFEATED.\n".format(self.name))
            return False


class SmallCreature(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll*fire_modifier*scale_modifier
