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
TIME_BETWEEN_MESSAGES = 1.1
TIME_BETWEEN_WARNINGS = 1.8

CHARACTER_CREATION_NAME_MESSAGE = "\nComienza creando tu personaje!\n\nPrimero ingresa tu nombre (recuerda que solo puedes utilizar caracteres alfabéticos y sin espacios)"
CHARACTER_CREATION_INVALID_NAME = "\nNombre no valido! Solo utiliza caracteres alfabéticos sin espacios!\n"
CHARACTER_CREATION_NAME_MESSAGE_INSIST = "Por favor ingresa tu nombre"

CHARACTER_CREATION_CLASS_MESSAGE = "\nAhora selecciona una clase (solo utiliza números del 1-9)"
CHARACTER_CREATION_INVALID_CLASS = "\nClase no valida! Solo utiliza un número del 1-9!\n"
CHARACTER_CREATION_CLASS_MESSAGE_INSIST = "Por favor selecciona una clase"
CHARACTER_CREATION_ALL_CLASSES = "\n1. Arquero\n2. Mago\n3. Guerrero\n4. Ladrón\n5. Hechizero\n6. Paladín\n7. Nigromante\n8. Tanque\n9. Bardo\n"
CHARACTER_CREATION_CLASS_CONFIRM = "¿Deseas usar esta clase? (si/no)"
CHARACTER_CREATION_CLASS_INVALID_CONFIRM = "\nPor favor ingresa solamente \"si\" o \"no\".\n"

CHARACTER_CREATION_DESCRIPTION_ARCHER = "\n\n|| Arquero ||\nSalud: 120\nDefensa: 20\nMana: 20\nFuerza: 10\nAgilidad: 18" \
                                        "\nInteligencia: 7\nFé: 8\nPrecisión: 19\nResistencia mágica: 7%\nResistencia física: 5%" \
                                        "\n\nDescripción:\n Maestro del arco y armas de distancia, el arquero se especializa en ataques a distancias, donde" \
                                        " su agilidad es muy importante para moverse junto a su gran presición.\n No tiene mucha salud ni resistencia, pero" \
                                        " sus capacidades de esquivar e huir le son más que suficientes para sus batallas y descubrimientos a lo largo del mundo.\n"

CHARACTER_CREATION_DESCRIPTION_WIZARD = "\n\n|| Mago ||\nSalud: 100\nDefensa: 15\nMana: 75\nFuerza: 10\nAgilidad: 6" \
                                        "\nInteligencia: 30\nFé: 6\nPrecisión: 15\nResistencia mágica: 10%\nResistencia física: 3%" \
                                        "\n\nDescripción:\n Los magos son famosos por controlar el campo de batalla debido a sus manejos de los elementos, son personas que estudian la magia y los elementos para su beneficio.\n" \
                                        " Son muy lentos y de bajo daño físico, pero sus grandes poderes mágicos les son más que suficientes para ganar un combate.\n"

CHARACTER_CREATION_DESCRIPTION_WARRIOR = "\n\n|| Guerrero ||\nSalud: 275\nDefensa: 40\nMana: 25\nFuerza: 20\nAgilidad: 10" \
                                        "\nInteligencia: 8\nFé: 6\nPrecisión: 6\nResistencia mágica: 2%\nResistencia física: 10%" \
                                        "\n\nDescripción:\n Guerreros dispuestos a la batalla sin miedo a la muerte, con sus espadas listas y sus armaduras preparadas para la batalla.\n" \
                                         " Su fuerza fisica es remarcable, dicen que llega incluso a atravezar armaduras como si fueran meros papeles.\n" \
                                         " Cuentan con un físico intermedio en aspectos como la agilidad, fuerza y defensa, pero son muy débiles contra la magia ya que son fáciles de poseer y de entrar en su mente.\n"

CHARACTER_CREATION_DESCRIPTION_THIEF = "\n\n|| Ladrón ||\nSalud: 150\nDefensa: 20\nMana: 30\nFuerza: 18\nAgilidad: 24" \
                                        "\nInteligencia: 0\nFé: 5\nPrecisión: 10\nResistencia mágica: 8%\nResistencia física: 10%" \
                                        "\n\nDescripción:\n Ladrones de naturaleza, con agilidad como un felino y precisión como un Alcón a la ahora de atacar, son muy cautelosos y dificiles de rastrear.\n" \
                                       " En batalla, su audacia junto a su experiencia de salir de problemas apretados lo ayudan a ganar la contienda.\n" \
                                       " Si bien su salud es intermedia, su agilidad y fuerza le son más que suficientes para salir adelante.\n"

