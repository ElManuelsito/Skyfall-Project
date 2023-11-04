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

global player_info


class GameManager:
    def __init__(self):
        pass

    def initializeGame(self):
        self.showMessage(Constants.WELCOMING_MESSAGE)
        self.showMessage(Constants.MAIN_MENU_OPTIONS)
        player_main_menu_choice = self.getPlayerChoice()
        if player_main_menu_choice == "1":
            self.createCharacter()

    def createCharacter(self):
        # método que es llamado al elegir "nuevo juego" en el menu principal
        # el usuario podrá crear su personaje y elegir su spawnpoint
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_NAME_MESSAGE)
        while True:
            # while para prevenir que el usuario ingrese un nombre no válido
            player_name = self.getPlayerChoice(Constants.PLAYER_PROMPT_NAME)
            if player_name.isalpha():
                break
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_NAME)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_CLASS_MESSAGE)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        while True:
            # while principal para prevenir que el usuario ingrese una clase o carácter no válido/a
            player_class_choice = self.getPlayerChoice()
            # se le asigna a una variable porque si no estaría preguntando "Opción: " una y otra vez en cada elif
            if player_class_choice == "1":      # Opción 1 corresponde a Arquero
                # Cl_Archer se refiere al módulo y .Archer a la clase. Esto aplica para los otros player_class_choice.
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_ARCHER,
                                                                Cl_Archer.Archer(player_name))
                # si el usuario ingresó si, entonces variable player existe y es instancia. De lo contrario será None.
                if player:
                    # este chequeo no es función, ya que no hay forma de retornar un break o continue
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "2":    # Opción 2 corresponde a Mago
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_WIZARD,
                                                                Cl_Wizard.Wizard(player_name))
                if player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "3":    # Opción 3 corresponde a Guerrero
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_WARRIOR,
                                                                Cl_Warrior.Warrior(player_name))
                if player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "4":    # Opción 4 corresponde a Ladrón
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_THIEF,
                                                                Cl_Thief.Thief(player_name))
                if player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "5":    # Opción 5 corresponde a Hechicero
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_SORCERER,
                                                                Cl_Sorcerer.Sorcerer(player_name))
                if player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "6":    # Opción 6 corresponde a Paladin
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_PALADIN,
                                                                Cl_Paladin.Paladin(player_name))
                if player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "7":    # Opción 7 corresponde a Nigromante
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_NECROMANCER,
                                                                Cl_Necro.Necromancer(player_name))
                if player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "8":    # Opción 8 corresponde a Tanque
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_TANK,
                                                                Cl_Tank.Tank(player_name))
                if player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "9":    # Opción 9 corresponde a Bardo
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_BARD,
                                                                Cl_Bard.Bard(player_name))
                if player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_CLASS)
        del player_class_choice
        del player_name
        # se eliminan de memoria las variables que ya no harán falta por el resto de la ejecución del juego
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_WORLD_MESSAGE)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_WORLD_SPAWNPOINTS)
        while True:
            player_spawnpoint_choice = self.getPlayerChoice()
            if player_spawnpoint_choice == "1":     # Opción 1 Corresponde a Muldraugh
                player_spawnpoint_choice = "muldraugh"
                break
            elif player_spawnpoint_choice == "2":   # Opción 2 corresponde a Riverside
                player_spawnpoint_choice = "riverside"
                break
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_SPAWNPOINT_CHOICE)



    def battle(self, enemy):
        pass

    def confirmPlayerClassChoiceAndAssign(self, class_description, class_type_with_player_name_as_argument):
        #
        # Método verifica que el usuario elige a la clase descrita, asegurando una respuesta esperada ("si" o "no")
        # <constante de descripción de la clase correspondiente a player_class_choice> pasada como primer argumento,
        # por ejemplo la constante Constantes.CHARACTER_DESCRIPTION_ARCHER
        #
        # Método devuelve la clase a asignar a la variable <player> (fuera de este método) si el usuario elige "si"
        # (la clase a asignar es pasada como segundo argumento, debe ser paquete.módulo(<variable del nombre
        # del jugador>) donde esa <variable del nombre> es pasada como argumento para el constructor de la clase
        # que se requiera, por ejemplo Archer.Archer(player_name)
        # También se puede decir que este método devuelve el segundo argumento para instanciar dicho argumento (clase)
        #
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(class_description)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_CLASS_CONFIRM)
        while True:
            # while para prevenir que usuario escriba otra cosa que no sea "si" o "no" cuando confirma su clase
            player_class_choice_confirmation = self.getPlayerChoice()
            if player_class_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_YES:
                return class_type_with_player_name_as_argument
            elif player_class_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_NO:
                return None
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)

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

    def showMessage(self, message):
        # Mostrará por pantalla la cadena pasada como argumento
        return print(message)

    def showWarning(self, message):
        self.showMessage("\n"+message)
        self.waitSeconds(Constants.TIME_BETWEEN_WARNINGS)
        up = '\033[1A'
        clear = '\x1b[2K'
        print(up, end=clear)
        print(up, end=clear)
        return print(up, end=clear)

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
