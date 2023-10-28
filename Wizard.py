from Character import Character

# class Wizard(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Wizard(Character):
    def __init__(self,name):
        super().__init__(name, health=100, armor=15, str=10, agi=6, int=30, faith=6, acc=15, res_magic=6,
                         res_phys=4, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def skill_a(self):
        pass #bola de fuego

    def skill_b(self):
        pass #Rayo


player = Wizard("Roge.2000")
player.skill_a()

