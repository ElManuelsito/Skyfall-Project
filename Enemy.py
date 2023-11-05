import ClassesRPG.Archer as Cl_Archer
import ClassesRPG.Tank as Cl_Tank
import ClassesRPG.Wizard as Cl_Wizard
import ClassesRPG.Thief as Cl_Thief
import ClassesRPG.Bard as Cl_Bard
import ClassesRPG.Necromancer as Cl_Necro
import ClassesRPG.Paladin as Cl_Paladin
import ClassesRPG.Sorcerer as Cl_Sorcerer
import ClassesRPG.Warrior as Cl_Warrior
from Skyfall import Manager


class Enemy:
    def __init__(self, name, health, dmg):
        self.name = name
        self.health = health
        self.dmg = dmg

    def attack(self, player):
        player.takeDamage(self)

    def takeDamageFromPlayerCommon(self, player_classobj):
        if type(player_classobj) is Cl_Archer.Archer:
            self.health = Manager.calculateEnemyHealthAfterPlayerAttack(player_classobj.acc, self.health, 200)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Bard.Bard:
            self.health = Manager.calculateEnemyHealthAfterPlayerAttack(player_classobj.acc, self.health, 150)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Necro.Necromancer:
            self.health = Manager.calculateEnemyHealthAfterPlayerAttack(player_classobj.acc, self.health, 200)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Paladin.Paladin:
            self.health = Manager.calculateEnemyHealthAfterPlayerAttack(player_classobj.acc, self.health, 150)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Sorcerer.Sorcerer:
            self.health = Manager.calculateEnemyHealthAfterPlayerAttack(player_classobj.acc, self.health, 200)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Tank.Tank:
            self.health = Manager.calculateEnemyHealthAfterPlayerAttack(player_classobj.acc, self.health, 200)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Thief.Thief:
            self.health = Manager.calculateEnemyHealthAfterPlayerAttack(player_classobj.acc, self.health, 150)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Warrior.Warrior:
            self.health = Manager.calculateEnemyHealthAfterPlayerAttack(player_classobj.acc, self.health, 200)
            if self.health <= 0:
                return self.isDead()
        elif type(player_classobj) is Cl_Wizard.Wizard:
            self.health = Manager.calculateEnemyHealthAfterPlayerAttack(player_classobj.acc, self.health, 180)
            if self.health <= 0:
                return self.isDead()

    def takeDamageFromPlayerSpecial(self, player_classobj):
        if type(player_classobj) is Cl_Archer.Archer:
            # final_healt =  calculateEnemeyHealht()? u otro metodo?
            pass

    def isDead(self):
        return True
