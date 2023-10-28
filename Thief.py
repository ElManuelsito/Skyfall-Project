from Character import Character

# class Mage(Character):
#     def __init__(self, name):
#         super().__init__(name, health, armor, str, agi, int, faith,
#                  acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on)


class Thief(Character):
    def __init__(self,name):
        super().__init__(name,health=150,armor=20,str=18,agi=20,int=0,faith=5,acc=10,res_magic=8,res_phys=10,money=0,lvl=0,exp=0,armor_items_on=0,weapon_items_on=0)

    def skill_a(self):
        pass #Sigilo

    def skill_b(self):
        pass #Robar item

    def skill_c(self):
        pass #Ataque rapido


player = Thief("Rogue.sk")
player.skill_c()