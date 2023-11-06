import Constants
from Character import Character

# Para entender qué significa cada número:
#
# class Warrior(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)
#
# la variable "name" se deja como está ya que:
#   player = Warrior("Juan")
# esa linea establecerá el nombre de la clase guerrero sin alterar los otros valores.
# Es más, es el unico argumento posible dentro de Warrior(), cualquier otro argumento es rechazado.
# Por ejemplo, player = Warrior("Juan", 300) se rechaza, lo mismo si el nombre no es un string.


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=275, armor=40, mana=25, str=20, agi=10, int=8, faith=6, acc=6, res_magic=2,
                         res_phys=10, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def attackWithSkillA(self, enemy):  # Multiples Cortes
        enemy.takeDamageFromPlayerSpecial(self)

    def getSpecialAttackOptions(self):
        return Constants.SPECIAL_ATTACK_WARRIOR

    def getSpecialAttackDescription(self):
        return Constants.SPECIAL_ATTACK_DESC_WARR
