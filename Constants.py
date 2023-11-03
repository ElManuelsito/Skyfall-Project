#     print(INTRO_GAME)
# se deben guardar las constantes en un archivo "constant"
# INTRO_GAME = "INTRODUCCION AL JUEGO"
# MENU = "1- Entrar al juego" \
#        "2- Etc."
# MAX_PLAYERS = 5

# -- Testeando pickle --
# import pickle
#
# player_inv = {"weapon_1": False, "weapon_2": False, "helmet": False, "breastplate": False, "chausses": False,
#               "gauntlets": False, "money": 0}
# with open("savefile.pickle", "wb") as f:
#     pickle.dump(player_inv, f, protocol=0)
# f.close()
#
# with open("savefile.pickle", "rb") as f:
#     player_inv = pickle.load(f)
# f.close()
# print(player_inv.items())

# -----


# -------------------- Menu Related --------------------

# [ PLAYER INTERACTION WITH SYSTEM]
PLAYER_PROMPT_OPTION = "Opción: "
PLAYER_PROMPT_NAME = "Nombre: "
PRESS_ENTER_TO_CONTINUE = "\nPresiona Enter para continuar...\n"
PRESS_ENTER_TO_RETURN = "\nPresiona Enter para volver...\n"

# [ OPTIONS AND MESSAGES ]
WELCOMING_MESSAGE = "\n\n                    ~ Skyfall ~\nSelecciona una opción ingresando su número por teclado.\n"
MAIN_MENU_OPTIONS = "1. Nuevo juego\n2. Continuar\n3. Opciones\n4. Instrucciones\n5. Salir\n"
PLAYER_PROMPT_SET_FOR_YES = {"si", "sí", "SI", "SÍ", "Si", "Sí", "sI", "sÍ", "y", "Y", "yes", "Yes", "YES"}     # estructura de datos Set, incluye posibilidades para la respuesta del usuario "si"
PLAYER_PROMPT_SET_FOR_NO = {"no", "No", "NO", "nO", "n", "N"}                                                   # misma estructura pero para "No"
TIME_BETWEEN_MESSAGES = 1.7

CHARACTER_CREATION_NAME_MESSAGE = "Comienza creando tu personaje!\nPrimero ingresa tu nombre (recuerda que solo puedes utilizar caracteres alfabéticos y sin espacios)"
CHARACTER_CREATION_INVALID_NAME = "\nNombre no valido! Solo utiliza caracteres del alfabeto sin espacios!\n"
CHARACTER_CREATION_NAME_MESSAGE_INSIST = "Por favor ingresa tu nombre"

CHARACTER_CREATION_CLASS_MESSAGE = "\nAhora selecciona una clase (solo utiliza números del 1-9)\n"
CHARACTER_CREATION_INVALID_CLASS = "\nClase no valida! Solo utiliza un número del 1-9!\n"
CHARACTER_CREATION_CLASS_MESSAGE_INSIST = "Por favor selecciona una clase\n"
CHARACTER_CREATION_ALL_CLASSES = "1. Arquero\n2. Mago\n3. Guerrero\n4. Ladrón\n5. Invocador\n6. Paladín\n7. Nigromante\n8. Tanque\n9. Bardo\n"
CHARACTER_CREATION_CLASS_CONFIRM = "¿Deseas usar esta clase? (si/no)"
CHARACTER_CREATION_CLASS_INVALID_CONFIRM = "\nPor favor ingresa solamente \"si\" o \"no\".\n"

CHARACTER_CREATION_DESCRIPTION_ARCHER = "\n|| Arquero ||\nSalud: 120\nDefensa: 20\nMana: 20\nFuerza: 10\nAgilidad: 18" \
                                        "\nInteligencia: 7\nFé: 8\nPrecisión: 19\nResistencia mágica: 7\nResistencia física: 5" \
                                        "\n\nDescripción:\nMaestro del arco y sabio en proyectiles, el arquero se especializa " \
                                        "en ataques a distancia, por lo que dependerá mucho de su precisión y de armas de distancia. " \
                                        "No ofrece mucha salud ni tampoco armadura, pero lo compensa con su capacidad de esquivar y huir más seguido en sus batallas.\n"

