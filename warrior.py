from characterABC import CharacterABC
from random import random


class Warrior(CharacterABC):
    def __init__(self, name, hp, strength, intelligence, damage):
        super().__init__(name, hp, strength, intelligence)
        self.damage = damage

    def attack(self):
        damage = 2 * self.getStrength()
        if random() < 0.2:
            damage = 2 * 2 * self.getStrength()
            print("Critical hit!")
        return damage

    def defend(self, damage):
        damage = damage - self.strength
        if damage > 0:
            hp = self.hp - damage
            if hp >= 0:
                self.hp = hp

            else:
                self.hp = 0
        else:
            return

    def specialAbility(self):
        self.strength += 5
        print(f"Special ability +5 power applied to {self.name}!")


