import Constants
from Character import Character


class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, max_health=100, armor=9, mana=55, max_mana=55, str=7, agi=5, int=40, faith=0, acc=20, res_magic=7,
                         res_phys=9, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self):  # Invoacion de NO-MUERTO
        return True

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACK_NEC

    def getSpecialAttackDescription(self):
        return Constants.SPECIAL_ATTACK_DESC_NEC
