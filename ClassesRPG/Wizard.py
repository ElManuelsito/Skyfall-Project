import Constants
from Character import Character


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, health=100, armor=15, mana=75, str=10, agi=6, int=30, faith=6, acc=15, res_magic=10,
                         res_phys=3, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self, enemy):  # Bola de fuego
        enemy.takeDamageFromPlayerSpecial(self)

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACK_WIZARD

    def getSpecialAttackDescription(self):
        return Constants.SPECIAL_ATTACK_DESC_WIZ