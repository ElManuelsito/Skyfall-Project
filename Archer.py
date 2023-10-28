from Character import Character

# class Archer(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Archer(Character):
    def __init__(self,name):
        super().__init__(name, health=120, armor=20, str=15, agi=18, int=7, faith=8, acc=15, res_magic=7,
                         res_phys=5, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0)

    def skill_a(self):
        pass #Lluvia de flechas

    def skill_b(self):
        pass #Flecha de fuego
        
    def skill_c(self):
        pass #Aumenta precisión


player = Archer("Arrow.x")
player.skill_a()
