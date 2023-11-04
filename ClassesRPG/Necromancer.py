from Character import Character

# class Necromancer(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, armor=9, mana=55, str=7, agi=5, int=40, faith=0, acc=20, res_magic=7,
                         res_phys=9, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def skill_a(self):
        pass #Invocacion de no muertos. 

    def skill_b(self):
        pass #Magia Dark  
        
    def getCommonAttackOptions(self):
        return Constants.COMMON_ATTACKS_NEC

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACKS_NEC

    def getSpecialAttackDescription(self, option):
        if option == 1:
            return Constants.SPECIAL_ATTACK_A_DESC_NEC
        elif option == 2:
            return Constants.SPECIAL_ATTACK_B_DESC_NEC
        elif option == 3:
            return Constants.SPECIAL_ATTACK_C_DESC_NEC
