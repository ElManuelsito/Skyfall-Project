from Character import Character

# class Wizard(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, health=100, armor=15, mana=100, str=10, agi=6, int=30, faith=6, acc=15, res_magic=10,
                         res_phys=3, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def skill_a(self):
        pass #bola de fuego

    def skill_b(self):
        pass #Rayo



