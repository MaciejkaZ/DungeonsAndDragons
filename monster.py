from characterABC import CharacterABC
from math import floor

class Monster(CharacterABC):
    def __init__(self, name, hp, strength, intelligence, level):
        super().__init__(name, hp, strength, intelligence)
        self.level = level

    # getters
    def getLevel(self):
        return self.level

    # setters
    def setLevel(self, level):
        self.level = level

    def attack(self):
        return self.level * self.strength

    def defend(self, damage):
        damage = damage - floor(self.strength/2)
        if damage > 0:
            self.hp = max(self.hp - damage, 0)
        else:
            return

