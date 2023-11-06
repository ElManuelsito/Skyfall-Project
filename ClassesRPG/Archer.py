import Constants
from Character import Character

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, max_health=120, armor=20, mana=20, max_mana=20, str=10, agi=18, int=7, faith=8, acc=19, res_magic=7,
                         res_phys=5, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self):  # Lluvia de Flecha
        return True

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACK_ARCHER

    def getSpecialAttackDescription(self):
        return Constants.SPECIAL_ATTACK_DESC_ARCH

