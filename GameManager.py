# cada clase, cada archivo
import ClassesRPG.Archer as Cl_Archer
import ClassesRPG.Tank as Cl_Tank
import ClassesRPG.Wizard as Cl_Wizard
import ClassesRPG.Thief as Cl_Thief
import ClassesRPG.Bard as Cl_Bard
import ClassesRPG.Necromancer as Cl_Necro
import ClassesRPG.Paladin as Cl_Paladin
import ClassesRPG.Sorcerer as Cl_Sorcerer
import ClassesRPG.Warrior as Cl_Warrior
import Item
import Constants
import pickle
import time
import random


class GameManager:
    def __init__(self):
        pass

    def initializeGame(self):
        self.showOnScreen(Constants.WELCOMING_MESSAGE)
        self.showOnScreen(Constants.MAIN_MENU_OPTIONS)
        if self.getPlayerChoice() == "1":
            self.createCharacter()

    def createCharacter(self):
        # metodo que ocurre al elegir "nuevo juego" en el menu principal, ayuda al usuario a crear su clase y spawnpoint
        self.showOnScreen(Constants.CHARACTER_CREATION_NAME_MESSAGE)
        while True:
            # while para prevenir que el usuario ingrese un nombre no valido
            player_name = self.getPlayerChoice(Constants.PLAYER_PROMPT_NAME)
            if player_name.isalpha():
                break
            else:
                self.showOnScreen(Constants.CHARACTER_CREATION_INVALID_NAME)
                self.showOnScreen(Constants.CHARACTER_CREATION_NAME_MESSAGE_INSIST)
        self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_MESSAGE)
        while True:
            # while principal para prevenir que el usuario ingrese una clase o caracter no valido/a
            self.showOnScreen(Constants.CHARACTER_CREATION_ALL_CLASSES)
            player_class_choice = self.getPlayerChoice()
            # se le asigna a una variable porque sino estaria preguntando "Opcion: " una y otra vez en cada elif
            if player_class_choice == "1":      # Opcion 1 es Arquero
                # Cl_Archer se refiere al modulo y .Archer a la clase. Esto aplica para los otros elif.
                self.showOnScreen(Constants.CHARACTER_CREATION_DESCRIPTION_ARCHER)
                while True:
                    # while para prevenir que usuario escriba otra cosa que no sea "si" o "no" para confirmar su clase
                    self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_CONFIRM)
                    player_class_choice_confirm = self.getPlayerChoice()
                    if player_class_choice_confirm in Constants.PLAYER_PROMPT_SET_FOR_YES:
                        player = Cl_Archer.Archer(player_name)
                        player_class_was_created = True
                        break
                    elif player_class_choice_confirm in Constants.PLAYER_PROMPT_SET_FOR_NO:
                        player_class_was_created = False
                        break
                    else:
                        self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_INVALID_CONFIRM)
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                if player_class_was_created:
                    # si el usuario elige esta clase, se rompe el while principal y se pasa a la seccion de spawnpoint
                    break
                else:
                    # si usuario no elige esta clase, continua el while principal y le muestra las clases para que elija
                    self.showOnScreen(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "2":    # Opcion 2 es Mago
                self.showOnScreen(Constants.CHARACTER_CREATION_DESCRIPTION_WIZARD)
                while True:
                    self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_CONFIRM)
                    player_class_choice_confirm = self.getPlayerChoice()
                    if player_class_choice_confirm in Constants.PLAYER_PROMPT_SET_FOR_YES:
                        player = Cl_Archer.Archer(player_name)
                        player_class_was_created = True
                        break
                    elif player_class_choice_confirm in Constants.PLAYER_PROMPT_SET_FOR_NO:
                        player_class_was_created = False
                        break
                    else:
                        self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_INVALID_CONFIRM)
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                if player_class_was_created:
                    break
                else:
                    self.showOnScreen(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "3":    # Opcion 3 es Guerrero
                player = Cl_Warrior.Warrior(player_name)
                break
            elif player_class_choice == "4":    # Opcion 4 es Ladron
                player = Cl_Thief.Thief(player_name)
                break
            elif player_class_choice == "5":    # Opcion 5 es Invocador
                player = Cl_Sorcerer.Sorcerer(player_name)
                break
            elif player_class_choice == "6":    # Opcion 6 es Paladin
                player = Cl_Paladin.Paladin(player_name)
                break
            elif player_class_choice == "7":    # Opcion 7 es Nigromante
                player = Cl_Necro.Necromancer(player_name)
                break
            elif player_class_choice == "8":    # Opcion 8 es Tanque
                player = Cl_Tank.Tank(player_name)
                break
            elif player_class_choice == "9":    # Opcion 9 es Bardo
                player = Cl_Bard.Bard(player_name)
                break
            elif player_class_choice.isalnum() is False:
                self.showOnScreen(Constants.CHARACTER_CREATION_INVALID_CLASS)
                self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_MESSAGE_INSIST)
                self.showOnScreen(Constants.CHARACTER_CREATION_ALL_CLASSES)
            else:
                self.showOnScreen(Constants.CHARACTER_CREATION_INVALID_CLASS)
                self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_MESSAGE_INSIST)
                self.showOnScreen(Constants.CHARACTER_CREATION_ALL_CLASSES)

        del player_class_choice
        del player_class_choice_confirm
        del player_class_was_created
        del player_name

    def battle(self, enemy):
        pass

    def calculateChance(self, chance):
        # Devolverá un valor booleano, random.random() devuelve un flotante cualquiera
        # Por ej. 0.619374830802 el cual es menor (<) a 0.80 (es decir 80/100)
        if random.random() < (chance / 100):
            return True
        else:
            return False

    def getPlayerChoice(self, prompt=Constants.PLAYER_PROMPT_OPTION):
        # por defecto hará input("Opción: "), ingresar argumento para cambiar el mensaje
        if prompt is Constants.PLAYER_PROMPT_OPTION:
            return input(prompt)
        else:
            return input(prompt)

    def showOnScreen(self, message):
        # Mostrará por pantalla la cadena pasada como argumento
        return print(message)

    def waitSeconds(self, seconds):
        time.sleep(seconds)
        return None

    def waitForButtonPress(self):
        input(Constants.PRESS_ENTER_TO_CONTINUE)
        return None


# Testeando
# print(Constants.player_inv["weapon_r"])
# Constants.player_inv["weapon_r"] = "Espada de Tenshi"

# manager = GameManager()
# manager.waitForButtonPress()
# print(Constants.COMBAT_OPTIONS)
