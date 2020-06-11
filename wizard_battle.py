import random
import time
from wizard_creatures import Wizard, Creature, SmallCreature, Dragon


def print_header():
    print('--------------------------------')
    print('      Wizard Battle App')
    print('--------------------------------\n')


def game_loop():
    creatures = [
        SmallCreature("Niffler", 1),
        SmallCreature("Pixie", 5),
        SmallCreature("Gnome", 3),
        Creature("Mountain Troll", 20),
        Creature("Hippogriff", 25),
        Creature("Acromantula", 27),
        Creature("Basilisk", 239),
        Creature("Thestral", 42),
        Creature("Dementor", 23),
        Dragon("Hungerian Horntail", 53, 45, True),
        Dragon("Norwegian Ridgeback", 47, 25, True),
        Dragon("Chinese Fireball", 47, 5, True),
        Dragon("Welsh Green", 47, 65, False),
        Wizard("Lord Voldemort", 500),
        Wizard("Bellatrix Lestrange", 150),
        Wizard("Lucius Malfoy", 90),
        Wizard("Salazar Slytherin", 1000),
    ]

    hero = Wizard("Harry", 250)

    playing = True
    while playing:

        active_creature = random.choice(creatures)
        print("{} of level {} has appeared from the forbidden forest...\n".format(active_creature.name,
                                                                                  active_creature.level))

        choice = input("Do you want to [a]ttack, [r]unaway, [l]ook around or e[x]it the game: ").lower().strip()

        if choice == 'a':

            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs hides taking time to recover....")
                input("Press 'F' to revive the wizard: ")
                time.sleep(5)
                print("\nThe wizard returns revitalized!\n")

        elif choice == 'r':
            print("\nThe wizard has become unsure of his powers and flees...\n")
        elif choice == 'l':
            print("\nThe wizard {} takes in the surroundings and sees: ".format(hero.name))
            for creature in creatures:
                print("--> {} of level {}".format(creature.name, creature.level))
            print()
        elif choice == 'x':
            print("Thank you! Hope you had fun playing the game.\n\t\t\tExiting game....")
            playing = False
        else:
            print("Please enter a valid choice.")

        if not creatures:
            print("You defeated all the creatures. Well Done!!!")
            playing = False


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
