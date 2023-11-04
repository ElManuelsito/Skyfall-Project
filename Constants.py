#     print(INTRO_GAME)
# se deben guardar las constantes en un archivo "constant"
# INTRO_GAME = "INTRODUCCIÓN AL JUEGO"
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
PLAYER_PROMPT_SET_FOR_NO = {"no", "No", "NO", "nO", "n", "N"}                                                   # misma estructura, pero para "No"
TIME_BETWEEN_MESSAGES = 1.1
TIME_BETWEEN_WARNINGS = 1.8

CHARACTER_CREATION_NAME_MESSAGE = "\nComienza creando tu personaje!\n\nPrimero ingresa tu nombre (recuerda que solo puedes utilizar caracteres alfabéticos y sin espacios)"
CHARACTER_CREATION_INVALID_NAME = "\nNombre no valido! Solo utiliza caracteres alfabéticos sin espacios!\n"
CHARACTER_CREATION_NAME_MESSAGE_INSIST = "Por favor ingresa tu nombre"

CHARACTER_CREATION_CLASS_MESSAGE = "\nAhora selecciona una clase (solo utiliza números del 1-9)"
CHARACTER_CREATION_INVALID_CLASS = "\nClase no valida! Solo utiliza un número del 1-9!\n"
CHARACTER_CREATION_CLASS_MESSAGE_INSIST = "Por favor selecciona una clase"
CHARACTER_CREATION_ALL_CLASSES = "\n1. Arquero\n2. Mago\n3. Guerrero\n4. Ladrón\n5. Hechicero\n6. Paladín\n7. Nigromante\n8. Tanque\n9. Bardo\n"
CHARACTER_CREATION_CLASS_CONFIRM = "¿Deseas usar esta clase? (si/no)"
CHARACTER_CREATION_CLASS_INVALID_CONFIRM = "\nPor favor ingresa solamente \"si\" o \"no\".\n"

CHARACTER_CREATION_DESCRIPTION_ARCHER = "\n\n|| Arquero ||\nSalud: 120\nDefensa: 20\nMana: 20\nFuerza: 10\nAgilidad: 18" \
                                        "\nInteligencia: 7\nFé: 8\nPrecisión: 19\nResistencia mágica: 7%\nResistencia física: 5%" \
                                        "\n\nDescripción:\n Maestro del arco y armas de distancia, el arquero se especializa en ataques a distancias, donde" \
                                        " su agilidad es muy importante para moverse junto a su gran precisión.\n No tiene mucha salud ni resistencia, pero" \
                                        " sus capacidades de esquivar e huir le son más que suficientes para sus batallas y descubrimientos a lo largo del mundo.\n"

CHARACTER_CREATION_DESCRIPTION_WIZARD = "\n\n|| Mago ||\nSalud: 100\nDefensa: 15\nMana: 75\nFuerza: 10\nAgilidad: 6" \
                                        "\nInteligencia: 30\nFé: 6\nPrecisión: 15\nResistencia mágica: 10%\nResistencia física: 3%" \
                                        "\n\nDescripción:\n Los magos son famosos por controlar el campo de batalla debido a sus manejos de los elementos, son personas que estudian la magia y los elementos para su beneficio.\n" \
                                        " Son muy lentos y de bajo daño físico, pero sus grandes poderes mágicos les son más que suficientes para ganar un combate.\n"

CHARACTER_CREATION_DESCRIPTION_WARRIOR = "\n\n|| Guerrero ||\nSalud: 275\nDefensa: 40\nMana: 25\nFuerza: 20\nAgilidad: 10" \
                                        "\nInteligencia: 8\nFé: 6\nPrecisión: 6\nResistencia mágica: 2%\nResistencia física: 10%" \
                                        "\n\nDescripción:\n Guerreros dispuestos a la batalla sin miedo a la muerte, con sus espadas listas y sus armaduras preparadas para la batalla.\n" \
                                         " Su fuerza física es remarcable, dicen que llega incluso a atravesar armaduras como si fueran meros papeles.\n" \
                                         " Cuentan con un físico intermedio en aspectos como la agilidad, fuerza y defensa, pero son muy débiles contra la magia ya que son fáciles de poseer y de entrar en su mente.\n"

