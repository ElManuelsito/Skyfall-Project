import Constants
from Character import Character


class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, max_health=100, armor=10, mana=60, max_mana=60, str=8, agi=5, int=45, faith=3, acc=20, res_magic=5,
                         res_phys=4, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self):  # Magia Control
        return True

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACK_SORC

    def getSpecialAttackDescription(self):
        return Constants.SPECIAL_ATTACK_DESC_SORC

