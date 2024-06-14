# This is the main script for the game: Dungeons and Dragons

from warrior import Warrior
from mage import Mage
from monster import Monster
from equipment import Equipment
from random import randint, random
from item import Item


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def printStats(character):
    print("=" * 20)
    print(f"Class: {type(character).__name__}")
    print(f"Name: {character.getName()}")
    print(f'HP: {character.getHp()}')
    print(f'Strength: {character.getStrength()}')
    print(f'Intelligence: {character.getIntelligence()}')
    print(f"Inventory:{character.getInventory()}")
    print("=" * 20)
    #
    #

# defining effects
def power_1(character):
    character.strength -= 1

def power_2(character):
    character.strength += 2


def battle(ch1, ch2):
    turn = randint(1, 2)
    counter = 0
    while ch1.hp > 0 and ch2.hp > 0:

        if turn % 2 == 0:
            #display turn
            counter += 1
            print(f" This is turn {counter}!")

            # attack
            damage = ch1.attack()

            #display damage
            print(f"Attack at {ch2.name} at the level: {damage}")

            #defend
            ch2.defend(damage)

            # display health (hp) of the attacked character
            print(f"{ch2.name}'s health is: {ch2.hp}.")
        else:
            #calc and display turn
            counter += 1
            print(f" This is turn {counter}!")

            # attack
            damage = ch2.attack()
            print(f"Attack at {ch1.name} at the level: {damage}")

            # defend
            ch1.defend(damage)

            # display health (hp) of the attacked character
            print(f"{ch1.name}'s health is: {ch1.hp}.")
        turn += 1
        print(50 * "-")

    if ch1.hp > ch2.hp:
        print(f"The winner is {ch1.name} ")
    else:
        print(f"The winner is {ch2.name} ")


def main():
    # create objects
    w1 = Warrior("Wolf", 15, 3, 2, 0)
    m1 = Mage("Wizard", 15, 1, 3, 0)
    mon1 = Monster("Dracula", 10, 2, 1, 2)

    printStats(w1)
    printStats(m1)
    printStats(mon1)

    i1 = Item("Elixir", power_2)
    i2 = Item("Poison", power_1)

    w1.addItem(i1)
    w1.addItem(i2)

    printStats(w1)
    printStats(m1)
    w1.useItem("Elixir")
    printStats(w1)
    printStats(m1)

    # create equipment
    e1 = Equipment("Fire", 2, 1, 1)
    e2 = Equipment("Magic", 1, 1, 1)

    # calling equipment method
    w1.equip(e1)
    m1.equip(e2)

    if random() < 0.2:
        m1.specialAbility()
    if random() > 0.8:
        w1.specialAbility()

    # display strengths of the characters
    print("\n", 10 * "-", "After the equipment have been added", 10 * "-")
    printStats(w1)
    printStats(m1)

    # add item

    # the battle starts
    print("\n", 20 * "*", "Battle starts!!!", 20 * "*")
    battle(w1, m1)

    # display health (hp) of the characters after the battle
    printStats(w1)
    printStats(m1)

    # display GAME OVER
    print("\n", 20 * "*", "GAME OVER!!!", 20 * "*")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
