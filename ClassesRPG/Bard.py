from Character import Character

# class Bard(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Bard(Character):
    def __init__(self, name):
        super().__init__(name, health=80, armor=10, mana=40, str=5, agi=6, int=30, faith=15, acc=13, res_magic=6,
                         res_phys=4, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def skill_a(self):
        pass #Helear

    def skill_b(self):
        pass #provoca un debuff de veneno al enemigo.

    def skill_c(self):
        pass #Ispiracion de valentia(provoca un aumento de vida)

    def getCommonAttackOptions(self):
        return Constants.COMMON_ATTACKS_BARD

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACKS_BARD

    def getSpecialAttackDescription(self, option):
        if option == 1:
            return Constants.SPECIAL_ATTACK_A_DESC_BARD
        elif option == 2:
            return Constants.SPECIAL_ATTACK_B_DESC_BARD
        elif option == 3:
            return Constants.SPECIAL_ATTACK_C_DESC_BARD

