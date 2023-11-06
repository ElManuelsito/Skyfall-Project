import Constants
from Character import Character


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=200, armor=40, mana=25, str=10, agi=4, int=20, faith=11, acc=8, res_magic=10,
                         res_phys=10, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self, enemy):  # Sentencia
        enemy.takeDamageFromPlayerSpecial(self)

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACK_PAL

    def getSpecialAttackDescription(self):
        return Constants.SPECIAL_ATTACK_DESC_PAL
