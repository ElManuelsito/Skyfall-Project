import ClassesRPG.Archer as Cl_Archer
import ClassesRPG.Tank as Cl_Tank
import ClassesRPG.Wizard as Cl_Wizard
import ClassesRPG.Thief as Cl_Thief
import ClassesRPG.Bard as Cl_Bard
import ClassesRPG.Necromancer as Cl_Necro
import ClassesRPG.Paladin as Cl_Paladin
import ClassesRPG.Sorcerer as Cl_Sorcerer
import ClassesRPG.Warrior as Cl_Warrior
import random
import Constants


class Enemy:
    def __init__(self, name="Enemigo", health=100, dmg=20):
        self.name = name
        self.health = health
        self.dmg = dmg

    def attack(self, player):
        player.takeDamage(self)

    def takeDamageFromPlayerCommon(self, player_classobj, player_info_dict):
        if type(player_classobj) is Cl_Archer.Archer:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.acc, player_info_dict, 200)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Bard.Bard:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.int, player_info_dict, 150)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Necro.Necromancer:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.int, player_info_dict, 200)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Paladin.Paladin:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.str, player_info_dict, 150)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Sorcerer.Sorcerer:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.int, player_info_dict, 200)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Tank.Tank:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.str, player_info_dict, 200)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Thief.Thief:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.str, player_info_dict, 150)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Warrior.Warrior:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.str, player_info_dict, 200)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Wizard.Wizard:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.int, player_info_dict, 180)
            if self.health <= 0:
                return self.isDead()

    def takeDamageFromPlayerSpecial(self, player_classobj, player_info_dict):
        if type(player_classobj) is Cl_Archer.Archer:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.acc, player_info_dict, 200, True)
            player_classobj.mana = player_classobj.mana - 10
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Bard.Bard:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.int, player_info_dict, 150, True)
            player_classobj.mana = player_classobj.mana - 10
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Necro.Necromancer:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.int, player_info_dict, 200, True)
            player_classobj.mana = player_classobj.mana - 25
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Paladin.Paladin:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.str, player_info_dict, 150, True)
            player_classobj.mana = player_classobj.mana - 5
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Sorcerer.Sorcerer:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.int, player_info_dict, 200, True)
            player_classobj.mana = player_classobj.mana - 15
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Tank.Tank:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.str, player_info_dict, 200, True)
            player_classobj.mana = player_classobj.mana - 15
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Thief.Thief:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.agi, player_info_dict, 150, True)
            player_classobj.mana = player_classobj.mana - 10
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Warrior.Warrior:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.str, player_info_dict, 200, True)
            player_classobj.mana = player_classobj.mana - 5
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Wizard.Wizard:
            self.health = self.calculateHealthAfterPlayerAttack(player_classobj, player_classobj.int, player_info_dict, 180, True)
            player_classobj.mana = player_classobj.mana - 25
            if self.health <= 0:
                return self.isDead()

    def calculateHealthAfterPlayerAttack(self, player_classobj, stat, player_info_dict, stat_bonus_divider, special=False):
        if not special:
            if random.random() < ((70 + ((70 * player_classobj.acc) / 100)) / 100):
                final_health = self.health - (player_info_dict["weapon_1"].dmg + ((player_info_dict["weapon_1"].dmg * stat) / stat_bonus_divider))
                final_health = float(f"{final_health:.2f}")
                return final_health
            else:
                print(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)
                return self.health
        else:
            if random.random() < ((70 + ((70 * player_classobj.acc) / 100)) / 100):
                final_health = self.health - ((player_info_dict["weapon_1"].dmg + ((player_info_dict["weapon_1"].dmg * stat) / stat_bonus_divider)) * 2)
                final_health = float(f"{final_health:.2f}")
                return final_health
            else:
                print(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)
                return self.health

    def isDead(self):
        return True
