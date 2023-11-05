from Character import Character

# class Tank(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Tank(Character):
    def __init__(self, name):
        super().__init__(name, health=300, armor=60, mana=15, str=15, agi=6, int=4, faith=9, acc=4, res_magic=10,
                         res_phys=15, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self, enemy):
        enemy.takeDamageFromPlayerSpecial(self) #Power Up

    def getSpecialAttack(self):
        return Constants.SPECIAL_ATTACKS_TANK

    def getSpecialAttackDescription(self, option):
        if option == 1:
            return Constants.SPECIAL_ATTACK_A_DESC_TANK