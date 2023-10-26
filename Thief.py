from Character import Character

# class Mage(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Thief(Character):
    def __init__(self,name):
        super().__init__(name,150,20,18,20,0,5,10,8,10,0,0,0,0,0)

    def skill_a(self):
        pass #Sigilo

    def skill_b(self):
        pass #Robar item

    def skill_c(self):
        pass #Ataque rapido


player = Thief("Rogue.sk")
player.skill_c()
