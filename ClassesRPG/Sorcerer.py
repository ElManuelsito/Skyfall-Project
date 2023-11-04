from Character import Character

# class Sorcerer(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, armor=10, mana=60, str=8, agi=5, int=45, faith=3, acc=20, res_magic=5,
                         res_phys=4, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def skill_a(self):
        pass #Invoca criaturas para atacar 

    def skill_b(self):
        pass #Hace que el enemigo se dañe asi mismo. 

    def getCommonAttackOptions(self):
        return Constants.COMMON_ATTACKS_SORC

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACKS_SORC

    def getSpecialAttackDescription(self, option):
        if option == 1:
            return Constants.SPECIAL_ATTACK_A_DESC_SORC
        elif option == 2:
            return Constants.SPECIAL_ATTACK_B_DESC_SORC
        elif option == 3:
            return Constants.SPECIAL_ATTACK_C_DESC_SORC

