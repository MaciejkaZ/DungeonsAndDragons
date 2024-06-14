from characterABC import CharacterABC
from random import random

class Mage(CharacterABC):

    def __init__(self, name, hp, strength, intelligence, damage):
        super().__init__(name, hp, strength, intelligence)
        self.damage = damage

    def attack(self):
        damage = 3 * self.intelligence
        if random() < 0.2:
            damage = 2 * 3 * self.intelligence
            print("Critical hit!")
        return damage

    def defend(self, damage):
        damage = damage - self.intelligence
        if damage > 0:
            hp = self.hp - damage
            if hp >= 0:
                self.hp = hp
            else:
                self.hp = 0
        else:
            return

    def specialAbility(self):
        self.intelligence += 5
        print(f"Special ability +5 power applied to {self.name}!")
