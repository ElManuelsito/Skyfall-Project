import Constants
from Character import Character


class Tank(Character):
    def __init__(self, name):
        super().__init__(name, health=300, armor=60, mana=15, str=15, agi=6, int=4, faith=9, acc=4, res_magic=10,
                         res_phys=15, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self, enemy):  # Power Up
        enemy.takeDamageFromPlayerSpecial(self)

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACK_TANK

    def getSpecialAttackDescription(self):
        return Constants.SPECIAL_ATTACK_DESC_TANK
