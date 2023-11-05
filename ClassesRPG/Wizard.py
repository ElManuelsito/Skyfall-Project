from Character import Character

# class Wizard(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, health=100, armor=15, mana=75, str=10, agi=6, int=30, faith=6, acc=15, res_magic=10,
                         res_phys=3, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self, enemy):
        enemy.takeDamageFromPlayerSpecial(self) #Bola de fuego

    def getSpecialAttack(self):
        return Constants.SPECIAL_ATTACKS_WIZARD

    def getSpecialAttackDescription(self, option):
        if option == 1:
            return Constants.SPECIAL_ATTACK_A_DESC_WIZ