CHARACTER_CREATION_DESCRIPTION_THIEF = "\n\n|| Ladrón ||\nSalud: 150\nDefensa: 20\nMana: 30\nFuerza: 18\nAgilidad: 24" \
                                        "\nInteligencia: 0\nFé: 5\nPrecisión: 10\nResistencia mágica: 8%\nResistencia física: 10%" \
                                        "\n\nDescripción:\n Ladrones de naturaleza, con agilidad como un felino y precisión como un Halcón a la ahora de atacar, son muy cautelosos y difíciles de rastrear.\n" \
                                       " En batalla, su audacia junto a su experiencia de salir de problemas apretados lo ayudan a ganar la contienda.\n" \
                                       " Si bien su salud es intermedia, su agilidad y fuerza le son más que suficientes para salir adelante.\n"

CHARACTER_CREATION_DESCRIPTION_SORCERER = "\n\n|| Hechicero ||\nSalud: 100\nDefensa: 10\nMana: 60\nFuerza: 8\nAgilidad: 5" \
                                        "\nInteligencia: 45\nFé: 3\nPrecisión: 20\nResistencia mágica: 5%\nResistencia física: 4%" \
                                        "\n\nDescripción:\n Los hechiceros son especialistas en la magia de control e invocaciones de criaturas vivas, su magia es muy poderosa pero su cuerpo y debilidad física no lo acompañan.\n" \
                                          " Compensan sus debilidades físicas invocando criaturas que pelean por ellos, permitiéndoles ganar sus batallas.\n" \
                                          " Son muy astutos pero su movilidad es muy lenta, no creen en la fe divina pero sí en su divina magia.\n"

CHARACTER_CREATION_DESCRIPTION_PALADIN = "\n\n|| Paladin ||\nSalud: 200\nDefensa: 40\nMana: 25\nFuerza: 10\nAgilidad: 4" \
                                        "\nInteligencia: 20\nFé: 1\nPrecisión: 8\nResistencia mágica: 10%\nResistencia física: 12%" \
                                        "\n\nDescripción:\n Los paladines son una clase hibrida entre Caballero y Sacerdote que pueden ser denominados como caballeros sagrados.\n" \
                                         " Se recubren con sus armaduras, junto a sus escudos y espadas, pero por el peso que llevan son muy lentos a la hora de la batalla.\n" \
                                         " Su fe divina siempre lo protege junto a la dureza de su armadura y su noble corazón.\n"

CHARACTER_CREATION_DESCRIPTION_NECROMANCER = "\n\n|| Nigromante ||\nSalud: 100\nDefensa: 9\nMana: 55\nFuerza: 7\nAgilidad: 5" \
                                        "\nInteligencia: 40\nFé: 0\nPrecisión: 20\nResistencia mágica: 9%\nResistencia física: 4%" \
                                        "\n\nDescripción:\n Maestro de las magias de la muerte, capaces de invocar seres no-muertos y magias infernales. Sus armas pueden ser dagas o varitas para realizar invocaciones.\n" \
                                             " Siempre en búsqueda de lo desconocido y lo prohibido de la magia, son personas muy cautelosas, donde su salud es baja pero su magia es poderosa.\n"

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
INSTRUCTIONS_MENU = "\nBienvenido a Skyfall! Para comenzar por favor lea estas instrucciones:\n1. Navegar el menú\n2. Navegar el mundo\n 3. Combate\n 4. Items\n"
TIPS = ["Tip: para abrir el menu de opciones durante el combate, ingresar \"pausa\"."]


# -------------------- Combat Related --------------------

# [ GENERAL OPTIONS & MESSAGES ]
COMBAT_OPTIONS = "Decide qué hacer:\n1. Ataques comunes     2. Habilidades\n" \
                 "3. item                4. Huir\n"
SPECIAL_ATTACK_CONFIRM = "¿Deseas usar esta habilidad? (si/no)"

