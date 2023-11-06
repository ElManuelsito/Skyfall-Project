import Constants
from Character import Character


class Thief(Character):
    def __init__(self, name):
        super().__init__(name,health=150,armor=20, mana=30, str=18, agi=24, int=0, faith=5, acc=10, res_magic=8,
                         res_phys=10, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self, enemy):  # Golpe Bajo
        enemy.takeDamageFromPlayerSpecial(self)

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACK_THIEF

    def getSpecialAttackDescription(self):
        return Constants.SPECIAL_ATTACK_DESC_THIE