CHARACTER_CREATION_DESCRIPTION_WIZARD = "\n|| Mago ||\nSalud: 100\nDefensa: 15\nMana: 75\nFuerza: 10\nAgilidad: 6" \
                                        "\nInteligencia: 30\nFé: 6\nPrecisión: 15\nResistencia mágica: 10\nResistencia física: 3" \
                                        "\n\nDescripción:\n \n"
CHARACTER_CREATION_DESCRIPTION_WARRIOR = "\n|| Guerrero ||\nSalud: 275\nDefensa: 40\nMana: 25\nFuerza: 20\nAgilidad: 10" \
                                        "\nInteligencia: 8\nFé: 6\nPrecisión: 6\nResistencia mágica: 5\nResistencia física: 12" \
                                        "\n\nDescripción:\n \n"
CHARACTER_CREATION_DESCRIPTION_THIEF = "\n|| Ladrón ||\nSalud: 100\nDefensa: 15\nMana: 75\nFuerza: 10\nAgilidad: 6" \
                                        "\nInteligencia: 30\nFé: 6\nPrecisión: 15\nResistencia mágica: 10\nResistencia física: 3" \
                                        "\n\nDescripción:\n \n"
CHARACTER_CREATION_DESCRIPTION_SORCERER = "inserte descripcion"
CHARACTER_CREATION_DESCRIPTION_PALADIN = "inserte descripcion"
CHARACTER_CREATION_DESCRIPTION_NECROMANCER = "inserte descripcion"
CHARACTER_CREATION_DESCRIPTION_TANK = "inserte descripcion"
CHARACTER_CREATION_DESCRIPTION_BARD = "inserte descripcion"

CHARACTER_CREATION_REQUEST_WORLD_MESSAGE = "Para finalizar, elige tu punto de aparición"
CHARACTER_CREATION_REQUEST_WORLD_SPAWNPOINT = ""
INSTRUCTIONS_MENU = "\nBienvenido a Skyfall! Para comenzar por favor lea estas instruccines:\n1. Navegar el menú\n2. Navegar el mundo\n 3. Combate\n 4. Items\n"
TIPS = ["Tip: para abrir el menu de opciones durante el combate, ingresar \"pausa\"."]


# -------------------- Combat Related --------------------

# [ GENERAL OPTIONS & MESSAGES ]
COMBAT_OPTIONS = "Decide qué hacer:\n1. Ataques comunes     2. Habilidades\n" \
                 "3. item                4. Huir\n"
SPECIAL_ATTACK_CONFIRM = "¿Deseas usar esta habilidad? (si/no)"

# [ ARCHER ]
COMMON_ATTACKS_ARCHER = "\nAtaques Comunes:\n1. Disparo Certero      2. Disparo Rápido\n"
SPECIAL_ATTACKS_ARCHER = "\nHabilidades:\n1. Lluvia de flechas\n2. Flecha de fuego\n3. Ojo de Ágila\n"
SPECIAL_ATTACK_A_DESC = "Lluvia de flechas:\n+ Daña multiples enemigos a la vez\n- Utiliza más Mana de lo normal\n"
SPECIAL_ATTACK_B_DESC = "Flecha de fuego:\n+ Enemigo recibe daño por turno dependiendo de tu INT\n+ Más daño de lo normal\n- 20% Chance de no aplicar el efecto\n"
SPECIAL_ATTACK_B_CHANCE = 80
SPECIAL_ATTACK_C_DESC = "Ojo de Ágila:\n+ Aumenta tu precisión por un turno\n"


# print(COMBAT_OPTIONS)
# input(USER_PROMPT)
# print(COMMON_ATTACKS_ARCHER)
# input(USER_PROMPT)