# [ ARCHER ]
COMMON_ATTACKS_ARCHER = "\nAtaques Comunes:\n1. Disparo Certero      2. Disparo Rápido\n"
SPECIAL_ATTACKS_ARCHER = "\nHabilidades:\n1. Lluvia de flechas\n2. Flecha de fuego\n3. Ojo de Águila\n"
SPECIAL_ATTACK_A_DESC_ARCH = "Lluvia de flechas:\n+ Daña multiples enemigos a la vez\n- Utiliza más Mana de lo normal\n"
SPECIAL_ATTACK_B_DESC_ARCH = "Flecha de fuego:\n+ Enemigo recibe daño por turno dependiendo de tu INT\n+ Más daño de lo normal\n -20% Chance de no aplicar el efecto\n"
SPECIAL_ATTACK_B_CHANCE_ARCH = 80
SPECIAL_ATTACK_C_DESC_ARCH = "Ojo de Águila:\n+ Aumenta tu precisión por un turno\n"

#[Wizard]
COMMON_ATTACKS_WIZARD = "\nAtaques Comunes:\n1. Aurora Magica      2.Bastonazo\n"
SPECIAL_ATTACKS_WIZARD = "\nHabilidades:\n1. Bola de Fuego\n2. LLuvida de fuego\n3. Congelamiento \n"
SPECIAL_ATTACK_A_DESC_WIZ = "Bola de Fuego:\n+ Mete mucho daño a un solo objetivo\n- Coste Intermedio de Mana\n"
SPECIAL_ATTACK_B_DESC_WIZ = "Lluvia de Fuego:\n+ En una Zona circular cae una lluvia de fuego, donde mete daño en Area y afectando a mas de un enemigo\n+ Coste Alto de Mana\n"
SPECIAL_ATTACK_C_DESC_WIZ = "Congelamiento:\n+ En una zona crea un escarcha de hielo provocando que los enemigos queden congelado y aturdido\n+ Coste Intermedio de Mana"
SPECIAL_ATTACK_C_CHANCE_WIZ = 70

#[Warrior]
COMMON_ATTACKS_WARRIOR = "\nAtaques Comunes:\n1.Basico a Espada    2.Basico a Hacha\n"
SPECIAL_ATTACKS_WARRIOR = "\nHabilidades:\n1. Corte \n2. Spiral Splash \n3. Multiples cortes  \n"
SPECIAL_ATTACK_A_DESC_WARR = "Corte:\n+ Provoca un daño intermedio a un objetivo \n- Coste bajo de Mana\n"
SPECIAL_ATTACK_B_DESC_WARR = "Spiral Splash:\n+ Genera un espiral de fuego en la espada provocando daño a un objetivo\n+ Coste intermedio de Mana\n"
IAL_ATTACK_B_CHANCE_WARR = 50
SPECIAL_ATTACK_C_DESC_WARR = "Multix Cortes:\n+ Provoca multiples cortes a un objetivo, provocando mucho daño\n+ Coste Alto de mana"

#[THIEF]
COMMON_ATTACKS_THIEF = "\nAtaques Comunes:\n1.Basico a Daga"
SPECIAL_ATTACKS_THIEF = "\nHabilidades:\n1.Golpe bajo \n2. Corte desgarrador \n3. Golpe en los Riñones\n"
SPECIAL_ATTACK_A_DESC_THIE = "Golpe Bajo:\n+ Provoca un daño intermedio a un objetivo golpeando en los puntos bajo \n- Coste bajo de Mana\n"
SPECIAL_ATTACK_B_DESC_THIE = "Corte desgarrador:\n+  Provoca un corte con sangrado \n+ Coste intermedio de Mana\n"
SPECIAL_ATTACK_B_CHANCE_THIE = 70
SPECIAL_ATTACK_C_DESC_THIE = "Golpe en los Riñones:\n+ Provoca mucho daño al objetivo logrando paralizarlo \n+ Coste Alto de mana"
SPECIAL_ATTACK_C_CHANCE_THIE = 40

#[SORCERER]
COMMON_ATTACKS_SORC = "\nAtaques Comunes:\n1.Aurora magica"
SPECIAL_ATTACKS_SORC = "\nHabilidades:\n1.Magia Control \n2. Invocacion bestia \n3. Fear\n"
SPECIAL_ATTACK_A_DESC_SORC = "Magia Control :\n+ Controla por un breve momento al enemigo haciendo que se lastime el mismo \n- Coste intermedio de Mana\n"
SPECIAL_ATTACK_B_DESC_SORC = "Invocacion Bestia:\n+ Invoca a una criatura que le ayuda a luchar provocando daño a un objetivo \n+ Coste Alto de Mana\n"
SPECIAL_ATTACK_C_DESC_SORC = "Fear:\n+ Provoca un miedo al enemigo que hace que no ataque por un breve momento \n+ Coste intermedio  de mana"
SPECIAL_ATTACK_C_CHANCE_SORC = 45

