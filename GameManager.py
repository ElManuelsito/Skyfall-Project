# cada clase, cada archivo
# GameManager, donde se realizan la mayoría de las tareas del juego

import os
import pickle
import random
import time

import ClassesRPG.Archer as Cl_Archer
import ClassesRPG.Bard as Cl_Bard
import ClassesRPG.Necromancer as Cl_Necro
import ClassesRPG.Paladin as Cl_Paladin
import ClassesRPG.Sorcerer as Cl_Sorcerer
import ClassesRPG.Tank as Cl_Tank
import ClassesRPG.Thief as Cl_Thief
import ClassesRPG.Warrior as Cl_Warrior
import ClassesRPG.Wizard as Cl_Wizard
import PointOfInterest as POI
import Constants
import Item


global player_info
global Player


class GameManager:
    def __init__(self):
        pass

    def initializeGame(self):
        global player_info
        global Player
        self.showMessage(Constants.WELCOMING_MESSAGE)
        self.showMessage(Constants.MAIN_MENU_OPTIONS)
        while True:
            player_main_menu_choice = self.getPlayerChoice()
            if player_main_menu_choice == "1":
                if os.path.isfile("savefile.pickle"):
                    if not self.confirmPlayerSaveFileDeletion():
                        return self.initializeGame()
                self.createCharacter()
                self.clearScreen()
                self.showMessage("\n" + Constants.MAIN_MENU_MESSAGE_GAME_LOADING)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.clearScreen()
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.beginGame()
            elif player_main_menu_choice == "2":
                pass # cargar la partida
            elif player_main_menu_choice == "3":
                pass # instrucciones / manual del juego
            elif player_main_menu_choice == "4":
                return None
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_MAIN_MENU_OPTION)

    def beginGame(self):
        if self.checkIfPlayerIsInLocation(POI.Muldraugh):
            self.showMessage(Constants.INTRO_MESSAGE_MULDRAUGH)
        elif self.checkIfPlayerIsInLocation(POI.Riverside):
            self.showMessage(Constants.INTRO_MESSAGE_RIVERSIDE)
        while True:
            self.showCombinedMessage(Constants.WORLD_PLAYER_IS_IN_POI, player_info["location"])
            break

    def getTravelOptions(self):
        pass

    def battle(self, enemy):
        pass

    def createCharacter(self):
        global player_info
        global Player
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
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_ARCHER,
                                                                Cl_Archer.Archer(player_name))
                # si el usuario ingresó si, entonces variable player existe y es instancia. De lo contrario será None.
                if Player:
                    # este chequeo no es función, ya que no hay forma de retornar un break o continue
                    player_info = {"weapon_1": Item.bow_newborn,
                                   "weapon_2": False,
                                   "helmet": False,
                                   "breastplate": False,
                                   "chausses": False,
                                   "gauntlets": False,
                                   "backpack_items": {"weapons": [],
                                                      "potions": [],
                                                      "armors": []},
                                   "location": None}
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "2":    # Opción 2 corresponde a Mago
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_WIZARD,
                                                                Cl_Wizard.Wizard(player_name))
                if Player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "3":    # Opción 3 corresponde a Guerrero
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_WARRIOR,
                                                                Cl_Warrior.Warrior(player_name))
                if Player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "4":    # Opción 4 corresponde a Ladrón
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_THIEF,
                                                                Cl_Thief.Thief(player_name))
                if Player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "5":    # Opción 5 corresponde a Hechicero
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_SORCERER,
                                                                Cl_Sorcerer.Sorcerer(player_name))
                if Player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "6":    # Opción 6 corresponde a Paladin
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_PALADIN,
                                                                Cl_Paladin.Paladin(player_name))
                if Player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "7":    # Opción 7 corresponde a Nigromante
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_NECROMANCER,
                                                                Cl_Necro.Necromancer(player_name))
                if Player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "8":    # Opción 8 corresponde a Tanque
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_TANK,
                                                                Cl_Tank.Tank(player_name))
                if Player:
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "9":    # Opción 9 corresponde a Bardo
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_BARD,
                                                                Cl_Bard.Bard(player_name))
                if Player:
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
                if self.confirmPlayerSpawnpoint(POI.Muldraugh):
                    break
                else:
                    continue
            elif player_spawnpoint_choice == "2":   # Opción 2 corresponde a Riverside
                if self.confirmPlayerSpawnpoint(POI.Riverside):
                    break
                else:
                    continue
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_SPAWNPOINT_CHOICE)

        return self.saveGame()

    def confirmPlayerClassChoiceAndAssign(self, class_description, classrpg_with_player_name_classobj):
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
                return classrpg_with_player_name_classobj
            elif player_class_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_NO:
                return None
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)

    def confirmPlayerSpawnpoint(self, location_clasobj):
        global player_info
        self.showCombinedMessage(location_clasobj.Name, "\n" + location_clasobj.description)
        player_spawnpoint_choice_confirm = self.getPlayerChoice(Constants.
                                                                CHARACTER_CREATION_WORLD_SPAWNPOINT_CONFIRMATION)
        if player_spawnpoint_choice_confirm in Constants.PLAYER_PROMPT_SET_FOR_YES:
            player_info["location"] = location_clasobj
            return True
        elif player_spawnpoint_choice_confirm in Constants.PLAYER_PROMPT_SET_FOR_NO:
            self.showMessage(Constants.CHARACTER_CREATION_WORLD_SPAWNPOINTS)
            return False
        else:
            self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)

    def checkIfPlayerIsInLocation(self, location_classobj):
        global player_info
        if player_info["location"] == location_classobj:
            return True
        else:
            return False

    def confirmPlayerSaveFileDeletion(self):
        self.showMessage(Constants.MAIN_MENU_MESSAGE_SAVEFILE_ALREADY_EXISTS)
        self.showMessage(Constants.MAIN_MENU_MESSAGE_SAVEFILE_DELETE_CONFIRMATION)
        while True:
            player_delete_savefile_confirmation = self.getPlayerChoice()
            if player_delete_savefile_confirmation in Constants.PLAYER_PROMPT_SET_FOR_YES:
                os.remove("savefile.pickle")
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.showMessage(Constants.MAIN_MENU_MESSAGE_SAVEFILE_DELETED)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                return True
            elif player_delete_savefile_confirmation in Constants.PLAYER_PROMPT_SET_FOR_NO:
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.showMessage(Constants.MAIN_MENU_MESSAGE_SAVEFILE_NOT_DELETED_GOING_BACK_TO_MENU)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.clearScreen()
                return False
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)

    def calculateChance(self, chance):
        # Devolverá un valor booleano, random.random() devuelve un flotante cualquiera
        # Por ej. 0.619374830802 el cual es menor (<) a 0.80 (es decir 80/100)
        # Por ej2: si quiero saber si algo ocurre con un 80% de chance, simplemente ingresar 80 como argumento
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

    def saveGame(self):
        global player_info
        global Player
        with open("savefile.pickle", "wb") as f:
            pickle.dump(player_info, f, protocol=0)
            pickle.dump(Player, f, protocol=0)
            f.close()
        with open("savefile.pickle", "rb") as f:
            player_info = pickle.load(f)
            Player = pickle.load(f)
            f.close()

    def clearScreen(self):
        return os.system("cls")

    def showMessage(self, message):
        # Mostrará por pantalla la cadena pasada como argumento
        return print(message)

    def showCombinedMessage(self, msg1, msg2, msg3="", msg4="", msg5="",
                            msg6="", msg7="", msg8="", msg9="", msg10=""):
        return print(msg1, msg2, msg3, msg4, msg5,
                     msg6, msg7, msg8, msg9, msg10)

    def showWarning(self, message):
        self.showMessage("\n"+message)
        self.waitSeconds(Constants.TIME_BETWEEN_WARNINGS)
        #
        # A continuación se hace uso de Secuencias de Escape, Secuencias de códigos de Escape y Secuencias de Control
        #
        # - El carácter ESC (como si estuviéramos apretando esa tecla) se llama carácter de control.
        # - Barra \ en python (y específicamente en C) es el "carácter de escape", se usa para indicar que
        #   la siguiente letra debe ser interpretada de otra forma, esto permite controlar la salida en pantalla,
        #   es decir, el standard output. Esto incluye nueva linea (\n), eliminar una linea (carriage return: \r),
        #   tabulación (\t), entre otros.
        #
        # ° Secuencias de escape utilizadas: \033 y \x1b.
        #   - El primero usa el sistema octal. Para utilizar el sistema octal se debe hacer uso
        #     del carácter de escape (\) con tres números consecuentes (ej. \000, \033, \127).
        #   - En el código ASCII (googlear tabla), el carácter de control ESC en valores octales es 033.
        #   - Por otro lado, \x1b utiliza hexadecimal, para usar hexadecimal se debe escribir \x con dos números que le
        #     sigan a la x sin espacios. \x1b o \x1B también entonces hacen referencia al carácter de control ESC.
        #   - Extra: el carácter de control ESC en Unicode es \u001b
        #   - Aclaración: no hay una razón específica por la cual se usó dos sistemas distintos en up y clear, fue
        #     simplemente una decisión para que quede más claro cómo funcionan las secuencias. Tranquilamente los dos
        #     podrían usar solamente \x1B o solamente \003.
        #
        # ° Códigos de escape utilizados: [1A y [2K.
        #   - Existen muchos códigos de escape y llevan a cabo una función distinta (por ej. [#A, [#B, [s, [J, etc.
        #     donde # es el argumento y puede ir cualquier número)
        #   - En este caso, [1A indica que el cursor se desplace un lugar arriba. Por tanto [2A indicará que se desplace
        #     2 lugares arriba. Si no se especifica ningún valor simplemente se moverá 1 lugar arriba.
        #   - Para el caso de [2K, indica que se borre la línea entera en donde está parado el cursor. [1k borraría solo
        #     hasta el principio de la línea, y [0K, borraría solo hasta el final de la línea.
        #   - Se llaman así porque se escriben después del carácter de control ESC, es decir \x1B (o \033, o tmb \u001b)

        # ° Secuencias de control (o Secuencias de código de escape) utilizadas: \033[1A y \x1B[2K.
        #   - No son más que las secuencias de escape + los códigos escape en una misma cadena. Fueron guardados en
        #     variables para que sea más claro de entender lo que hacen.
        #   - Para saber más buscar CSI (Control Sequence Introducer)
        #
        #  Por último, el código debajo de este comentario hace lo siguiente: en un print, por defecto, el end= no se ve
        #  y hace que el cursor se pare en la línea debajo del texto que se acaba de mostrar por pantalla,
        #  por lo que si escribimos print("hola") el cursor no va a quedarse en "hola", va a quedarse
        #  en la línea debajo de hola. Al escribir print("hola", end={algo}), estamos especificando qué queremos
        #  que el interpretador haga después de printear, por lo tanto, si escribimos print("hola", end=up), el cursor
        #  ahora SÍ va a estar parado en la misma línea que hola. Con un ejemplo:
        #   print("hola")
        #   time.sleep(1)
        #   print(up, clear)
        #  Esto mostrará "hola" por un segundo, el cursor se moverá arriba en la misma línea que "hola", y la eliminará.
        #
        # Por eso, al mostrar un WARNING_MESSAGE, primero se eliminará el mensaje de advertencia, luego se eliminará el
        # espacio en blanco añadido con \n en ("\n"+message), y por último se eliminará el mensaje de "Opción:" o
        # "Nombre:" ya que se va a mostrar de nuevo de todas formas cuando termine de ejecutarse esta función.
        #
        up = '\033[1A'  # secuencia de control que mueve el cursor 1 línea arriba
        clear = '\x1B[2K'   # secuencia de control que elimina la línea entera en donde el cursor esté parado
        print(up, end=clear)    # eliminará el mensaje de advertencia
        print(up, end=clear)    # eliminará la nueva línea anidada al mensaje de advertencia (es decir el \n)
        return print(up, end=clear)  # eliminará el mensaje para el usuario "Opción:" o "Nombre:" o cualquier otro

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
