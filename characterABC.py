from abc import ABC, abstractmethod

class CharacterABC(ABC):
    def __init__(self, name, hp, strength, intelligence):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.intelligence = intelligence
        self.inventory = []


    # getters
    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def getStrength(self):
        return self.strength

    def getIntelligence(self):
        return self.intelligence

    def getInventory(self):
        names = [o.name for o in self.inventory]
        return ", ".join(names)

    # setters

    def setName(self, name):
        self.name = name

    def setHp(self, hp):
        self.hp = hp

    def setStrength(self, strength):
        self.strength = strength

    def setIntelligence(self, intelligence):
        self.intelligence = intelligence

    def setInventory(self, item):
        self.inventory.append(item)

    # methods
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self, damage):
        pass

    def equip(self, equipment):
        self.hp += equipment.bonus_hp
        self.strength += equipment.bonus_strength
        self.intelligence += equipment.bonus_intelligence
        print(f"{self.name} uses equipment {equipment}.")

    def addItem(self, item):
        self.inventory.append(item)
        print(f"{self.name} received the equipment: {item.name}")

    def useItem(self, itemName):
        for item in self.inventory:
            if item.name == itemName:
                item.effect(self)
                print(f"{self.getName()} uses {itemName}.")
                self.inventory.remove(item)
                break


        """
        #tried to implement the way so if two equipments are stored , only one is removed - not working
         def useItem(self, itemName):
            done = False
            i=0
            while not done and i in range(len(self.inventory)):
                if self.inventory[i].name == itemName:
                    self.inventory[i].effect()
                    self.inventory.pop(i)
                    done = True
                    i += 1
                    return """
