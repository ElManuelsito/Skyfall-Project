import Constants
from Character import Character


class Bard(Character):
    def __init__(self, name):
        super().__init__(name, health=80, armor=10, mana=40, str=5, agi=6, int=30, faith=15, acc=13, res_magic=6,
                         res_phys=4, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self, enemy):  # Inspiración
        enemy.takeDamageFromPlayerSpecial(self)

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACK_BARD

    def getSpecialAttackDescription(self):
        return Constants.SPECIAL_ATTACK_DESC_BARD