#[Paladin]
COMMON_ATTACKS_PAL = "\nAtaques Comunes:\n1.Ataque Basico con Espada"
SPECIAL_ATTACKS_PAL = "\nHabilidades:\n1.Sentencia \n2. Destello de luz  \n3. Golpe de Cruzado \n"
SPECIAL_ATTACK_A_DESC_PAL = "Sentencia:\n+ Juzga al enemigo provocandole un daño con la espada sagrada \n- Coste Bajo de Mana\n"
SPECIAL_ATTACK_B_DESC_PAL = "Destello de Luz:\n+ Invoca una luz que cae en el provocando curarce un 20% de su vida faltante \n+ Coste Alto de Mana\n"
SPECIAL_ATTACK_C_DESC_PAL = "Golpe de Cruzada:\n+ Golpea al objetivo provocando un gran daño y aturdiendolo brevemente\n+ Coste intermedio  de mana"
SPECIAL_ATTACK_C_CHANCE_PAL = 50

#[NECROMANCER]
COMMON_ATTACKS_NEC = "\nAtaques Comunes:\n1.Magia Dark   2.Basico con Daga"
SPECIAL_ATTACKS_NEC = "\nHabilidades:\n1.Invoacion NO-MUERTO \n2. Invoaciones Infernales \n3. Descomposición \n"
SPECIAL_ATTACK_A_DESC_NEC = "Invoacion NO-MUERTO:\n+ Invoca personas sin vida para atacar a un objetivo \n- Coste Bajo de Mana\n"
SPECIAL_ATTACK_B_DESC_NEC = "Invoacion Infernal:\n+ Invoca Bestias del Infierno para dañar todo lo que se ponga por delante \n+ Coste Alto de Mana\n"
SPECIAL_ATTACK_C_DESC_NEC = "Descomposición:\n+ Lanza una maldicion que hace que el objetivo se descomponga como si estuviera envenenado\n+ Coste intermedio de mana"
SPECIAL_ATTACK_C_CHANCE_NEC = 50

#[TANK]
COMMON_ATTACKS_TANK = "\nAtaques Comunes:\n1.Basico con Espada"
SPECIAL_ATTACKS_TANK = "\nHabilidades:\n1.Power up \n2. Focus \n3. Desesperacion \n"
SPECIAL_ATTACK_A_DESC_TANK = "Power UP:\n+ Hace que su ataque aumente \n- Coste Bajo de Mana\n"
SPECIAL_ATTACK_B_DESC_TANK = "Focus:\n+ Se concentra aumentando su defensa a todo tipo de daño \n+ Coste bajo de Mana\n"
SPECIAL_ATTACK_C_DESC_TANK = "Desesperacion:\n+ Cuando ya se esta por rendir entra en su desesperacion aumentando drasticamente su defensa y daño \n+ Coste intermedio de mana"

# [BARD]
COMMON_ATTACKS_BARD = "\nAtaques Comunes:\n1. Basico Melodico   2. Rafaga melodica\n"
SPECIAL_ATTACKS_BARD = "\nHabilidades:\n1.Ispiracion \n2. Curar \n3. Remover Efectos\n"
SPECIAL_ATTACK_A_BARD = "Ispiracion:\n+ Sube los stat de si mismo inspirandose \n- Coste Bajo de mana \n"
SPECIAL_ATTACK_B_BARD = "Helear:\n+ Restaura un 40HP de vida \n+ Coste Intermedio de Mana \n"
SPECIAL_ATTACK_C_DESC_BAR = "Remover Efecto:\n+ Remueve cualquier efecto que le hallan tirado\n+ Coste Intermedio de Mana \n"

#
# print(COMBAT_OPTIONS)
# input(USER_PROMPT)
# print(COMMON_ATTACKS_ARCHER)
# input(USER_PROMPT)
