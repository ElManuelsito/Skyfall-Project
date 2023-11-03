import Constants
from Character import Character
import random

# class Archer(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, armor=20, mana=20, str=10, agi=18, int=7, faith=8, acc=19, res_magic=7,
                         res_phys=5, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def skill_a(self):
        print("usando habilidad a")

    def skill_b(self):
        print("Usando habilidad b")
        
    def skill_c(self):
        print("Usando habilidad c")

    def getCommonAttackOptions(self):
        return Constants.COMMON_ATTACKS_ARCHER

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACKS_ARCHER

    def getSpecialAttackDescription(self, option):
        if option == 1:
            return Constants.SPECIAL_ATTACK_A_DESC
        elif option == 2:
            return Constants.SPECIAL_ATTACK_B_DESC
        elif option == 3:
            return Constants.SPECIAL_ATTACK_C_DESC

