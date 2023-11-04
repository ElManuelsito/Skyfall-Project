from Character import Character

# class Paladin(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=200, armor=40, mana=25, str=10, agi=4, int=20, faith=11, acc=8, res_magic=10,
                         res_phys=10, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def skill_a(self):
        pass #Helear de un 10% de su vida faltante

    def skill_b(self):
        pass #Proteccion divina

    def skill_c(self):
        pass #Desacer debuff 
        
    def getCommonAttackOptions(self):
        return Constants.COMMON_ATTACKS_PAL

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACKS_PAL

    def getSpecialAttackDescription(self, option):
        if option == 1:
            return Constants.SPECIAL_ATTACK_A_DESC_PAL
        elif option == 2:
            return Constants.SPECIAL_ATTACK_B_DESC_PAL
        elif option == 3:
            return Constants.SPECIAL_ATTACK_C_DESC_PAL

