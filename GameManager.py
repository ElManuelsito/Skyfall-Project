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
        player_main_menu_choice = self.getPlayerChoice()
        if player_main_menu_choice == "1":
            self.createCharacter()

    def createCharacter(self):
        # metodo que ocurre al elegir "nuevo juego" en el menu principal, ayuda al usuario a crear su clase y spawnpoint
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showOnScreen(Constants.CHARACTER_CREATION_NAME_MESSAGE)
        while True:
            # while para prevenir que el usuario ingrese un nombre no valido
            player_name = self.getPlayerChoice(Constants.PLAYER_PROMPT_NAME)
            if player_name.isalpha():
                break
            else:
                self.showOnScreen(Constants.CHARACTER_CREATION_INVALID_NAME)
                self.waitSeconds(Constants.TIME_BETWEEN_WARNINGS)
                self.showOnScreen(Constants.CHARACTER_CREATION_NAME_MESSAGE_INSIST)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_MESSAGE)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        while True:
            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
            # while principal para prevenir que el usuario ingrese una clase o caracter no valido/a
            self.showOnScreen(Constants.CHARACTER_CREATION_ALL_CLASSES)
            player_class_choice = self.getPlayerChoice()
            # se le asigna a una variable porque sino estaria preguntando "Opcion: " una y otra vez en cada elif
            if player_class_choice == "1":      # Opcion 1 corresponde a Arquero
                # Cl_Archer se refiere al modulo y .Archer a la clase. Esto aplica para los otros player_class_choice.
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_ARCHER,
                                                                Cl_Archer.Archer(player_name))
                # si el usuario ingresó si, entonces variable player existe y es instancia. De lo contrario será None.
                if player:
                    # este chequeo no es funcion ya que no hay forma de retornar un break o continue
                    break
                else:
                    continue
            elif player_class_choice == "2":    # Opcion 2 corresponde a Mago
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_WIZARD,
                                                                Cl_Wizard.Wizard(player_name))
                if player:
                    break
                else:
                    continue
            elif player_class_choice == "3":    # Opcion 3 corresponde a Guerrero
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_WARRIOR,
                                                                Cl_Warrior.Warrior(player_name))
                if player:
                    break
                else:
                    continue
            elif player_class_choice == "4":    # Opcion 4 corresponde a Ladron
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_THIEF,
                                                                Cl_Thief.Thief(player_name))
                if player:
                    break
                else:
                    continue
            elif player_class_choice == "5":    # Opcion 5 corresponde a Hechizero
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_SORCERER,
                                                                Cl_Sorcerer.Sorcerer(player_name))
                if player:
                    break
                else:
                    continue
            elif player_class_choice == "6":    # Opcion 6 corresponde a Paladin
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_PALADIN,
                                                                Cl_Paladin.Paladin(player_name))
                if player:
                    break
                else:
                    continue
            elif player_class_choice == "7":    # Opcion 7 corresponde a Nigromante
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_NECROMANCER,
                                                                Cl_Necro.Necromancer(player_name))
                if player:
                    break
                else:
                    continue
            elif player_class_choice == "8":    # Opcion 8 corresponde a Tanque
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_TANK,
                                                                Cl_Tank.Tank(player_name))
                if player:
                    break
                else:
                    continue
            elif player_class_choice == "9":    # Opcion 9 corresponde a Bardo
                player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_BARD,
                                                                Cl_Bard.Bard(player_name))
                if player:
                    break
                else:
                    continue
            else:
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.showOnScreen(Constants.CHARACTER_CREATION_INVALID_CLASS)
                self.waitSeconds(Constants.TIME_BETWEEN_WARNINGS)
                self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_MESSAGE_INSIST)
        del player_class_choice
        del player_name
        # se eliminan de la memoria las variables que ya no haran falta por el resto de la ejecucion del juego
        # faltaria aca abajo empezar a escribir la parte de seleccion del spawnpoint

    def battle(self, enemy):
        pass

    def confirmPlayerClassChoiceAndAssign(self, class_description, class_type_with_player_name_as_argument):
        #
        # Metodo verifica que el usuario elige a la clase descripta, asegurando una respuesta esperada ("si" o "no")
        # <constante de descripcion de la clase correspondiente a player_class_choice> pasada como primer argumento,
        # por ejemplo la constante Constantes.CHARACTER_DESCRIPTION_ARCHER
        #
        # Metodo devuelve la clase a asignar a la variable <player> (fuera de este método) si el usuario elige "si"
        # (la clase a asignar es pasada como segundo argumento, debe ser paquete.modulo(<variable del nombre
        # del jugador>) donde esa <variable del nombre> es pasada como argumento para el constructor de la clase
        # que se requiera, por ejemplo Archer.Archer(player_name)
        # Tambien se puede decir que este metodo devuelve el segundo argumento para instanciar dicho argumento (clase)
        #
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showOnScreen(class_description)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        while True:
            # while para prevenir que usuario escriba otra cosa que no sea "si" o "no" cuando confirma su clase
            self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_CONFIRM)
            player_class_choice_confirmation = self.getPlayerChoice()
            if player_class_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_YES:
                return class_type_with_player_name_as_argument
            elif player_class_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_NO:
                return None
            else:
                self.showOnScreen(Constants.CHARACTER_CREATION_CLASS_INVALID_CONFIRM)
                self.waitSeconds(Constants.TIME_BETWEEN_WARNINGS)

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
