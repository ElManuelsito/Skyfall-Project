import ClassesRPG.Archer as Cl_Archer
import ClassesRPG.Tank as Cl_Tank
import ClassesRPG.Wizard as Cl_Wizard
import ClassesRPG.Thief as Cl_Thief
import ClassesRPG.Bard as Cl_Bard
import ClassesRPG.Necromancer as Cl_Necro
import ClassesRPG.Paladin as Cl_Paladin
import ClassesRPG.Sorcerer as Cl_Sorcerer
import ClassesRPG.Warrior as Cl_Warrior
import Constants
from Skyfall import Manager


class Enemy:
    def __init__(self, name, health, dmg):
        self.name = name
        self.health = health
        self.dmg = dmg

    def attack(self, player):
        player.takeDamage(self)

    def takeDamageFromPlayerPrimary(self, player_classobj, player_info_dictobj):
        if type(player_classobj) == Cl_Archer.Archer:
            if Manager.GameManager.calculateChance((70 + ((70 * player_classobj.acc)/100))):
                final_health = self.health - (player_info_dictobj["weapon_1"].dmg + ((player_info_dictobj["weapon_1"] * player_classobj.acc)/200))
                self.health = float(f"{final_health:.2f}")
                if self.health <= 0:
                    return self.isDead()
            else:
                Manager.showCombinedMessage(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)

        elif type(player_classobj)==Cl_Bard.Bard:
            if Manager.GameManager.calculateChance((Constants.BASE_ACC+((Constants.BASE_ACC* player_classobj.acc)/100))):
                final_health = self.health - (player_info_dictobj["weapon_1"].dmg + ((player_info_dictobj["weapon_1"] * player_classobj.int)/150))
                self.health = float(f"{final_health:.2f}")
                if self.health <= 0:
                    return self.isDead()
            else:
                Manager.showCombinedMessage(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)

        elif type(player_classobj)==Cl_Necro.Necromancer:
            if Manager.GameManager.calculateChance((Constants.BASE_ACC+((Constants.BASE_ACC* player_classobj.acc)/100))):
                final_health = self.health - (player_info_dictobj["weapon_1"].dmg + ((player_info_dictobj["weapon_1"] * player_classobj.int)/200))
                self.health = float(f"{final_health:.2f}")
                if self.health <= 0:
                    return self.isDead()
            else:
                Manager.showCombinedMessage(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)

        elif type(player_classobj)==Cl_Paladin.Paladin:
            if Manager.GameManager.calculateChance((Constants.BASE_ACC+((Constants.BASE_ACC* player_classobj.acc)/100))):
                final_health = self.health - (player_info_dictobj["weapon_1"].dmg + ((player_info_dictobj["weapon_1"] * player_classobj.str)/150))
                self.health = float(f"{final_health:.2f}")
                if self.health <= 0:
                    return self.isDead()
            else:
                Manager.showCombinedMessage(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)

        elif type(player_classobj)==Cl_Sorcerer.Sorcerer:
            if Manager.GameManager.calculateChance((Constants.BASE_ACC+((Constants.BASE_ACC* player_classobj.acc)/100))):
                final_health = self.health - (player_info_dictobj["weapon_1"].dmg + ((player_info_dictobj["weapon_1"] * player_classobj.int)/200))
                self.health = float(f"{final_health:.2f}")
                if self.health <= 0:
                    return self.isDead()
            else:
                Manager.showCombinedMessage(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)

        elif type(player_classobj)==Cl_Tank.Tank:
            if Manager.GameManager.calculateChance((Constants.BASE_ACC+((Constants.BASE_ACC* player_classobj.acc)/100))):
                final_health = self.health - (player_info_dictobj["weapon_1"].dmg + ((player_info_dictobj["weapon_1"] * player_classobj.str)/200))
                self.health = float(f"{final_health:.2f}")
                if self.health <= 0:
                    return self.isDead()
            else:
                Manager.showCombinedMessage(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)

        elif type(player_classobj)==Cl_Thief.Thief:
            if Manager.GameManager.calculateChance((Constants.BASE_ACC+((Constants.BASE_ACC* player_classobj.acc)/100))):
                final_health = self.health - (player_info_dictobj["weapon_1"].dmg + ((player_info_dictobj["weapon_1"] * player_classobj.str)/150))
                self.health = float(f"{final_health:.2f}")
                if self.health <= 0:
                    return self.isDead()
            else:
                Manager.showCombinedMessage(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)

        elif type(player_classobj)==Cl_Warrior.Warrior:
            if Manager.GameManager.calculateChance((Constants.BASE_ACC+((Constants.BASE_ACC* player_classobj.acc)/100))):
                final_health = self.health - (player_info_dictobj["weapon_1"].dmg + ((player_info_dictobj["weapon_1"] * player_classobj.str)/200))
                self.health = float(f"{final_health:.2f}")
                if self.health <= 0:
                    return self.isDead()
            else:
                Manager.showCombinedMessage(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)

        elif type(player_classobj)==Cl_Wizard.Wizard:
            if Manager.GameManager.calculateChance((Constants.BASE_ACC+((Constants.BASE_ACC* player_classobj.acc)/100))):
                final_health = self.health - (player_info_dictobj["weapon_1"].dmg + ((player_info_dictobj["weapon_1"] * player_classobj.int)/180))
                self.health = float(f"{final_health:.2f}")
                if self.health <= 0:
                    return self.isDead()
            else:
                Manager.showCombinedMessage(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)
    def takeDamageFromPlayerSpecial(self, player_classobj,player_info_dictobj):
        if type(player_classobj) == Cl_Archer.Archer:
            if Manager.GameManager.calculateChance((Constants.BASE_ACC + ((Constants.BASE_ACC * player_classobj.acc)/100))):
            final_health = self.health - (player_info_dictobj["weapon_1"].dmg + ((player_info_dictobj["weapon_1"] * player_classobj.acc)/200))*2
            self.health=float(f"{final_health:.2f}")
            if self.health <= 0:
                return self.isDead()
            else:
                Manager.showCombinedMessage(player_classobj.name, Constants.SOMEONE_ATTACKS_AND_MISSES)

    def isDead(self):
        return True