CHARACTER_CREATION_DESCRIPTION_SORCERER = "\n\n|| Hechizero ||\nSalud: 100\nDefensa: 10\nMana: 60\nFuerza: 8\nAgilidad: 5" \
                                        "\nInteligencia: 45\nFé: 3\nPrecisión: 20\nResistencia mágica: 5%\nResistencia física: 4%" \
                                        "\n\nDescripción:\n Los hechizeros son especialistas en la magia de control e invociones de criaturas vivas, su magia es muy poderosa pero su cuerpo y debilidad fisica no lo acompañan.\n" \
                                          " Compensan sus debilidades físicas invocando criaturas que pelean por ellos, permitiéndoles ganar sus batallas.\n" \
                                          " Son muy astutos pero su movilidad es muy lenta, no creen en la fe divina pero sí en su divina magia.\n"

CHARACTER_CREATION_DESCRIPTION_PALADIN = "\n\n|| Paladin ||\nSalud: 200\nDefensa: 40\nMana: 25\nFuerza: 10\nAgilidad: 4" \
                                        "\nInteligencia: 20\nFé: 1\nPrecisión: 8\nResistencia mágica: 10%\nResistencia física: 12%" \
                                        "\n\nDescripción:\n Los paladines son una clase hibrida entre Caballero y Sarcedote que pueden ser denomidados como caballeros sagrados.\n" \
                                         " Se recubren con sus armaduras, junto a sus escudos y espadas, pero por el peso que llevan son muy lentos a la hora de la batalla.\n" \
                                         " Su fe divina siempre lo protege junto a la dureza de su armadura y su noble corazón.\n"

CHARACTER_CREATION_DESCRIPTION_NECROMANCER = "\n\n|| Nigromante ||\nSalud: 100\nDefensa: 9\nMana: 55\nFuerza: 7\nAgilidad: 5" \
                                        "\nInteligencia: 40\nFé: 0\nPrecisión: 20\nResistencia mágica: 9%\nResistencia física: 4%" \
                                        "\n\nDescripción:\n Maestro de las magias de la muerte, capaces de invocar seres no-numertos y magias infernales. Sus armas pueden ser dagas o varitas para realizar invocaciones.\n" \
                                             " Siempre en busqueda de lo desconocido y lo prohibido de la magia, son personas muy cautelosas, donde su salud es baja pero su magia es poderosa.\n"

CHARACTER_CREATION_DESCRIPTION_TANK = "\n\n|| Tanque ||\nSalud: 300\nDefensa: 60\nMana: 15\nFuerza: 15\nAgilidad: 6" \
                                        "\nInteligencia: 4\nFé: 9\nPrecisión: 4\nResistencia mágica: 11%\nResistencia física: 15%" \
                                        "\n\nDescripción:\n Guerreros con armaduras pesadas junto a un escudo y un fiel mazo o espada que los acompañan para la guerra, nunca titubean a la hora de defender e ir en primera fila para proteger a su gente.\n " \
                                      "Poseen un corazón noble y siempre dispuesto ayudar a su Reino, debido a sus pesadas armaduras son muy lentos pero tienen una resistencia inigualable.\n"

CHARACTER_CREATION_DESCRIPTION_BARD = "\n\n|| Bardo ||\nSalud: 80\nDefensa: 10\nMana: 40\nFuerza: 5\nAgilidad: 6" \
                                        "\nInteligencia: 30\nFé: 15\nPrecisión: 13\nResistencia mágica: 6%\nResistencia física: 4%" \
                                        "\n\nDescripción:\n Bardo es un elegante luchador que utiliza el poder de la canción para mejorar a sus aliados y derrotar a sus enemigos.\n" \
                                      " Abriéndose paso entre sus enemigos con una variedad de ataques llamativos, el Bardo inspira a sus aliados a nunca bajar los brazos, dándoles ánimo y mejoras para seguir luchando.\n"

CHARACTER_CREATION_REQUEST_WORLD_MESSAGE = "Para finalizar, elige tu punto de aparición"
CHARACTER_CREATION_REQUEST_WORLD_SPAWNPOINT = "ingresar nombre de mundos acá"
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
