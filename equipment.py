class Equipment:
    def __init__(self, equip_name, bonus_hp, bonus_strength, bonus_intelligence):
        self.equip_name = equip_name
        self.bonus_hp = bonus_hp
        self.bonus_intelligence = bonus_intelligence
        self.bonus_strength = bonus_strength

    def getName(self):
        return self.equip_name

    def getBonus_hp(self):
        return self.bonus_hp

    def getBonus_intelligence(self):
        return self.bonus_intelligence

    # .... etc. to be finished




